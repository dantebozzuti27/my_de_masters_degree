# Workspace Directory

This directory contains all exercises and projects for the 6-month Data Engineer curriculum.

## Structure

```
workspace/
├── month1-foundations/     # Weeks 1-5: Days 1-35
│   ├── week-01/           # Days 1-7: Python Fundamentals
│   │   └── exercises/
│   ├── week-02/           # Days 8-14: Production Python + Git
│   │   ├── exercises/
│   │   └── projects/
│   ├── week-03/           # Days 15-21: AWS + Docker Basics
│   ├── week-04/           # Days 22-28: Project 1 Part 1
│   └── week-05/           # Days 29-35: Project 1 Part 2
├── month2-dbt/            # Weeks 6-9: Days 36-63
├── month3-airflow/        # Weeks 10-13: Days 64-91
├── month4-aws-cert/       # Weeks 14-17: Days 92-119
├── month5-interviews/     # Weeks 18-21: Days 120-147
└── month6-close/          # Weeks 22-24: Days 148-168
```

## Week-to-Day Mapping

| Week | Days | Location |
|------|------|----------|
| 1 | 1-7 | month1-foundations/week-01 |
| 2 | 8-14 | month1-foundations/week-02 |
| 3 | 15-21 | month1-foundations/week-03 |
| 4 | 22-28 | month1-foundations/week-04 |
| 5 | 29-35 | month1-foundations/week-05 |
| 6 | 36-42 | month2-dbt/week-06 |
| 7 | 43-49 | month2-dbt/week-07 |
| 8 | 50-56 | month2-dbt/week-08 |
| 9 | 57-63 | month2-dbt/week-09 |
| 10 | 64-70 | month3-airflow/week-10 |
| 11 | 71-77 | month3-airflow/week-11 |
| 12 | 78-84 | month3-airflow/week-12 |
| 13 | 85-91 | month3-airflow/week-13 |
| 14 | 92-98 | month4-aws-cert/week-14 |
| 15 | 99-105 | month4-aws-cert/week-15 |
| 16 | 106-112 | month4-aws-cert/week-16 |
| 17 | 113-119 | month4-aws-cert/week-17 |
| 18 | 120-126 | month5-interviews/week-18 |
| 19 | 127-133 | month5-interviews/week-19 |
| 20 | 134-140 | month5-interviews/week-20 |
| 21 | 141-147 | month5-interviews/week-21 |
| 22 | 148-154 | month6-close/week-22 |
| 23 | 155-161 | month6-close/week-23 |
| 24 | 162-168 | month6-close/week-24 |

## Current Progress

**Week 1 (Days 1-7):** ✅ Complete  
**Week 2 (Days 8-14):** 🔄 In Progress (Day 13 - CLI Tool Project)

## File Naming Convention

- Exercises: `dayX_topic_name.py`
- Projects: `dayX_project/` directory with multiple files

## How Progress is Tracked

The scanner (`scripts/scan-workspace.js`) looks for:
1. Files named `dayX_*.py` in `exercises/` or `projects/` directories
2. Completion markers indicating all tests pass
3. Reports progress to the web dashboard
