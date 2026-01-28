#!/usr/bin/env python3
"""
Day 27: Project 1 Deep Work - Credit Markets Pipeline
======================================================
Duration: 4-5 hours (Extended project day)

Today you'll build a complete data pipeline combining EVERYTHING from Month 1:
- API extraction with proper patterns (FRED, SEC EDGAR)
- S3 storage with partitioning
- PostgreSQL loading
- Docker containerization
- Error handling and logging

This is your CAPSTONE PROJECT for Month 1.

DATA SOURCES:
- FRED API: Treasury yields, credit spreads, economic indicators
- SEC EDGAR: Corporate filings, 10-K, 10-Q

VALUE PROPOSITION:
- Corporate credit health monitoring
- Early warning signals for credit deterioration
- Relevant to fintech (Ramp, Brex, Stripe)

DAILY STRUCTURE:
├── DESIGN (30 min): Architecture planning
├── BUILD (3-4 hrs): Implementation
└── DOCUMENT (30 min): README and commit

PREREQUISITES: Weeks 1-4 complete

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PROJECT OVERVIEW
# =============================================================================
"""
THE PROJECT: End-to-End Data Pipeline
======================================

You will build a pipeline that:

1. EXTRACTS data from multiple API endpoints
2. LOADS raw data to S3 (bronze layer)
3. TRANSFORMS and LOADS to PostgreSQL
4. Creates AGGREGATE tables for analytics
5. Runs in DOCKER containers
6. Has proper LOGGING and ERROR HANDLING


ARCHITECTURE:
=============

    ┌─────────────────────────────────────────────────────────────┐
    │                    Data Pipeline                             │
    │                                                              │
    │   ┌──────────┐         ┌─────────┐         ┌──────────────┐ │
    │   │   API    │         │   S3    │         │  PostgreSQL  │ │
    │   │ Extract  │ ──────► │ Bronze  │ ──────► │   Warehouse  │ │
    │   └──────────┘         └─────────┘         └──────────────┘ │
    │        │                    │                     │         │
    │        ▼                    ▼                     ▼         │
    │   ┌──────────┐         ┌─────────┐         ┌──────────────┐ │
    │   │  Users   │         │  JSONL  │         │   raw.*      │ │
    │   │  Posts   │         │  Files  │         │   clean.*    │ │
    │   │ Comments │         │         │         │   marts.*    │ │
    │   └──────────┘         └─────────┘         └──────────────┘ │
    └─────────────────────────────────────────────────────────────┘


PROJECT STRUCTURE:
==================

    ~/project1-pipeline/
    ├── docker-compose.yml
    ├── .env
    ├── .env.example
    ├── README.md
    │
    ├── pipeline/
    │   ├── Dockerfile
    │   ├── requirements.txt
    │   ├── __init__.py
    │   ├── config.py
    │   ├── logging_setup.py
    │   ├── api_client.py
    │   ├── s3_client.py
    │   ├── db_client.py
    │   ├── extractors/
    │   │   ├── __init__.py
    │   │   └── api_extractor.py
    │   ├── loaders/
    │   │   ├── __init__.py
    │   │   ├── s3_loader.py
    │   │   └── postgres_loader.py
    │   ├── transformers/
    │   │   ├── __init__.py
    │   │   └── data_transformer.py
    │   └── main.py
    │
    └── sql/
        ├── 01_create_schemas.sql
        ├── 02_create_tables.sql
        └── 03_create_marts.sql
"""


# =============================================================================
# STEP 1: CREATE PROJECT STRUCTURE (15 min)
# =============================================================================
"""
Run these commands to create the project structure:

    mkdir -p ~/project1-pipeline/{pipeline/{extractors,loaders,transformers},sql}
    cd ~/project1-pipeline
    
    touch pipeline/__init__.py
    touch pipeline/extractors/__init__.py
    touch pipeline/loaders/__init__.py
    touch pipeline/transformers/__init__.py
"""


# =============================================================================
# STEP 2: CONFIGURATION (config.py)
# =============================================================================

CONFIG_PY = '''
"""Configuration management for the pipeline."""

import os
from dataclasses import dataclass
from typing import List


@dataclass
class Config:
    """Pipeline configuration from environment variables."""
    
    # API Settings
    api_base_url: str = "https://jsonplaceholder.typicode.com"
    api_timeout: int = 30
    api_rate_limit: float = 10.0
    
    # S3 Settings
    s3_bucket: str = ""
    s3_prefix: str = "bronze"
    aws_region: str = "us-east-1"
    
    # Database Settings
    db_host: str = "postgres"
    db_port: int = 5432
    db_name: str = "warehouse"
    db_user: str = "dataeng"
    db_password: str = ""
    
    # Pipeline Settings
    endpoints: List[str] = None
    log_level: str = "INFO"
    
    def __post_init__(self):
        """Load from environment variables."""
        self.api_base_url = os.getenv("API_BASE_URL", self.api_base_url)
        self.api_timeout = int(os.getenv("API_TIMEOUT", self.api_timeout))
        
        self.s3_bucket = os.getenv("S3_BUCKET", self.s3_bucket)
        self.s3_prefix = os.getenv("S3_PREFIX", self.s3_prefix)
        self.aws_region = os.getenv("AWS_REGION", self.aws_region)
        
        self.db_host = os.getenv("DB_HOST", self.db_host)
        self.db_port = int(os.getenv("DB_PORT", self.db_port))
        self.db_name = os.getenv("DB_NAME", self.db_name)
        self.db_user = os.getenv("DB_USER", self.db_user)
        self.db_password = os.getenv("DB_PASSWORD", self.db_password)
        
        endpoints_str = os.getenv("ENDPOINTS", "users,posts,comments")
        self.endpoints = [e.strip() for e in endpoints_str.split(",")]
        
        self.log_level = os.getenv("LOG_LEVEL", self.log_level)
    
    def validate(self):
        """Validate required configuration."""
        errors = []
        if not self.s3_bucket:
            errors.append("S3_BUCKET is required")
        if not self.db_password:
            errors.append("DB_PASSWORD is required")
        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")
    
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
'''


# =============================================================================
# STEP 3: LOGGING SETUP (logging_setup.py)
# =============================================================================

LOGGING_SETUP_PY = '''
"""Structured logging configuration."""

import logging
import json
import sys
from datetime import datetime, timezone


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_entry)


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure and return root logger."""
    logger = logging.getLogger("pipeline")
    logger.setLevel(getattr(logging, level.upper()))
    
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JSONFormatter())
    
    logger.handlers.clear()
    logger.addHandler(handler)
    
    return logger
'''


# =============================================================================
# STEP 4: API CLIENT (api_client.py)
# =============================================================================

API_CLIENT_PY = '''
"""API client with rate limiting and retries."""

import requests
import time
import logging
from typing import List, Dict, Optional


class RateLimiter:
    def __init__(self, requests_per_second: float = 10):
        self.min_interval = 1.0 / requests_per_second
        self.last_request = 0.0
    
    def wait(self):
        elapsed = time.time() - self.last_request
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_request = time.time()


class APIClient:
    def __init__(self, base_url: str, timeout: int = 30, rate_limit: float = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.rate_limiter = RateLimiter(rate_limit)
        self.logger = logging.getLogger("pipeline.api")
    
    def fetch(self, endpoint: str, max_retries: int = 3) -> Optional[List[Dict]]:
        """Fetch data from endpoint with retries."""
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(max_retries):
            try:
                self.rate_limiter.wait()
                self.logger.info(f"Fetching {url} (attempt {attempt + 1})")
                
                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()
                
                data = response.json()
                self.logger.info(f"Fetched {len(data)} records from {endpoint}")
                return data
                
            except requests.HTTPError as e:
                if e.response.status_code == 429:
                    wait = 2 ** attempt
                    self.logger.warning(f"Rate limited, waiting {wait}s")
                    time.sleep(wait)
                else:
                    self.logger.error(f"HTTP error: {e}")
                    return None
                    
            except requests.RequestException as e:
                self.logger.error(f"Request failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
        
        return None
'''


# =============================================================================
# STEP 5: S3 CLIENT (s3_client.py)
# =============================================================================

S3_CLIENT_PY = '''
"""S3 client for data lake operations."""

import boto3
import json
import logging
from datetime import datetime, timezone
from typing import List, Dict


class S3Client:
    def __init__(self, bucket: str, region: str = "us-east-1"):
        self.bucket = bucket
        self.client = boto3.client("s3", region_name=region)
        self.logger = logging.getLogger("pipeline.s3")
    
    def write_jsonl(
        self,
        records: List[Dict],
        prefix: str,
        source: str,
        entity: str,
        timestamp: datetime = None
    ) -> str:
        """Write records as JSONL to partitioned path."""
        ts = timestamp or datetime.now(timezone.utc)
        
        # Generate partitioned key
        partition = f"year={ts.year}/month={ts.month:02d}/day={ts.day:02d}"
        filename = f"{entity}_{ts.strftime('%Y%m%d_%H%M%S')}.jsonl"
        key = f"{prefix}/{source}/{entity}/{partition}/{filename}"
        
        # Convert to JSONL
        body = "\\n".join(json.dumps(r, default=str) for r in records)
        
        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=body.encode("utf-8"),
            ContentType="application/x-ndjson"
        )
        
        self.logger.info(f"Wrote {len(records)} records to s3://{self.bucket}/{key}")
        return f"s3://{self.bucket}/{key}"
'''


# =============================================================================
# STEP 6: DATABASE CLIENT (db_client.py)
# =============================================================================

DB_CLIENT_PY = '''
"""PostgreSQL client for warehouse operations."""

import psycopg2
import psycopg2.extras
import logging
from typing import List, Dict
from contextlib import contextmanager


class DatabaseClient:
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.config = {
            "host": host,
            "port": port,
            "database": database,
            "user": user,
            "password": password
        }
        self.logger = logging.getLogger("pipeline.db")
    
    @contextmanager
    def get_connection(self):
        conn = psycopg2.connect(**self.config)
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_sql(self, sql: str):
        """Execute SQL statement."""
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                conn.commit()
    
    def upsert_records(
        self,
        table: str,
        records: List[Dict],
        key_columns: List[str],
        update_columns: List[str]
    ) -> int:
        """Upsert records using ON CONFLICT."""
        if not records:
            return 0
        
        columns = list(records[0].keys())
        
        # Build INSERT ... ON CONFLICT statement
        insert_cols = ", ".join(columns)
        placeholders = ", ".join([f"%({c})s" for c in columns])
        conflict_cols = ", ".join(key_columns)
        update_set = ", ".join([f"{c} = EXCLUDED.{c}" for c in update_columns])
        
        sql = f"""
            INSERT INTO {table} ({insert_cols})
            VALUES ({placeholders})
            ON CONFLICT ({conflict_cols}) DO UPDATE SET
                {update_set}
        """
        
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                psycopg2.extras.execute_batch(cur, sql, records)
                conn.commit()
        
        self.logger.info(f"Upserted {len(records)} records to {table}")
        return len(records)
'''


# =============================================================================
# STEP 7: MAIN PIPELINE (main.py)
# =============================================================================

MAIN_PY = '''
#!/usr/bin/env python3
"""
Main pipeline orchestration.
"""

import sys
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Dict, List

from config import Config
from logging_setup import setup_logging
from api_client import APIClient
from s3_client import S3Client
from db_client import DatabaseClient


@dataclass
class PipelineMetrics:
    start_time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    end_time: datetime = None
    records_extracted: int = 0
    records_loaded_s3: int = 0
    records_loaded_db: int = 0
    errors: List[str] = field(default_factory=list)
    
    @property
    def success(self) -> bool:
        return len(self.errors) == 0


def enrich_records(records: List[Dict], source: str) -> List[Dict]:
    """Add metadata to records."""
    ingested_at = datetime.now(timezone.utc).isoformat()
    for record in records:
        record["_source"] = source
        record["_ingested_at"] = ingested_at
    return records


def run_pipeline(config: Config) -> PipelineMetrics:
    """Execute the full pipeline."""
    logger = setup_logging(config.log_level)
    metrics = PipelineMetrics()
    
    logger.info("=" * 60)
    logger.info("PIPELINE STARTING")
    logger.info(f"Endpoints: {config.endpoints}")
    logger.info("=" * 60)
    
    # Initialize clients
    api = APIClient(config.api_base_url, config.api_timeout, config.api_rate_limit)
    s3 = S3Client(config.s3_bucket, config.aws_region)
    db = DatabaseClient(
        config.db_host, config.db_port, config.db_name,
        config.db_user, config.db_password
    )
    
    run_timestamp = datetime.now(timezone.utc)
    
    for endpoint in config.endpoints:
        try:
            logger.info(f"Processing endpoint: {endpoint}")
            
            # EXTRACT
            records = api.fetch(endpoint)
            if records is None:
                metrics.errors.append(f"Failed to fetch {endpoint}")
                continue
            
            metrics.records_extracted += len(records)
            
            # ENRICH
            records = enrich_records(records, endpoint)
            
            # LOAD TO S3
            s3.write_jsonl(records, config.s3_prefix, "api", endpoint, run_timestamp)
            metrics.records_loaded_s3 += len(records)
            
            # LOAD TO DATABASE
            # Transform for DB schema
            db_records = []
            for r in records:
                db_records.append({
                    "source_id": r.get("id"),
                    "raw_json": r,
                    "ingested_at": r.get("_ingested_at")
                })
            
            table = f"raw.api_{endpoint}"
            db.upsert_records(
                table=table,
                records=db_records,
                key_columns=["source_id"],
                update_columns=["raw_json", "ingested_at"]
            )
            metrics.records_loaded_db += len(db_records)
            
            logger.info(f"✅ {endpoint}: {len(records)} records processed")
            
        except Exception as e:
            logger.error(f"Error processing {endpoint}: {e}")
            metrics.errors.append(str(e))
    
    metrics.end_time = datetime.now(timezone.utc)
    
    # Log summary
    duration = (metrics.end_time - metrics.start_time).total_seconds()
    logger.info("=" * 60)
    logger.info("PIPELINE COMPLETE")
    logger.info(f"Duration: {duration:.2f}s")
    logger.info(f"Records extracted: {metrics.records_extracted}")
    logger.info(f"Records to S3: {metrics.records_loaded_s3}")
    logger.info(f"Records to DB: {metrics.records_loaded_db}")
    logger.info(f"Errors: {len(metrics.errors)}")
    logger.info("=" * 60)
    
    return metrics


def main():
    config = Config()
    
    try:
        config.validate()
    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)
    
    metrics = run_pipeline(config)
    sys.exit(0 if metrics.success else 1)


if __name__ == "__main__":
    main()
'''


# =============================================================================
# STEP 8: SQL SCRIPTS
# =============================================================================

SQL_SCHEMAS = '''
-- 01_create_schemas.sql
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS clean;
CREATE SCHEMA IF NOT EXISTS marts;
'''

SQL_TABLES = '''
-- 02_create_tables.sql
CREATE TABLE IF NOT EXISTS raw.api_users (
    id SERIAL PRIMARY KEY,
    source_id INTEGER UNIQUE,
    raw_json JSONB,
    ingested_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS raw.api_posts (
    id SERIAL PRIMARY KEY,
    source_id INTEGER UNIQUE,
    raw_json JSONB,
    ingested_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS raw.api_comments (
    id SERIAL PRIMARY KEY,
    source_id INTEGER UNIQUE,
    raw_json JSONB,
    ingested_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_users_source_id ON raw.api_users(source_id);
CREATE INDEX IF NOT EXISTS idx_posts_source_id ON raw.api_posts(source_id);
CREATE INDEX IF NOT EXISTS idx_comments_source_id ON raw.api_comments(source_id);
'''

SQL_MARTS = '''
-- 03_create_marts.sql
CREATE TABLE IF NOT EXISTS marts.user_post_summary (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT,
    post_count INTEGER,
    comment_count INTEGER,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Populate mart
INSERT INTO marts.user_post_summary (user_id, username, email, post_count, comment_count)
SELECT 
    u.source_id AS user_id,
    u.raw_json->>'username' AS username,
    u.raw_json->>'email' AS email,
    COALESCE(p.post_count, 0) AS post_count,
    COALESCE(c.comment_count, 0) AS comment_count
FROM raw.api_users u
LEFT JOIN (
    SELECT (raw_json->>'userId')::int AS user_id, COUNT(*) AS post_count
    FROM raw.api_posts
    GROUP BY 1
) p ON u.source_id = p.user_id
LEFT JOIN (
    SELECT 
        (SELECT (raw_json->>'userId')::int FROM raw.api_posts WHERE source_id = (c.raw_json->>'postId')::int) AS user_id,
        COUNT(*) AS comment_count
    FROM raw.api_comments c
    GROUP BY 1
) c ON u.source_id = c.user_id
ON CONFLICT (user_id) DO UPDATE SET
    post_count = EXCLUDED.post_count,
    comment_count = EXCLUDED.comment_count,
    updated_at = NOW();
'''


# =============================================================================
# STEP 9: DOCKERFILE
# =============================================================================

DOCKERFILE = '''
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
'''

REQUIREMENTS_TXT = '''
requests>=2.31.0
boto3>=1.28.0
psycopg2-binary>=2.9.9
'''


# =============================================================================
# STEP 10: DOCKER COMPOSE
# =============================================================================

DOCKER_COMPOSE = '''
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: ${DB_PASSWORD:-dataengpass}
      POSTGRES_DB: warehouse
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./sql:/docker-entrypoint-initdb.d:ro
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d warehouse"]
      interval: 5s
      timeout: 5s
      retries: 5

  pipeline:
    build: ./pipeline
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      S3_BUCKET: ${S3_BUCKET}
      DB_HOST: postgres
      DB_PASSWORD: ${DB_PASSWORD:-dataengpass}
      AWS_ACCESS_KEY_ID: ${AWS_ACCESS_KEY_ID}
      AWS_SECRET_ACCESS_KEY: ${AWS_SECRET_ACCESS_KEY}
      LOG_LEVEL: INFO

volumes:
  postgres_data:
'''


# =============================================================================
# REVIEW
# =============================================================================

"""
PROJECT COMPLETION CHECKLIST:
=============================

Structure:
[ ] Created project directory structure
[ ] Created all Python modules
[ ] Created SQL initialization scripts
[ ] Created Dockerfile and docker-compose.yml
[ ] Created .env file with credentials

Functionality:
[ ] Pipeline extracts from 3 API endpoints
[ ] Data is written to S3 with proper partitioning
[ ] Data is loaded to PostgreSQL raw tables
[ ] Mart table is populated
[ ] Error handling works properly
[ ] Logging is structured and informative

Testing:
[ ] docker compose up works
[ ] All three endpoints are processed
[ ] Data appears in S3
[ ] Data appears in PostgreSQL
[ ] Mart query returns results


COMMIT YOUR WORK:
=================

    cd ~/project1-pipeline
    git init
    git add -A
    git commit -m "Project 1: Full Stack Data Pipeline - API to S3 to PostgreSQL"
    
    # Also update tracker
    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 27: Project 1 Deep Work"
    git push


WHAT'S NEXT:
============
Day 28: Week 4 Review
- Review all concepts
- Fill knowledge gaps
- Prepare for Month 2
"""


if __name__ == "__main__":
    print("Day 27: Project 1 Deep Work")
    print("=" * 50)
    print("\nThis is an extended project day.")
    print("Follow the steps above to build the complete pipeline.")
    print("\nProject location: ~/project1-pipeline/")
