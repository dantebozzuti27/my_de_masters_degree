#!/usr/bin/env python3
"""
Day 17: S3 Fundamentals - Complete Beginner to Production
==========================================================
Duration: 3-4 hours total

Today you'll learn Amazon S3 from absolute scratch - what it is, why it matters,
and how to use it like a senior data engineer.

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: AWS account with CLI configured (Day 16)

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# DAY 17 COMPLETE - S3 Fundamentals mastered
def day17_complete(): return True

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHAT IS S3?
===========
S3 = Simple Storage Service. It's Amazon's object storage service.

Think of it like an infinite hard drive in the cloud where you can store
any type of file: JSON, CSV, Parquet, images, videos, anything.

WHY DOES S3 MATTER FOR DATA ENGINEERING?
========================================
- It's the BACKBONE of modern data architecture
- Every data pipeline stores data in S3
- It's incredibly cheap ($0.023 per GB/month)
- It's infinitely scalable
- It's 99.999999999% durable (11 9s)

KEY CONCEPTS (memorize these):
=============================

1. BUCKET
   - A container for objects (like a folder at the root level)
   - Name must be GLOBALLY unique across ALL of AWS
   - Example: "dante-data-lake-dev" (no one else can use this name)

2. OBJECT
   - Any file you store in S3
   - Has a KEY (the path/filename) and VALUE (the data)
   - Example: Key = "raw/users/2026/01/25/users.json"

3. PREFIX
   - The "folder path" to objects
   - S3 doesn't actually have folders - it's flat storage
   - The "/" in keys creates the illusion of folders
   - Example: Prefix = "raw/users/" returns all objects starting with that

4. STORAGE CLASSES
   - Standard: Frequently accessed data (most expensive)
   - Intelligent-Tiering: Auto-moves based on access patterns
   - Glacier: Archive storage (cheap but slow to retrieve)

5. VERSIONING
   - Keep multiple versions of the same object
   - Protects against accidental deletes
   - ALWAYS enable for production data lakes


LEARNING RESOURCES (Pick 1-2, spend 60-90 min):
===============================================

VIDEO (Choose one):
- AWS S3 Tutorial for Beginners (TechWorld with Nana) - 25 min
  https://www.youtube.com/watch?v=e6w9LwZJFIA
  
- AWS S3 Masterclass (Be A Better Dev) - 45 min  
  https://www.youtube.com/watch?v=tfU0JEZjcsg

READING:
- "Fundamentals of Data Engineering" Chapter 6: Storage
  Focus on: Object Storage section (pages 180-195)
  
- AWS S3 Documentation - Getting Started
  https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html

After watching/reading, answer these questions in your notes:
1. What's the difference between a bucket and an object?
2. Why would you use Glacier instead of Standard storage?
3. What does "11 9s durability" mean in practice?

When you've completed the LEARN section, move to BUILD.
"""

# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

import boto3
import json
import os
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from botocore.exceptions import ClientError

"""
EXERCISE 1: VERIFY YOUR S3 ACCESS (5 min)
=========================================

Before we build anything, let's verify your AWS CLI can access S3.

Run these commands in your terminal:

    aws s3 ls
    
This lists all your buckets. If you see your bucket from Day 16
(dante-data-lake-dev), you're ready.

If you get an error, go back to Day 16 and fix your AWS CLI configuration.
"""


"""
EXERCISE 2: UNDERSTAND BUCKET NAMING (10 min)
=============================================

S3 bucket names have strict rules. Let's understand them.

RULES:
- 3-63 characters long
- Only lowercase letters, numbers, and hyphens
- Must start with a letter or number
- Cannot end with a hyphen
- Cannot contain consecutive periods
- Cannot be formatted like an IP address (e.g., 192.168.1.1)
- GLOBALLY UNIQUE across all AWS accounts worldwide

GOOD NAMES:
- dante-data-lake-dev
- acme-analytics-prod
- my-company-raw-data-2026

BAD NAMES:
- Data_Lake (uppercase and underscore)
- my.bucket.name (consecutive periods)
- -bucket-name (starts with hyphen)
- a (too short)

YOUR TASK:
Think of a naming convention for your future projects:
    {your-name}-{project}-{environment}
    
Example: dante-stockpipeline-dev, dante-stockpipeline-prod
"""


"""
EXERCISE 3: CREATE BUCKET VIA CLI (15 min)
==========================================

You already have a bucket from Day 16, but let's practice creating
one via CLI (the command line - how you'll do it in production).

Run this in your terminal (replace YOUR_UNIQUE_NAME):

    aws s3api create-bucket \
        --bucket YOUR_UNIQUE_NAME-learning-bucket \
        --region us-east-1
        
NOTE: For us-east-1, you don't need LocationConstraint.
For other regions, you'd add:
    --create-bucket-configuration LocationConstraint=us-west-2

Verify it was created:

    aws s3 ls

You should see both buckets now.

IMPORTANT: We'll delete this learning bucket later to avoid charges.
"""


"""
EXERCISE 4: UNDERSTAND DATA LAKE STRUCTURE (20 min)
===================================================

Professional data engineers organize S3 buckets with a standard structure:

    bucket/
    ├── raw/              # Original data, NEVER modified
    │   ├── source1/      # Data from first source
    │   └── source2/      # Data from second source
    ├── processed/        # Cleaned, validated data
    ├── curated/          # Business-ready, aggregated
    └── archive/          # Old data, moved to Glacier

WHY THIS STRUCTURE?
- raw/: Keep original data forever. If you mess up, you can reprocess.
- processed/: Cleaned data that's ready for analysis
- curated/: Final datasets for business users/dashboards
- archive/: Old data you rarely need but must keep

PARTITIONING:
For large datasets, we partition by date:

    raw/users/year=2026/month=01/day=25/users.json
    
WHY PARTITION?
- Query engines (Athena, Spark) only read the partitions you need
- Instead of scanning 1TB, you might scan 10GB for one day
- MASSIVE cost and speed savings

CREATE THE STRUCTURE:
Run these commands in your terminal:

    aws s3api put-object --bucket dante-data-lake-dev --key raw/
    aws s3api put-object --bucket dante-data-lake-dev --key processed/
    aws s3api put-object --bucket dante-data-lake-dev --key curated/
    aws s3api put-object --bucket dante-data-lake-dev --key archive/
    
Verify:

    aws s3 ls s3://dante-data-lake-dev/
    
You should see:
    PRE archive/
    PRE curated/
    PRE processed/
    PRE raw/
"""


"""
EXERCISE 5: UPLOAD DATA WITH CLI (20 min)
=========================================

Let's upload some test data using CLI commands.

STEP 1: Create a test file locally

    echo '{"id": 1, "name": "Alice", "email": "alice@example.com"}' > /tmp/user1.json
    echo '{"id": 2, "name": "Bob", "email": "bob@example.com"}' > /tmp/user2.json

STEP 2: Upload single file

    aws s3 cp /tmp/user1.json s3://dante-data-lake-dev/raw/api/users/
    
STEP 3: Upload with partitioned path (production pattern)

    aws s3 cp /tmp/user2.json s3://dante-data-lake-dev/raw/api/users/year=2026/month=01/day=25/
    
STEP 4: List what you uploaded

    aws s3 ls s3://dante-data-lake-dev/raw/api/users/ --recursive

KEY CLI COMMANDS TO MEMORIZE:

    aws s3 cp <local> <s3>     # Upload file
    aws s3 cp <s3> <local>     # Download file
    aws s3 sync <local> <s3>   # Sync folder (only changed files)
    aws s3 ls <s3-path>        # List objects
    aws s3 rm <s3-path>        # Delete object
    aws s3 rm <s3-path> --recursive  # Delete folder
"""


"""
EXERCISE 6: DOWNLOAD DATA WITH CLI (10 min)
===========================================

Now let's download data from S3.

STEP 1: Download single file

    aws s3 cp s3://dante-data-lake-dev/raw/api/users/user1.json /tmp/downloaded_user1.json
    cat /tmp/downloaded_user1.json

STEP 2: Download entire folder

    mkdir -p /tmp/s3-download
    aws s3 cp s3://dante-data-lake-dev/raw/api/users/ /tmp/s3-download/ --recursive
    ls -la /tmp/s3-download/

STEP 3: Sync (only copy changed files - great for incremental updates)

    mkdir -p /tmp/s3-sync
    aws s3 sync s3://dante-data-lake-dev/raw/api/users/ /tmp/s3-sync/

Run sync again - notice it says "0 files" because nothing changed.
"""


"""
EXERCISE 7: PYTHON + BOTO3 BASICS (30 min)
==========================================

Now let's use Python to interact with S3. This is how you'll build pipelines.

boto3 is the official AWS SDK for Python. You installed it on Day 16.
"""

# S3 Client Setup
def get_s3_client():
    """
    Create an S3 client.
    
    boto3 automatically uses credentials from:
    1. Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    2. ~/.aws/credentials file (created by 'aws configure')
    3. IAM role (when running on AWS)
    """
    return boto3.client('s3')


def list_buckets() -> List[str]:
    """
    List all buckets in your account.
    
    Returns:
        List of bucket names
    """
    s3 = get_s3_client()
    response = s3.list_buckets()
    
    buckets = []
    for bucket in response['Buckets']:
        buckets.append(bucket['Name'])
        print(f"  {bucket['Name']} (created: {bucket['CreationDate']})")
    
    return buckets


def list_objects(bucket: str, prefix: str = "") -> List[Dict]:
    """
    List objects in a bucket with optional prefix filter.
    
    Args:
        bucket: Name of the bucket
        prefix: Filter objects by prefix (e.g., "raw/api/")
        
    Returns:
        List of object metadata dictionaries
    """
    s3 = get_s3_client()
    
    # Use paginator for buckets with many objects (>1000)
    paginator = s3.get_paginator('list_objects_v2')
    
    objects = []
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            objects.append({
                'key': obj['Key'],
                'size': obj['Size'],
                'last_modified': obj['LastModified'].isoformat()
            })
    
    return objects


"""
EXERCISE 8: UPLOAD DATA WITH PYTHON (30 min)
============================================

Let's build production-quality upload functions.
"""

def upload_json(bucket: str, key: str, data: Any) -> bool:
    """
    Upload JSON data to S3.
    
    Args:
        bucket: Bucket name
        key: Object key (path)
        data: Python object to serialize as JSON
        
    Returns:
        True if successful
        
    Example:
        upload_json(
            bucket="dante-data-lake-dev",
            key="raw/api/users/user1.json",
            data={"id": 1, "name": "Alice"}
        )
    """
    s3 = get_s3_client()
    
    try:
        # Serialize to JSON string
        body = json.dumps(data, indent=2, default=str)
        
        # Upload with proper content type
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=body.encode('utf-8'),
            ContentType='application/json'
        )
        
        print(f"✅ Uploaded {key} ({len(body)} bytes)")
        return True
        
    except ClientError as e:
        print(f"❌ Failed to upload {key}: {e}")
        return False


def upload_jsonl(bucket: str, key: str, records: List[Dict]) -> bool:
    """
    Upload data as JSON Lines (one JSON object per line).
    
    JSON Lines (JSONL) is preferred for big data because:
    - Each line is a complete JSON object
    - Can be processed line-by-line (streaming)
    - Works better with Spark, Athena, etc.
    
    Args:
        bucket: Bucket name
        key: Object key (should end with .jsonl)
        records: List of dictionaries
        
    Example:
        upload_jsonl(
            bucket="dante-data-lake-dev",
            key="raw/api/users/users_20260125.jsonl",
            records=[{"id": 1}, {"id": 2}, {"id": 3}]
        )
    """
    s3 = get_s3_client()
    
    try:
        # Convert to JSON Lines format
        lines = [json.dumps(record, default=str) for record in records]
        body = '\n'.join(lines)
        
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=body.encode('utf-8'),
            ContentType='application/x-ndjson'  # JSONL content type
        )
        
        print(f"✅ Uploaded {key} ({len(records)} records, {len(body)} bytes)")
        return True
        
    except ClientError as e:
        print(f"❌ Failed to upload {key}: {e}")
        return False


def generate_partitioned_key(prefix: str, source: str, entity: str) -> str:
    """
    Generate a properly partitioned S3 key.
    
    This is THE pattern for data engineering. Memorize it.
    
    Args:
        prefix: Base prefix (e.g., "raw")
        source: Data source (e.g., "api", "database")
        entity: Entity name (e.g., "users", "orders")
        
    Returns:
        Partitioned key like: raw/api/users/year=2026/month=01/day=25/users_20260125_143022.jsonl
    """
    now = datetime.now(timezone.utc)
    
    partition = f"year={now.year}/month={now.month:02d}/day={now.day:02d}"
    filename = f"{entity}_{now.strftime('%Y%m%d_%H%M%S')}.jsonl"
    
    return f"{prefix}/{source}/{entity}/{partition}/{filename}"


"""
EXERCISE 9: DOWNLOAD DATA WITH PYTHON (20 min)
==============================================

Now let's read data back from S3.
"""

def download_json(bucket: str, key: str) -> Optional[Any]:
    """
    Download and parse JSON from S3.
    
    Args:
        bucket: Bucket name
        key: Object key
        
    Returns:
        Parsed JSON data, or None if failed
    """
    s3 = get_s3_client()
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read().decode('utf-8')
        data = json.loads(body)
        
        print(f"✅ Downloaded {key}")
        return data
        
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            print(f"❌ Object not found: {key}")
        else:
            print(f"❌ Failed to download {key}: {e}")
        return None


def download_jsonl(bucket: str, key: str) -> List[Dict]:
    """
    Download and parse JSON Lines from S3.
    
    Args:
        bucket: Bucket name
        key: Object key
        
    Returns:
        List of parsed records
    """
    s3 = get_s3_client()
    
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read().decode('utf-8')
        
        records = []
        for line in body.strip().split('\n'):
            if line:  # Skip empty lines
                records.append(json.loads(line))
        
        print(f"✅ Downloaded {key} ({len(records)} records)")
        return records
        
    except ClientError as e:
        print(f"❌ Failed to download {key}: {e}")
        return []


def check_object_exists(bucket: str, key: str) -> bool:
    """
    Check if an object exists in S3.
    
    Useful for idempotency - don't re-upload if already exists.
    """
    s3 = get_s3_client()
    
    try:
        s3.head_object(Bucket=bucket, Key=key)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        raise


"""
EXERCISE 10: BUILD A MINI PIPELINE (45 min)
===========================================

Let's put it all together with a real-world pattern:
1. Fetch data from an API
2. Add metadata (ingestion timestamp, source)
3. Upload to S3 with proper partitioning
4. Verify the upload
"""

import requests

def run_pipeline():
    """
    Mini data pipeline: API → S3
    
    This is the core pattern you'll use in production.
    """
    bucket = "dante-data-lake-dev"
    
    print("=" * 60)
    print("MINI DATA PIPELINE")
    print("=" * 60)
    
    # STEP 1: Fetch data from API
    print("\n📥 Step 1: Fetching data from API...")
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/users",
            timeout=30
        )
        response.raise_for_status()
        users = response.json()
        print(f"   Fetched {len(users)} users")
    except requests.RequestException as e:
        print(f"   ❌ Failed to fetch: {e}")
        return
    
    # STEP 2: Add metadata to each record
    print("\n🏷️  Step 2: Adding metadata...")
    ingestion_time = datetime.now(timezone.utc).isoformat()
    
    for user in users:
        user['_ingested_at'] = ingestion_time
        user['_source'] = 'jsonplaceholder_api'
        user['_pipeline_version'] = '1.0'
    
    print(f"   Added metadata to {len(users)} records")
    
    # STEP 3: Generate partitioned key
    print("\n📁 Step 3: Generating partitioned key...")
    key = generate_partitioned_key(
        prefix="raw",
        source="api",
        entity="users"
    )
    print(f"   Key: {key}")
    
    # STEP 4: Check if already exists (idempotency)
    print("\n🔍 Step 4: Checking for existing data...")
    if check_object_exists(bucket, key):
        print(f"   ⚠️  Object already exists, skipping upload")
        return
    print("   Object does not exist, proceeding with upload")
    
    # STEP 5: Upload to S3
    print("\n📤 Step 5: Uploading to S3...")
    success = upload_jsonl(bucket, key, users)
    
    if not success:
        print("   ❌ Pipeline failed!")
        return
    
    # STEP 6: Verify the upload
    print("\n✅ Step 6: Verifying upload...")
    downloaded = download_jsonl(bucket, key)
    
    if len(downloaded) == len(users):
        print(f"   ✅ Verified: {len(downloaded)} records match!")
    else:
        print(f"   ❌ Mismatch: expected {len(users)}, got {len(downloaded)}")
    
    # Summary
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(f"Records processed: {len(users)}")
    print(f"S3 location: s3://{bucket}/{key}")


"""
EXERCISE 11: LIFECYCLE POLICIES (20 min - Console)
===================================================

Lifecycle policies automatically manage data as it ages.

Go to AWS Console:
1. S3 → Your bucket → Management tab
2. Create lifecycle rule:
   - Name: "archive-old-raw-data"
   - Scope: Prefix "raw/"
   - Transitions:
     * Move to Glacier after 90 days
   - Expiration:
     * Delete after 365 days

This automatically:
- Moves old raw data to cheap storage
- Deletes ancient data you don't need
- Saves money without manual intervention
"""


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Technical Skills - can you do these without looking?
[ ] Create an S3 bucket with aws s3api
[ ] Upload a file with aws s3 cp
[ ] Download a file with aws s3 cp
[ ] List objects with aws s3 ls
[ ] Upload JSON with boto3 put_object()
[ ] Download JSON with boto3 get_object()
[ ] Generate partitioned S3 keys

Concepts - can you explain these?
[ ] What's the difference between a bucket and an object?
[ ] Why do we partition data by date?
[ ] What's the difference between S3 Standard and Glacier?
[ ] Why use JSON Lines instead of regular JSON?
[ ] What does "idempotent" mean for a pipeline?

KNOWLEDGE CHECK QUESTIONS:
==========================

1. You have 5 years of sales data (500GB). Users only query the last 30 days.
   How would you structure this in S3? What lifecycle policy would you use?
   
2. Your pipeline runs daily at midnight. Sometimes it fails and reruns.
   How do you prevent duplicate data in S3?
   
3. A data scientist complains that Athena queries are slow. They're querying
   one day of data but it takes 10 minutes. What's likely wrong?

Write your answers in a notes file before moving on.


COMMIT YOUR WORK:
================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 17: S3 Fundamentals"
    git push

WHAT'S NEXT:
============
Day 18: Docker Fundamentals
- What Docker is and why it matters
- Images vs containers
- Building your first Dockerfile
- Running containers locally
"""


# =============================================================================
# MAIN - Test your code
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("DAY 17: S3 FUNDAMENTALS")
    print("=" * 60)
    
    print("\nChoose an exercise to test:")
    print("1. List buckets")
    print("2. List objects in bucket")
    print("3. Run mini pipeline")
    print("4. Test upload/download")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        print("\n📦 Your S3 Buckets:")
        list_buckets()
        
    elif choice == "2":
        bucket = input("Bucket name: ").strip() or "dante-data-lake-dev"
        prefix = input("Prefix (or Enter for all): ").strip()
        
        print(f"\n📂 Objects in s3://{bucket}/{prefix}")
        objects = list_objects(bucket, prefix)
        for obj in objects:
            print(f"  {obj['key']} ({obj['size']} bytes)")
        print(f"\nTotal: {len(objects)} objects")
        
    elif choice == "3":
        run_pipeline()
        
    elif choice == "4":
        bucket = "dante-data-lake-dev"
        
        # Test upload
        test_data = {"test": True, "timestamp": datetime.now().isoformat()}
        key = "raw/test/test_upload.json"
        
        print("\n📤 Testing upload...")
        upload_json(bucket, key, test_data)
        
        print("\n📥 Testing download...")
        downloaded = download_json(bucket, key)
        print(f"Downloaded: {downloaded}")
        
        print("\n🗑️  Cleaning up test file...")
        s3 = get_s3_client()
        s3.delete_object(Bucket=bucket, Key=key)
        print("Done!")
    
    else:
        print("Invalid choice")
