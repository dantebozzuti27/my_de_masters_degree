#!/usr/bin/env python3
"""
Day 20: Week 3 Project - Containerized S3 Data Pipeline
========================================================
Duration: 3-4 hours total

Today you'll build a COMPLETE production-style data pipeline:
- Dockerized Python application
- Fetches data from multiple APIs
- Uploads to S3 with proper partitioning
- Logs everything properly
- Handles errors gracefully

This is the culmination of Week 3. You're combining:
- S3 knowledge (Day 17)
- Docker knowledge (Days 18-19)
- Python skills (Weeks 1-2)

DAILY STRUCTURE:
├── LEARN (30 min): Review architecture patterns
├── BUILD (3+ hrs): Build the complete pipeline
└── REVIEW (30 min): Document + commit

PREREQUISITES: Days 17-19 completed

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (30 minutes)
# =============================================================================
"""
PRODUCTION DATA PIPELINE ARCHITECTURE
=====================================

Before building, let's understand the pattern we're implementing.


WHAT WE'RE BUILDING:
-------------------

    ┌─────────────────────────────────────────────────────────┐
    │                    Docker Container                      │
    │  ┌──────────────────────────────────────────────────┐   │
    │  │                  Data Pipeline                    │   │
    │  │                                                   │   │
    │  │   ┌───────────┐     ┌────────────┐     ┌──────┐  │   │
    │  │   │  Extract  │ ──► │ Transform  │ ──► │ Load │  │   │
    │  │   │  (APIs)   │     │ (Metadata) │     │ (S3) │  │   │
    │  │   └───────────┘     └────────────┘     └──────┘  │   │
    │  │                                                   │   │
    │  │   ┌───────────────────────────────────────────┐  │   │
    │  │   │              Logging & Metrics            │  │   │
    │  │   └───────────────────────────────────────────┘  │   │
    │  └──────────────────────────────────────────────────┘   │
    └─────────────────────────────────────────────────────────┘
                              │
                              ▼
    ┌─────────────────────────────────────────────────────────┐
    │                    Amazon S3                             │
    │                                                          │
    │  dante-data-lake-dev/                                    │
    │  ├── raw/                                                │
    │  │   └── api/                                            │
    │  │       ├── users/year=2026/month=01/day=26/           │
    │  │       ├── posts/year=2026/month=01/day=26/           │
    │  │       └── comments/year=2026/month=01/day=26/        │
    │  └── processed/                                          │
    └─────────────────────────────────────────────────────────┘


KEY PATTERNS WE'LL IMPLEMENT:
----------------------------

1. CONFIGURATION FROM ENVIRONMENT
   - Never hardcode secrets
   - Different configs for dev/prod
   
2. STRUCTURED LOGGING
   - JSON format for production
   - Log levels (INFO, ERROR, DEBUG)
   - Timestamps and context
   
3. ERROR HANDLING
   - Retry logic for API calls
   - Graceful failure
   - Error reporting
   
4. DATA ENRICHMENT
   - Add ingestion timestamp
   - Add source information
   - Add pipeline version
   
5. PARTITIONED STORAGE
   - Year/month/day partitions
   - Enables efficient querying
   - Standard data lake pattern


READING (Optional):
==================
- "Fundamentals of Data Engineering" - Chapter 8: Ingestion
- AWS Well-Architected Framework - Data Analytics Lens


Let's build it.
"""


# =============================================================================
# PART 2: BUILD (3+ hours)
# =============================================================================

"""
PROJECT STRUCTURE:
==================

We'll build this project from scratch:

    ~/week3-project/
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    ├── .env.example
    └── src/
        ├── __init__.py
        ├── config.py         # Configuration management
        ├── logging_setup.py  # Structured logging
        ├── s3_client.py      # S3 operations
        ├── api_client.py     # API fetching with retries
        ├── pipeline.py       # Main orchestration
        └── main.py           # Entry point


EXERCISE 1: CREATE PROJECT STRUCTURE (10 min)
==============================================

Run these commands in your terminal:

    # Create project directory
    mkdir -p ~/week3-project/src
    cd ~/week3-project
    
    # Create __init__.py
    touch ~/week3-project/src/__init__.py
"""


"""
EXERCISE 2: CONFIGURATION MODULE (15 min)
=========================================

Create the configuration module. This is how production code handles settings.
"""

# File: ~/week3-project/src/config.py
CONFIG_PY = '''
"""
Configuration Module
====================
Loads configuration from environment variables with sensible defaults.

USAGE:
    from config import Config
    config = Config()
    print(config.s3_bucket)
"""

import os
from dataclasses import dataclass
from typing import List


@dataclass
class Config:
    """Pipeline configuration loaded from environment variables."""
    
    # S3 Settings
    s3_bucket: str = ""
    s3_prefix: str = "raw"
    aws_region: str = "us-east-1"
    
    # API Settings
    api_base_url: str = "https://jsonplaceholder.typicode.com"
    api_timeout: int = 30
    api_retry_count: int = 3
    
    # Pipeline Settings
    pipeline_name: str = "week3-pipeline"
    pipeline_version: str = "1.0.0"
    log_level: str = "INFO"
    
    # Endpoints to fetch
    endpoints: List[str] = None
    
    def __post_init__(self):
        """Load values from environment, overriding defaults."""
        self.s3_bucket = os.getenv("S3_BUCKET", self.s3_bucket)
        self.s3_prefix = os.getenv("S3_PREFIX", self.s3_prefix)
        self.aws_region = os.getenv("AWS_REGION", self.aws_region)
        
        self.api_base_url = os.getenv("API_BASE_URL", self.api_base_url)
        self.api_timeout = int(os.getenv("API_TIMEOUT", self.api_timeout))
        self.api_retry_count = int(os.getenv("API_RETRY_COUNT", self.api_retry_count))
        
        self.pipeline_name = os.getenv("PIPELINE_NAME", self.pipeline_name)
        self.pipeline_version = os.getenv("PIPELINE_VERSION", self.pipeline_version)
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)
        
        # Parse endpoints from comma-separated string
        endpoints_str = os.getenv("ENDPOINTS", "users,posts,comments")
        self.endpoints = [e.strip() for e in endpoints_str.split(",")]
    
    def validate(self) -> bool:
        """Validate required configuration is present."""
        if not self.s3_bucket:
            raise ValueError("S3_BUCKET environment variable is required")
        return True
    
    def __str__(self) -> str:
        return f"""
Pipeline Configuration:
  S3 Bucket: {self.s3_bucket}
  S3 Prefix: {self.s3_prefix}
  API URL: {self.api_base_url}
  Endpoints: {self.endpoints}
  Log Level: {self.log_level}
"""
'''

"""
Create the file:

    cat > ~/week3-project/src/config.py << 'CONFIGEOF'
# Paste the CONFIG_PY content here
CONFIGEOF

Or copy from this lesson file.
"""


"""
EXERCISE 3: LOGGING MODULE (20 min)
===================================

Production pipelines use structured logging (JSON format).
"""

# File: ~/week3-project/src/logging_setup.py
LOGGING_PY = '''
"""
Logging Module
==============
Configures structured logging for production pipelines.

Features:
- JSON format for log aggregation (CloudWatch, ELK, etc.)
- Configurable log levels
- Automatic context (timestamp, level, module)
"""

import logging
import json
import sys
from datetime import datetime, timezone
from typing import Any, Dict


class JSONFormatter(logging.Formatter):
    """Formats log records as JSON for production systems."""
    
    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }
        
        # Add exception info if present
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        
        # Add extra fields if provided
        if hasattr(record, "extra_data"):
            log_entry.update(record.extra_data)
        
        return json.dumps(log_entry)


class PrettyFormatter(logging.Formatter):
    """Human-readable format for local development."""
    
    def format(self, record: logging.LogRecord) -> str:
        timestamp = datetime.now().strftime("%H:%M:%S")
        return f"{timestamp} [{record.levelname:5}] {record.name}: {record.getMessage()}"


def setup_logging(name: str = "pipeline", level: str = "INFO", json_format: bool = True) -> logging.Logger:
    """
    Configure and return a logger.
    
    Args:
        name: Logger name
        level: Log level (DEBUG, INFO, WARNING, ERROR)
        json_format: Use JSON format (True for production, False for local)
    
    Returns:
        Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    
    # Remove existing handlers
    logger.handlers.clear()
    
    # Create handler
    handler = logging.StreamHandler(sys.stdout)
    
    # Choose formatter
    if json_format:
        handler.setFormatter(JSONFormatter())
    else:
        handler.setFormatter(PrettyFormatter())
    
    logger.addHandler(handler)
    
    return logger


def log_with_context(logger: logging.Logger, level: str, message: str, **context):
    """Log a message with additional context data."""
    record = logger.makeRecord(
        logger.name,
        getattr(logging, level.upper()),
        "",
        0,
        message,
        (),
        None
    )
    record.extra_data = context
    logger.handle(record)
'''


"""
EXERCISE 4: S3 CLIENT MODULE (25 min)
=====================================

A reusable S3 client with error handling.
"""

# File: ~/week3-project/src/s3_client.py
S3_CLIENT_PY = '''
"""
S3 Client Module
================
Handles all S3 operations with proper error handling.

Features:
- JSON and JSONL uploads
- Partitioned key generation
- Existence checking (idempotency)
- Comprehensive error handling
"""

import boto3
import json
import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from botocore.exceptions import ClientError


class S3Client:
    """Production-ready S3 client."""
    
    def __init__(self, bucket: str, region: str = "us-east-1"):
        """
        Initialize S3 client.
        
        Args:
            bucket: S3 bucket name
            region: AWS region
        """
        self.bucket = bucket
        self.region = region
        self.client = boto3.client("s3", region_name=region)
        self.logger = logging.getLogger("pipeline.s3")
    
    def generate_partitioned_key(
        self,
        prefix: str,
        source: str,
        entity: str,
        timestamp: Optional[datetime] = None
    ) -> str:
        """
        Generate a properly partitioned S3 key.
        
        Args:
            prefix: Base prefix (e.g., "raw", "processed")
            source: Data source (e.g., "api", "database")
            entity: Entity name (e.g., "users", "posts")
            timestamp: Timestamp for partition (defaults to now)
        
        Returns:
            Partitioned key like: raw/api/users/year=2026/month=01/day=26/users_20260126_143022.jsonl
        """
        ts = timestamp or datetime.now(timezone.utc)
        
        partition = f"year={ts.year}/month={ts.month:02d}/day={ts.day:02d}"
        filename = f"{entity}_{ts.strftime('%Y%m%d_%H%M%S')}.jsonl"
        
        return f"{prefix}/{source}/{entity}/{partition}/{filename}"
    
    def upload_jsonl(self, key: str, records: List[Dict]) -> bool:
        """
        Upload records as JSON Lines format.
        
        Args:
            key: S3 object key
            records: List of dictionaries
        
        Returns:
            True if successful
        """
        try:
            # Convert to JSONL
            lines = [json.dumps(record, default=str) for record in records]
            body = "\\n".join(lines)
            
            # Upload
            self.client.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=body.encode("utf-8"),
                ContentType="application/x-ndjson"
            )
            
            self.logger.info(
                f"Uploaded {len(records)} records to s3://{self.bucket}/{key}"
            )
            return True
            
        except ClientError as e:
            self.logger.error(f"Failed to upload {key}: {e}")
            return False
    
    def check_exists(self, key: str) -> bool:
        """Check if an object exists in S3."""
        try:
            self.client.head_object(Bucket=self.bucket, Key=key)
            return True
        except ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return False
            raise
    
    def list_objects(self, prefix: str) -> List[Dict]:
        """List objects with a given prefix."""
        try:
            paginator = self.client.get_paginator("list_objects_v2")
            objects = []
            
            for page in paginator.paginate(Bucket=self.bucket, Prefix=prefix):
                for obj in page.get("Contents", []):
                    objects.append({
                        "key": obj["Key"],
                        "size": obj["Size"],
                        "last_modified": obj["LastModified"].isoformat()
                    })
            
            return objects
            
        except ClientError as e:
            self.logger.error(f"Failed to list objects: {e}")
            return []
'''


"""
EXERCISE 5: API CLIENT MODULE (25 min)
======================================

API client with retry logic.
"""

# File: ~/week3-project/src/api_client.py
API_CLIENT_PY = '''
"""
API Client Module
=================
Handles API requests with retry logic and error handling.

Features:
- Automatic retries with exponential backoff
- Timeout handling
- Structured error responses
"""

import requests
import logging
import time
from typing import Any, Dict, List, Optional


class APIClient:
    """Production-ready API client with retries."""
    
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        max_retries: int = 3
    ):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL for API
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        self.logger = logging.getLogger("pipeline.api")
    
    def fetch(self, endpoint: str) -> Optional[List[Dict]]:
        """
        Fetch data from an endpoint with retries.
        
        Args:
            endpoint: API endpoint (e.g., "users")
        
        Returns:
            List of records, or None if all retries failed
        """
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(1, self.max_retries + 1):
            try:
                self.logger.info(f"Fetching {url} (attempt {attempt})")
                
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                
                data = response.json()
                self.logger.info(f"Fetched {len(data)} records from {endpoint}")
                
                return data
                
            except requests.Timeout:
                self.logger.warning(f"Timeout on attempt {attempt}")
                
            except requests.HTTPError as e:
                self.logger.error(f"HTTP error: {e}")
                if response.status_code >= 400 and response.status_code < 500:
                    # Client error - don't retry
                    return None
                
            except requests.RequestException as e:
                self.logger.error(f"Request failed: {e}")
            
            # Exponential backoff before retry
            if attempt < self.max_retries:
                wait_time = 2 ** attempt
                self.logger.info(f"Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
        
        self.logger.error(f"All {self.max_retries} attempts failed for {endpoint}")
        return None
'''


"""
EXERCISE 6: MAIN PIPELINE MODULE (30 min)
=========================================

The orchestration logic that ties everything together.
"""

# File: ~/week3-project/src/pipeline.py
PIPELINE_PY = '''
"""
Pipeline Module
===============
Main orchestration logic for the data pipeline.

This is where all components come together.
"""

import logging
from datetime import datetime, timezone
from typing import Dict, List, Any
from dataclasses import dataclass, field

from config import Config
from s3_client import S3Client
from api_client import APIClient


@dataclass
class PipelineMetrics:
    """Track pipeline execution metrics."""
    start_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: datetime = None
    endpoints_processed: int = 0
    endpoints_failed: int = 0
    total_records: int = 0
    total_bytes: int = 0
    
    @property
    def duration_seconds(self) -> float:
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0


class DataPipeline:
    """Main pipeline orchestrator."""
    
    def __init__(self, config: Config):
        """
        Initialize pipeline with configuration.
        
        Args:
            config: Pipeline configuration
        """
        self.config = config
        self.logger = logging.getLogger("pipeline.main")
        
        # Initialize clients
        self.s3 = S3Client(
            bucket=config.s3_bucket,
            region=config.aws_region
        )
        self.api = APIClient(
            base_url=config.api_base_url,
            timeout=config.api_timeout,
            max_retries=config.api_retry_count
        )
        
        self.metrics = PipelineMetrics()
    
    def run(self) -> bool:
        """
        Execute the pipeline.
        
        Returns:
            True if all endpoints succeeded, False otherwise
        """
        self.logger.info("=" * 60)
        self.logger.info("PIPELINE STARTING")
        self.logger.info(f"Endpoints: {self.config.endpoints}")
        self.logger.info("=" * 60)
        
        run_timestamp = datetime.now(timezone.utc)
        
        for endpoint in self.config.endpoints:
            success = self._process_endpoint(endpoint, run_timestamp)
            
            if success:
                self.metrics.endpoints_processed += 1
            else:
                self.metrics.endpoints_failed += 1
        
        self.metrics.end_time = datetime.now(timezone.utc)
        self._log_summary()
        
        return self.metrics.endpoints_failed == 0
    
    def _process_endpoint(self, endpoint: str, timestamp: datetime) -> bool:
        """
        Process a single endpoint: fetch, transform, load.
        
        Args:
            endpoint: API endpoint name
            timestamp: Run timestamp for partitioning
        
        Returns:
            True if successful
        """
        self.logger.info(f"Processing endpoint: {endpoint}")
        
        # EXTRACT
        records = self.api.fetch(endpoint)
        if records is None:
            self.logger.error(f"Failed to fetch {endpoint}")
            return False
        
        # TRANSFORM - Add metadata
        enriched_records = self._enrich_records(records, endpoint)
        self.metrics.total_records += len(enriched_records)
        
        # LOAD - Upload to S3
        key = self.s3.generate_partitioned_key(
            prefix=self.config.s3_prefix,
            source="api",
            entity=endpoint,
            timestamp=timestamp
        )
        
        success = self.s3.upload_jsonl(key, enriched_records)
        
        if success:
            self.logger.info(f"✅ {endpoint}: {len(records)} records → s3://{self.config.s3_bucket}/{key}")
        
        return success
    
    def _enrich_records(self, records: List[Dict], source: str) -> List[Dict]:
        """Add metadata to each record."""
        ingested_at = datetime.now(timezone.utc).isoformat()
        
        for record in records:
            record["_metadata"] = {
                "ingested_at": ingested_at,
                "source": source,
                "pipeline_name": self.config.pipeline_name,
                "pipeline_version": self.config.pipeline_version
            }
        
        return records
    
    def _log_summary(self):
        """Log pipeline execution summary."""
        self.logger.info("=" * 60)
        self.logger.info("PIPELINE COMPLETE")
        self.logger.info(f"Duration: {self.metrics.duration_seconds:.2f}s")
        self.logger.info(f"Endpoints processed: {self.metrics.endpoints_processed}")
        self.logger.info(f"Endpoints failed: {self.metrics.endpoints_failed}")
        self.logger.info(f"Total records: {self.metrics.total_records}")
        self.logger.info("=" * 60)
'''


"""
EXERCISE 7: ENTRY POINT (15 min)
================================

The main entry point that runs the pipeline.
"""

# File: ~/week3-project/src/main.py
MAIN_PY = '''
#!/usr/bin/env python3
"""
Pipeline Entry Point
====================
Run with: python main.py
"""

import sys
from config import Config
from logging_setup import setup_logging
from pipeline import DataPipeline


def main():
    # Load configuration
    config = Config()
    
    # Set up logging
    # Use JSON format in production, pretty format locally
    use_json = config.log_level != "DEBUG"
    logger = setup_logging(
        name="pipeline",
        level=config.log_level,
        json_format=use_json
    )
    
    # Validate configuration
    try:
        config.validate()
    except ValueError as e:
        logger.error(f"Configuration error: {e}")
        sys.exit(1)
    
    logger.info(str(config))
    
    # Create and run pipeline
    pipeline = DataPipeline(config)
    success = pipeline.run()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
'''


"""
EXERCISE 8: REQUIREMENTS FILE (5 min)
=====================================

Create the requirements.txt file.
"""

REQUIREMENTS_TXT = '''boto3>=1.28.0
requests>=2.31.0
'''

"""
Command:
    cat > ~/week3-project/requirements.txt << 'EOF'
boto3>=1.28.0
requests>=2.31.0
EOF
"""


"""
EXERCISE 9: DOCKERFILE (15 min)
===============================

Production-ready Dockerfile.
"""

DOCKERFILE = '''# Multi-stage build for smaller production image
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim AS production

# Don't run as root
RUN useradd --create-home --shell /bin/bash pipeline

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /home/pipeline/.local

# Make sure scripts in .local are usable
ENV PATH=/home/pipeline/.local/bin:$PATH

# Copy application code
COPY src/ ./

# Switch to non-root user
USER pipeline

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \\
    CMD python -c "import boto3; print('OK')"

CMD ["python", "main.py"]
'''


"""
EXERCISE 10: DOCKER COMPOSE (15 min)
====================================

Docker Compose for easy running.
"""

DOCKER_COMPOSE_YML = '''version: '3.8'

services:
  pipeline:
    build: .
    container_name: week3-pipeline
    environment:
      # Required
      S3_BUCKET: dante-data-lake-dev
      
      # Optional - override defaults
      S3_PREFIX: raw
      API_BASE_URL: https://jsonplaceholder.typicode.com
      ENDPOINTS: users,posts,comments
      LOG_LEVEL: INFO
      
      # AWS credentials (from host)
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      AWS_REGION: us-east-1
    
    # Mount AWS credentials from host
    volumes:
      - ~/.aws:/home/pipeline/.aws:ro
'''


"""
EXERCISE 11: CREATE ALL FILES (15 min)
======================================

Now let's create all the files. You can either:

A) Copy each module from this lesson file into the appropriate location
B) Run this script to create them all:

    cd ~/week3-project
    
    # Create each file...
    # (Copy the contents from the code blocks above)

After creating all files, verify structure:

    ls -la ~/week3-project/
    ls -la ~/week3-project/src/
"""


"""
EXERCISE 12: BUILD AND RUN (20 min)
===================================

STEP 1: Build the Docker image

    cd ~/week3-project
    docker compose build

STEP 2: Run the pipeline

    # Make sure AWS credentials are available
    export AWS_ACCESS_KEY_ID=$(aws configure get aws_access_key_id)
    export AWS_SECRET_ACCESS_KEY=$(aws configure get aws_secret_access_key)
    
    # Run the pipeline
    docker compose up

STEP 3: Verify data in S3

    aws s3 ls s3://dante-data-lake-dev/raw/api/ --recursive

You should see files for users, posts, and comments!

STEP 4: Check the data

    aws s3 cp s3://dante-data-lake-dev/raw/api/users/year=2026/month=01/day=26/<filename>.jsonl - | head -5
"""


"""
EXERCISE 13: ADD ERROR HANDLING TEST (15 min)
=============================================

Let's test that our error handling works.

STEP 1: Run with a bad endpoint

    docker compose run -e ENDPOINTS=users,invalid_endpoint,posts pipeline

The pipeline should:
- Successfully process users
- Fail on invalid_endpoint (but continue)
- Successfully process posts
- Report 1 failure in summary

STEP 2: Run with no bucket

    docker compose run -e S3_BUCKET="" pipeline

Should fail immediately with a configuration error.
"""


"""
EXERCISE 14: SCHEDULE MULTIPLE RUNS (15 min)
============================================

Real pipelines run on a schedule. Let's simulate that.

STEP 1: Run the pipeline 3 times

    for i in 1 2 3; do
        echo "=== Run $i ==="
        docker compose run --rm pipeline
        sleep 5
    done

STEP 2: Check S3 for multiple partitions

    aws s3 ls s3://dante-data-lake-dev/raw/api/users/ --recursive

You should see multiple files with different timestamps.
"""


# =============================================================================
# PART 3: REVIEW (30 min)
# =============================================================================

"""
PROJECT CHECKLIST:
==================

Structure:
[ ] Created project directory with proper structure
[ ] Created all Python modules (config, logging, s3, api, pipeline, main)
[ ] Created Dockerfile with multi-stage build
[ ] Created docker-compose.yml

Functionality:
[ ] Pipeline fetches from multiple API endpoints
[ ] Records are enriched with metadata
[ ] Data is uploaded to S3 with proper partitioning
[ ] Errors are handled gracefully (retry, continue on failure)
[ ] Logging is structured and informative

Testing:
[ ] Successfully ran pipeline end-to-end
[ ] Verified data in S3
[ ] Tested error handling with bad endpoint
[ ] Ran pipeline multiple times


KNOWLEDGE CHECK:
================

1. Why do we use environment variables for configuration instead of
   hardcoding values?

2. Why is JSON Lines (JSONL) better than regular JSON for data pipelines?

3. What happens if the API fails on one endpoint? Does the whole
   pipeline fail?

4. Why do we add metadata (_ingested_at, _source, etc.) to each record?

5. What's the benefit of partitioning data by year/month/day?


COMMIT YOUR WORK:
=================

    cd ~/week3-project
    git init
    git add -A
    git commit -m "Week 3 Project: Containerized S3 Data Pipeline"
    
    # Also commit to your tracker repo
    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 20: Week 3 Project"
    git push


WHAT'S NEXT:
============
Day 21: Week 3 Review
- Review all Week 3 concepts
- Identify gaps
- Prepare for Week 4
"""


if __name__ == "__main__":
    print("Day 20: Week 3 Project")
    print("=" * 50)
    print("\nThis is a BUILD day - follow the exercises above")
    print("to create a complete containerized data pipeline.")
    print("\nProject location: ~/week3-project/")
