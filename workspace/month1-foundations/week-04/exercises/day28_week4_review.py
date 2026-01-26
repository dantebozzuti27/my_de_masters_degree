#!/usr/bin/env python3
"""
Day 28: Week 4 Review - Month 1 Consolidation
==============================================
Duration: 2-3 hours

Today is a consolidation day. You'll:
1. Review all Week 4 concepts
2. Review all Month 1 concepts
3. Self-assess your skills
4. Prepare for Month 2

DAILY STRUCTURE:
├── REVIEW (60 min): Concept review and self-assessment
├── PRACTICE (90 min): Hands-on reinforcement
└── PREPARE (30 min): Month 2 preview

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: WEEK 4 REVIEW (30 min)
# =============================================================================
"""
WEEK 4 SELF-ASSESSMENT
======================

Rate yourself 1-5 on each topic:
1 = Never heard of it
2 = Heard of it, don't understand
3 = Understand concept, can't do it
4 = Can do with reference
5 = Can do from memory


DAY 22: ADVANCED DOCKER COMPOSE
-------------------------------

[ ] Multi-service docker-compose.yml
    Rating: ___

[ ] Networks for service isolation
    Rating: ___

[ ] Environment files (.env)
    Rating: ___

[ ] Health checks and depends_on
    Rating: ___


DAY 23: API INTEGRATION
-----------------------

[ ] Rate limiting implementation
    Rating: ___

[ ] Retry with exponential backoff
    Rating: ___

[ ] Pagination handling (offset, cursor)
    Rating: ___

[ ] Authentication (API key, Bearer)
    Rating: ___


DAY 24: AWS LAMBDA
------------------

[ ] Lambda handler function structure
    Rating: ___

[ ] Creating Lambda via CLI
    Rating: ___

[ ] S3 triggers for Lambda
    Rating: ___

[ ] Scheduled Lambda (EventBridge)
    Rating: ___


DAY 25: ADVANCED S3
-------------------

[ ] Medallion architecture (bronze/silver/gold)
    Rating: ___

[ ] Hive-style partitioning
    Rating: ___

[ ] S3 Select for server-side filtering
    Rating: ___

[ ] Lifecycle policies
    Rating: ___


DAY 26: POSTGRESQL
------------------

[ ] Schema and table creation
    Rating: ___

[ ] COPY command for bulk loading
    Rating: ___

[ ] Indexing strategies
    Rating: ___

[ ] UPSERT with ON CONFLICT
    Rating: ___


DAY 27: PROJECT 1
-----------------

[ ] Complete end-to-end pipeline
    Rating: ___

[ ] API → S3 → PostgreSQL flow
    Rating: ___

[ ] Error handling and logging
    Rating: ___

[ ] Docker containerization
    Rating: ___


Any rating below 4? Review that day's exercises!
"""


# =============================================================================
# PART 2: MONTH 1 COMPREHENSIVE REVIEW (30 min)
# =============================================================================
"""
MONTH 1 SKILLS CHECKLIST
========================

WEEK 1: PYTHON FOUNDATIONS
--------------------------
[ ] Variables, data types, operators
[ ] Functions with args, kwargs, returns
[ ] Lists, tuples, sets, dictionaries
[ ] List/dict comprehensions
[ ] File I/O (read, write, JSON)

WEEK 2: PYTHON ADVANCED
-----------------------
[ ] Error handling (try/except/finally)
[ ] Classes and OOP basics
[ ] Logging configuration
[ ] Git fundamentals (add, commit, push)
[ ] GitHub PRs and code review
[ ] CLI applications with argparse

WEEK 3: CLOUD & CONTAINERS
--------------------------
[ ] Advanced Git (rebase, bisect, hooks)
[ ] AWS IAM (users, policies, CLI)
[ ] S3 basics (buckets, objects, boto3)
[ ] Docker fundamentals (images, containers)
[ ] Docker Compose (multi-service)

WEEK 4: INTEGRATION
-------------------
[ ] Advanced Docker Compose
[ ] API integration patterns
[ ] AWS Lambda basics
[ ] Advanced S3 patterns
[ ] PostgreSQL for data engineering
[ ] End-to-end pipeline project


KNOWLEDGE CHECK QUESTIONS:
==========================

Answer these without looking at notes:

1. Python: What's the difference between a list and a tuple?

2. Error handling: When would you use a custom exception?

3. Git: How do you squash the last 3 commits into one?

4. AWS: What's the difference between root account and IAM user?

5. S3: Why do we partition data by year/month/day?

6. Docker: What's the difference between an image and a container?

7. Lambda: What's a cold start?

8. PostgreSQL: Why use COPY instead of INSERT for bulk data?

Write your answers before checking the solutions below.


ANSWERS:
--------

1. List is mutable (can change), tuple is immutable (can't change)

2. When you need to distinguish your errors from Python built-in errors,
   or when you want to carry additional information

3. git rebase -i HEAD~3, then change "pick" to "squash" on last 2 commits

4. Root has unlimited access and can't be restricted. IAM users have
   only the permissions you assign. Never use root for daily work.

5. Query engines (Athena, Spark) only scan needed partitions.
   If you query one day, you scan ~1/365 of the data.

6. Image is a blueprint/template (read-only). Container is a running
   instance of an image (can have multiple containers from one image).

7. First invocation is slower because AWS needs to initialize the
   container. Subsequent calls reuse the warm container.

8. COPY streams data directly to tables, bypassing SQL parsing.
   10-100x faster than individual INSERT statements.
"""


# =============================================================================
# PART 3: HANDS-ON PRACTICE (60 min)
# =============================================================================
"""
EXERCISE 1: QUICK COMMAND DRILL (15 min)
========================================

Without looking, write the commands for:

GIT:
1. Stage all changes: _______________
2. Commit with message: _______________
3. Interactive rebase last 5: _______________
4. Create and switch branch: _______________

AWS CLI:
1. Upload file to S3: _______________
2. List S3 bucket contents: _______________
3. Invoke Lambda function: _______________
4. Check current identity: _______________

DOCKER:
1. Build image with tag: _______________
2. Run container with env var: _______________
3. Start Compose in background: _______________
4. View container logs: _______________

POSTGRESQL:
1. Connect to database: _______________
2. List tables: _______________
3. Describe table structure: _______________


ANSWERS:
--------

GIT:
1. git add -A (or git add .)
2. git commit -m "message"
3. git rebase -i HEAD~5
4. git checkout -b branch-name

AWS CLI:
1. aws s3 cp local-file s3://bucket/key
2. aws s3 ls s3://bucket/
3. aws lambda invoke --function-name name output.json
4. aws sts get-caller-identity

DOCKER:
1. docker build -t name .
2. docker run -e VAR=value image
3. docker compose up -d
4. docker compose logs

POSTGRESQL:
1. psql -U user -d database -h host
2. \dt
3. \d tablename
"""


"""
EXERCISE 2: TROUBLESHOOTING SCENARIOS (20 min)
==============================================

For each scenario, what would you check/do?

SCENARIO 1:
Your Docker container can't connect to PostgreSQL.
Error: "connection refused"

What to check:
- _______________
- _______________
- _______________


SCENARIO 2:
Your Lambda function times out after 3 seconds.

What to do:
- _______________
- _______________


SCENARIO 3:
aws s3 cp returns "Access Denied"

What to check:
- _______________
- _______________
- _______________


SCENARIO 4:
Your PostgreSQL query is slow (30 seconds).

What to do:
- _______________
- _______________
- _______________


ANSWERS:
--------

SCENARIO 1:
- Is PostgreSQL container running? (docker compose ps)
- Are you using correct hostname? (service name, not localhost)
- Is the database healthy? (check healthcheck)
- Is port exposed? (check docker-compose.yml)

SCENARIO 2:
- Increase timeout in Lambda config (max 15 minutes)
- Increase memory (more memory = faster CPU)
- Check if external API is slow (add logging)

SCENARIO 3:
- Check IAM user has correct S3 permissions
- Check bucket policy allows access
- Check aws configure credentials are correct

SCENARIO 4:
- Run EXPLAIN ANALYZE to see query plan
- Add indexes on filtered/joined columns
- Check for missing WHERE clause
- Consider partitioning if table is huge
"""


"""
EXERCISE 3: BUILD SOMETHING (25 min)
====================================

Quick challenge: Build a mini pipeline that:
1. Fetches data from JSONPlaceholder /todos
2. Writes to S3
3. Logs the result

Do this without looking at previous code!

    mkdir -p ~/month1-review
    cd ~/month1-review
    
    # Create your solution here
    # Time yourself - aim for under 25 minutes
"""


# =============================================================================
# PART 4: MONTH 2 PREVIEW (30 min)
# =============================================================================
"""
MONTH 2: DATA TRANSFORMATION & ORCHESTRATION
=============================================

You've built the foundation. Month 2 adds:

WEEK 5-6: AIRFLOW
-----------------
- DAGs (Directed Acyclic Graphs)
- Operators and sensors
- Scheduling and dependencies
- Airflow + AWS integration
- Monitoring and alerts

WEEK 7-8: DBT & SQL
-------------------
- dbt fundamentals
- Models, tests, documentation
- Incremental models
- Advanced SQL (window functions, CTEs)
- Data modeling best practices


PREP CHECKLIST FOR MONTH 2:
===========================

[ ] Docker Desktop running
[ ] AWS CLI configured
[ ] PostgreSQL accessible
[ ] Project 1 complete and working
[ ] All Month 1 skills at 4+ rating


RESOURCES TO EXPLORE:
====================

Before Month 2, optionally explore:

1. VIDEO: "Apache Airflow Tutorial" - TechWorld with Nana
   https://www.youtube.com/watch?v=K9AnJ9_ZAXE

2. VIDEO: "dbt Tutorial for Beginners" - Kahan Data Solutions
   https://www.youtube.com/watch?v=5rNquRnNb4E

3. READING: "Fundamentals of Data Engineering" - Chapter 8
   Focus on: Orchestration section


MONTH 1 ACCOMPLISHMENTS:
========================

Look at what you've learned in 4 weeks:

✅ Python: Variables → Classes → CLI applications
✅ Git: Basic commits → Interactive rebase → Hooks
✅ AWS: Account setup → IAM → S3 → Lambda
✅ Docker: Basics → Multi-container → Full pipelines
✅ PostgreSQL: Setup → Schemas → Bulk loading
✅ Project: Complete API → S3 → DB pipeline

You're already ahead of many junior data engineers!
"""


# =============================================================================
# FINAL TASKS
# =============================================================================
"""
MONTH 1 COMPLETION:
==================

1. SELF-ASSESSMENT
   Rate all skills above. Any below 4 need more practice.

2. PROJECT CHECK
   Is Project 1 working? Can you run it end-to-end?

3. DOCUMENTATION
   Is your GitHub repo updated with all work?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 28: Week 4 Review - Month 1 Complete!"
    git push


CELEBRATE:
==========

You've completed Month 1 of your data engineering journey!

- 28 days of learning
- Python fundamentals to production code
- Cloud services (AWS)
- Container orchestration (Docker)
- Database management (PostgreSQL)
- A working end-to-end pipeline

Next: Month 2 - Airflow, dbt, and advanced orchestration!
"""


if __name__ == "__main__":
    print("Day 28: Week 4 Review")
    print("=" * 50)
    print("\nMonth 1 Complete!")
    print("\nComplete the self-assessment above.")
    print("Review any topics rated below 4.")
    print("\nThen prepare for Month 2: Airflow & dbt!")
