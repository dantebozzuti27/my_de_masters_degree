#!/usr/bin/env python3
"""
Day 19: Docker for Data Engineering
=====================================
Duration: 2 hours

Apply Docker to data engineering workflows.
Build containerized data pipelines and local development environments.

WHY THIS MATTERS:
- Real data pipelines run in containers
- Local development should mirror production
- Docker Compose = instant data stack
- This is how senior engineers work

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import json
from typing import Dict, List, Optional

# =============================================================================
# DATA ENGINEERING DOCKER EXERCISES
# =============================================================================

"""
EXERCISE 1: Containerized Data Pipeline (30 min)
=================================================

Build a complete data extraction pipeline in Docker.

1. Create project structure:
   data-pipeline/
   ├── Dockerfile
   ├── requirements.txt
   ├── src/
   │   ├── __init__.py
   │   ├── extractor.py
   │   └── transformer.py
   └── config/
       └── config.json

2. requirements.txt:
   requests==2.31.0
   pandas==2.1.0
   python-dotenv==1.0.0

3. src/extractor.py:
   import requests
   import json
   import os
   
   def extract_data(url: str) -> dict:
       response = requests.get(url)
       response.raise_for_status()
       return response.json()
   
   def save_raw(data: dict, output_path: str):
       os.makedirs(os.path.dirname(output_path), exist_ok=True)
       with open(output_path, 'w') as f:
           json.dump(data, f, indent=2)
       print(f"Saved raw data to {output_path}")
   
   if __name__ == "__main__":
       url = os.getenv("DATA_URL", "https://jsonplaceholder.typicode.com/users")
       output = os.getenv("OUTPUT_PATH", "/data/raw/users.json")
       
       data = extract_data(url)
       save_raw(data, output)

4. Dockerfile:
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY src/ ./src/
   COPY config/ ./config/
   
   ENV PYTHONPATH=/app
   ENV PYTHONUNBUFFERED=1
   
   CMD ["python", "-m", "src.extractor"]

5. Build and run:
   docker build -t data-pipeline .
   docker run -v $(pwd)/output:/data data-pipeline


EXERCISE 2: Local Data Stack with Docker Compose (40 min)
==========================================================

Create a complete local development environment:

docker-compose.yml:

version: '3.8'

services:
  # PostgreSQL database
  postgres:
    image: postgres:15
    container_name: de_postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: localdev123
      POSTGRES_DB: warehouse
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d warehouse"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Adminer for database UI
  adminer:
    image: adminer
    container_name: de_adminer
    ports:
      - "8081:8080"
    depends_on:
      - postgres

  # MinIO (S3-compatible storage)
  minio:
    image: minio/minio
    container_name: de_minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - minio_data:/data
    command: server /data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  # Redis for caching
  redis:
    image: redis:7-alpine
    container_name: de_redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Your Python app
  app:
    build: .
    container_name: de_app
    environment:
      DATABASE_URL: postgresql://dataeng:localdev123@postgres:5432/warehouse
      S3_ENDPOINT: http://minio:9000
      S3_ACCESS_KEY: minioadmin
      S3_SECRET_KEY: minioadmin
      REDIS_URL: redis://redis:6379
    volumes:
      - ./src:/app/src
      - ./data:/data
    depends_on:
      postgres:
        condition: service_healthy
      minio:
        condition: service_healthy

volumes:
  postgres_data:
  minio_data:
  redis_data:

Commands:
  docker-compose up -d       # Start all services
  docker-compose ps          # See service status
  docker-compose logs -f     # Follow logs
  docker-compose down        # Stop all services
  docker-compose down -v     # Stop and remove volumes


EXERCISE 3: Database Init Scripts (20 min)
==========================================

Create init-scripts/01_create_tables.sql:

-- Create schema
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS mart;

-- Raw layer
CREATE TABLE raw.api_users (
    id SERIAL PRIMARY KEY,
    raw_data JSONB NOT NULL,
    extracted_at TIMESTAMP DEFAULT NOW(),
    source VARCHAR(255)
);

-- Staging layer
CREATE TABLE staging.users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    company VARCHAR(255),
    city VARCHAR(255),
    loaded_at TIMESTAMP DEFAULT NOW()
);

-- Mart layer
CREATE TABLE mart.user_summary (
    city VARCHAR(255),
    user_count INTEGER,
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes
CREATE INDEX idx_users_city ON staging.users(city);
CREATE INDEX idx_raw_extracted ON raw.api_users(extracted_at);

This runs automatically when Postgres container first starts.


EXERCISE 4: Python App with Database Connection (25 min)
=========================================================

Update src/transformer.py:

import os
import json
import psycopg2
from psycopg2.extras import execute_values

def get_db_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def load_raw_to_staging(conn, raw_path: str):
    with open(raw_path) as f:
        users = json.load(f)
    
    # Insert to raw
    with conn.cursor() as cur:
        for user in users:
            cur.execute(
                \"\"\"INSERT INTO raw.api_users (raw_data, source) 
                   VALUES (%s, %s)\"\"\",
                (json.dumps(user), 'jsonplaceholder')
            )
    
    # Transform to staging
    staging_data = [
        (u['id'], u['name'], u['email'], 
         u['company']['name'], u['address']['city'])
        for u in users
    ]
    
    with conn.cursor() as cur:
        execute_values(
            cur,
            \"\"\"INSERT INTO staging.users (id, name, email, company, city) 
               VALUES %s ON CONFLICT (id) DO UPDATE SET
               name = EXCLUDED.name, email = EXCLUDED.email\"\"\",
            staging_data
        )
    
    conn.commit()
    print(f"Loaded {len(users)} users to staging")

def create_mart(conn):
    with conn.cursor() as cur:
        cur.execute(\"\"\"
            INSERT INTO mart.user_summary (city, user_count)
            SELECT city, COUNT(*) 
            FROM staging.users 
            GROUP BY city
            ON CONFLICT DO NOTHING
        \"\"\")
    conn.commit()
    print("Created mart summary")

if __name__ == "__main__":
    conn = get_db_connection()
    load_raw_to_staging(conn, "/data/raw/users.json")
    create_mart(conn)
    conn.close()


EXERCISE 5: Running the Full Pipeline (15 min)
===============================================

1. Start the stack:
   docker-compose up -d

2. Wait for services:
   docker-compose ps  # All should show "healthy"

3. Run extractor:
   docker-compose run app python -m src.extractor

4. Run transformer:
   docker-compose run app python -m src.transformer

5. Check results:
   - Open http://localhost:8081 (Adminer)
   - Login: postgres, dataeng, localdev123, warehouse
   - Query: SELECT * FROM staging.users;


EXERCISE 6: Development Workflow (10 min)
==========================================

Hot reload for development:

1. Your code is mounted via volume:
   volumes:
     - ./src:/app/src

2. Changes in ./src/ immediately appear in container

3. Run commands without rebuilding:
   docker-compose run app python -m src.my_script

4. Interactive shell:
   docker-compose run app bash

5. Install new packages:
   # Add to requirements.txt, then:
   docker-compose build app
   docker-compose up -d app
"""

# =============================================================================
# DOCKER COMPOSE TEMPLATES
# =============================================================================

COMPOSE_TEMPLATES = {
    "minimal_data_stack": """version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: datawarehouse
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
""",

    "full_data_stack": """version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: localdev
      POSTGRES_DB: warehouse
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready"]
      interval: 10s
      timeout: 5s
      retries: 5

  minio:
    image: minio/minio
    ports:
      - "9000:9000"
      - "9001:9001"
    environment:
      MINIO_ROOT_USER: minioadmin
      MINIO_ROOT_PASSWORD: minioadmin
    volumes:
      - minio_data:/data
    command: server /data --console-address ":9001"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  adminer:
    image: adminer
    ports:
      - "8081:8080"
    depends_on:
      - postgres

volumes:
  postgres_data:
  minio_data:
""",

    "airflow_local": """version: '3.8'

x-airflow-common: &airflow-common
  image: apache/airflow:2.7.0
  environment:
    AIRFLOW__CORE__EXECUTOR: LocalExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
  depends_on:
    postgres:
      condition: service_healthy

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "8080:8080"

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler

  airflow-init:
    <<: *airflow-common
    command: version
    environment:
      _AIRFLOW_DB_UPGRADE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: admin
      _AIRFLOW_WWW_USER_PASSWORD: admin
"""
}


def print_compose_template(name: str) -> None:
    """Print a Docker Compose template."""
    if name not in COMPOSE_TEMPLATES:
        print(f"Unknown template. Available: {', '.join(COMPOSE_TEMPLATES.keys())}")
        return
    
    print(f"# docker-compose.yml template: {name}")
    print("-" * 40)
    print(COMPOSE_TEMPLATES[name])


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def create_data_pipeline_project(path: str = "data-pipeline") -> None:
    """Create a starter data pipeline project structure."""
    
    # Create directories
    os.makedirs(f"{path}/src", exist_ok=True)
    os.makedirs(f"{path}/config", exist_ok=True)
    os.makedirs(f"{path}/init-scripts", exist_ok=True)
    os.makedirs(f"{path}/data/raw", exist_ok=True)
    os.makedirs(f"{path}/data/processed", exist_ok=True)
    
    # Create __init__.py
    open(f"{path}/src/__init__.py", 'w').close()
    
    # Create requirements.txt
    with open(f"{path}/requirements.txt", 'w') as f:
        f.write("requests==2.31.0\npandas==2.1.0\npsycopg2-binary==2.9.9\npython-dotenv==1.0.0\n")
    
    # Create Dockerfile
    with open(f"{path}/Dockerfile", 'w') as f:
        f.write("""FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY config/ ./config/

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

CMD ["python", "-m", "src.main"]
""")
    
    # Create docker-compose.yml
    with open(f"{path}/docker-compose.yml", 'w') as f:
        f.write(COMPOSE_TEMPLATES["full_data_stack"])
    
    # Create .gitignore
    with open(f"{path}/.gitignore", 'w') as f:
        f.write("__pycache__/\n*.pyc\n.env\ndata/\n*.log\n")
    
    # Create sample extractor
    with open(f"{path}/src/extractor.py", 'w') as f:
        f.write("""import requests
import json
import os

def extract_data(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_raw(data, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    url = os.getenv("DATA_URL", "https://jsonplaceholder.typicode.com/users")
    output = os.getenv("OUTPUT_PATH", "/data/raw/users.json")
    data = extract_data(url)
    save_raw(data, output)
""")
    
    print(f"✅ Created data pipeline project at {path}/")
    print("\nNext steps:")
    print(f"  cd {path}")
    print("  docker-compose up -d")
    print("  docker-compose run app python -m src.extractor")


# =============================================================================
# Verification
# =============================================================================

def verify_data_stack() -> None:
    """Verify the data engineering stack is running."""
    import subprocess
    
    print("=" * 60)
    print("DATA STACK VERIFICATION")
    print("=" * 60 + "\n")
    
    # Check if docker-compose is available
    try:
        result = subprocess.run(
            ["docker", "compose", "version"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ Docker Compose: {result.stdout.strip()}")
        else:
            # Try legacy docker-compose
            result = subprocess.run(
                ["docker-compose", "--version"],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                print(f"✅ Docker Compose: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Docker Compose not found")
        return
    
    # Check running containers
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}\t{{.Status}}"],
            capture_output=True, text=True
        )
        
        if result.returncode == 0 and result.stdout.strip():
            print("\n📦 Running containers:")
            for line in result.stdout.strip().split("\n"):
                parts = line.split("\t")
                name = parts[0]
                status = parts[1] if len(parts) > 1 else "unknown"
                healthy = "✅" if "healthy" in status.lower() or "up" in status.lower() else "⚠️"
                print(f"   {healthy} {name}: {status}")
        else:
            print("\n⚠️  No containers running")
            print("   Run: docker-compose up -d")
    except Exception as e:
        print(f"❌ Error checking containers: {e}")
    
    print("\n" + "-" * 40)
    print("Service URLs (when running):")
    print("  PostgreSQL: localhost:5432")
    print("  Adminer:    http://localhost:8081")
    print("  MinIO:      http://localhost:9001")
    print("  Redis:      localhost:6379")
    print("-" * 40)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "verify":
            verify_data_stack()
        elif cmd == "template":
            name = sys.argv[2] if len(sys.argv) > 2 else "minimal_data_stack"
            print_compose_template(name)
        elif cmd == "templates":
            print("Available Docker Compose templates:")
            for name in COMPOSE_TEMPLATES:
                print(f"  - {name}")
        elif cmd == "create":
            path = sys.argv[2] if len(sys.argv) > 2 else "data-pipeline"
            create_data_pipeline_project(path)
    else:
        print("Day 19: Docker for Data Engineering")
        print("=" * 40)
        print("\nApply Docker to data engineering workflows.")
        print("\nCommands:")
        print("  python day19_docker_data_engineering.py verify    - Check running services")
        print("  python day19_docker_data_engineering.py templates - List compose templates")
        print("  python day19_docker_data_engineering.py template <name> - Show template")
        print("  python day19_docker_data_engineering.py create [path] - Create starter project")
