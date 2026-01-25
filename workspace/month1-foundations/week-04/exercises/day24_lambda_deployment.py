#!/usr/bin/env python3
"""
Day 24: AWS Lambda Deployment
==============================
Duration: 2-2.5 hours

Deploy your stock extractor as a serverless Lambda function.
Learn the Lambda development workflow.

WHY THIS MATTERS:
- Lambda = serverless data engineering
- No servers to manage
- Pay only for what you use
- This is modern cloud architecture

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import json
import zipfile
from typing import Dict, Any, Optional
from datetime import datetime

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Lambda Basics (20 min)
==================================

Understand Lambda concepts:
- Handler: Entry point function
- Event: Input to your function
- Context: Runtime information
- Layers: Shared dependencies
- Timeout: Max execution time (default 3s)
- Memory: 128MB - 10GB

Lambda structure:
def handler(event, context):
    # Your code here
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


EXERCISE 2: Create Lambda Package (30 min)
==========================================

1. Create lambda folder structure:
   lambda-function/
   ├── handler.py
   └── requirements.txt

2. handler.py (see LAMBDA_HANDLER below)

3. requirements.txt:
   requests==2.31.0

4. Create deployment package:
   cd lambda-function
   pip install -r requirements.txt -t .
   zip -r ../function.zip .


EXERCISE 3: Deploy via Console (20 min)
=======================================

1. Go to AWS Lambda console
2. Create function → Author from scratch
3. Function name: stock-data-extractor
4. Runtime: Python 3.11
5. Upload function.zip
6. Set handler: handler.lambda_handler
7. Environment variables:
   - ALPHA_VANTAGE_API_KEY=your_key
8. Timeout: 30 seconds
9. Test with sample event


EXERCISE 4: Deploy via CLI (20 min)
===================================

# Create role first (or use existing)
aws iam create-role --role-name lambda-execution-role \\
    --assume-role-policy-document file://trust-policy.json

# Create function
aws lambda create-function \\
    --function-name stock-data-extractor \\
    --runtime python3.11 \\
    --handler handler.lambda_handler \\
    --role arn:aws:iam::ACCOUNT:role/lambda-execution-role \\
    --zip-file fileb://function.zip \\
    --timeout 30

# Update function code
aws lambda update-function-code \\
    --function-name stock-data-extractor \\
    --zip-file fileb://function.zip


EXERCISE 5: CloudWatch Scheduling (20 min)
==========================================

Schedule Lambda to run periodically:

1. Go to CloudWatch → Rules → Create rule
2. Schedule: Fixed rate, 1 hour
3. Target: Lambda function → stock-data-extractor
4. Configure input (optional)

Or via CLI:
aws events put-rule \\
    --name hourly-stock-extraction \\
    --schedule-expression "rate(1 hour)"


EXERCISE 6: Add S3 Output (30 min)
==================================

Modify Lambda to write to S3:

1. Add S3 permissions to Lambda role
2. Update code to write to S3
3. Test and verify data lands in bucket
"""

# =============================================================================
# LAMBDA HANDLER TEMPLATE
# =============================================================================

LAMBDA_HANDLER = '''
import os
import json
import boto3
from datetime import datetime
import requests

def lambda_handler(event, context):
    """
    Lambda handler for stock data extraction.
    
    Event can contain:
    - symbols: List of stock symbols to fetch (default: ["AAPL"])
    """
    # Get configuration
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    s3_bucket = os.environ.get("S3_BUCKET")
    
    if not api_key:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Missing API key"})
        }
    
    # Get symbols from event or use default
    symbols = event.get("symbols", ["AAPL"])
    
    # Fetch quotes
    results = []
    for symbol in symbols:
        quote = fetch_quote(symbol, api_key)
        if quote:
            results.append(quote)
    
    # Save to S3 if bucket configured
    if s3_bucket and results:
        save_to_s3(s3_bucket, results)
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "extracted_at": datetime.utcnow().isoformat(),
            "count": len(results),
            "quotes": results
        })
    }


def fetch_quote(symbol: str, api_key: str) -> dict:
    """Fetch stock quote from Alpha Vantage."""
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": api_key
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        quote_data = data.get("Global Quote", {})
        
        if quote_data:
            return {
                "symbol": symbol,
                "price": float(quote_data.get("05. price", 0)),
                "volume": int(quote_data.get("06. volume", 0)),
                "change_percent": quote_data.get("10. change percent", "0%"),
                "timestamp": datetime.utcnow().isoformat()
            }
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
    
    return None


def save_to_s3(bucket: str, data: list) -> None:
    """Save extracted data to S3."""
    s3 = boto3.client("s3")
    
    timestamp = datetime.utcnow().strftime("%Y/%m/%d/%H%M%S")
    key = f"raw/stocks/{timestamp}/quotes.json"
    
    s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=json.dumps(data, indent=2),
        ContentType="application/json"
    )
    
    print(f"Saved to s3://{bucket}/{key}")
'''


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_deployment_package(source_dir: str, output_file: str) -> bool:
    """
    Create a Lambda deployment package (zip file).
    
    Args:
        source_dir: Directory containing Lambda code
        output_file: Output zip file path
    
    Returns:
        True if successful
    """
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_name = os.path.relpath(file_path, source_dir)
                    zf.write(file_path, arc_name)
        
        print(f"✅ Created {output_file}")
        return True
    except Exception as e:
        print(f"❌ Failed: {e}")
        return False


def show_handler_template() -> None:
    """Print the Lambda handler template."""
    print("=" * 60)
    print("LAMBDA HANDLER TEMPLATE (handler.py)")
    print("=" * 60)
    print(LAMBDA_HANDLER)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "template":
            show_handler_template()
        elif cmd == "package":
            if len(sys.argv) > 2:
                create_deployment_package(sys.argv[2], "function.zip")
            else:
                print("Usage: python day24_lambda_deployment.py package <source_dir>")
    else:
        print("Day 24: AWS Lambda Deployment")
        print("=" * 35)
        print("\nDeploy your extractor as a Lambda function.")
        print("\nCommands:")
        print("  python day24_lambda_deployment.py template     - Show handler code")
        print("  python day24_lambda_deployment.py package <dir> - Create zip package")
