#!/usr/bin/env python3
"""
Day 22: Docker Compose + Local Dev Stack
==========================================
Duration: 2-2.5 hours

Set up a complete local development environment with Docker Compose.
PostgreSQL, Adminer, and your pipeline - all containerized.

WHY THIS MATTERS:
- Real development uses multi-container setups
- Database + app + tools in one command
- Reproducible across machines
- This is how teams work

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Multi-Container Setup (30 min)
==========================================

Create a docker-compose.yml with:
- PostgreSQL database
- Adminer (database UI)
- Your pipeline from Week 3

docker-compose.yml:
---
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: pipeline
      POSTGRES_PASSWORD: pipeline123
      POSTGRES_DB: stockdata
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  adminer:
    image: adminer
    ports:
      - "8080:8080"
    depends_on:
      - postgres

volumes:
  postgres_data:


Commands:
  docker-compose up -d
  docker-compose logs postgres
  # Open http://localhost:8080 for Adminer


EXERCISE 2: Environment Variables (20 min)
==========================================

Create .env file:
  POSTGRES_USER=pipeline
  POSTGRES_PASSWORD=pipeline123
  POSTGRES_DB=stockdata
  API_KEY=your_alpha_vantage_key

Reference in docker-compose.yml:
  environment:
    - POSTGRES_USER=${POSTGRES_USER}
    - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}


EXERCISE 3: Health Checks (20 min)
==================================

Add health checks to ensure services are ready:

postgres:
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U pipeline"]
    interval: 5s
    timeout: 5s
    retries: 5

pipeline:
  depends_on:
    postgres:
      condition: service_healthy


EXERCISE 4: Networking (20 min)
===============================

Create custom network for isolation:

networks:
  pipeline-network:
    driver: bridge

services:
  postgres:
    networks:
      - pipeline-network


EXERCISE 5: Init Scripts (20 min)
==================================

Auto-create tables on startup:

volumes:
  - ./init:/docker-entrypoint-initdb.d

Create init/01_schema.sql:
  CREATE TABLE IF NOT EXISTS stock_prices (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(10, 2),
    volume BIGINT,
    timestamp TIMESTAMP DEFAULT NOW()
  );


EXERCISE 6: Verify Everything (30 min)
======================================

1. Start all services: docker-compose up -d
2. Check logs: docker-compose logs -f
3. Open Adminer: http://localhost:8080
4. Login: postgres / pipeline / pipeline123 / stockdata
5. Verify tables exist
6. Insert test data
7. Query from Python
"""

import os
import subprocess
from typing import Dict, Optional

def check_docker_compose() -> bool:
    """Check if docker-compose is installed."""
    try:
        result = subprocess.run(
            ["docker-compose", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except:
        return False


def check_running_containers() -> Dict[str, str]:
    """Get status of running containers."""
    try:
        result = subprocess.run(
            ["docker", "ps", "--format", "{{.Names}}: {{.Status}}"],
            capture_output=True,
            text=True
        )
        containers = {}
        for line in result.stdout.strip().split('\n'):
            if ':' in line:
                name, status = line.split(':', 1)
                containers[name.strip()] = status.strip()
        return containers
    except:
        return {}


def verify_setup() -> None:
    """Verify Docker Compose setup."""
    print("=" * 50)
    print("DOCKER COMPOSE SETUP VERIFICATION")
    print("=" * 50)
    
    if check_docker_compose():
        print("✅ docker-compose installed")
    else:
        print("❌ docker-compose not found")
    
    containers = check_running_containers()
    if containers:
        print("\nRunning containers:")
        for name, status in containers.items():
            print(f"  {name}: {status}")
    else:
        print("\n⚠️ No containers running")
    
    # Check for docker-compose.yml
    if os.path.exists("docker-compose.yml"):
        print("\n✅ docker-compose.yml found")
    else:
        print("\n⚠️ No docker-compose.yml in current directory")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "verify":
        verify_setup()
    else:
        print("Day 22: Docker Compose + Local Dev Stack")
        print("=" * 45)
        print("\nBuild a complete local development environment.")
        print("\nCommands:")
        print("  python day22_docker_compose.py verify - Check your setup")
