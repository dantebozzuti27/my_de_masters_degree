#!/usr/bin/env python3
"""
Day 26: PostgreSQL Deep Dive - Databases for Data Engineering
===============================================================
Duration: 3-4 hours total

Today you'll master PostgreSQL for data engineering:
- Database fundamentals
- Schema design patterns
- Bulk loading with COPY
- Indexing for performance
- Connection management in Python

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: Docker (for PostgreSQL), Python basics

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHY POSTGRESQL FOR DATA ENGINEERING?
====================================

PostgreSQL is the most versatile open-source database:
- Full SQL support (window functions, CTEs, etc.)
- JSON/JSONB for semi-structured data
- Excellent Python integration
- Used by most companies as primary database
- Foundation for analytics databases (Redshift, TimescaleDB)


DATABASE FUNDAMENTALS:
=====================

1. DATABASE
   A container for schemas, tables, and objects
   Example: CREATE DATABASE warehouse;

2. SCHEMA
   A namespace within a database
   Organizes tables logically
   Example: CREATE SCHEMA staging;

3. TABLE
   Stores data in rows and columns
   Has a defined structure (columns, types)
   Example: CREATE TABLE users (...);

4. INDEX
   Speed up queries on specific columns
   Trade-off: faster reads, slower writes
   Example: CREATE INDEX idx_users_email ON users(email);


DATA TYPES FOR DATA ENGINEERING:
================================

TEXT TYPES:
- VARCHAR(n): Variable length, max n characters
- TEXT: Unlimited length
- CHAR(n): Fixed length

NUMERIC TYPES:
- INTEGER: Whole numbers (-2B to 2B)
- BIGINT: Large whole numbers
- NUMERIC(p,s): Exact decimals (for money!)
- REAL/DOUBLE: Floating point

DATE/TIME TYPES:
- DATE: Just date (2026-01-25)
- TIME: Just time (14:30:00)
- TIMESTAMP: Date + time
- TIMESTAMPTZ: Timestamp with timezone (ALWAYS USE THIS!)

JSON TYPES:
- JSON: Stores as text, parsed on access
- JSONB: Binary format, faster queries, indexable


NORMALIZATION VS DENORMALIZATION:
=================================

NORMALIZED (3NF):
- Each fact stored once
- Less storage
- Harder to query (many JOINs)
- Good for: OLTP (transactional systems)

DENORMALIZED:
- Data duplicated for convenience
- More storage
- Faster queries (fewer JOINs)
- Good for: OLAP (analytics)

Data engineers often DENORMALIZE for analytics!


LEARNING RESOURCES:
==================

VIDEO:
- "PostgreSQL Tutorial for Beginners" - freeCodeCamp (4 hours)
  https://www.youtube.com/watch?v=qw--VYLpxG4
  Watch first hour for basics

- "PostgreSQL Tutorial" - Socratica (15 videos, 5 min each)
  https://www.youtube.com/playlist?list=PLi01XoE8jYojRqM4qGBF1U90Ee1Ecb5tt

READING:
- PostgreSQL Tutorial
  https://www.postgresqltutorial.com/
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

"""
EXERCISE 1: START POSTGRESQL WITH DOCKER (10 min)
==================================================

Let's start a PostgreSQL instance.

    # Create docker-compose.yml
    mkdir -p ~/postgres-practice
    cd ~/postgres-practice
    
    cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  postgres:
    image: postgres:15
    container_name: dataeng-postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: dataengpass
      POSTGRES_DB: warehouse
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
EOF

    # Start it
    docker compose up -d
    
    # Verify it's running
    docker compose ps
"""


"""
EXERCISE 2: CONNECT AND EXPLORE (15 min)
========================================

Connect to PostgreSQL and explore.

    # Connect via docker exec
    docker compose exec postgres psql -U dataeng -d warehouse
    
    # Inside psql:
    
    # List databases
    \l
    
    # List schemas
    \dn
    
    # List tables (none yet)
    \dt
    
    # Check current database and user
    SELECT current_database(), current_user;
    
    # Check version
    SELECT version();
    
    # Exit
    \q

PSQL COMMANDS CHEAT SHEET:
    \l          - List databases
    \c dbname   - Connect to database
    \dn         - List schemas
    \dt         - List tables
    \d table    - Describe table
    \di         - List indexes
    \q          - Quit
    \?          - Help
"""


"""
EXERCISE 3: CREATE SCHEMA FOR DATA LAKE (20 min)
================================================

Let's create a proper schema structure.
"""

CREATE_SCHEMA_SQL = """
-- Connect to PostgreSQL and run this:

-- Create schemas for different stages
CREATE SCHEMA IF NOT EXISTS staging;   -- Temporary landing zone
CREATE SCHEMA IF NOT EXISTS raw;       -- Raw data as-is
CREATE SCHEMA IF NOT EXISTS clean;     -- Cleaned/validated
CREATE SCHEMA IF NOT EXISTS marts;     -- Business aggregates

-- Verify
SELECT schema_name FROM information_schema.schemata;
"""

"""
Run this in psql:

    docker compose exec postgres psql -U dataeng -d warehouse
    
Then paste the SQL above.
"""


"""
EXERCISE 4: CREATE DATA TABLES (25 min)
=======================================

Let's create tables with proper data types.
"""

CREATE_TABLES_SQL = """
-- Raw users table (from API ingestion)
CREATE TABLE IF NOT EXISTS raw.users (
    id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    region VARCHAR(50),
    signup_date DATE,
    is_active BOOLEAN DEFAULT true,
    raw_json JSONB,  -- Store original API response
    ingested_at TIMESTAMPTZ DEFAULT NOW()
);

-- Raw orders table
CREATE TABLE IF NOT EXISTS raw.orders (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50) NOT NULL UNIQUE,
    user_id INTEGER,
    product VARCHAR(100),
    quantity INTEGER,
    price NUMERIC(10, 2),  -- Exact decimal for money!
    order_date DATE,
    region VARCHAR(50),
    raw_json JSONB,
    ingested_at TIMESTAMPTZ DEFAULT NOW()
);

-- Clean users (deduplicated, validated)
CREATE TABLE IF NOT EXISTS clean.users (
    id SERIAL PRIMARY KEY,
    source_id INTEGER NOT NULL UNIQUE,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    region VARCHAR(50),
    signup_date DATE,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Mart: Daily user stats
CREATE TABLE IF NOT EXISTS marts.daily_user_stats (
    date DATE NOT NULL,
    region VARCHAR(50),
    total_users INTEGER,
    active_users INTEGER,
    new_signups INTEGER,
    PRIMARY KEY (date, region)
);

-- Mart: Daily revenue
CREATE TABLE IF NOT EXISTS marts.daily_revenue (
    date DATE NOT NULL,
    region VARCHAR(50),
    product VARCHAR(100),
    order_count INTEGER,
    total_revenue NUMERIC(12, 2),
    avg_order_value NUMERIC(10, 2),
    PRIMARY KEY (date, region, product)
);

-- Verify tables
SELECT schemaname, tablename FROM pg_tables 
WHERE schemaname IN ('raw', 'clean', 'marts')
ORDER BY schemaname, tablename;
"""


"""
EXERCISE 5: BULK LOADING WITH COPY (30 min)
===========================================

The COPY command is THE way to load data fast.
Much faster than individual INSERTs!
"""

import psycopg2
import csv
import io
from typing import List, Dict

def get_connection():
    """Get PostgreSQL connection."""
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="warehouse",
        user="dataeng",
        password="dataengpass"
    )


def bulk_insert_with_copy(
    table: str,
    columns: List[str],
    data: List[tuple]
) -> int:
    """
    Bulk insert using COPY command.
    
    COPY is 10-100x faster than individual INSERTs!
    
    Args:
        table: Target table (schema.table)
        columns: Column names
        data: List of tuples with values
        
    Returns:
        Number of rows inserted
    """
    conn = get_connection()
    cur = conn.cursor()
    
    # Create a file-like object from the data
    buffer = io.StringIO()
    writer = csv.writer(buffer, delimiter='\t')
    
    for row in data:
        writer.writerow(row)
    
    buffer.seek(0)
    
    # Use COPY to bulk load
    cur.copy_from(
        buffer,
        table,
        columns=columns,
        sep='\t',
        null=''
    )
    
    conn.commit()
    
    rows_inserted = len(data)
    
    cur.close()
    conn.close()
    
    return rows_inserted


def demo_bulk_insert():
    """Demonstrate bulk insert performance."""
    import time
    import random
    
    # Generate test data
    print("Generating 10,000 test records...")
    data = []
    regions = ['us-east', 'us-west', 'eu-west', 'ap-south']
    
    for i in range(10000):
        data.append((
            i + 1,                           # source_id
            f'user_{i+1:05d}',               # username
            f'user{i+1}@example.com',        # email
            random.choice(regions),          # region
            f'2025-{random.randint(1,12):02d}-{random.randint(1,28):02d}',  # signup_date
            random.random() > 0.2            # is_active
        ))
    
    # Bulk insert
    print("Bulk inserting with COPY...")
    start = time.time()
    
    rows = bulk_insert_with_copy(
        table='raw.users',
        columns=['source_id', 'username', 'email', 'region', 'signup_date', 'is_active'],
        data=data
    )
    
    elapsed = time.time() - start
    print(f"Inserted {rows} rows in {elapsed:.2f} seconds")
    print(f"Rate: {rows/elapsed:.0f} rows/second")


"""
EXERCISE 6: INDEXING STRATEGIES (25 min)
========================================

Indexes speed up queries but slow down writes.
"""

INDEXING_SQL = """
-- B-tree index (default, most common)
-- Good for: equality, range queries, sorting
CREATE INDEX idx_users_email ON raw.users(email);
CREATE INDEX idx_users_region ON raw.users(region);
CREATE INDEX idx_orders_user_id ON raw.orders(user_id);
CREATE INDEX idx_orders_date ON raw.orders(order_date);

-- Composite index (multiple columns)
-- Good for: queries filtering on multiple columns
CREATE INDEX idx_orders_region_date ON raw.orders(region, order_date);

-- Partial index (only index some rows)
-- Good for: queries that always filter the same way
CREATE INDEX idx_active_users ON raw.users(email) WHERE is_active = true;

-- Expression index
-- Good for: queries using functions
CREATE INDEX idx_users_email_lower ON raw.users(LOWER(email));

-- Check existing indexes
SELECT indexname, indexdef 
FROM pg_indexes 
WHERE schemaname = 'raw';

-- Analyze query performance
EXPLAIN ANALYZE SELECT * FROM raw.users WHERE email = 'user00001@example.com';
EXPLAIN ANALYZE SELECT * FROM raw.users WHERE region = 'us-east' AND is_active = true;
"""


"""
EXERCISE 7: UPSERT PATTERN (20 min)
===================================

UPSERT = UPDATE if exists, INSERT if not.
Essential for idempotent data pipelines!
"""

def upsert_users(users: List[Dict]) -> int:
    """
    Upsert users to clean.users table.
    
    Uses ON CONFLICT for idempotent loads.
    """
    conn = get_connection()
    cur = conn.cursor()
    
    upserted = 0
    
    for user in users:
        cur.execute("""
            INSERT INTO clean.users (source_id, username, email, region, signup_date, is_active, updated_at)
            VALUES (%(source_id)s, %(username)s, %(email)s, %(region)s, %(signup_date)s, %(is_active)s, NOW())
            ON CONFLICT (source_id) DO UPDATE SET
                username = EXCLUDED.username,
                email = EXCLUDED.email,
                region = EXCLUDED.region,
                is_active = EXCLUDED.is_active,
                updated_at = NOW()
        """, user)
        upserted += 1
    
    conn.commit()
    cur.close()
    conn.close()
    
    return upserted


"""
EXERCISE 8: AGGREGATION TO MARTS (25 min)
=========================================

Create materialized aggregations for fast analytics.
"""

AGGREGATION_SQL = """
-- Populate daily user stats
INSERT INTO marts.daily_user_stats (date, region, total_users, active_users, new_signups)
SELECT 
    signup_date AS date,
    region,
    COUNT(*) AS total_users,
    COUNT(*) FILTER (WHERE is_active = true) AS active_users,
    COUNT(*) AS new_signups
FROM raw.users
WHERE signup_date IS NOT NULL
GROUP BY signup_date, region
ON CONFLICT (date, region) DO UPDATE SET
    total_users = EXCLUDED.total_users,
    active_users = EXCLUDED.active_users,
    new_signups = EXCLUDED.new_signups;

-- Populate daily revenue
INSERT INTO marts.daily_revenue (date, region, product, order_count, total_revenue, avg_order_value)
SELECT 
    order_date AS date,
    region,
    product,
    COUNT(*) AS order_count,
    SUM(price * quantity) AS total_revenue,
    AVG(price * quantity) AS avg_order_value
FROM raw.orders
WHERE order_date IS NOT NULL
GROUP BY order_date, region, product
ON CONFLICT (date, region, product) DO UPDATE SET
    order_count = EXCLUDED.order_count,
    total_revenue = EXCLUDED.total_revenue,
    avg_order_value = EXCLUDED.avg_order_value;

-- Query the marts
SELECT * FROM marts.daily_user_stats ORDER BY date DESC LIMIT 10;
SELECT * FROM marts.daily_revenue ORDER BY date DESC, total_revenue DESC LIMIT 10;
"""


"""
EXERCISE 9: CONNECTION POOLING (20 min)
=======================================

In production, use connection pooling to manage database connections efficiently.
"""

from contextlib import contextmanager

class DatabasePool:
    """
    Simple connection pool pattern.
    
    In production, use:
    - psycopg2.pool.ThreadedConnectionPool
    - Or better: SQLAlchemy with connection pooling
    """
    
    def __init__(self, **kwargs):
        self.config = kwargs
    
    @contextmanager
    def get_connection(self):
        """Get a connection from the pool."""
        conn = psycopg2.connect(**self.config)
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_query(self, query: str, params: tuple = None) -> List:
        """Execute a query and return results."""
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, params)
                
                if cur.description:  # SELECT query
                    columns = [desc[0] for desc in cur.description]
                    rows = cur.fetchall()
                    return [dict(zip(columns, row)) for row in rows]
                else:  # INSERT/UPDATE/DELETE
                    conn.commit()
                    return []
    
    def execute_many(self, query: str, params_list: List[tuple]):
        """Execute same query with multiple parameter sets."""
        with self.get_connection() as conn:
            with conn.cursor() as cur:
                cur.executemany(query, params_list)
                conn.commit()


# Usage example
def demo_connection_pool():
    pool = DatabasePool(
        host="localhost",
        port=5432,
        database="warehouse",
        user="dataeng",
        password="dataengpass"
    )
    
    # Query
    users = pool.execute_query(
        "SELECT * FROM raw.users WHERE region = %s LIMIT 5",
        ('us-east',)
    )
    
    print(f"Found {len(users)} users")
    for user in users:
        print(f"  {user['username']}: {user['email']}")


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

PostgreSQL Concepts:
[ ] Databases, schemas, tables
[ ] Data types (VARCHAR, INTEGER, NUMERIC, TIMESTAMPTZ, JSONB)
[ ] Normalization vs denormalization

SQL Skills:
[ ] CREATE SCHEMA, CREATE TABLE
[ ] INSERT, UPDATE, DELETE
[ ] SELECT with WHERE, GROUP BY, ORDER BY
[ ] UPSERT with ON CONFLICT

Performance:
[ ] COPY command for bulk loading
[ ] Indexing strategies (B-tree, composite, partial)
[ ] EXPLAIN ANALYZE for query plans

Python Integration:
[ ] psycopg2 for connections
[ ] Parameterized queries
[ ] Connection pooling


KNOWLEDGE CHECK:
================

1. You need to load 1 million rows. Would you use INSERT or COPY? Why?

2. Your query on the orders table is slow. It filters by order_date 
   and region. What index would you create?

3. Your pipeline runs hourly and might process the same records twice.
   How do you prevent duplicates?

4. Why use NUMERIC instead of FLOAT for money?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 26: PostgreSQL Deep Dive"
    git push


WHAT'S NEXT:
============
Day 27: Project 1 Deep Work
- Extended project implementation
- Combining all Week 4 skills
- Documentation and testing
"""


if __name__ == "__main__":
    print("Day 26: PostgreSQL Deep Dive")
    print("=" * 50)
    print("\nMake sure PostgreSQL is running:")
    print("  cd ~/postgres-practice && docker compose up -d")
    print("\nThen follow the exercises in the comments above.")
