#!/usr/bin/env python3
"""
Day 27: Project 1 Deep Work Session
=====================================
Duration: 6-7 hours (Saturday project day)

Connect all the pieces: API → Lambda → S3 → PostgreSQL.
Build the complete stock data pipeline.

WHY THIS MATTERS:
- This is your first portfolio project
- End-to-end pipeline building
- Real deployable infrastructure
- Interview-ready demonstration

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PROJECT 1 DEEP WORK: STOCK MARKET PIPELINE
# =============================================================================

"""
TODAY'S GOALS (6-7 hours)
=========================

By end of today, you should have:
1. ✅ Lambda function extracting real stock data
2. ✅ Data landing in S3 with proper partitions
3. ✅ PostgreSQL schema created and populated
4. ✅ Basic transformation loading to database
5. ✅ Error handling and logging throughout
6. ✅ README with architecture diagram


HOUR 1: Review and Setup (60 min)
=================================

□ Review Days 22-26 code
□ Ensure all components are working individually:
  - Docker Compose with PostgreSQL
  - Alpha Vantage API extractor
  - Lambda function
  - S3 bucket with structure
  - Database schema

□ Create project repository:
  github.com/YOUR_USERNAME/stock-market-pipeline


HOUR 2: Lambda to S3 (60 min)
=============================

□ Update Lambda to write to S3:
  - Add S3 permissions to Lambda role
  - Add S3_BUCKET environment variable
  - Write with proper partitioning

□ Test manually:
  aws lambda invoke --function-name stock-data-extractor output.json
  aws s3 ls s3://your-bucket/raw/stocks/ --recursive


HOUR 3: S3 to PostgreSQL (60 min)
=================================

□ Create loader script:
  - Read from S3 partition
  - Transform data
  - Load to PostgreSQL

□ Options:
  A) Python script (simple)
  B) Lambda triggered by S3 (advanced)

□ Test:
  python load_to_postgres.py
  psql -c "SELECT COUNT(*) FROM fact_stock_prices"


HOUR 4: Orchestration (60 min)
==============================

□ Set up CloudWatch Events:
  - Hourly extraction trigger
  - Or: Simple cron + Lambda

□ Add monitoring:
  - CloudWatch Logs
  - Error alerts
  - Basic dashboard

□ Test the schedule:
  - Wait for trigger
  - Verify data flow


HOUR 5: Error Handling (60 min)
===============================

□ Add robust error handling:
  - API failures
  - S3 failures
  - Database failures
  - Retries with backoff

□ Add comprehensive logging:
  - Log each step
  - Include timestamps
  - Log data counts

□ Add data validation:
  - Check required fields
  - Validate data types
  - Skip bad records


HOUR 6: Documentation (60 min)
==============================

□ Create README.md:
  - Project overview
  - Architecture diagram
  - Setup instructions
  - Environment variables
  - How to run

□ Architecture diagram (use mermaid or draw.io):
  [Alpha Vantage API]
         ↓
  [AWS Lambda] → [CloudWatch Logs]
         ↓
  [S3 Bucket]
         ↓
  [Python Loader]
         ↓
  [PostgreSQL]

□ Clean up code:
  - Remove debug prints
  - Add docstrings
  - Consistent formatting


HOUR 7: Polish and Test (60 min)
================================

□ End-to-end test:
  1. Trigger Lambda manually
  2. Verify S3 data
  3. Run loader
  4. Query database
  5. Check logs

□ Edge case testing:
  - Empty response
  - API error
  - Network timeout
  - Duplicate data

□ Commit and push:
  git add .
  git commit -m "Complete Project 1: Stock Market Pipeline"
  git push origin main
"""

# =============================================================================
# PROJECT STRUCTURE
# =============================================================================

PROJECT_STRUCTURE = """
stock-market-pipeline/
├── README.md
├── .gitignore
├── .env.example
├── docker-compose.yml
├── requirements.txt
│
├── lambda/
│   ├── handler.py
│   └── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extractor.py
│   ├── loader.py
│   └── transform.py
│
├── sql/
│   ├── schema.sql
│   └── queries/
│       ├── daily_summary.sql
│       └── symbol_performance.sql
│
├── scripts/
│   ├── deploy_lambda.sh
│   ├── run_pipeline.py
│   └── backfill.py
│
└── tests/
    ├── test_extractor.py
    └── test_loader.py
"""

# =============================================================================
# CHECKLIST
# =============================================================================

def print_checklist():
    """Print the project checklist."""
    checklist = """
╔══════════════════════════════════════════════════════════════╗
║                PROJECT 1 COMPLETION CHECKLIST                 ║
╠══════════════════════════════════════════════════════════════╣
║                                                               ║
║ INFRASTRUCTURE                                                ║
║ [ ] AWS account with billing alerts                           ║
║ [ ] S3 bucket with data lake structure                        ║
║ [ ] Lambda function deployed                                  ║
║ [ ] PostgreSQL database running                               ║
║ [ ] CloudWatch Events scheduled                               ║
║                                                               ║
║ CODE                                                          ║
║ [ ] API extractor with error handling                         ║
║ [ ] Lambda handler writing to S3                              ║
║ [ ] S3 to PostgreSQL loader                                   ║
║ [ ] Logging throughout                                        ║
║ [ ] Data validation                                           ║
║                                                               ║
║ DATA                                                          ║
║ [ ] Partitioned data in S3                                    ║
║ [ ] Dimensional schema in PostgreSQL                          ║
║ [ ] Sample data loaded                                        ║
║ [ ] Queries working                                           ║
║                                                               ║
║ DOCUMENTATION                                                 ║
║ [ ] README with setup instructions                            ║
║ [ ] Architecture diagram                                      ║
║ [ ] Environment variables documented                          ║
║ [ ] Clean, commented code                                     ║
║                                                               ║
║ DEPLOYMENT                                                    ║
║ [ ] GitHub repository created                                 ║
║ [ ] All code committed                                        ║
║ [ ] .gitignore includes secrets                               ║
║ [ ] End-to-end test passing                                   ║
║                                                               ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(checklist)


def print_architecture():
    """Print architecture diagram."""
    diagram = """
STOCK MARKET PIPELINE ARCHITECTURE
==================================

┌─────────────────────────────────────────────────────────────────┐
│                         DATA SOURCE                              │
│                   [Alpha Vantage API]                           │
│                    (Stock quotes)                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       EXTRACTION LAYER                           │
│  ┌────────────────┐    ┌────────────────┐                       │
│  │  CloudWatch    │───▶│  AWS Lambda    │                       │
│  │  Events (cron) │    │  (extractor)   │                       │
│  └────────────────┘    └────────────────┘                       │
│                              │                                   │
│                              ▼                                   │
│                    ┌────────────────┐                           │
│                    │  CloudWatch    │                           │
│                    │  Logs          │                           │
│                    └────────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        STORAGE LAYER                             │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                     S3 Data Lake                            │ │
│  │                                                             │ │
│  │  raw/stocks/year=2024/month=01/day=15/quotes.json          │ │
│  │  processed/stocks/daily_summary.parquet                    │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      TRANSFORMATION LAYER                        │
│  ┌────────────────┐                                              │
│  │ Python Loader  │  (reads S3, transforms, loads to DB)        │
│  └────────────────┘                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SERVING LAYER                              │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │                    PostgreSQL                               │ │
│  │                                                             │ │
│  │  dim_symbol, dim_date, fact_stock_prices                   │ │
│  └────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
"""
    print(diagram)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "checklist":
            print_checklist()
        elif cmd == "architecture":
            print_architecture()
        elif cmd == "structure":
            print(PROJECT_STRUCTURE)
    else:
        print("Day 27: Project 1 Deep Work Session")
        print("=" * 40)
        print("\n6-7 HOURS of focused project work.")
        print("\nCommands:")
        print("  python day27_project1_deepwork.py checklist    - Completion checklist")
        print("  python day27_project1_deepwork.py architecture - Architecture diagram")
        print("  python day27_project1_deepwork.py structure    - Project structure")
