#!/usr/bin/env python3
"""
Day 25: S3 Storage + Data Partitioning
=======================================
Duration: 2-2.5 hours

Learn proper data organization in S3 for analytics workloads.
Partitioning is critical for performance and cost.

WHY THIS MATTERS:
- Partitioning = 10-100x query performance
- Proper structure = lower costs
- This is how data lakes work
- Required for Athena, Glue, Spark

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import json
import boto3
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Understand Partitioning (20 min)
============================================

Why partition?
- Query only the data you need
- Reduce data scanned = lower costs
- Faster query times
- Better data organization

Common partition schemes:
- By date: year=2024/month=01/day=15/
- By source: source=api/date=2024-01-15/
- By region: region=us-east/date=2024-01-15/

Hive-style partitions (key=value):
  s3://bucket/raw/stocks/year=2024/month=01/day=15/data.json

This allows query engines to filter by partition.


EXERCISE 2: Design Your Partition Strategy (20 min)
===================================================

For stock data, design partitions:

Option A: By date only
  raw/stocks/year=2024/month=01/day=15/stocks.json

Option B: By symbol then date
  raw/stocks/symbol=AAPL/year=2024/month=01/day=15/data.json

Option C: By date then symbol
  raw/stocks/year=2024/month=01/day=15/symbol=AAPL/data.json

Best practice for time-series data:
- Date first (most common query filter)
- Then other dimensions
- Avoid too many small files


EXERCISE 3: Implement Partitioned Writer (30 min)
=================================================

Write data with proper partitioning.
See PartitionedS3Writer class below.


EXERCISE 4: Verify Partitions in S3 (15 min)
============================================

Check your partition structure:

aws s3 ls s3://your-bucket/raw/stocks/ --recursive

Should see:
  raw/stocks/year=2024/month=01/day=15/quotes_123456.json
  raw/stocks/year=2024/month=01/day=16/quotes_654321.json


EXERCISE 5: Query with Athena (30 min)
======================================

1. Go to AWS Athena
2. Create database:
   CREATE DATABASE stockdata;

3. Create table with partitions:
   CREATE EXTERNAL TABLE stocks (
     symbol STRING,
     price DOUBLE,
     volume BIGINT,
     timestamp TIMESTAMP
   )
   PARTITIONED BY (year STRING, month STRING, day STRING)
   ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
   LOCATION 's3://your-bucket/raw/stocks/';

4. Load partitions:
   MSCK REPAIR TABLE stocks;

5. Query with partition filter:
   SELECT * FROM stocks 
   WHERE year='2024' AND month='01' AND day='15';


EXERCISE 6: Monitor Costs (15 min)
==================================

Check S3 costs and data scanned:
- Go to S3 → Metrics
- Check bytes stored per prefix
- Compare queries with/without partition filters
"""

# =============================================================================
# IMPLEMENTATION
# =============================================================================

class PartitionedS3Writer:
    """Write data to S3 with proper partitioning."""
    
    def __init__(self, bucket: str, prefix: str = "raw"):
        self.bucket = bucket
        self.prefix = prefix
        self.s3 = boto3.client('s3')
    
    def write(
        self,
        data: List[Dict],
        partition_date: Optional[datetime] = None,
        extra_partitions: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Write data with date partitions.
        
        Args:
            data: List of records to write
            partition_date: Date for partitioning (default: now)
            extra_partitions: Additional partition keys
        
        Returns:
            S3 key where data was written
        """
        if partition_date is None:
            partition_date = datetime.utcnow()
        
        # Build partition path
        partition_path = self._build_partition_path(partition_date, extra_partitions)
        
        # Generate unique filename
        timestamp = datetime.utcnow().strftime("%H%M%S")
        filename = f"data_{timestamp}.json"
        
        key = f"{self.prefix}/{partition_path}/{filename}"
        
        # Write to S3
        self.s3.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=json.dumps(data, indent=2, default=str),
            ContentType='application/json'
        )
        
        print(f"✅ Wrote {len(data)} records to s3://{self.bucket}/{key}")
        return key
    
    def _build_partition_path(
        self,
        date: datetime,
        extra_partitions: Optional[Dict[str, str]] = None
    ) -> str:
        """Build Hive-style partition path."""
        parts = [
            f"year={date.strftime('%Y')}",
            f"month={date.strftime('%m')}",
            f"day={date.strftime('%d')}"
        ]
        
        if extra_partitions:
            for key, value in extra_partitions.items():
                parts.append(f"{key}={value}")
        
        return "/".join(parts)


class PartitionedS3Reader:
    """Read data from partitioned S3 location."""
    
    def __init__(self, bucket: str, prefix: str = "raw"):
        self.bucket = bucket
        self.prefix = prefix
        self.s3 = boto3.client('s3')
    
    def read_date_range(
        self,
        start_date: datetime,
        end_date: datetime
    ) -> List[Dict]:
        """
        Read all data in a date range.
        
        Args:
            start_date: Start of range (inclusive)
            end_date: End of range (inclusive)
        
        Returns:
            Combined list of all records
        """
        all_data = []
        current = start_date
        
        while current <= end_date:
            partition_path = f"year={current.strftime('%Y')}/month={current.strftime('%m')}/day={current.strftime('%d')}"
            prefix = f"{self.prefix}/{partition_path}/"
            
            data = self._read_partition(prefix)
            all_data.extend(data)
            
            current += timedelta(days=1)
        
        return all_data
    
    def _read_partition(self, prefix: str) -> List[Dict]:
        """Read all files in a partition."""
        data = []
        
        try:
            response = self.s3.list_objects_v2(
                Bucket=self.bucket,
                Prefix=prefix
            )
            
            for obj in response.get('Contents', []):
                if obj['Key'].endswith('.json'):
                    file_data = self._read_file(obj['Key'])
                    if isinstance(file_data, list):
                        data.extend(file_data)
                    else:
                        data.append(file_data)
        
        except Exception as e:
            print(f"Error reading {prefix}: {e}")
        
        return data
    
    def _read_file(self, key: str) -> Any:
        """Read a single JSON file."""
        response = self.s3.get_object(Bucket=self.bucket, Key=key)
        content = response['Body'].read().decode('utf-8')
        return json.loads(content)


def demo_partitioning():
    """Demonstrate partitioned writing."""
    bucket = os.environ.get("S3_BUCKET")
    
    if not bucket:
        print("⚠️  Set S3_BUCKET environment variable")
        print("   Example: export S3_BUCKET=my-data-lake")
        return
    
    # Sample data
    sample_data = [
        {"symbol": "AAPL", "price": 175.50, "volume": 1000000},
        {"symbol": "MSFT", "price": 380.25, "volume": 800000},
        {"symbol": "GOOGL", "price": 140.75, "volume": 500000}
    ]
    
    writer = PartitionedS3Writer(bucket, prefix="raw/stocks")
    key = writer.write(sample_data)
    
    print(f"\nData written with Hive-style partitions!")
    print(f"Location: s3://{bucket}/{key}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "demo":
            demo_partitioning()
        elif cmd == "path":
            # Show partition path for a date
            date_str = sys.argv[2] if len(sys.argv) > 2 else datetime.now().strftime("%Y-%m-%d")
            date = datetime.strptime(date_str, "%Y-%m-%d")
            path = f"year={date.strftime('%Y')}/month={date.strftime('%m')}/day={date.strftime('%d')}"
            print(f"Partition path for {date_str}: {path}")
    else:
        print("Day 25: S3 Storage + Data Partitioning")
        print("=" * 40)
        print("\nLearn proper data organization for analytics.")
        print("\nCommands:")
        print("  python day25_s3_partitioning.py demo        - Demo partitioned writing")
        print("  python day25_s3_partitioning.py path [date] - Show partition path")
