#!/usr/bin/env python3
"""
Day 17: S3 Fundamentals & Best Practices
=========================================
Duration: 2 hours

Learn S3 - the backbone of data engineering on AWS.
Storage, organization, and access patterns for data pipelines.

WHY THIS MATTERS:
- S3 is the universal data lake storage
- Understanding S3 = understanding modern data architecture
- Every data pipeline uses S3 somewhere
- Cost optimization depends on S3 knowledge

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import boto3
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from botocore.exceptions import ClientError

# =============================================================================
# S3 EXERCISES (AWS Console + Code)
# =============================================================================

"""
EXERCISE 1: Create Your First Bucket (15 min)
==============================================

Using AWS Console:

1. Go to S3 service
2. Click "Create bucket"
3. Bucket name: your-name-data-lake-dev (must be globally unique!)
   Example: dante-data-lake-dev
4. Region: us-east-1 (or your preferred)
5. Block Public Access: Keep ALL blocked (default)
6. Versioning: Enable (important for data protection)
7. Tags: Add "Environment: dev", "Project: learning"
8. Click "Create bucket"

Naming conventions:
- company-project-environment (e.g., acme-analytics-prod)
- Use lowercase, hyphens, no underscores
- Be consistent across projects


EXERCISE 2: S3 Organization Structure (20 min)
===============================================

Create a proper data lake structure:

Using AWS Console or CLI:

aws s3api put-object --bucket YOUR-BUCKET --key raw/
aws s3api put-object --bucket YOUR-BUCKET --key processed/
aws s3api put-object --bucket YOUR-BUCKET --key curated/
aws s3api put-object --bucket YOUR-BUCKET --key archive/

Standard data lake layers:
├── raw/              # Original data, never modified
│   ├── api/          # Data from APIs
│   ├── database/     # Database exports
│   └── files/        # Uploaded files
├── processed/        # Cleaned, validated data
├── curated/          # Business-ready, aggregated
└── archive/          # Old data, cheap storage

Partition pattern:
raw/api/users/year=2024/month=01/day=15/users_20240115.json

Why partitions matter:
- Query only what you need
- Massive cost and speed improvements
- Essential for big data


EXERCISE 3: Upload/Download Data (20 min)
==========================================

Practice with CLI and Python:

CLI commands:
# Upload a file
aws s3 cp local_file.json s3://your-bucket/raw/api/

# Upload a folder
aws s3 cp ./data/ s3://your-bucket/raw/ --recursive

# Download a file
aws s3 cp s3://your-bucket/raw/file.json ./local/

# Sync folders (only copy changed files)
aws s3 sync ./data/ s3://your-bucket/raw/

# List bucket contents
aws s3 ls s3://your-bucket/
aws s3 ls s3://your-bucket/raw/ --recursive

See Python code below for programmatic access.


EXERCISE 4: S3 Select - Query Data in Place (15 min)
=====================================================

S3 Select lets you query data without downloading it all.

1. Upload a JSON Lines file to your bucket
2. Use S3 Select to query it
3. Compare cost/speed to downloading entire file

See s3_select_example() function below.


EXERCISE 5: Lifecycle Policies (15 min)
========================================

Automatically manage data lifecycle:

1. Go to your bucket → Management → Lifecycle rules
2. Create a lifecycle rule:
   - Name: "archive-old-data"
   - Apply to: Prefix "archive/"
   - Transitions:
     - Move to S3 Standard-IA after 30 days
     - Move to Glacier after 90 days
   - Expiration: Delete after 365 days

Storage classes:
- Standard: Frequent access, highest cost
- Standard-IA: Infrequent access, lower cost
- Glacier: Archive, very low cost, retrieval takes time
- Deep Archive: Cheapest, retrieval takes hours


EXERCISE 6: Bucket Policies (20 min)
=====================================

Control access at the bucket level:

1. Go to bucket → Permissions → Bucket policy
2. Add a policy that allows read access from a specific IAM role

Example policy (read-only for a role):
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowDataPipelineRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::YOUR_ACCOUNT:role/data-pipeline-role"
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket",
                "arn:aws:s3:::your-bucket/*"
            ]
        }
    ]
}


EXERCISE 7: Event Notifications (15 min)
========================================

Trigger actions when files arrive:

1. Go to bucket → Properties → Event notifications
2. Create a notification:
   - Name: "new-file-notification"
   - Prefix: "raw/" (only for raw folder)
   - Event: PUT (new files)
   - Destination: SNS topic (or Lambda later)

This is how you build reactive pipelines:
New file → S3 event → Lambda → Process → Store
"""

# =============================================================================
# S3 PYTHON HELPERS
# =============================================================================

def get_s3_client():
    """Get S3 client with default credentials."""
    return boto3.client('s3')


def list_buckets() -> List[str]:
    """
    List all S3 buckets in your account.
    
    Returns:
        List of bucket names
    """
    s3 = get_s3_client()
    response = s3.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]


def list_objects(bucket: str, prefix: str = "", max_keys: int = 100) -> List[Dict]:
    """
    List objects in a bucket with optional prefix filter.
    
    Args:
        bucket: Bucket name
        prefix: Only return objects starting with this prefix
        max_keys: Maximum number of objects to return
    
    Returns:
        List of object metadata dicts
    
    Example:
        >>> list_objects("my-bucket", prefix="raw/api/")
    """
    s3 = get_s3_client()
    
    try:
        response = s3.list_objects_v2(
            Bucket=bucket,
            Prefix=prefix,
            MaxKeys=max_keys
        )
        
        objects = []
        for obj in response.get('Contents', []):
            objects.append({
                'key': obj['Key'],
                'size': obj['Size'],
                'last_modified': obj['LastModified'].isoformat(),
                'storage_class': obj.get('StorageClass', 'STANDARD')
            })
        
        return objects
    except ClientError as e:
        print(f"Error: {e}")
        return []


def upload_file(bucket: str, local_path: str, s3_key: str) -> bool:
    """
    Upload a file to S3.
    
    Args:
        bucket: Bucket name
        local_path: Local file path
        s3_key: S3 object key (path in bucket)
    
    Returns:
        True if successful
    
    Example:
        >>> upload_file("my-bucket", "data.json", "raw/api/data.json")
    """
    s3 = get_s3_client()
    
    try:
        s3.upload_file(local_path, bucket, s3_key)
        print(f"✅ Uploaded {local_path} to s3://{bucket}/{s3_key}")
        return True
    except ClientError as e:
        print(f"❌ Upload failed: {e}")
        return False


def download_file(bucket: str, s3_key: str, local_path: str) -> bool:
    """
    Download a file from S3.
    
    Args:
        bucket: Bucket name
        s3_key: S3 object key
        local_path: Local destination path
    
    Returns:
        True if successful
    """
    s3 = get_s3_client()
    
    try:
        s3.download_file(bucket, s3_key, local_path)
        print(f"✅ Downloaded s3://{bucket}/{s3_key} to {local_path}")
        return True
    except ClientError as e:
        print(f"❌ Download failed: {e}")
        return False


def upload_json(bucket: str, s3_key: str, data: Any) -> bool:
    """
    Upload JSON data directly to S3 (no local file needed).
    
    Args:
        bucket: Bucket name
        s3_key: S3 object key
        data: Data to serialize as JSON
    
    Returns:
        True if successful
    """
    s3 = get_s3_client()
    
    try:
        s3.put_object(
            Bucket=bucket,
            Key=s3_key,
            Body=json.dumps(data, indent=2, default=str),
            ContentType='application/json'
        )
        print(f"✅ Uploaded JSON to s3://{bucket}/{s3_key}")
        return True
    except ClientError as e:
        print(f"❌ Upload failed: {e}")
        return False


def read_json(bucket: str, s3_key: str) -> Optional[Any]:
    """
    Read JSON file from S3.
    
    Args:
        bucket: Bucket name
        s3_key: S3 object key
    
    Returns:
        Parsed JSON data
    """
    s3 = get_s3_client()
    
    try:
        response = s3.get_object(Bucket=bucket, Key=s3_key)
        content = response['Body'].read().decode('utf-8')
        return json.loads(content)
    except ClientError as e:
        print(f"❌ Read failed: {e}")
        return None


def generate_partitioned_key(
    prefix: str,
    date: datetime,
    filename: str,
    partition_format: str = "year={Y}/month={m}/day={d}"
) -> str:
    """
    Generate a partitioned S3 key.
    
    Args:
        prefix: Base prefix (e.g., "raw/api/users")
        date: Date for partitioning
        filename: File name
        partition_format: Format string for partitions
    
    Returns:
        Full S3 key
    
    Example:
        >>> generate_partitioned_key("raw/users", datetime(2024, 1, 15), "data.json")
        'raw/users/year=2024/month=01/day=15/data.json'
    """
    partition = partition_format.format(
        Y=date.strftime("%Y"),
        m=date.strftime("%m"),
        d=date.strftime("%d")
    )
    return f"{prefix}/{partition}/{filename}"


def s3_select_example(bucket: str, s3_key: str, query: str) -> List[Dict]:
    """
    Query JSON data in S3 using S3 Select.
    
    This is more efficient than downloading entire files.
    
    Args:
        bucket: Bucket name
        s3_key: S3 key to a JSON Lines file
        query: SQL-like query
    
    Returns:
        Query results
    
    Example:
        >>> s3_select_example(
        ...     "my-bucket",
        ...     "data.jsonl",
        ...     "SELECT * FROM s3object s WHERE s.age > 25"
        ... )
    """
    s3 = get_s3_client()
    
    try:
        response = s3.select_object_content(
            Bucket=bucket,
            Key=s3_key,
            ExpressionType='SQL',
            Expression=query,
            InputSerialization={'JSON': {'Type': 'LINES'}},
            OutputSerialization={'JSON': {}}
        )
        
        results = []
        for event in response['Payload']:
            if 'Records' in event:
                for line in event['Records']['Payload'].decode().strip().split('\n'):
                    if line:
                        results.append(json.loads(line))
        
        return results
    except ClientError as e:
        print(f"❌ S3 Select failed: {e}")
        return []


# =============================================================================
# S3 COST CALCULATOR
# =============================================================================

S3_PRICING = {
    "STANDARD": 0.023,       # per GB per month
    "STANDARD_IA": 0.0125,   # Infrequent Access
    "GLACIER": 0.004,        # Archive
    "DEEP_ARCHIVE": 0.00099  # Deep Archive
}

def estimate_storage_cost(size_gb: float, storage_class: str = "STANDARD", months: int = 1) -> float:
    """
    Estimate S3 storage cost.
    
    Args:
        size_gb: Size in gigabytes
        storage_class: S3 storage class
        months: Number of months
    
    Returns:
        Estimated cost in USD
    """
    rate = S3_PRICING.get(storage_class, S3_PRICING["STANDARD"])
    return size_gb * rate * months


def print_cost_comparison(size_gb: float, months: int = 12) -> None:
    """Print cost comparison across storage classes."""
    print(f"\nCost comparison for {size_gb} GB over {months} months:\n")
    print(f"{'Storage Class':<20} {'Monthly':<12} {'Annual':<12}")
    print("-" * 44)
    
    for storage_class, rate in S3_PRICING.items():
        monthly = size_gb * rate
        annual = monthly * min(months, 12)
        print(f"{storage_class:<20} ${monthly:>10.2f}  ${annual:>10.2f}")


# =============================================================================
# Verification
# =============================================================================

def verify_s3_setup() -> None:
    """Verify S3 setup and permissions."""
    print("=" * 60)
    print("S3 SETUP VERIFICATION")
    print("=" * 60 + "\n")
    
    try:
        buckets = list_buckets()
        print(f"✅ S3 access verified - found {len(buckets)} buckets")
        
        if buckets:
            print("\nYour buckets:")
            for bucket in buckets:
                print(f"   - {bucket}")
        else:
            print("\n⚠️  No buckets found. Create one following Exercise 1.")
        
    except Exception as e:
        print(f"❌ Cannot access S3: {e}")
        print("   Check your AWS credentials and permissions.")
    
    print("\n" + "-" * 40)
    print("Checklist:")
    print("[ ] Created data lake bucket")
    print("[ ] Set up folder structure (raw/processed/curated)")
    print("[ ] Enabled versioning")
    print("[ ] Created lifecycle rules")
    print("[ ] Tested upload/download")
    print("-" * 40)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "verify":
            verify_s3_setup()
        elif cmd == "list":
            buckets = list_buckets()
            print("Your S3 buckets:")
            for b in buckets:
                print(f"  - {b}")
        elif cmd == "cost":
            size = float(sys.argv[2]) if len(sys.argv) > 2 else 100
            print_cost_comparison(size)
        elif cmd == "partition":
            key = generate_partitioned_key(
                "raw/api/users",
                datetime.now(),
                "data.json"
            )
            print(f"Example partitioned key: {key}")
    else:
        print("Day 17: S3 Fundamentals")
        print("=" * 40)
        print("\nThis is an S3-focused day.")
        print("Follow exercises in AWS Console and with this code.")
        print("\nCommands:")
        print("  python day17_s3_fundamentals.py verify    - Verify S3 access")
        print("  python day17_s3_fundamentals.py list      - List your buckets")
        print("  python day17_s3_fundamentals.py cost [GB] - Cost comparison")
        print("  python day17_s3_fundamentals.py partition - Show partition example")
