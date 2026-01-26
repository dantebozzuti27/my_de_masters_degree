#!/usr/bin/env python3
"""
Day 24: AWS Lambda Basics - Introduction to Serverless
========================================================
Duration: 3-4 hours total

Today you'll learn AWS Lambda from scratch:
- What serverless means and why it matters
- Creating your first Lambda function
- Event triggers and invocation
- Lambda + S3 integration

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: AWS account, CLI configured (Day 16)

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHAT IS SERVERLESS?
===================

"Serverless" doesn't mean "no servers" - it means YOU don't manage servers.

TRADITIONAL:
    You: Provision server → Install OS → Install dependencies → Deploy code
         → Monitor server → Scale manually → Pay 24/7
    
SERVERLESS:
    You: Upload code → Done
    AWS: Everything else


WHAT IS AWS LAMBDA?
===================

Lambda runs your code in response to EVENTS:
- File uploaded to S3
- HTTP request (via API Gateway)
- Schedule (like cron)
- Database change
- Queue message

You pay only when your code runs (per millisecond!).


KEY CONCEPTS:
=============

1. FUNCTION
   Your code packaged for Lambda
   - Handler: The entry point function
   - Runtime: Python, Node.js, etc.
   - Memory: 128 MB to 10 GB
   - Timeout: Up to 15 minutes

2. TRIGGER
   What causes the function to run
   - S3: Object created/deleted
   - API Gateway: HTTP request
   - EventBridge: Schedule
   - SQS: Queue message

3. HANDLER
   The function Lambda calls:
   
   def handler(event, context):
       # event = data from trigger
       # context = runtime info
       return result

4. EVENT
   Data passed to your function
   Different for each trigger type

5. COLD START
   First invocation is slower (loading code)
   Subsequent calls reuse the container


LAMBDA PRICING:
==============
- $0.20 per 1 million requests
- $0.0000166667 per GB-second
- Free tier: 1M requests, 400,000 GB-seconds/month

For a function with 128MB memory running 100ms:
- 1 million invocations ≈ $0.20 + $0.21 = $0.41/month


WHY LAMBDA FOR DATA ENGINEERING?
================================
- Trigger pipelines when data arrives
- Process files without managing servers
- Scale automatically (0 to thousands of concurrent executions)
- Cost-effective for sporadic workloads


LEARNING RESOURCES:
==================

VIDEO:
- "AWS Lambda Tutorial" - TechWorld with Nana (30 min)
  https://www.youtube.com/watch?v=97q30JjEq9Y
  
- "AWS Lambda in 5 Minutes" - Be A Better Dev
  https://www.youtube.com/watch?v=eOBq__h4OJ4

READING:
- AWS Lambda Developer Guide - Getting Started
  https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html

After watching/reading, answer:
1. What triggers can invoke a Lambda function?
2. What is a cold start?
3. How is Lambda priced?
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

"""
EXERCISE 1: CREATE LAMBDA VIA CONSOLE (20 min)
==============================================

Let's create your first Lambda function using the AWS Console.

STEP 1: Go to AWS Console
    https://console.aws.amazon.com/lambda

STEP 2: Click "Create function"

STEP 3: Configure:
    - Author from scratch
    - Function name: hello-lambda
    - Runtime: Python 3.11
    - Architecture: x86_64
    - Permissions: Create a new role with basic Lambda permissions
    
    Click "Create function"

STEP 4: Replace the default code with:

    def lambda_handler(event, context):
        print(f"Received event: {event}")
        
        name = event.get("name", "World")
        message = f"Hello, {name}! From Lambda."
        
        return {
            "statusCode": 200,
            "body": message
        }

STEP 5: Click "Deploy" (orange button)

STEP 6: Test the function
    - Click "Test"
    - Create test event:
      Name: test-event
      Event JSON: {"name": "Data Engineer"}
    - Click "Test"
    
You should see the output!

STEP 7: Check logs
    - Click "Monitor" tab
    - Click "View logs in CloudWatch"
"""


"""
EXERCISE 2: CREATE LAMBDA VIA CLI (25 min)
==========================================

Now let's create a Lambda using the CLI (the production way).

STEP 1: Create project directory

    mkdir -p ~/lambda-practice/hello-cli
    cd ~/lambda-practice/hello-cli

STEP 2: Create the Lambda function code

    cat > ~/lambda-practice/hello-cli/lambda_function.py << 'EOF'
import json
from datetime import datetime, timezone


def lambda_handler(event, context):
    """
    Lambda handler function.
    
    Args:
        event: Event data from trigger
        context: Runtime information
        
    Returns:
        Response dict
    """
    print(f"Function: {context.function_name}")
    print(f"Request ID: {context.aws_request_id}")
    print(f"Event: {json.dumps(event)}")
    
    # Get name from event
    name = event.get("name", "World")
    
    # Build response
    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Hello, {name}!",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "function": context.function_name,
            "request_id": context.aws_request_id
        })
    }
    
    return response
EOF

STEP 3: Create deployment package (ZIP)

    cd ~/lambda-practice/hello-cli
    zip function.zip lambda_function.py

STEP 4: Create IAM role for Lambda (if not exists)

    # Create trust policy
    cat > ~/lambda-practice/trust-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF

    # Create role
    aws iam create-role \
        --role-name lambda-basic-execution \
        --assume-role-policy-document file://$HOME/lambda-practice/trust-policy.json
    
    # Attach basic execution policy
    aws iam attach-role-policy \
        --role-name lambda-basic-execution \
        --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
    
    # Wait for role to propagate
    sleep 10

STEP 5: Get your AWS account ID

    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    echo $ACCOUNT_ID

STEP 6: Create the Lambda function

    cd ~/lambda-practice/hello-cli
    
    aws lambda create-function \
        --function-name hello-cli-lambda \
        --runtime python3.11 \
        --role arn:aws:iam::${ACCOUNT_ID}:role/lambda-basic-execution \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://function.zip \
        --timeout 30 \
        --memory-size 128

STEP 7: Invoke the function

    aws lambda invoke \
        --function-name hello-cli-lambda \
        --payload '{"name": "CLI User"}' \
        --cli-binary-format raw-in-base64-out \
        response.json
    
    cat response.json

STEP 8: Check logs

    aws logs describe-log-groups --log-group-name-prefix /aws/lambda/hello-cli
"""


"""
EXERCISE 3: LAMBDA WITH DEPENDENCIES (30 min)
=============================================

Real Lambda functions have dependencies. Let's handle that.

STEP 1: Create project

    mkdir -p ~/lambda-practice/with-deps
    cd ~/lambda-practice/with-deps

STEP 2: Create requirements.txt

    cat > ~/lambda-practice/with-deps/requirements.txt << 'EOF'
requests>=2.31.0
EOF

STEP 3: Create Lambda function

    cat > ~/lambda-practice/with-deps/lambda_function.py << 'EOF'
import json
import requests
from datetime import datetime, timezone


def lambda_handler(event, context):
    """
    Lambda that fetches data from an API.
    """
    print(f"Starting execution at {datetime.now(timezone.utc)}")
    
    # Get endpoint from event or use default
    endpoint = event.get("endpoint", "users")
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Limit to first 5 for brevity
        if isinstance(data, list):
            data = data[:5]
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "endpoint": endpoint,
                "count": len(data) if isinstance(data, list) else 1,
                "data": data
            })
        }
        
    except requests.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
EOF

STEP 4: Install dependencies to package directory

    cd ~/lambda-practice/with-deps
    pip install -r requirements.txt -t package/

STEP 5: Create deployment package

    cd ~/lambda-practice/with-deps/package
    zip -r ../function.zip .
    
    cd ~/lambda-practice/with-deps
    zip function.zip lambda_function.py

STEP 6: Update or create the function

    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    
    # Try to update existing, or create new
    aws lambda update-function-code \
        --function-name api-fetcher-lambda \
        --zip-file fileb://function.zip \
    || \
    aws lambda create-function \
        --function-name api-fetcher-lambda \
        --runtime python3.11 \
        --role arn:aws:iam::${ACCOUNT_ID}:role/lambda-basic-execution \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://function.zip \
        --timeout 30 \
        --memory-size 128

STEP 7: Test it

    aws lambda invoke \
        --function-name api-fetcher-lambda \
        --payload '{"endpoint": "posts"}' \
        --cli-binary-format raw-in-base64-out \
        response.json
    
    cat response.json | python3 -m json.tool
"""


"""
EXERCISE 4: LAMBDA + S3 TRIGGER (40 min)
========================================

The most common data engineering pattern: process files when uploaded.

STEP 1: Create Lambda for S3 processing

    mkdir -p ~/lambda-practice/s3-processor
    cd ~/lambda-practice/s3-processor

    cat > ~/lambda-practice/s3-processor/lambda_function.py << 'EOF'
import json
import boto3
import logging
from datetime import datetime, timezone
from urllib.parse import unquote_plus

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client
s3 = boto3.client('s3')


def lambda_handler(event, context):
    """
    Process files uploaded to S3.
    
    Triggered when objects are created in the bucket.
    """
    logger.info(f"Received event: {json.dumps(event)}")
    
    # Process each record (could be multiple files)
    for record in event.get('Records', []):
        # Get bucket and key from event
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        size = record['s3']['object']['size']
        
        logger.info(f"Processing: s3://{bucket}/{key} ({size} bytes)")
        
        # Only process JSON files in raw/
        if not key.startswith('raw/') or not key.endswith('.json'):
            logger.info(f"Skipping {key} - not a raw JSON file")
            continue
        
        try:
            # Read the file
            response = s3.get_object(Bucket=bucket, Key=key)
            content = response['Body'].read().decode('utf-8')
            data = json.loads(content)
            
            logger.info(f"Loaded JSON with {len(data) if isinstance(data, list) else 1} records")
            
            # Transform: add processing metadata
            if isinstance(data, list):
                for record in data:
                    record['_processed_at'] = datetime.now(timezone.utc).isoformat()
                    record['_processed_by'] = context.function_name
            else:
                data['_processed_at'] = datetime.now(timezone.utc).isoformat()
                data['_processed_by'] = context.function_name
            
            # Write to processed/
            processed_key = key.replace('raw/', 'processed/')
            
            s3.put_object(
                Bucket=bucket,
                Key=processed_key,
                Body=json.dumps(data, indent=2),
                ContentType='application/json'
            )
            
            logger.info(f"Wrote processed file to s3://{bucket}/{processed_key}")
            
        except Exception as e:
            logger.error(f"Error processing {key}: {e}")
            raise
    
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Processing complete'})
    }
EOF

STEP 2: Create deployment package

    cd ~/lambda-practice/s3-processor
    zip function.zip lambda_function.py

STEP 3: Create IAM policy for S3 access

    cat > ~/lambda-practice/s3-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::dante-data-lake-dev/*"
        }
    ]
}
EOF

    aws iam create-policy \
        --policy-name lambda-s3-access \
        --policy-document file://$HOME/lambda-practice/s3-policy.json

    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    
    aws iam attach-role-policy \
        --role-name lambda-basic-execution \
        --policy-arn arn:aws:iam::${ACCOUNT_ID}:policy/lambda-s3-access

STEP 4: Create the Lambda function

    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    
    aws lambda create-function \
        --function-name s3-file-processor \
        --runtime python3.11 \
        --role arn:aws:iam::${ACCOUNT_ID}:role/lambda-basic-execution \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://function.zip \
        --timeout 60 \
        --memory-size 256

STEP 5: Add S3 trigger permission

    aws lambda add-permission \
        --function-name s3-file-processor \
        --statement-id s3-trigger \
        --action lambda:InvokeFunction \
        --principal s3.amazonaws.com \
        --source-arn arn:aws:s3:::dante-data-lake-dev

STEP 6: Configure S3 to trigger Lambda

Go to AWS Console:
1. S3 → dante-data-lake-dev → Properties
2. Event notifications → Create event notification
3. Name: trigger-on-upload
4. Prefix: raw/
5. Suffix: .json
6. Event types: All object create events
7. Destination: Lambda function → s3-file-processor
8. Save

STEP 7: Test the trigger

    # Create test file
    echo '{"test": true, "data": [1,2,3]}' > /tmp/test_lambda.json
    
    # Upload to S3
    aws s3 cp /tmp/test_lambda.json s3://dante-data-lake-dev/raw/test/test_lambda.json
    
    # Wait a moment, then check processed folder
    sleep 5
    aws s3 ls s3://dante-data-lake-dev/processed/test/

You should see the processed file!
"""


"""
EXERCISE 5: SCHEDULED LAMBDA (20 min)
=====================================

Run Lambda on a schedule (like cron).

STEP 1: Create a scheduled Lambda

    mkdir -p ~/lambda-practice/scheduled
    cd ~/lambda-practice/scheduled

    cat > ~/lambda-practice/scheduled/lambda_function.py << 'EOF'
import json
import boto3
import requests
from datetime import datetime, timezone

s3 = boto3.client('s3')
BUCKET = 'dante-data-lake-dev'


def lambda_handler(event, context):
    """
    Scheduled job: Fetch data from API daily.
    """
    print(f"Scheduled execution at {datetime.now(timezone.utc)}")
    
    # Fetch data
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=30
    )
    data = response.json()
    
    # Add metadata
    for record in data:
        record['_fetched_at'] = datetime.now(timezone.utc).isoformat()
    
    # Generate key with date
    now = datetime.now(timezone.utc)
    key = f"raw/scheduled/users/year={now.year}/month={now.month:02d}/day={now.day:02d}/users.json"
    
    # Upload
    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=json.dumps(data),
        ContentType='application/json'
    )
    
    print(f"Uploaded {len(data)} records to s3://{BUCKET}/{key}")
    
    return {'statusCode': 200}
EOF

STEP 2: Create deployment package with requests

    cd ~/lambda-practice/scheduled
    pip install requests -t package/
    cd package && zip -r ../function.zip . && cd ..
    zip function.zip lambda_function.py

STEP 3: Create function

    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    
    aws lambda create-function \
        --function-name scheduled-data-fetch \
        --runtime python3.11 \
        --role arn:aws:iam::${ACCOUNT_ID}:role/lambda-basic-execution \
        --handler lambda_function.lambda_handler \
        --zip-file fileb://function.zip \
        --timeout 60 \
        --memory-size 256

STEP 4: Create EventBridge rule for schedule

    # Create rule (runs daily at 6 AM UTC)
    aws events put-rule \
        --name daily-data-fetch \
        --schedule-expression "cron(0 6 * * ? *)" \
        --state ENABLED

    # Add Lambda as target
    ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    
    aws events put-targets \
        --rule daily-data-fetch \
        --targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:${ACCOUNT_ID}:function:scheduled-data-fetch"

    # Allow EventBridge to invoke Lambda
    aws lambda add-permission \
        --function-name scheduled-data-fetch \
        --statement-id eventbridge-trigger \
        --action lambda:InvokeFunction \
        --principal events.amazonaws.com \
        --source-arn arn:aws:events:us-east-1:${ACCOUNT_ID}:rule/daily-data-fetch
"""


"""
EXERCISE 6: CLEANUP (10 min)
============================

Let's clean up test resources to avoid charges.

    # Delete Lambda functions (keep the useful ones)
    aws lambda delete-function --function-name hello-lambda
    aws lambda delete-function --function-name hello-cli-lambda
    
    # Keep these for future use:
    # - s3-file-processor
    # - scheduled-data-fetch (you can disable the schedule)
    
    # Disable the schedule (to avoid daily runs)
    aws events disable-rule --name daily-data-fetch
"""


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Lambda concepts:
[ ] What serverless means
[ ] Lambda handler function structure
[ ] Event and context parameters
[ ] Cold starts

Triggers:
[ ] Manual invocation
[ ] S3 triggers (object created)
[ ] Scheduled triggers (EventBridge)

Deployment:
[ ] Console deployment
[ ] CLI deployment
[ ] Deployment packages with dependencies

IAM:
[ ] Lambda execution role
[ ] S3 access policies


KNOWLEDGE CHECK:
================

1. Your Lambda times out after 3 seconds but you need 5 minutes.
   What do you change and what's the maximum?

2. Your Lambda needs to read/write S3 but gets "Access Denied".
   What's missing?

3. You want a Lambda to run every hour. How do you set it up?

4. What's a cold start and when does it happen?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 24: AWS Lambda Basics"
    git push


WHAT'S NEXT:
============
Day 25: Advanced S3 Patterns
- Lifecycle policies
- S3 Select for querying
- Cross-region replication
- Event notifications
"""


if __name__ == "__main__":
    print("Day 24: AWS Lambda Basics")
    print("=" * 50)
    print("\nThis lesson is primarily done in AWS Console and CLI.")
    print("Follow the exercises in the comments above.")
    print("\nKey concepts:")
    print("  - Lambda handler(event, context)")
    print("  - S3 triggers for file processing")
    print("  - Scheduled execution with EventBridge")
