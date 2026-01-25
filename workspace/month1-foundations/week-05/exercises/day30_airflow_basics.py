#!/usr/bin/env python3
"""
Day 30: Airflow DAG Basics
===========================
Duration: 2-2.5 hours

Introduction to Apache Airflow - the standard for data pipeline orchestration.
Understand the architecture and build your first DAG.

WHY THIS MATTERS:
- Airflow is the #1 orchestration tool
- Required skill for data engineer roles
- Manages complex pipeline dependencies
- This is how production pipelines run

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

from datetime import datetime, timedelta
from typing import Dict, List, Any

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Understand Airflow Architecture (20 min)
====================================================

Key Components:
- Scheduler: Triggers DAGs on schedule
- Executor: Runs tasks (Local, Celery, Kubernetes)
- Webserver: UI for monitoring
- Metadata DB: Stores state (usually PostgreSQL)
- DAG: Directed Acyclic Graph of tasks

Key Concepts:
- DAG: Collection of tasks with dependencies
- Task: Single unit of work
- Operator: Template for tasks (BashOperator, PythonOperator)
- Hook: Connection to external systems
- Connection: Stored credentials


EXERCISE 2: Set Up Local Airflow (30 min)
=========================================

Option A: Docker Compose (Recommended)
--------------------------------------
# Download docker-compose
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'

# Initialize
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env

# Initialize database
docker-compose up airflow-init

# Start all services
docker-compose up -d

# Access UI: http://localhost:8080
# Default login: airflow/airflow


Option B: Pip Install (Simpler but less production-like)
--------------------------------------------------------
pip install apache-airflow
airflow db init
airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com
airflow webserver -p 8080 &
airflow scheduler &


EXERCISE 3: Create Your First DAG (30 min)
==========================================

Create dags/hello_world.py:

See HELLO_WORLD_DAG below.


EXERCISE 4: Understand Operators (20 min)
=========================================

Common Operators:
- BashOperator: Run bash commands
- PythonOperator: Run Python functions
- PostgresOperator: Run SQL queries
- S3Hook/Operator: Interact with S3
- EmailOperator: Send emails
- DummyOperator: Placeholder/branching


EXERCISE 5: Task Dependencies (20 min)
======================================

Three ways to set dependencies:

# Method 1: >> and <<
task1 >> task2 >> task3  # task1 → task2 → task3

# Method 2: set_downstream/set_upstream
task1.set_downstream(task2)
task2.set_downstream(task3)

# Method 3: Lists
[task1, task2] >> task3  # task1 and task2 both run before task3


EXERCISE 6: Trigger Your DAG (20 min)
=====================================

1. Place DAG file in dags/ folder
2. Wait for scheduler to pick it up (~30s)
3. Go to Airflow UI
4. Find your DAG
5. Toggle it ON
6. Trigger manually
7. Watch it run!
"""

# =============================================================================
# EXAMPLE DAGS
# =============================================================================

HELLO_WORLD_DAG = '''
"""
Hello World DAG - Your first Airflow DAG!

Place this file in your Airflow dags/ folder.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


# Default arguments for all tasks
default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


def print_hello():
    """A simple Python function."""
    print("Hello from Airflow!")
    return "hello"


def print_date(**context):
    """Print execution date."""
    execution_date = context['ds']
    print(f"Execution date: {execution_date}")
    return execution_date


# Define the DAG
with DAG(
    dag_id='hello_world',
    default_args=default_args,
    description='My first DAG',
    schedule_interval='@daily',  # Run daily
    start_date=datetime(2024, 1, 1),
    catchup=False,  # Don't backfill
    tags=['example', 'tutorial'],
) as dag:
    
    # Task 1: Bash command
    task_bash = BashOperator(
        task_id='print_date_bash',
        bash_command='date'
    )
    
    # Task 2: Python function
    task_python_hello = PythonOperator(
        task_id='print_hello',
        python_callable=print_hello
    )
    
    # Task 3: Python with context
    task_python_date = PythonOperator(
        task_id='print_execution_date',
        python_callable=print_date,
        provide_context=True
    )
    
    # Task 4: Another bash command
    task_complete = BashOperator(
        task_id='complete',
        bash_command='echo "DAG complete!"'
    )
    
    # Define dependencies
    task_bash >> task_python_hello >> task_python_date >> task_complete
'''


STOCK_PIPELINE_DAG = '''
"""
Stock Pipeline DAG - Orchestrate your stock data pipeline.
"""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.operators.lambda_function import LambdaInvokeFunctionOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'data-engineering',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}


with DAG(
    dag_id='stock_pipeline',
    default_args=default_args,
    description='Stock data extraction and loading pipeline',
    schedule_interval='0 * * * *',  # Every hour
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['stocks', 'production'],
) as dag:
    
    # Task 1: Extract data (invoke Lambda)
    extract = LambdaInvokeFunctionOperator(
        task_id='extract_stock_data',
        function_name='stock-data-extractor',
        aws_conn_id='aws_default',
    )
    
    # Task 2: Load to database
    load = PythonOperator(
        task_id='load_to_database',
        python_callable=lambda: print("Loading data..."),
    )
    
    # Task 3: Run quality checks
    quality_check = PostgresOperator(
        task_id='quality_check',
        postgres_conn_id='postgres_default',
        sql="""
            SELECT COUNT(*) 
            FROM fact_stock_prices 
            WHERE price_date = CURRENT_DATE;
        """,
    )
    
    # Dependencies
    extract >> load >> quality_check
'''


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def print_dag_template(name: str = "hello"):
    """Print a DAG template."""
    templates = {
        "hello": HELLO_WORLD_DAG,
        "stock": STOCK_PIPELINE_DAG
    }
    
    if name in templates:
        print(templates[name])
    else:
        print(f"Available templates: {', '.join(templates.keys())}")


def check_airflow_status():
    """Check if Airflow is running."""
    import subprocess
    
    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", "name=airflow"],
            capture_output=True,
            text=True
        )
        if "airflow" in result.stdout:
            print("✅ Airflow containers are running")
            print(result.stdout)
        else:
            print("⚠️ No Airflow containers found")
            print("   Run: docker-compose up -d")
    except:
        print("⚠️ Docker not available or Airflow not running")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "dag":
            template = sys.argv[2] if len(sys.argv) > 2 else "hello"
            print_dag_template(template)
        elif cmd == "status":
            check_airflow_status()
    else:
        print("Day 30: Airflow DAG Basics")
        print("=" * 30)
        print("\nIntroduction to Apache Airflow.")
        print("\nCommands:")
        print("  python day30_airflow_basics.py dag hello  - Hello world DAG")
        print("  python day30_airflow_basics.py dag stock  - Stock pipeline DAG")
        print("  python day30_airflow_basics.py status     - Check Airflow status")
