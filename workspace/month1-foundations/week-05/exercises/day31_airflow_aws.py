#!/usr/bin/env python3
"""
Day 31: Connect Airflow to Lambda + S3
=======================================
Duration: 2-2.5 hours

Integrate Airflow with AWS services.
Trigger Lambda functions and work with S3 from your DAGs.

WHY THIS MATTERS:
- Real pipelines orchestrate cloud services
- AWS is the most common cloud platform
- This is production-ready architecture
- Combines orchestration with serverless

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Set Up AWS Connection in Airflow (20 min)
=====================================================

1. Go to Airflow UI → Admin → Connections
2. Add new connection:
   - Connection Id: aws_default
   - Connection Type: Amazon Web Services
   - AWS Access Key ID: (your key)
   - AWS Secret Access Key: (your secret)
   - Extra: {"region_name": "us-east-1"}

3. Test connection (in a DAG or ad-hoc):
   from airflow.providers.amazon.aws.hooks.s3 import S3Hook
   hook = S3Hook(aws_conn_id='aws_default')
   print(hook.list_buckets())


EXERCISE 2: S3 Operators and Sensors (30 min)
=============================================

Common S3 operations:

# Check if file exists
S3KeySensor(
    task_id='wait_for_file',
    bucket_key='raw/data.json',
    bucket_name='my-bucket',
    aws_conn_id='aws_default',
)

# Upload file
LocalFilesystemToS3Operator(
    task_id='upload_to_s3',
    filename='/local/path/file.json',
    dest_key='raw/file.json',
    dest_bucket='my-bucket',
    aws_conn_id='aws_default',
)

# Download file
S3ToLocalFilesystemOperator(
    task_id='download_from_s3',
    key='raw/file.json',
    bucket='my-bucket',
    dest_path='/local/path/',
    aws_conn_id='aws_default',
)


EXERCISE 3: Lambda Operators (30 min)
=====================================

Invoke Lambda from Airflow:

from airflow.providers.amazon.aws.operators.lambda_function import (
    LambdaInvokeFunctionOperator
)

invoke_lambda = LambdaInvokeFunctionOperator(
    task_id='invoke_extractor',
    function_name='stock-data-extractor',
    aws_conn_id='aws_default',
    payload=json.dumps({"symbols": ["AAPL", "MSFT"]}),
)


EXERCISE 4: Build Stock Extraction DAG (40 min)
===============================================

Create a DAG that:
1. Invokes Lambda to extract data
2. Waits for data in S3
3. Triggers downstream processing

See STOCK_EXTRACTION_DAG below.


EXERCISE 5: XComs - Passing Data Between Tasks (20 min)
=======================================================

XComs allow tasks to share small amounts of data.

# Push data
def extract(**context):
    result = {"count": 10, "status": "success"}
    context['ti'].xcom_push(key='extract_result', value=result)

# Pull data
def process(**context):
    result = context['ti'].xcom_pull(
        task_ids='extract', 
        key='extract_result'
    )
    print(f"Processing {result['count']} records")


EXERCISE 6: Error Handling and Retries (20 min)
===============================================

Configure robust error handling:

task = PythonOperator(
    task_id='risky_task',
    python_callable=my_function,
    retries=3,
    retry_delay=timedelta(minutes=5),
    retry_exponential_backoff=True,
    on_failure_callback=alert_on_failure,
)

def alert_on_failure(context):
    '''Send alert when task fails.'''
    task_id = context['task_instance'].task_id
    exception = context['exception']
    print(f"Task {task_id} failed: {exception}")
"""

# =============================================================================
# EXAMPLE DAGS
# =============================================================================

STOCK_EXTRACTION_DAG = '''
"""
Stock Extraction DAG with AWS Integration.
"""
from datetime import datetime, timedelta
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor


default_args = {
    'owner': 'data-engineering',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


def process_lambda_result(**context):
    """Process the Lambda invocation result."""
    # Get XCom from Lambda task
    ti = context['ti']
    lambda_result = ti.xcom_pull(task_ids='invoke_lambda')
    
    if lambda_result:
        result = json.loads(lambda_result)
        print(f"Lambda returned: {result}")
        
        # Could parse S3 path and push for next task
        if 'body' in result:
            body = json.loads(result['body'])
            print(f"Extracted {body.get('count', 0)} records")


def run_quality_checks(**context):
    """Run data quality checks."""
    execution_date = context['ds']
    print(f"Running quality checks for {execution_date}")
    
    # In production, you'd query the database
    # and validate the data
    
    return {"status": "passed", "checks": 5}


with DAG(
    dag_id='stock_extraction_pipeline',
    default_args=default_args,
    description='Extract stock data via Lambda, process, and validate',
    schedule_interval='0 */4 * * *',  # Every 4 hours
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['stocks', 'aws', 'production'],
) as dag:
    
    # Task 1: Invoke Lambda to extract data
    invoke_lambda = LambdaInvokeFunctionOperator(
        task_id='invoke_lambda',
        function_name='stock-data-extractor',
        aws_conn_id='aws_default',
        payload=json.dumps({
            "symbols": ["AAPL", "MSFT", "GOOGL"],
            "source": "airflow"
        }),
    )
    
    # Task 2: Wait for data to appear in S3
    wait_for_data = S3KeySensor(
        task_id='wait_for_data',
        bucket_key='raw/stocks/{{ ds }}/data.json',
        bucket_name='your-data-lake',
        aws_conn_id='aws_default',
        timeout=300,  # 5 minutes
        poke_interval=30,  # Check every 30 seconds
        mode='poke',
    )
    
    # Task 3: Process Lambda result
    process_result = PythonOperator(
        task_id='process_result',
        python_callable=process_lambda_result,
        provide_context=True,
    )
    
    # Task 4: Run quality checks
    quality_checks = PythonOperator(
        task_id='quality_checks',
        python_callable=run_quality_checks,
        provide_context=True,
    )
    
    # Dependencies
    invoke_lambda >> [wait_for_data, process_result]
    wait_for_data >> quality_checks
'''


def print_dag():
    """Print the stock extraction DAG."""
    print(STOCK_EXTRACTION_DAG)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "dag":
        print_dag()
    else:
        print("Day 31: Connect Airflow to Lambda + S3")
        print("=" * 42)
        print("\nIntegrate Airflow with AWS services.")
        print("\nCommands:")
        print("  python day31_airflow_aws.py dag - Show AWS DAG example")
