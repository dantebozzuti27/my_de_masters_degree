#!/usr/bin/env python3
"""
Day 25: Advanced S3 Patterns - Production Data Lake Design
============================================================
Duration: 3-4 hours total

Today you'll master production S3 patterns:
- Data lake organization strategies
- Partitioning for query performance
- Lifecycle policies for cost optimization
- S3 Select for server-side filtering
- Event notifications

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: S3 basics (Day 17)

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
DATA LAKE ORGANIZATION
======================

A data lake is organized storage for raw and processed data.

MEDALLION ARCHITECTURE (Industry Standard):
============================================

    ┌─────────────────────────────────────────────────────────┐
    │                     DATA LAKE                            │
    │                                                          │
    │   ┌─────────┐    ┌─────────┐    ┌─────────┐             │
    │   │ BRONZE  │ ─► │ SILVER  │ ─► │  GOLD   │             │
    │   │  (Raw)  │    │(Cleaned)│    │(Business)│            │
    │   └─────────┘    └─────────┘    └─────────┘             │
    │                                                          │
    │   - Original     - Validated    - Aggregated             │
    │   - Immutable    - Deduplicated - Optimized             │
    │   - Full history - Standardized - Query-ready           │
    └─────────────────────────────────────────────────────────┘


BUCKET STRUCTURE:
=================

    s3://company-data-lake/
    │
    ├── bronze/                    # Raw data (never modify)
    │   ├── source1/
    │   │   └── entity/
    │   │       └── year=YYYY/month=MM/day=DD/
    │   └── source2/
    │
    ├── silver/                    # Cleaned, validated
    │   └── domain/
    │       └── entity/
    │           └── partitions/
    │
    ├── gold/                      # Business-ready
    │   └── domain/
    │       └── aggregates/
    │
    └── _metadata/                 # Schemas, manifests


PARTITIONING STRATEGIES:
========================

1. DATE-BASED (Most common)
   year=2026/month=01/day=25/
   
   - Great for time-series data
   - Enables efficient date range queries
   - Matches typical access patterns

2. CATEGORICAL
   region=us-east/product_category=electronics/
   
   - Great for filtered analysis
   - Reduces data scanned

3. HYBRID
   year=2026/month=01/region=us-east/
   
   - Combines multiple dimensions
   - Balance between partitions

4. HIVE-STYLE vs DIRECTORY-STYLE
   Hive: year=2026/month=01/
   Directory: 2026/01/
   
   Hive-style is preferred (tools understand it automatically)


FILE FORMATS:
=============

1. JSON Lines (.jsonl)
   + Human readable
   + Easy to debug
   - Large file sizes
   - Slow queries
   Use for: Bronze/raw layer

2. Parquet
   + Columnar (fast queries)
   + Compressed (small files)
   + Schema embedded
   - Not human readable
   Use for: Silver/Gold layers

3. CSV
   + Simple
   + Universal
   - No types
   - Large files
   Use for: External data exchange


LEARNING RESOURCES:
==================

VIDEO:
- "Data Lake vs Data Warehouse" - Alex The Analyst (10 min)
  https://www.youtube.com/watch?v=1P_e9CenDY0

READING:
- AWS Well-Architected - Data Analytics Lens
  https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/

- "Fundamentals of Data Engineering" - Chapter 6: Storage
  Focus on: Object Storage patterns
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

import boto3
import json
import os
from datetime import datetime, timezone, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import random

# Initialize S3 client
s3 = boto3.client('s3')
BUCKET = 'dante-data-lake-dev'


"""
EXERCISE 1: CREATE PROPER LAKE STRUCTURE (15 min)
=================================================

Let's set up a proper data lake structure.

Run in terminal:

    # Create bronze/silver/gold structure
    aws s3api put-object --bucket dante-data-lake-dev --key bronze/
    aws s3api put-object --bucket dante-data-lake-dev --key silver/
    aws s3api put-object --bucket dante-data-lake-dev --key gold/
    aws s3api put-object --bucket dante-data-lake-dev --key _metadata/
    
    # Verify
    aws s3 ls s3://dante-data-lake-dev/
"""


"""
EXERCISE 2: IMPLEMENT PARTITIONED WRITES (25 min)
=================================================

Let's build proper partitioning logic.
"""

def generate_partition_path(
    layer: str,
    source: str,
    entity: str,
    timestamp: Optional[datetime] = None,
    extra_partitions: Optional[Dict[str, str]] = None
) -> str:
    """
    Generate a properly partitioned S3 path.
    
    Args:
        layer: bronze, silver, or gold
        source: Data source (e.g., "api", "database")
        entity: Entity name (e.g., "users", "orders")
        timestamp: Timestamp for date partitions
        extra_partitions: Additional partition keys
        
    Returns:
        Partitioned path
        
    Example:
        >>> generate_partition_path("bronze", "api", "users")
        "bronze/api/users/year=2026/month=01/day=25/"
    """
    ts = timestamp or datetime.now(timezone.utc)
    
    # Base path
    path = f"{layer}/{source}/{entity}"
    
    # Date partitions
    path += f"/year={ts.year}/month={ts.month:02d}/day={ts.day:02d}"
    
    # Extra partitions
    if extra_partitions:
        for key, value in extra_partitions.items():
            path += f"/{key}={value}"
    
    return path + "/"


def generate_file_name(entity: str, format: str = "jsonl") -> str:
    """
    Generate unique filename with timestamp.
    
    Returns:
        Filename like: users_20260125_143022_a1b2c3.jsonl
    """
    ts = datetime.now(timezone.utc)
    random_suffix = hex(random.randint(0, 0xFFFFFF))[2:]
    return f"{entity}_{ts.strftime('%Y%m%d_%H%M%S')}_{random_suffix}.{format}"


class PartitionedS3Writer:
    """
    Write data to S3 with proper partitioning.
    """
    
    def __init__(self, bucket: str):
        self.bucket = bucket
        self.s3 = boto3.client('s3')
    
    def write_jsonl(
        self,
        records: List[Dict],
        layer: str,
        source: str,
        entity: str,
        timestamp: Optional[datetime] = None,
        extra_partitions: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Write records as JSON Lines to partitioned location.
        
        Returns:
            S3 key of written file
        """
        # Generate path
        partition_path = generate_partition_path(
            layer, source, entity, timestamp, extra_partitions
        )
        filename = generate_file_name(entity, "jsonl")
        key = partition_path + filename
        
        # Convert to JSONL
        body = '\n'.join(json.dumps(r, default=str) for r in records)
        
        # Upload
        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=body.encode('utf-8'),
            ContentType='application/x-ndjson'
        )
        
        print(f"Wrote {len(records)} records to s3://{self.bucket}/{key}")
        return key


"""
EXERCISE 3: GENERATE TEST DATA (20 min)
=======================================

Let's populate the lake with realistic test data.
"""

def generate_user_records(count: int = 100) -> List[Dict]:
    """Generate fake user records."""
    regions = ['us-east', 'us-west', 'eu-west', 'ap-south']
    
    records = []
    for i in range(count):
        records.append({
            'id': i + 1,
            'username': f'user_{i+1:04d}',
            'email': f'user{i+1}@example.com',
            'region': random.choice(regions),
            'signup_date': (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
            'is_active': random.random() > 0.2,
            'login_count': random.randint(0, 1000)
        })
    return records


def generate_order_records(count: int = 500) -> List[Dict]:
    """Generate fake order records."""
    products = ['laptop', 'phone', 'tablet', 'headphones', 'monitor']
    
    records = []
    for i in range(count):
        order_date = datetime.now() - timedelta(days=random.randint(0, 30))
        records.append({
            'order_id': f'ORD-{i+1:06d}',
            'user_id': random.randint(1, 100),
            'product': random.choice(products),
            'quantity': random.randint(1, 5),
            'price': round(random.uniform(10, 1000), 2),
            'order_date': order_date.isoformat(),
            'region': random.choice(['us-east', 'us-west', 'eu-west'])
        })
    return records


def populate_data_lake():
    """Populate the data lake with test data."""
    writer = PartitionedS3Writer(BUCKET)
    
    print("=" * 60)
    print("POPULATING DATA LAKE")
    print("=" * 60)
    
    # Generate data for multiple days
    for days_ago in range(7):
        date = datetime.now(timezone.utc) - timedelta(days=days_ago)
        
        # Users
        users = generate_user_records(50)
        writer.write_jsonl(users, "bronze", "api", "users", date)
        
        # Orders
        orders = generate_order_records(200)
        writer.write_jsonl(orders, "bronze", "system", "orders", date)
    
    print("\nData lake populated!")


"""
EXERCISE 4: LIFECYCLE POLICIES (25 min)
=======================================

Lifecycle policies automatically manage data over time.

Go to AWS Console:
1. S3 → dante-data-lake-dev → Management
2. Create lifecycle rule

RULE 1: Archive old bronze data
- Name: archive-old-bronze
- Prefix: bronze/
- Transitions:
  - Move to Glacier Instant Retrieval after 90 days
- Expiration: Delete after 365 days

RULE 2: Cleanup incomplete uploads
- Name: cleanup-incomplete
- Prefix: (leave empty for all)
- Delete incomplete multipart uploads after 7 days

RULE 3: Expire old versions
- Name: expire-old-versions
- Prefix: (leave empty)
- Expire noncurrent versions after 30 days
"""


"""
EXERCISE 5: S3 SELECT - QUERY WITHOUT DOWNLOADING (30 min)
==========================================================

S3 Select lets you run SQL queries on S3 data.
The data is filtered ON S3 - you only download matching rows.
"""

def s3_select_query(
    bucket: str,
    key: str,
    query: str,
    input_format: str = 'JSON'
) -> List[Dict]:
    """
    Run S3 Select query on a file.
    
    Args:
        bucket: S3 bucket
        key: S3 key
        query: SQL query
        input_format: JSON or CSV
        
    Returns:
        Query results as list of dicts
    """
    s3 = boto3.client('s3')
    
    # Configure input based on format
    if input_format == 'JSON':
        input_serialization = {
            'JSON': {'Type': 'LINES'}
        }
    else:
        input_serialization = {
            'CSV': {'FileHeaderInfo': 'USE', 'FieldDelimiter': ','}
        }
    
    # Run query
    response = s3.select_object_content(
        Bucket=bucket,
        Key=key,
        ExpressionType='SQL',
        Expression=query,
        InputSerialization=input_serialization,
        OutputSerialization={'JSON': {}}
    )
    
    # Process results
    results = []
    for event in response['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            for line in records.strip().split('\n'):
                if line:
                    results.append(json.loads(line))
    
    return results


def demo_s3_select():
    """Demonstrate S3 Select capabilities."""
    print("=" * 60)
    print("S3 SELECT DEMO")
    print("=" * 60)
    
    # First, let's create a test file
    test_data = [
        {'id': 1, 'name': 'Alice', 'age': 30, 'department': 'Engineering'},
        {'id': 2, 'name': 'Bob', 'age': 25, 'department': 'Sales'},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'department': 'Engineering'},
        {'id': 4, 'name': 'Diana', 'age': 28, 'department': 'Marketing'},
        {'id': 5, 'name': 'Eve', 'age': 32, 'department': 'Engineering'},
    ]
    
    key = 'bronze/test/employees/test_employees.jsonl'
    body = '\n'.join(json.dumps(r) for r in test_data)
    
    s3.put_object(
        Bucket=BUCKET,
        Key=key,
        Body=body.encode('utf-8'),
        ContentType='application/x-ndjson'
    )
    print(f"Created test file: s3://{BUCKET}/{key}")
    
    # Query 1: Select all
    print("\n1. SELECT * (all records):")
    results = s3_select_query(
        BUCKET, key,
        "SELECT * FROM s3object s"
    )
    for r in results:
        print(f"   {r}")
    
    # Query 2: Filter by department
    print("\n2. WHERE department = 'Engineering':")
    results = s3_select_query(
        BUCKET, key,
        "SELECT * FROM s3object s WHERE s.department = 'Engineering'"
    )
    for r in results:
        print(f"   {r}")
    
    # Query 3: Select specific columns
    print("\n3. SELECT name, age WHERE age > 28:")
    results = s3_select_query(
        BUCKET, key,
        "SELECT s.name, s.age FROM s3object s WHERE s.age > 28"
    )
    for r in results:
        print(f"   {r}")
    
    print("\n" + "=" * 60)


"""
EXERCISE 6: LISTING AND DISCOVERING DATA (20 min)
=================================================

Build tools to discover what's in your data lake.
"""

def list_partitions(
    bucket: str,
    prefix: str
) -> Dict[str, List[str]]:
    """
    Discover partition values in a prefix.
    
    Returns dict like:
    {
        'year': ['2025', '2026'],
        'month': ['01', '02'],
        'day': ['01', '02', '03']
    }
    """
    s3 = boto3.client('s3')
    
    paginator = s3.get_paginator('list_objects_v2')
    
    partitions = {}
    
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix, Delimiter='/'):
        for common_prefix in page.get('CommonPrefixes', []):
            prefix_path = common_prefix['Prefix']
            # Extract partition key=value
            parts = prefix_path.rstrip('/').split('/')
            for part in parts:
                if '=' in part:
                    key, value = part.split('=', 1)
                    if key not in partitions:
                        partitions[key] = set()
                    partitions[key].add(value)
    
    return {k: sorted(v) for k, v in partitions.items()}


def get_lake_summary(bucket: str) -> Dict:
    """
    Get summary statistics of the data lake.
    """
    s3 = boto3.client('s3')
    
    layers = ['bronze', 'silver', 'gold']
    summary = {}
    
    for layer in layers:
        paginator = s3.get_paginator('list_objects_v2')
        
        file_count = 0
        total_size = 0
        
        for page in paginator.paginate(Bucket=bucket, Prefix=f"{layer}/"):
            for obj in page.get('Contents', []):
                if not obj['Key'].endswith('/'):
                    file_count += 1
                    total_size += obj['Size']
        
        summary[layer] = {
            'files': file_count,
            'size_bytes': total_size,
            'size_mb': round(total_size / (1024 * 1024), 2)
        }
    
    return summary


def print_lake_summary():
    """Print a nice summary of the data lake."""
    print("=" * 60)
    print("DATA LAKE SUMMARY")
    print("=" * 60)
    
    summary = get_lake_summary(BUCKET)
    
    total_files = 0
    total_size = 0
    
    for layer, stats in summary.items():
        print(f"\n{layer.upper()}:")
        print(f"  Files: {stats['files']}")
        print(f"  Size: {stats['size_mb']} MB")
        total_files += stats['files']
        total_size += stats['size_bytes']
    
    print(f"\nTOTAL:")
    print(f"  Files: {total_files}")
    print(f"  Size: {round(total_size / (1024 * 1024), 2)} MB")


"""
EXERCISE 7: MANIFEST FILES (20 min)
===================================

Manifests track what files are in the lake - essential for processing.
"""

def generate_manifest(
    bucket: str,
    prefix: str,
    output_key: str
) -> Dict:
    """
    Generate a manifest of files in a prefix.
    
    Manifests are used by:
    - Spark to know what files to read
    - Auditing to track data lineage
    - Incremental processing
    """
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    
    files = []
    
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get('Contents', []):
            if not obj['Key'].endswith('/'):
                files.append({
                    'key': obj['Key'],
                    'size': obj['Size'],
                    'last_modified': obj['LastModified'].isoformat()
                })
    
    manifest = {
        'bucket': bucket,
        'prefix': prefix,
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'file_count': len(files),
        'total_bytes': sum(f['size'] for f in files),
        'files': files
    }
    
    # Write manifest
    s3.put_object(
        Bucket=bucket,
        Key=output_key,
        Body=json.dumps(manifest, indent=2),
        ContentType='application/json'
    )
    
    print(f"Generated manifest with {len(files)} files: s3://{bucket}/{output_key}")
    
    return manifest


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Data Lake Concepts:
[ ] Medallion architecture (bronze/silver/gold)
[ ] Partitioning strategies
[ ] File formats (JSON Lines, Parquet, CSV)

S3 Skills:
[ ] Create proper partition paths
[ ] Implement lifecycle policies
[ ] Use S3 Select for queries
[ ] Generate manifests

Best Practices:
[ ] Never modify bronze data
[ ] Use Hive-style partitions
[ ] Implement lifecycle policies for cost
[ ] Generate manifests for processing


KNOWLEDGE CHECK:
================

1. You have 5 years of sales data. How would you partition it
   for efficient monthly reports?

2. Your S3 costs are high. Raw data older than 6 months is rarely accessed.
   What lifecycle policy would you implement?

3. You need to find all orders over $1000 in a 10GB file.
   How can you do this without downloading the whole file?

4. What's the difference between bronze, silver, and gold layers?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 25: Advanced S3 Patterns"
    git push


WHAT'S NEXT:
============
Day 26: PostgreSQL Deep Dive
- Schema design for data engineering
- Indexing strategies
- COPY command for bulk loading
- Query optimization
"""


if __name__ == "__main__":
    print("Choose an exercise:")
    print("1. Populate data lake with test data")
    print("2. Demo S3 Select")
    print("3. Print lake summary")
    print("4. Generate manifest")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        populate_data_lake()
    elif choice == "2":
        demo_s3_select()
    elif choice == "3":
        print_lake_summary()
    elif choice == "4":
        manifest = generate_manifest(
            BUCKET,
            "bronze/",
            "_metadata/bronze_manifest.json"
        )
        print(f"Files: {manifest['file_count']}")
        print(f"Total size: {manifest['total_bytes']} bytes")
