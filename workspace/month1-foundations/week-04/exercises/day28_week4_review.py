#!/usr/bin/env python3
"""
Day 28: Week 4 Review + Debug Session
======================================
Duration: 3-4 hours (Sunday review day)

Review Week 4, debug any issues, polish Project 1.
Prepare for Week 5.

WHY THIS MATTERS:
- Debugging is a core skill
- Polish separates good from great
- Review consolidates learning
- Planning ensures momentum

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# WEEK 4 REVIEW
# =============================================================================

WEEK_4_TOPICS = {
    "Day 22: Docker Compose": [
        "Multi-container applications",
        "Environment variables in compose",
        "Health checks",
        "Volume persistence",
        "Service networking"
    ],
    "Day 23: API Integration": [
        "Alpha Vantage API",
        "Rate limiting",
        "Error handling",
        "Data validation",
        "Batch extraction"
    ],
    "Day 24: Lambda Deployment": [
        "Lambda handler structure",
        "Deployment packages",
        "IAM roles for Lambda",
        "CloudWatch scheduling",
        "S3 output"
    ],
    "Day 25: S3 Partitioning": [
        "Hive-style partitions",
        "Partition design",
        "Athena queries",
        "Storage classes",
        "Cost optimization"
    ],
    "Day 26: PostgreSQL Schema": [
        "Dimensional modeling",
        "Fact vs dimension tables",
        "Indexes",
        "Upsert patterns",
        "Date dimensions"
    ],
    "Day 27: Project 1": [
        "End-to-end pipeline",
        "Infrastructure setup",
        "Error handling",
        "Logging",
        "Documentation"
    ]
}


def print_week_review():
    """Print Week 4 review."""
    print("=" * 60)
    print("WEEK 4 REVIEW: PROJECT 1 - STOCK MARKET PIPELINE")
    print("=" * 60)
    
    for day, topics in WEEK_4_TOPICS.items():
        print(f"\n{day}")
        print("-" * 40)
        for topic in topics:
            print(f"  [ ] {topic}")


# =============================================================================
# DEBUGGING GUIDE
# =============================================================================

DEBUG_GUIDE = """
DEBUGGING CHECKLIST
===================

1. LAMBDA ISSUES
   □ Check CloudWatch Logs
   □ Verify IAM permissions
   □ Check environment variables
   □ Test with small input first
   □ Check timeout settings

2. S3 ISSUES  
   □ Verify bucket permissions
   □ Check object key format
   □ Verify region settings
   □ Check CORS if accessing from browser

3. POSTGRESQL ISSUES
   □ Verify connection string
   □ Check if tables exist
   □ Verify user permissions
   □ Check for constraint violations
   □ Look at transaction state

4. API ISSUES
   □ Verify API key is valid
   □ Check rate limits
   □ Look at response status codes
   □ Print full response for debugging
   □ Check network/firewall

5. DOCKER ISSUES
   □ Check container logs: docker logs <container>
   □ Verify ports are mapped correctly
   □ Check if services are healthy
   □ Verify volumes are mounted
   □ Check for name conflicts

DEBUGGING COMMANDS
==================

# Lambda
aws lambda invoke --function-name NAME output.json
aws logs tail /aws/lambda/NAME --follow

# S3
aws s3 ls s3://bucket/prefix/ --recursive
aws s3 cp s3://bucket/key - | head

# PostgreSQL
docker exec -it postgres psql -U pipeline -d stockdata
\\dt  -- list tables
\\d tablename  -- describe table
SELECT * FROM table LIMIT 5;

# Docker
docker ps -a
docker logs container_name
docker exec -it container_name bash
docker-compose logs -f service_name
"""


# =============================================================================
# WEEK 5 PREVIEW
# =============================================================================

WEEK_5_PREVIEW = """
WEEK 5: PROJECT 1 COMPLETION + AIRFLOW INTRO (Days 29-35)
=========================================================

This week you finish Project 1 and get it interview-ready!

Day 29: Data Transformation Pipeline
  - Clean transformation logic
  - Data quality checks
  - Output to processed layer

Day 30: Airflow DAG Basics
  - Airflow architecture
  - Your first DAG
  - Operators overview

Day 31: Connect Airflow to Lambda + S3
  - AWS operators
  - Triggering Lambda from Airflow
  - S3 sensors

Day 32: Streamlit Dashboard Basics
  - Streamlit fundamentals
  - Connect to PostgreSQL
  - Basic visualizations

Day 33: Dashboard Data Integration
  - Charts and graphs
  - Real-time updates
  - Filtering and interactivity

Day 34: Project 1 Polish + Documentation (Saturday)
  - Final testing
  - Complete documentation
  - GitHub README polish
  - Deploy dashboard

Day 35: Month 1 Review + Planning
  - Review all Month 1 learning
  - Identify gaps
  - Plan Month 2 (dbt!)


PREPARATION FOR WEEK 5:
-----------------------
[ ] Project 1 components working
[ ] GitHub repo with code committed
[ ] Docker Compose running locally
[ ] Data flowing through pipeline
[ ] Basic understanding of orchestration concepts
"""


def print_debug_guide():
    """Print debugging guide."""
    print(DEBUG_GUIDE)


def print_week5_preview():
    """Print Week 5 preview."""
    print(WEEK_5_PREVIEW)


# =============================================================================
# PROJECT 1 STATUS CHECK
# =============================================================================

def check_project_status():
    """Interactive project status check."""
    print("=" * 60)
    print("PROJECT 1 STATUS CHECK")
    print("=" * 60)
    
    components = [
        ("Lambda function deployed", "Can you invoke it?"),
        ("S3 data landing correctly", "Check aws s3 ls"),
        ("PostgreSQL schema created", "Can you connect?"),
        ("Data loaded to database", "SELECT COUNT(*) works?"),
        ("Error handling in place", "What happens on failure?"),
        ("Logging working", "Can you see logs?"),
        ("README documentation", "Could someone else run it?"),
        ("GitHub repo created", "Is code committed?")
    ]
    
    status = []
    for component, check in components:
        print(f"\n{component}")
        print(f"  Check: {check}")
        response = input("  Status (y/n/partial): ").lower()
        status.append((component, response))
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    done = sum(1 for _, s in status if s == 'y')
    partial = sum(1 for _, s in status if s == 'partial')
    
    print(f"Complete: {done}/{len(components)}")
    print(f"Partial: {partial}/{len(components)}")
    
    if done == len(components):
        print("\n🎉 Project 1 is complete! Ready for Week 5!")
    else:
        print("\nNeeds work:")
        for component, s in status:
            if s != 'y':
                print(f"  ⚠️  {component}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "review":
            print_week_review()
        elif cmd == "debug":
            print_debug_guide()
        elif cmd == "week5":
            print_week5_preview()
        elif cmd == "status":
            check_project_status()
    else:
        print("Day 28: Week 4 Review + Debug Session")
        print("=" * 42)
        print("\nPolish Project 1 and prepare for Week 5.")
        print("\nCommands:")
        print("  python day28_week4_review.py review - Review Week 4 topics")
        print("  python day28_week4_review.py debug  - Debugging guide")
        print("  python day28_week4_review.py status - Check project status")
        print("  python day28_week4_review.py week5  - Preview Week 5")
