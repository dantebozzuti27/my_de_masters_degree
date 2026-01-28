#!/usr/bin/env python3
"""
Day 19: Docker for Data Engineering - Production Patterns
==========================================================
Duration: 3-4 hours total

Today you'll learn Docker patterns specific to data engineering:
- Docker Compose for multi-container setups
- Running databases in Docker
- Building production-ready pipeline images

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding  
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: Docker fundamentals (Day 18)

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# DAY 19 - Building Project 1 (Credit Markets Pipeline)
# COMPLETED - Built Credit Markets Pipeline with Bronze→Silver→Gold architecture

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHAT IS DOCKER COMPOSE?
=======================

Docker Compose lets you define and run MULTIPLE containers together.

THE PROBLEM IT SOLVES:
---------------------
Real applications have multiple parts:
- Web server
- Database
- Cache (Redis)
- Message queue
- Your data pipeline

Running each with `docker run` is tedious and error-prone.
Docker Compose defines everything in ONE file.


KEY CONCEPTS:
=============

1. docker-compose.yml
   - YAML file defining all services
   - Describes containers, networks, volumes
   - One command starts everything

2. SERVICE
   - One container definition
   - Example: "postgres" service, "pipeline" service

3. NETWORK
   - Containers in same Compose file share a network
   - Can reference each other by service name
   - "postgres" container is reachable at hostname "postgres"

4. VOLUME
   - Persistent storage
   - Survives container restarts


EXAMPLE docker-compose.yml:
===========================

version: '3.8'
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
  
  pipeline:
    build: .
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://postgres:secret@db:5432/postgres

volumes:
  postgres_data:


This single file:
- Starts a PostgreSQL database
- Builds and runs your pipeline
- Creates a network so they can communicate
- Persists database data in a volume


WHY THIS MATTERS FOR DATA ENGINEERING:
=====================================
- Local development mirrors production
- One command spins up entire stack
- Everyone on team uses same setup
- CI/CD uses same Docker Compose


LEARNING RESOURCES (Pick 1-2):
==============================

VIDEO:
- "Docker Compose Tutorial" - TechWorld with Nana (25 min)
  https://www.youtube.com/watch?v=HG6yIjZapSA
  
- "Docker Compose in 12 Minutes" - TechWorld with Nana
  https://www.youtube.com/watch?v=Qw9zlE3t8Ko

READING:
- Docker Compose Getting Started
  https://docs.docker.com/compose/gettingstarted/
  
- Docker Compose File Reference
  https://docs.docker.com/compose/compose-file/

After watching/reading, answer:
1. What's the difference between `docker run` and `docker compose up`?
2. How do containers in Compose communicate?
3. What does `depends_on` do?
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

"""
EXERCISE 1: DOCKER COMPOSE BASICS (20 min)
==========================================

Let's create a simple Docker Compose setup.

STEP 1: Create project directory

    mkdir -p ~/compose-practice
    cd ~/compose-practice

STEP 2: Create a simple docker-compose.yml

    cat > ~/compose-practice/docker-compose.yml << 'EOF'
version: '3.8'

services:
  # Simple Python container
  app:
    image: python:3.11-slim
    command: python -c "print('Hello from Docker Compose!')"
EOF

STEP 3: Run it

    cd ~/compose-practice
    docker compose up

You should see the message printed.

STEP 4: Run in detached mode (background)

    docker compose up -d
    docker compose logs
    docker compose down

COMMANDS TO KNOW:
    docker compose up       # Start all services
    docker compose up -d    # Start in background
    docker compose down     # Stop and remove containers
    docker compose logs     # View logs
    docker compose ps       # List running services
    docker compose build    # Rebuild images
"""


"""
EXERCISE 2: POSTGRES IN DOCKER (30 min)
=======================================

Let's run a real PostgreSQL database in Docker.

STEP 1: Create docker-compose.yml

    cat > ~/compose-practice/docker-compose.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: learning-postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: secretpassword
      POSTGRES_DB: pipeline_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d pipeline_db"]
      interval: 10s
      timeout: 5s
      retries: 5

volumes:
  postgres_data:
EOF

Let's break this down:

- image: postgres:15
    Official PostgreSQL 15 image
    
- environment:
    POSTGRES_USER: Username for database
    POSTGRES_PASSWORD: Password
    POSTGRES_DB: Database name to create
    
- ports: "5432:5432"
    Map container port to host
    
- volumes: postgres_data:/var/lib/postgresql/data
    Persist data even if container stops
    
- healthcheck:
    Docker checks if database is ready


STEP 2: Start PostgreSQL

    cd ~/compose-practice
    docker compose up -d

STEP 3: Wait for it to be healthy

    docker compose ps
    
Look for "healthy" in the status.

STEP 4: Connect to PostgreSQL

    # Using docker exec
    docker compose exec postgres psql -U dataeng -d pipeline_db
    
You're now in PostgreSQL! Try:

    \l                  -- List databases
    \dt                 -- List tables (empty)
    SELECT version();   -- PostgreSQL version
    \q                  -- Quit

STEP 5: Create a test table

    docker compose exec postgres psql -U dataeng -d pipeline_db -c "
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        created_at TIMESTAMP DEFAULT NOW()
    );
    "

STEP 6: Insert and query data

    docker compose exec postgres psql -U dataeng -d pipeline_db -c "
    INSERT INTO users (name, email) VALUES 
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com');
    "
    
    docker compose exec postgres psql -U dataeng -d pipeline_db -c "
    SELECT * FROM users;
    "

STEP 7: Test persistence

    # Stop and remove containers
    docker compose down
    
    # Start again
    docker compose up -d
    
    # Check data is still there!
    docker compose exec postgres psql -U dataeng -d pipeline_db -c "SELECT * FROM users;"

The data persists because of the volume!
"""


"""
EXERCISE 3: PYTHON + POSTGRES PIPELINE (45 min)
===============================================

Let's build a pipeline that loads data into PostgreSQL.

STEP 1: Create project structure

    mkdir -p ~/compose-practice/pipeline
    cd ~/compose-practice

STEP 2: Create the pipeline code

    cat > ~/compose-practice/pipeline/main.py << 'EOF'
import os
import json
import requests
import psycopg2
from datetime import datetime, timezone
from typing import List, Dict

def get_db_connection():
    """Create database connection from environment variables."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "pipeline_db"),
        user=os.getenv("DB_USER", "dataeng"),
        password=os.getenv("DB_PASSWORD", "secretpassword")
    )

def create_tables(conn):
    """Create tables if they don't exist."""
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS api_users (
                id INTEGER PRIMARY KEY,
                name VARCHAR(100),
                username VARCHAR(100),
                email VARCHAR(100),
                phone VARCHAR(50),
                website VARCHAR(100),
                company_name VARCHAR(100),
                ingested_at TIMESTAMP WITH TIME ZONE
            );
        """)
        conn.commit()
    print("✅ Tables created/verified")

def fetch_users() -> List[Dict]:
    """Fetch users from API."""
    print("📥 Fetching users from API...")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users",
        timeout=30
    )
    response.raise_for_status()
    users = response.json()
    print(f"   Fetched {len(users)} users")
    return users

def load_users(conn, users: List[Dict]):
    """Load users into database using UPSERT."""
    ingested_at = datetime.now(timezone.utc)
    
    with conn.cursor() as cur:
        for user in users:
            cur.execute("""
                INSERT INTO api_users (id, name, username, email, phone, website, company_name, ingested_at)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO UPDATE SET
                    name = EXCLUDED.name,
                    username = EXCLUDED.username,
                    email = EXCLUDED.email,
                    phone = EXCLUDED.phone,
                    website = EXCLUDED.website,
                    company_name = EXCLUDED.company_name,
                    ingested_at = EXCLUDED.ingested_at;
            """, (
                user['id'],
                user['name'],
                user['username'],
                user['email'],
                user.get('phone'),
                user.get('website'),
                user.get('company', {}).get('name'),
                ingested_at
            ))
        conn.commit()
    print(f"✅ Loaded {len(users)} users to database")

def get_row_count(conn) -> int:
    """Get current row count."""
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM api_users;")
        return cur.fetchone()[0]

def main():
    print("=" * 60)
    print("DATA PIPELINE: API → PostgreSQL")
    print("=" * 60)
    
    # Connect to database
    print("\n🔌 Connecting to database...")
    conn = get_db_connection()
    print(f"   Connected to {os.getenv('DB_HOST', 'postgres')}")
    
    # Create tables
    create_tables(conn)
    
    # Fetch data
    users = fetch_users()
    
    # Load data
    print("\n💾 Loading to database...")
    load_users(conn, users)
    
    # Verify
    count = get_row_count(conn)
    print(f"\n📊 Total rows in api_users: {count}")
    
    # Cleanup
    conn.close()
    
    print("\n" + "=" * 60)
    print("PIPELINE COMPLETE!")
    print("=" * 60)

if __name__ == "__main__":
    main()
EOF

STEP 3: Create requirements.txt

    cat > ~/compose-practice/pipeline/requirements.txt << 'EOF'
requests==2.31.0
psycopg2-binary==2.9.9
EOF

STEP 4: Create Dockerfile for pipeline

    cat > ~/compose-practice/pipeline/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY main.py .

CMD ["python", "main.py"]
EOF

STEP 5: Update docker-compose.yml

    cat > ~/compose-practice/docker-compose.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: learning-postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: secretpassword
      POSTGRES_DB: pipeline_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d pipeline_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  pipeline:
    build: ./pipeline
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      DB_HOST: postgres
      DB_PORT: 5432
      DB_NAME: pipeline_db
      DB_USER: dataeng
      DB_PASSWORD: secretpassword

volumes:
  postgres_data:
EOF

Key points:
- depends_on with condition: service_healthy waits for PostgreSQL
- Pipeline connects to "postgres" (the service name)
- Environment variables configure the connection


STEP 6: Build and run

    cd ~/compose-practice
    docker compose build
    docker compose up

Watch the output - pipeline waits for Postgres, then loads data.

STEP 7: Verify data in database

    docker compose exec postgres psql -U dataeng -d pipeline_db -c "SELECT id, name, email FROM api_users;"

STEP 8: Run pipeline again (test idempotency)

    docker compose run --rm pipeline

The UPSERT (ON CONFLICT) prevents duplicates!
"""


"""
EXERCISE 4: MULTI-STAGE BUILDS (20 min)
=======================================

Multi-stage builds create smaller, more secure images.

The problem: Development images have tools you don't need in production
(compilers, dev dependencies, etc.)

Multi-stage solution: Build in one stage, copy only artifacts to final stage.

STEP 1: Create example with multi-stage build

    cat > ~/compose-practice/pipeline/Dockerfile << 'EOF'
# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: Runtime (final image)
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY main.py .

# Run as non-root user
RUN useradd --create-home appuser
USER appuser

CMD ["python", "main.py"]
EOF

STEP 2: Rebuild and check image size

    docker compose build pipeline
    
    # Compare sizes
    docker images | grep -E "python|pipeline"

The multi-stage image is smaller because it doesn't include
build tools from the first stage.
"""


"""
EXERCISE 5: LOCAL DEVELOPMENT WORKFLOW (30 min)
===============================================

Let's set up a professional local development environment.

STEP 1: Create development docker-compose override

    cat > ~/compose-practice/docker-compose.override.yml << 'EOF'
version: '3.8'

services:
  postgres:
    # Add pgAdmin for database GUI
    ports:
      - "5432:5432"

  pgadmin:
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      - postgres

  pipeline:
    # Mount local code for development (hot reload)
    volumes:
      - ./pipeline:/app
    # Override command to just keep container running
    command: ["tail", "-f", "/dev/null"]
EOF

STEP 2: Start the development environment

    docker compose up -d

STEP 3: Access pgAdmin

    Open http://localhost:8080 in your browser
    Login: admin@admin.com / admin
    
    Add server:
    - Name: Local
    - Host: postgres (not localhost!)
    - Port: 5432
    - Username: dataeng
    - Password: secretpassword

STEP 4: Develop inside the container

    # Execute into the running container
    docker compose exec pipeline bash
    
    # Inside container, you can run Python
    python main.py
    
    # Make changes to local files, they appear in container immediately

STEP 5: Stop development environment

    docker compose down
"""


"""
EXERCISE 6: HEALTH CHECKS AND DEPENDENCIES (20 min)
===================================================

Proper health checks ensure services start in the right order.

STEP 1: Add health check to pipeline

    cat > ~/compose-practice/pipeline/healthcheck.py << 'EOF'
import sys
import psycopg2
import os

def check_health():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "postgres"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "pipeline_db"),
            user=os.getenv("DB_USER", "dataeng"),
            password=os.getenv("DB_PASSWORD", "secretpassword")
        )
        cur = conn.cursor()
        cur.execute("SELECT 1")
        conn.close()
        return True
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

if __name__ == "__main__":
    sys.exit(0 if check_health() else 1)
EOF

STEP 2: Update Dockerfile to include health check script

Add this to the Dockerfile:
    COPY healthcheck.py .
    HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
        CMD python healthcheck.py
"""


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Docker Compose Commands:
[ ] docker compose up
[ ] docker compose up -d
[ ] docker compose down
[ ] docker compose logs
[ ] docker compose exec <service> <command>
[ ] docker compose build
[ ] docker compose ps

docker-compose.yml concepts:
[ ] services
[ ] image vs build
[ ] environment variables
[ ] ports
[ ] volumes
[ ] depends_on
[ ] healthcheck

Data Engineering patterns:
[ ] Running PostgreSQL in Docker
[ ] Connecting Python to Dockerized database
[ ] Volume persistence for databases
[ ] Multi-stage builds
[ ] Development override files


KNOWLEDGE CHECK QUESTIONS:
==========================

1. Your pipeline container can't connect to the database container.
   The database hostname is "localhost". What's wrong?
   
2. You stop and restart Docker Compose. Your database data is gone.
   What did you forget?
   
3. Your production image is 2GB but your app is only 50MB.
   What technique could reduce the image size?

Write your answers before moving on.


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 19: Docker for Data Engineering"
    git push


WHAT'S NEXT:
============
Day 20: Week 3 Project - Containerized Data Pipeline
- Build a complete containerized pipeline
- API → S3 → PostgreSQL
- Full Docker Compose setup
- Proper logging and error handling
"""


if __name__ == "__main__":
    print("Day 19: Docker for Data Engineering")
    print("=" * 50)
    print("\nThis lesson uses Docker Compose.")
    print("Follow the exercises in the comments above.")
    print("\nKey commands:")
    print("  docker compose up -d")
    print("  docker compose exec postgres psql -U dataeng -d pipeline_db")
    print("  docker compose logs")
    print("  docker compose down")
