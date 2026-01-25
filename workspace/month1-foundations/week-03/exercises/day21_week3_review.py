#!/usr/bin/env python3
"""
Day 21: Week 3 Review + Plan Week 4
====================================
Duration: 3-4 hours (Sunday review day)

Review everything from Week 3, identify gaps, plan Week 4.
Consolidate your knowledge before moving to Project 1.

WHY THIS MATTERS:
- Review solidifies learning
- Gap identification prevents future problems
- Planning ensures focused execution
- This is how senior engineers maintain momentum

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

from typing import Dict, List
from datetime import datetime

# =============================================================================
# WEEK 3 REVIEW
# =============================================================================

WEEK_3_TOPICS = {
    "Day 15: Advanced Git": {
        "skills": [
            "Interactive rebase (squash, fixup, reword)",
            "Git bisect for bug hunting",
            "Cherry-pick and revert",
            "Pre-commit hooks",
            "Code review best practices"
        ],
        "commands": [
            "git rebase -i HEAD~N",
            "git bisect start/good/bad",
            "git cherry-pick <hash>",
            "git revert <hash>",
            "pre-commit install"
        ]
    },
    "Day 16: AWS IAM": {
        "skills": [
            "AWS account security (MFA, no root)",
            "IAM users vs roles",
            "IAM policies (JSON structure)",
            "Programmatic access (CLI)",
            "Billing alerts"
        ],
        "commands": [
            "aws configure",
            "aws sts get-caller-identity",
            "aws iam list-users",
            "aws iam get-policy"
        ]
    },
    "Day 17: S3 Fundamentals": {
        "skills": [
            "Bucket creation and naming",
            "Data lake structure (raw/processed/curated)",
            "Partitioning patterns",
            "Storage classes and lifecycle",
            "Bucket policies"
        ],
        "commands": [
            "aws s3 cp/sync",
            "aws s3 ls",
            "aws s3api put-object",
            "aws s3api create-bucket"
        ]
    },
    "Day 18: Docker Fundamentals": {
        "skills": [
            "Images vs containers",
            "Dockerfile writing",
            "Docker commands (build, run, exec)",
            "Port mapping and volumes",
            "Multi-stage builds"
        ],
        "commands": [
            "docker build -t name .",
            "docker run -d -p 8080:80 name",
            "docker exec -it container bash",
            "docker logs container",
            "docker ps / docker images"
        ]
    },
    "Day 19: Docker for Data Engineering": {
        "skills": [
            "Docker Compose basics",
            "Multi-container applications",
            "Environment variables",
            "Volume persistence",
            "Networking between containers"
        ],
        "commands": [
            "docker-compose up -d",
            "docker-compose down",
            "docker-compose logs -f",
            "docker-compose exec service bash"
        ]
    },
    "Day 20: Week 3 Project": {
        "skills": [
            "End-to-end containerized pipeline",
            "ETL pattern implementation",
            "Configuration management",
            "Error handling and logging",
            "Local and S3 storage"
        ],
        "deliverables": [
            "Working Dockerfile",
            "docker-compose.yml",
            "ETL pipeline code",
            "README documentation"
        ]
    }
}


def print_week_review() -> None:
    """Print Week 3 review checklist."""
    print("=" * 70)
    print("WEEK 3 REVIEW: Advanced Git + AWS + Docker")
    print("=" * 70)
    
    for day, content in WEEK_3_TOPICS.items():
        print(f"\n{day}")
        print("-" * 50)
        
        if "skills" in content:
            print("Skills:")
            for skill in content["skills"]:
                print(f"  [ ] {skill}")
        
        if "commands" in content:
            print("\nKey Commands:")
            for cmd in content["commands"]:
                print(f"      {cmd}")
        
        if "deliverables" in content:
            print("\nDeliverables:")
            for d in content["deliverables"]:
                print(f"  [ ] {d}")


# =============================================================================
# SELF-ASSESSMENT QUIZ
# =============================================================================

QUIZ_QUESTIONS = [
    {
        "topic": "Git",
        "question": "When should you NOT use git rebase -i?",
        "answer": "On commits that have been pushed to a shared branch"
    },
    {
        "topic": "AWS",
        "question": "What's the first thing you should do after creating an AWS account?",
        "answer": "Enable MFA on the root account"
    },
    {
        "topic": "IAM",
        "question": "What's the difference between IAM users and roles?",
        "answer": "Users = humans with credentials; Roles = temporary credentials for services"
    },
    {
        "topic": "S3",
        "question": "Why do we partition data in S3?",
        "answer": "To query only what we need - reduces cost and improves speed"
    },
    {
        "topic": "Docker",
        "question": "What's the difference between an image and a container?",
        "answer": "Image = template (class); Container = running instance (object)"
    },
    {
        "topic": "Docker",
        "question": "How do you persist data when a container is removed?",
        "answer": "Use volumes (-v or volumes: in docker-compose)"
    },
    {
        "topic": "Security",
        "question": "Where should you NEVER store AWS credentials?",
        "answer": "In a git repository (use environment variables or secrets manager)"
    }
]


def run_self_assessment() -> None:
    """Run self-assessment quiz."""
    print("=" * 60)
    print("WEEK 3 SELF-ASSESSMENT")
    print("=" * 60)
    print("\nFor each question, think of your answer before revealing.\n")
    
    score = 0
    for i, q in enumerate(QUIZ_QUESTIONS, 1):
        print(f"Q{i} [{q['topic']}]: {q['question']}")
        input("  (Press Enter to reveal answer...)")
        print(f"  ANSWER: {q['answer']}")
        
        response = input("  Did you get it right? (y/n): ").lower()
        if response == 'y':
            score += 1
            print("  ✅ Great!\n")
        else:
            print("  📚 Review this topic.\n")
    
    print("=" * 60)
    print(f"Score: {score}/{len(QUIZ_QUESTIONS)}")
    
    if score == len(QUIZ_QUESTIONS):
        print("🎉 Perfect! You've mastered Week 3!")
    elif score >= 5:
        print("👍 Good job! Minor review needed.")
    else:
        print("📚 Spend more time reviewing before Week 4.")


# =============================================================================
# WEEK 4 PLANNING
# =============================================================================

WEEK_4_PREVIEW = """
WEEK 4: PROJECT 1 - STOCK MARKET PIPELINE (Days 22-28)
======================================================

This week you start building your first portfolio project!

Day 22: Docker Compose + Local Dev Stack
  - Set up local development environment
  - PostgreSQL in Docker
  - Local Airflow (optional)

Day 23: Alpha Vantage API Integration
  - Sign up for free API key
  - Build stock data extractor
  - Handle rate limits and errors

Day 24: AWS Lambda Deployment
  - Deploy extraction as Lambda
  - CloudWatch scheduling
  - Error alerts

Day 25: S3 Storage + Partitioning
  - Raw data to S3
  - Proper partitioning
  - Data lake structure

Day 26: PostgreSQL Schema Design
  - Dimensional modeling
  - Fact and dimension tables
  - Loading patterns

Day 27: Project 1 Deep Work (Saturday)
  - Connect all components
  - End-to-end testing
  - Debug and fix issues

Day 28: Review + Debug (Sunday)
  - Polish and document
  - Prepare for Week 5

PREPARATION FOR WEEK 4:
-----------------------
[ ] Alpha Vantage API key (https://www.alphavantage.co/support/#api-key)
[ ] AWS account fully set up
[ ] Docker Desktop running
[ ] Week 3 project working
[ ] Create github.com/yourusername/stock-market-pipeline repo
"""


def print_week_4_plan() -> None:
    """Print Week 4 preview and preparation checklist."""
    print(WEEK_4_PREVIEW)


# =============================================================================
# GAP ANALYSIS
# =============================================================================

def identify_gaps() -> None:
    """Interactive gap identification."""
    print("=" * 60)
    print("GAP ANALYSIS - Be honest with yourself")
    print("=" * 60)
    
    areas = [
        ("Git rebase and history rewriting", "Day 15"),
        ("AWS console navigation", "Day 16"),
        ("IAM policies (reading and writing)", "Day 16"),
        ("S3 data organization", "Day 17"),
        ("Dockerfile writing", "Day 18"),
        ("Docker Compose", "Day 19"),
        ("End-to-end pipeline building", "Day 20")
    ]
    
    gaps = []
    
    for area, day in areas:
        print(f"\n{area} ({day})")
        rating = input("  Rate your confidence (1=weak, 5=strong): ")
        try:
            if int(rating) < 3:
                gaps.append((area, day))
        except:
            pass
    
    print("\n" + "=" * 60)
    if gaps:
        print("AREAS TO REVIEW:")
        for area, day in gaps:
            print(f"  ⚠️  {area} - Review {day}")
        print("\nSpend 30-60 min reviewing these before Week 4.")
    else:
        print("✅ No major gaps identified. You're ready for Week 4!")


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "review":
            print_week_review()
        elif cmd == "quiz":
            run_self_assessment()
        elif cmd == "gaps":
            identify_gaps()
        elif cmd == "week4":
            print_week_4_plan()
    else:
        print("Day 21: Week 3 Review + Plan Week 4")
        print("=" * 40)
        print("\nThis is a REVIEW day (3-4 hours).")
        print("Consolidate learning and prepare for Project 1.")
        print("\nCommands:")
        print("  python day21_week3_review.py review - Review Week 3 topics")
        print("  python day21_week3_review.py quiz   - Self-assessment quiz")
        print("  python day21_week3_review.py gaps   - Identify knowledge gaps")
        print("  python day21_week3_review.py week4  - Preview Week 4")
        print("\nRecommended order:")
        print("  1. review → 2. quiz → 3. gaps → 4. week4")
