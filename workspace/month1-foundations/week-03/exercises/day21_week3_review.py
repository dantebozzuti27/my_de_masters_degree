#!/usr/bin/env python3
"""
Day 21: Week 3 Review - Consolidation Day
==========================================
Duration: 2-3 hours

Today is a consolidation day. You'll:
1. Review all Week 3 concepts
2. Fill knowledge gaps
3. Practice key skills
4. Prepare for Week 4

DAILY STRUCTURE:
├── REVIEW (60 min): Concept review and self-assessment
├── PRACTICE (90 min): Hands-on reinforcement
└── PREPARE (30 min): Week 4 preview

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# DAY 21 - Building Project 1 (Credit Markets Pipeline)
# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: CONCEPT REVIEW (60 min)
# =============================================================================
"""
WEEK 3 LEARNING OBJECTIVES - Self Assessment
=============================================

Rate yourself on each topic (1-5):
1 = Never heard of it
2 = Heard of it, don't understand
3 = Understand concept, can't do it
4 = Can do with reference
5 = Can do from memory


DAY 15: ADVANCED GIT
--------------------

[ ] Interactive rebase (git rebase -i)
    Rating: ___
    Can you: Squash commits? Reorder commits? Reword messages?

[ ] Git bisect
    Rating: ___
    Can you: Find which commit introduced a bug?

[ ] Cherry-pick
    Rating: ___
    Can you: Apply a specific commit to another branch?

[ ] Pre-commit hooks
    Rating: ___
    Can you: Set up and configure pre-commit hooks?

If rating < 4, review Day 15 exercises.


DAY 16: AWS IAM
---------------

[ ] AWS account structure
    Rating: ___
    Can you: Explain root vs IAM users?

[ ] IAM policies
    Rating: ___
    Can you: Explain what a policy does?

[ ] AWS CLI configuration
    Rating: ___
    Can you: Run aws configure and verify it works?

[ ] aws sts get-caller-identity
    Rating: ___
    Can you: Verify your CLI is authenticated?

If rating < 4, review Day 16 exercises.


DAY 17: S3 FUNDAMENTALS
-----------------------

[ ] S3 buckets and objects
    Rating: ___
    Can you: Create a bucket? Upload/download objects?

[ ] S3 partitioning
    Rating: ___
    Can you: Explain year=YYYY/month=MM/day=DD pattern?

[ ] boto3 S3 operations
    Rating: ___
    Can you: Upload JSON with boto3? List objects?

[ ] Data lake structure (raw/processed/curated)
    Rating: ___
    Can you: Explain why we use this structure?

If rating < 4, review Day 17 exercises.


DAY 18: DOCKER FUNDAMENTALS
---------------------------

[ ] Images vs containers
    Rating: ___
    Can you: Explain the difference?

[ ] Dockerfile instructions
    Rating: ___
    Can you: Write FROM, WORKDIR, COPY, RUN, CMD?

[ ] docker run flags
    Rating: ___
    Can you: Use -it, -e, -v, -p correctly?

[ ] Docker layers and caching
    Rating: ___
    Can you: Explain why we order Dockerfile for caching?

If rating < 4, review Day 18 exercises.


DAY 19: DOCKER FOR DATA ENGINEERING
-----------------------------------

[ ] Docker Compose
    Rating: ___
    Can you: Write docker-compose.yml?

[ ] Running databases in Docker
    Rating: ___
    Can you: Start PostgreSQL in Docker?

[ ] Container networking
    Rating: ___
    Can you: Connect containers by service name?

[ ] Volumes for persistence
    Rating: ___
    Can you: Persist database data?

If rating < 4, review Day 19 exercises.


DAY 20: WEEK 3 PROJECT
----------------------

[ ] Multi-module Python project
    Rating: ___
    Did you: Build the complete pipeline?

[ ] Environment-based configuration
    Rating: ___
    Can you: Load config from environment variables?

[ ] Structured logging
    Rating: ___
    Can you: Set up JSON logging?

[ ] End-to-end pipeline
    Rating: ___
    Can you: Run API → S3 pipeline in Docker?

If you didn't complete Day 20, go back and finish it!
"""


# =============================================================================
# PART 2: PRACTICE EXERCISES (90 min)
# =============================================================================
"""
EXERCISE 1: QUICK COMMAND DRILL (15 min)
========================================

Without looking at notes, type these commands from memory.

AWS CLI:
1. List all S3 buckets: _______________
2. Upload file to S3: _______________
3. List objects in bucket: _______________
4. Download from S3: _______________
5. Check who you are: _______________

Docker:
1. List running containers: _______________
2. Run interactive container: _______________
3. Build image from Dockerfile: _______________
4. Run with environment variable: _______________
5. Run with volume mount: _______________

Docker Compose:
1. Start all services: _______________
2. Start in background: _______________
3. View logs: _______________
4. Stop and remove: _______________
5. Execute command in container: _______________


ANSWERS (check after attempting):

AWS CLI:
1. aws s3 ls
2. aws s3 cp <local> s3://<bucket>/<key>
3. aws s3 ls s3://<bucket>/ [--recursive]
4. aws s3 cp s3://<bucket>/<key> <local>
5. aws sts get-caller-identity

Docker:
1. docker ps
2. docker run -it <image> bash
3. docker build -t <name> .
4. docker run -e VAR=value <image>
5. docker run -v /host:/container <image>

Docker Compose:
1. docker compose up
2. docker compose up -d
3. docker compose logs
4. docker compose down
5. docker compose exec <service> <command>
"""


"""
EXERCISE 2: S3 OPERATIONS PRACTICE (20 min)
===========================================

Let's verify your S3 skills.

STEP 1: Create test data

    echo '{"exercise": "day21", "timestamp": "'$(date -Iseconds)'"}' > /tmp/review_test.json

STEP 2: Upload with partitioning

    aws s3 cp /tmp/review_test.json s3://dante-data-lake-dev/raw/test/review/year=2026/month=01/day=26/

STEP 3: List to verify

    aws s3 ls s3://dante-data-lake-dev/raw/test/review/ --recursive

STEP 4: Download and verify

    aws s3 cp s3://dante-data-lake-dev/raw/test/review/year=2026/month=01/day=26/review_test.json /tmp/downloaded_review.json
    cat /tmp/downloaded_review.json

STEP 5: Clean up

    aws s3 rm s3://dante-data-lake-dev/raw/test/ --recursive
"""


"""
EXERCISE 3: DOCKER SKILLS PRACTICE (25 min)
===========================================

Let's verify your Docker skills.

STEP 1: Pull and run Python container

    docker run -it --rm python:3.11-slim python -c "print('Hello from Docker')"

STEP 2: Run with environment variable

    docker run -it --rm -e GREETING="Data Engineering Rules" python:3.11-slim python -c "import os; print(os.getenv('GREETING'))"

STEP 3: Run with volume mount

    mkdir -p /tmp/docker-test
    echo "print('Hello from mounted file')" > /tmp/docker-test/script.py
    docker run -it --rm -v /tmp/docker-test:/app python:3.11-slim python /app/script.py

STEP 4: Build a quick image

    mkdir -p /tmp/quick-docker
    cat > /tmp/quick-docker/Dockerfile << 'EOF'
FROM python:3.11-slim
RUN pip install requests
CMD ["python", "-c", "import requests; print(requests.get('https://httpbin.org/ip').json())"]
EOF
    
    cd /tmp/quick-docker
    docker build -t quick-test .
    docker run --rm quick-test

STEP 5: Clean up

    docker rmi quick-test
    rm -rf /tmp/quick-docker /tmp/docker-test
"""


"""
EXERCISE 4: DOCKER COMPOSE PRACTICE (30 min)
============================================

Let's build a quick multi-container setup.

STEP 1: Create project

    mkdir -p ~/review-compose
    cd ~/review-compose

STEP 2: Create docker-compose.yml

    cat > ~/review-compose/docker-compose.yml << 'EOF'
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: review
      POSTGRES_PASSWORD: reviewpass
      POSTGRES_DB: review_db
    ports:
      - "5433:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U review -d review_db"]
      interval: 5s
      timeout: 5s
      retries: 5

  app:
    image: python:3.11-slim
    depends_on:
      db:
        condition: service_healthy
    command: >
      python -c "
      import time
      print('App starting...')
      print('Database is healthy!')
      print('App would connect to db:5432')
      time.sleep(10)
      print('App finished')
      "
EOF

STEP 3: Start and observe

    cd ~/review-compose
    docker compose up

Watch how:
- PostgreSQL starts first
- Health check runs
- App waits for healthy database
- App runs after database is ready

STEP 4: Stop and clean up

    docker compose down
    rm -rf ~/review-compose
"""


# =============================================================================
# PART 3: WEEK 4 PREVIEW (30 min)
# =============================================================================
"""
WEEK 4 PREVIEW
==============

Next week we go deeper into real data engineering:


DAY 22: ADVANCED DOCKER COMPOSE
-------------------------------
- Multi-service architectures
- Networks and service discovery
- Environment file management
- Production-ready configurations


DAY 23: API INTEGRATION PATTERNS
--------------------------------
- Rate limiting and throttling
- Pagination handling
- OAuth and API keys
- Error handling strategies


DAY 24: AWS LAMBDA BASICS
-------------------------
- What is serverless?
- Creating your first Lambda function
- Event triggers
- Lambda + S3 integration


DAY 25: ADVANCED S3 PATTERNS
----------------------------
- Lifecycle policies
- Cross-region replication
- S3 event notifications
- S3 Select for querying


DAY 26: POSTGRESQL DEEP DIVE
----------------------------
- Schema design for data engineering
- Indexing strategies
- COPY command for bulk loading
- Connection pooling


DAY 27: PROJECT 1 - DEEP WORK
-----------------------------
- Extended project work
- Building complete pipeline
- Documentation


DAY 28: WEEK 4 REVIEW
---------------------
- Consolidation and review
- Gap filling


PREP CHECKLIST FOR WEEK 4:
=========================

[ ] Docker Desktop running
[ ] AWS CLI configured and working
[ ] PostgreSQL running in Docker (from Day 19)
[ ] Week 3 project complete (Day 20)
[ ] All Week 3 concepts rated 4+ (or reviewed)


WHAT TO READ/WATCH THIS WEEK:
=============================

Optional but recommended:

1. VIDEO: "AWS Lambda Tutorial" - TechWorld with Nana (30 min)
   https://www.youtube.com/watch?v=97q30JjEq9Y
   
2. READING: "Fundamentals of Data Engineering" Chapter 7
   Focus on: Orchestration section

3. VIDEO: "PostgreSQL Tutorial for Beginners" - freeCodeCamp (4 hours)
   https://www.youtube.com/watch?v=qw--VYLpxG4
   Just watch the first hour for basics
"""


# =============================================================================
# WEEK 3 COMPLETION
# =============================================================================
"""
WEEK 3 COMPLETION CHECKLIST:
============================

Technical Milestones:
[ ] Git: Can do interactive rebase, bisect, cherry-pick
[ ] AWS: Have IAM user, CLI configured, S3 bucket created
[ ] S3: Can upload/download, understand partitioning
[ ] Docker: Can write Dockerfile, build image, run container
[ ] Compose: Can write docker-compose.yml, run multi-container apps
[ ] Project: Built containerized API → S3 pipeline

Knowledge Milestones:
[ ] Understand data lake structure (raw/processed/curated)
[ ] Understand container vs image vs Dockerfile
[ ] Understand environment-based configuration
[ ] Understand structured logging

Portfolio Milestones:
[ ] Week 3 project committed to GitHub
[ ] S3 bucket has organized data


FINAL COMMIT:
=============

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 21: Week 3 Review - All Week 3 objectives met"
    git push


CONGRATULATIONS!
================

You've completed Week 3. You now have:
- Real cloud experience (AWS S3)
- Container skills (Docker)
- A production-style data pipeline

Week 4 will build on this foundation with:
- AWS Lambda (serverless)
- PostgreSQL (databases)
- More complex pipelines

See you in Week 4!
"""


if __name__ == "__main__":
    print("Day 21: Week 3 Review")
    print("=" * 50)
    print("\nComplete the self-assessment above.")
    print("Any topic rated below 4? Review that day's exercises.")
    print("\nThen complete the practice exercises to reinforce skills.")
