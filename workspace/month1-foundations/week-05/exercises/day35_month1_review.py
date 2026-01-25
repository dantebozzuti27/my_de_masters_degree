#!/usr/bin/env python3
"""
Day 35: Month 1 Review + Planning
==================================
Duration: 3-4 hours (Sunday review day)

Review everything from Month 1. Celebrate your progress.
Prepare for Month 2: dbt Mastery.

WHY THIS MATTERS:
- 35 days complete = significant progress
- Review solidifies learning
- Planning maintains momentum
- You're ready for dbt

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

MONTH_1_SUMMARY = """
╔══════════════════════════════════════════════════════════════╗
║                    MONTH 1 SUMMARY                            ║
║              Foundations + Production Skills                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                               ║
║ WEEK 1: Python Fundamentals (Days 1-7)                        ║
║   ✅ Development environment                                  ║
║   ✅ Variables, functions, control flow                       ║
║   ✅ Data structures                                          ║
║   ✅ File I/O                                                 ║
║                                                               ║
║ WEEK 2: Production Python + Git (Days 8-14)                   ║
║   ✅ Error handling                                           ║
║   ✅ OOP                                                      ║
║   ✅ Logging & configuration                                  ║
║   ✅ Git & GitHub                                             ║
║   ✅ CLI Data Tool project                                    ║
║                                                               ║
║ WEEK 3: AWS + Docker (Days 15-21)                             ║
║   ✅ Advanced Git                                             ║
║   ✅ AWS IAM                                                  ║
║   ✅ S3 fundamentals                                          ║
║   ✅ Docker basics                                            ║
║   ✅ Docker for data engineering                              ║
║                                                               ║
║ WEEK 4: Project 1 Part 1 (Days 22-28)                         ║
║   ✅ Docker Compose                                           ║
║   ✅ API integration                                          ║
║   ✅ Lambda deployment                                        ║
║   ✅ S3 partitioning                                          ║
║   ✅ PostgreSQL schema                                        ║
║                                                               ║
║ WEEK 5: Project 1 Part 2 (Days 29-35)                         ║
║   ✅ Data transformation                                      ║
║   ✅ Airflow basics                                           ║
║   ✅ Streamlit dashboard                                      ║
║   ✅ Project polish                                           ║
║                                                               ║
║ DELIVERABLES                                                  ║
║   📦 CLI Data Tool (Week 2)                                   ║
║   📦 Stock Market Pipeline (Project 1)                        ║
║                                                               ║
╚══════════════════════════════════════════════════════════════╝
"""

MONTH_2_PREVIEW = """
╔══════════════════════════════════════════════════════════════╗
║                    MONTH 2 PREVIEW                            ║
║                   dbt Mastery + Project 2                     ║
╠══════════════════════════════════════════════════════════════╣
║                                                               ║
║ WEEK 6: dbt Fundamentals (Days 36-42)                         ║
║   - Models, refs, materializations                            ║
║   - Staging → Intermediate → Marts                            ║
║   - Sources and seeds                                         ║
║                                                               ║
║ WEEK 7: dbt Testing & Macros (Days 43-49)                     ║
║   - Schema and data tests                                     ║
║   - Custom tests                                              ║
║   - Jinja macros                                              ║
║   - Packages and documentation                                ║
║                                                               ║
║ WEEK 8: Project 2 Part 1 (Days 50-56)                         ║
║   - NBA API data ingestion                                    ║
║   - Snowflake setup                                           ║
║   - dbt models for NBA data                                   ║
║                                                               ║
║ WEEK 9: Project 2 Part 2 + dbt Cert (Days 57-63)              ║
║   - Complete NBA Analytics Platform                           ║
║   - Streamlit dashboard                                       ║
║   - dbt Analytics Engineering Certification                   ║
║                                                               ║
║ GOAL: dbt certification by Day 62                             ║
║                                                               ║
╚══════════════════════════════════════════════════════════════╝
"""

SKILLS_ASSESSMENT = """
SKILLS SELF-ASSESSMENT
======================

Rate yourself 1-5 (1=need work, 5=confident):

PYTHON
[ ] Variables, types, functions
[ ] Data structures (lists, dicts)
[ ] OOP (classes, methods)
[ ] Error handling
[ ] File I/O

GIT/GITHUB
[ ] Basic commands (add, commit, push)
[ ] Branching and merging
[ ] Pull requests
[ ] Code review

AWS
[ ] IAM basics
[ ] S3 operations
[ ] Lambda functions
[ ] CloudWatch

DOCKER
[ ] Dockerfile creation
[ ] Running containers
[ ] Docker Compose
[ ] Volumes and networks

DATA ENGINEERING
[ ] ETL concepts
[ ] Data partitioning
[ ] Dimensional modeling
[ ] Pipeline orchestration
"""

def print_summary():
    print(MONTH_1_SUMMARY)

def print_month2():
    print(MONTH_2_PREVIEW)

def print_assessment():
    print(SKILLS_ASSESSMENT)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "summary":
            print_summary()
        elif cmd == "month2":
            print_month2()
        elif cmd == "skills":
            print_assessment()
    else:
        print("Day 35: Month 1 Review + Planning")
        print("=" * 38)
        print("\n🎉 MONTH 1 COMPLETE!")
        print("\nCommands:")
        print("  python day35_month1_review.py summary - Month 1 summary")
        print("  python day35_month1_review.py month2  - Preview Month 2")
        print("  python day35_month1_review.py skills  - Skills assessment")
