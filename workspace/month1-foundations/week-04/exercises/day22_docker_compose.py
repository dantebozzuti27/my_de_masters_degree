#!/usr/bin/env python3
"""
Day 22: Advanced Docker Compose - Multi-Service Architectures
==============================================================
Duration: 3-4 hours total

Today you'll master Docker Compose for complex, production-like setups:
- Multi-service architectures
- Networks and service discovery
- Health checks and dependencies
- Environment management
- Scaling services

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: Docker fundamentals (Days 18-19)

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHAT ARE MULTI-SERVICE ARCHITECTURES?
=====================================

Real applications aren't single containers. They're systems of services:

    ┌─────────────────────────────────────────────────────────────┐
    │                     Typical Data Stack                       │
    │                                                              │
    │   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐ │
    │   │   API   │    │Pipeline │    │  Queue  │    │  Cache  │ │
    │   │ Server  │    │ Worker  │    │ (Redis) │    │ (Redis) │ │
    │   └────┬────┘    └────┬────┘    └────┬────┘    └────┬────┘ │
    │        │              │              │              │       │
    │        └──────────────┴──────────────┴──────────────┘       │
    │                            │                                 │
    │                     ┌──────┴──────┐                         │
    │                     │  PostgreSQL │                         │
    │                     │  (Primary)  │                         │
    │                     └─────────────┘                         │
    └─────────────────────────────────────────────────────────────┘

Docker Compose orchestrates ALL of these with ONE command.


DOCKER COMPOSE CONCEPTS:
========================

1. SERVICES
   Each container type is a "service"
   One service can have multiple containers (scaling)

2. NETWORKS
   Compose creates a default network
   Services can communicate by service name
   Can create custom networks for isolation

3. VOLUMES
   Persist data between container restarts
   Named volumes vs bind mounts
   
4. DEPENDS_ON
   Control startup order
   Wait for health checks

5. ENVIRONMENT FILES
   .env files for configuration
   Different files for dev/staging/prod


COMPOSE FILE STRUCTURE:
=======================

version: '3.8'              # Compose file format version

services:                   # Container definitions
  service-name:             # Service name (becomes hostname)
    image: ...              # Use existing image
    build: ...              # Or build from Dockerfile
    environment: ...        # Environment variables
    ports: ...              # Port mappings
    volumes: ...            # Data persistence
    networks: ...           # Network connections
    depends_on: ...         # Dependencies
    healthcheck: ...        # Health monitoring
    deploy: ...             # Scaling/resources

networks:                   # Custom networks
  network-name:
    driver: bridge

volumes:                    # Named volumes
  volume-name:


LEARNING RESOURCES:
==================

VIDEO:
- "Docker Compose Tutorial" - TechWorld with Nana (25 min)
  https://www.youtube.com/watch?v=HG6yIjZapSA

READING:
- Docker Compose specification
  https://docs.docker.com/compose/compose-file/

After learning, answer:
1. How do services discover each other in Compose?
2. What's the difference between `depends_on` and health checks?
3. When would you use custom networks?
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

"""
EXERCISE 1: MULTI-SERVICE BASICS (25 min)
=========================================

Let's build a realistic multi-service application.

STEP 1: Create project

    mkdir -p ~/compose-advanced
    cd ~/compose-advanced

STEP 2: Create a comprehensive docker-compose.yml

    cat > ~/compose-advanced/docker-compose.yml << 'EOF'
version: '3.8'

services:
  # ========================================
  # DATABASE: PostgreSQL
  # ========================================
  postgres:
    image: postgres:15
    container_name: app-postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: ${DB_PASSWORD:-secretpassword}
      POSTGRES_DB: appdb
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d:ro
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    networks:
      - backend

  # ========================================
  # CACHE: Redis
  # ========================================
  redis:
    image: redis:7-alpine
    container_name: app-redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  # ========================================
  # ADMIN: Adminer (DB GUI)
  # ========================================
  adminer:
    image: adminer:latest
    container_name: app-adminer
    ports:
      - "8080:8080"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - backend

networks:
  backend:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
EOF

Let's understand each part:

- postgres: Our main database
  - Uses environment variable with fallback: ${DB_PASSWORD:-secretpassword}
  - Mounts init scripts for automatic setup
  - Health check ensures database is ready
  
- redis: In-memory cache (used in real pipelines)
  - --appendonly yes: Persist data to disk
  - alpine: Smaller image
  
- adminer: Web UI for database management
  - Waits for postgres to be healthy
  
- networks: backend
  - All services share this network
  - Can reference each other by name
  
- volumes: Named volumes for persistence


STEP 3: Create database init script

    mkdir -p ~/compose-advanced/init-scripts
    
    cat > ~/compose-advanced/init-scripts/01-create-tables.sql << 'EOF'
-- This runs automatically when PostgreSQL first starts

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    event_type VARCHAR(50) NOT NULL,
    event_data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for common queries
CREATE INDEX idx_events_user_id ON events(user_id);
CREATE INDEX idx_events_created_at ON events(created_at);

-- Insert sample data
INSERT INTO users (username, email) VALUES 
    ('alice', 'alice@example.com'),
    ('bob', 'bob@example.com'),
    ('charlie', 'charlie@example.com')
ON CONFLICT DO NOTHING;
EOF


STEP 4: Start all services

    cd ~/compose-advanced
    docker compose up -d

STEP 5: Check status

    docker compose ps
    
All services should show "healthy" after a minute.

STEP 6: Test database connection

    docker compose exec postgres psql -U dataeng -d appdb -c "SELECT * FROM users;"

STEP 7: Test Redis

    docker compose exec redis redis-cli SET greeting "Hello from Redis"
    docker compose exec redis redis-cli GET greeting

STEP 8: Access Adminer

    Open http://localhost:8080
    System: PostgreSQL
    Server: postgres
    Username: dataeng
    Password: secretpassword
    Database: appdb
"""


"""
EXERCISE 2: ENVIRONMENT FILES (20 min)
======================================

Production systems use .env files for configuration.

STEP 1: Create environment file

    cat > ~/compose-advanced/.env << 'EOF'
# Database
DB_PASSWORD=myproductionpassword123
DB_USER=dataeng
DB_NAME=appdb

# Redis
REDIS_PASSWORD=redispassword

# Application
APP_ENV=development
LOG_LEVEL=DEBUG
EOF

STEP 2: Create .env.example (for version control)

    cat > ~/compose-advanced/.env.example << 'EOF'
# Copy this to .env and fill in values

# Database
DB_PASSWORD=
DB_USER=dataeng
DB_NAME=appdb

# Redis  
REDIS_PASSWORD=

# Application
APP_ENV=development
LOG_LEVEL=INFO
EOF

STEP 3: Update docker-compose.yml to use .env

    cat > ~/compose-advanced/docker-compose.yml << 'EOF'
version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: app-postgres
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d:ro
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER} -d ${DB_NAME}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  redis:
    image: redis:7-alpine
    container_name: app-redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  adminer:
    image: adminer:latest
    container_name: app-adminer
    ports:
      - "8080:8080"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - backend

networks:
  backend:

volumes:
  postgres_data:
  redis_data:
EOF

STEP 4: Restart with new config

    cd ~/compose-advanced
    docker compose down
    docker compose up -d

STEP 5: Verify environment was loaded

    docker compose exec postgres env | grep POSTGRES

IMPORTANT: Add .env to .gitignore!

    echo ".env" >> ~/compose-advanced/.gitignore
"""


"""
EXERCISE 3: CUSTOM NETWORKS (20 min)
====================================

Networks isolate services and control communication.

STEP 1: Create docker-compose with multiple networks

    cat > ~/compose-advanced/docker-compose.yml << 'EOF'
version: '3.8'

services:
  # Frontend network only
  web:
    image: nginx:alpine
    container_name: app-web
    ports:
      - "80:80"
    networks:
      - frontend
    healthcheck:
      test: ["CMD", "wget", "-q", "--spider", "http://localhost"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Both networks - can talk to web AND database
  api:
    image: python:3.11-slim
    container_name: app-api
    command: python -c "import time; print('API running...'); time.sleep(3600)"
    networks:
      - frontend
      - backend
    depends_on:
      postgres:
        condition: service_healthy

  # Backend only - isolated from web
  postgres:
    image: postgres:15
    container_name: app-postgres
    environment:
      POSTGRES_USER: ${DB_USER:-dataeng}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-secretpassword}
      POSTGRES_DB: ${DB_NAME:-appdb}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Backend only
  redis:
    image: redis:7-alpine
    container_name: app-redis
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge

volumes:
  postgres_data:
EOF

This creates:
- frontend network: web, api
- backend network: api, postgres, redis

The web server CANNOT reach postgres directly.
Only api can access both.

STEP 2: Start and test

    docker compose down
    docker compose up -d

STEP 3: Test network isolation

    # API can reach postgres
    docker compose exec api python -c "import socket; socket.create_connection(('postgres', 5432)); print('API can reach postgres')"
    
    # Web cannot reach postgres (this will fail - that's correct!)
    docker compose exec web sh -c "nc -zv postgres 5432 2>&1 || echo 'Web cannot reach postgres - CORRECT!'"
"""


"""
EXERCISE 4: HEALTH CHECKS AND DEPENDENCIES (25 min)
===================================================

Proper health checks are critical for production.

STEP 1: Create comprehensive health check example

    cat > ~/compose-advanced/docker-compose.yml << 'EOF'
version: '3.8'

services:
  # Database - must start first
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: secretpassword
      POSTGRES_DB: appdb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d appdb"]
      interval: 5s
      timeout: 5s
      retries: 10
      start_period: 10s
    networks:
      - backend

  # Cache - can start in parallel with postgres
  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 10
    networks:
      - backend

  # Worker - needs BOTH postgres AND redis
  worker:
    image: python:3.11-slim
    command: python -c "print('Worker starting'); import time; time.sleep(3600)"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    networks:
      - backend

  # Scheduler - needs worker to be running
  scheduler:
    image: python:3.11-slim
    command: python -c "print('Scheduler starting'); import time; time.sleep(3600)"
    depends_on:
      worker:
        condition: service_started
    networks:
      - backend

networks:
  backend:
EOF

STEP 2: Start and watch the ordering

    docker compose up

Watch how:
1. postgres and redis start in parallel
2. worker waits for BOTH to be healthy
3. scheduler waits for worker to start

STEP 3: See health status

    docker compose ps

The STATUS column shows health state.
"""


"""
EXERCISE 5: DATA PIPELINE STACK (30 min)
========================================

Let's build a realistic data engineering stack.

STEP 1: Create complete data stack

    mkdir -p ~/data-stack
    cd ~/data-stack

    cat > ~/data-stack/docker-compose.yml << 'EOF'
version: '3.8'

services:
  # ========================================
  # DATA STORAGE
  # ========================================
  
  # PostgreSQL - Primary data warehouse
  postgres:
    image: postgres:15
    container_name: datastack-postgres
    environment:
      POSTGRES_USER: dataeng
      POSTGRES_PASSWORD: ${DB_PASSWORD:-dataengpass}
      POSTGRES_DB: warehouse
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U dataeng -d warehouse"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - datastack

  # Redis - Caching and job queues
  redis:
    image: redis:7-alpine
    container_name: datastack-redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - datastack

  # ========================================
  # ADMIN TOOLS
  # ========================================
  
  # pgAdmin - PostgreSQL management
  pgadmin:
    image: dpage/pgadmin4:latest
    container_name: datastack-pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@dataeng.local
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "8080:80"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - datastack

  # Redis Commander - Redis management
  redis-commander:
    image: rediscommander/redis-commander:latest
    container_name: datastack-redis-commander
    environment:
      REDIS_HOSTS: local:redis:6379
    ports:
      - "8081:8081"
    depends_on:
      redis:
        condition: service_healthy
    networks:
      - datastack

networks:
  datastack:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
EOF

STEP 2: Create .env file

    cat > ~/data-stack/.env << 'EOF'
DB_PASSWORD=dataengpass
EOF

STEP 3: Start the stack

    cd ~/data-stack
    docker compose up -d

STEP 4: Verify all services

    docker compose ps
    
    # Check logs
    docker compose logs postgres
    docker compose logs redis

STEP 5: Access the tools

    - pgAdmin: http://localhost:8080
      Login: admin@dataeng.local / admin
      
    - Redis Commander: http://localhost:8081

STEP 6: Connect pgAdmin to PostgreSQL

    In pgAdmin:
    1. Right-click "Servers" → "Register" → "Server"
    2. Name: Local PostgreSQL
    3. Connection tab:
       - Host: postgres (not localhost!)
       - Port: 5432
       - Username: dataeng
       - Password: dataengpass
"""


"""
EXERCISE 6: COMPOSE COMMANDS MASTERY (20 min)
=============================================

Let's master all the essential Compose commands.

    cd ~/data-stack

VIEW SERVICES:
    docker compose ps              # Running services
    docker compose ps -a           # All services (including stopped)
    docker compose top             # Processes in each service

LOGS:
    docker compose logs            # All logs
    docker compose logs postgres   # Specific service
    docker compose logs -f         # Follow logs
    docker compose logs --tail=50  # Last 50 lines

START/STOP:
    docker compose up              # Start all
    docker compose up -d           # Detached mode
    docker compose up postgres     # Start specific service
    docker compose stop            # Stop all (keep containers)
    docker compose start           # Start stopped containers
    docker compose down            # Stop and remove containers
    docker compose down -v         # Also remove volumes (DELETES DATA!)

EXECUTE:
    docker compose exec postgres bash            # Shell into container
    docker compose exec postgres psql -U dataeng # Run command
    docker compose run --rm postgres psql -U dataeng  # Run in new container

BUILD:
    docker compose build           # Build all images
    docker compose build --no-cache  # Force rebuild
    docker compose up --build      # Build and start

CLEANUP:
    docker compose down            # Remove containers
    docker compose down -v         # Remove volumes too
    docker compose rm -f           # Force remove stopped containers
"""


"""
EXERCISE 7: SCALING SERVICES (15 min)
=====================================

Docker Compose can run multiple instances of a service.

STEP 1: Create scalable worker

    cat > ~/data-stack/docker-compose.override.yml << 'EOF'
version: '3.8'

services:
  worker:
    image: python:3.11-slim
    command: python -c "import os, time; print(f'Worker {os.getenv(\"HOSTNAME\")} starting'); time.sleep(3600)"
    depends_on:
      redis:
        condition: service_healthy
    networks:
      - datastack
EOF

STEP 2: Start with multiple workers

    docker compose up -d --scale worker=3

STEP 3: Check workers

    docker compose ps worker
    docker compose logs worker

You should see 3 worker containers with different hostnames.

STEP 4: Scale down

    docker compose up -d --scale worker=1

Note: For stateless services only! Databases can't be scaled this way.
"""


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Commands:
[ ] docker compose up -d
[ ] docker compose down
[ ] docker compose ps
[ ] docker compose logs <service>
[ ] docker compose exec <service> <command>
[ ] docker compose --scale <service>=N

Compose file concepts:
[ ] services
[ ] networks
[ ] volumes
[ ] environment variables
[ ] healthcheck
[ ] depends_on with conditions

Best practices:
[ ] Use .env files for configuration
[ ] Never commit .env to git
[ ] Use health checks for all services
[ ] Use named volumes for data persistence
[ ] Use custom networks for isolation


KNOWLEDGE CHECK:
================

1. Your pipeline can't connect to postgres with error "connection refused".
   The service name is correct. What could be wrong?

2. You run `docker compose down` and lose all your database data.
   What should you have done differently?

3. You want postgres to not be accessible from the public-facing web service.
   How would you structure networks?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 22: Advanced Docker Compose"
    git push


WHAT'S NEXT:
============
Day 23: API Integration Patterns
- Rate limiting and pagination
- Authentication (API keys, OAuth)
- Error handling strategies
"""


if __name__ == "__main__":
    print("Day 22: Advanced Docker Compose")
    print("=" * 50)
    print("\nKey commands to practice:")
    print("  docker compose up -d")
    print("  docker compose ps")
    print("  docker compose logs")
    print("  docker compose exec <service> <cmd>")
