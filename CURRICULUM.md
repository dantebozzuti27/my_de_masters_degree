# 6-MONTH DATA ENGINEER CURRICULUM
## Goal: Land Data Engineer Role by July 2026

**Schedule:** 30 hours/week
**Duration:** 24 weeks (172 days; includes Palantir Foundry block)
**Start Date:** February 2026
**Target End Date:** July 2026

---

## Current Progress

**43/172 days complete**

**Next:** Day 44 - Materializations (Table, View, Incremental, Ephemeral)

---

## MONTH 1: FOUNDATIONS + PROJECT 1

**Project:** Credit Markets Pipeline
**Stack:** Python, AWS Lambda, S3, PostgreSQL, Airflow, Streamlit, GitHub Actions

### Week 1: Python Fundamentals

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Development Environment Setup | Done |
| 2 | Python Variables & Syntax | Done |
| 3 | Functions & Control Flow | Done |
| 4 | Data Structures (Lists, Dicts) | Done |
| 5 | List Comprehensions | Done |
| 6 | Dictionaries & JSON | Done |
| 7 | File I/O & Context Managers | Done |

### Week 2: Production Python + Git

| Day | Topic | Status |
|-----|-------|--------|
| 8 | Error Handling & Defensive Code | Done |
| 9 | Python Classes & OOP | Done |
| 10 | Logging & Configuration | Done |
| 11 | Git Fundamentals | Done |
| 12 | GitHub PRs & Workflows | Done |
| 13 | Week 2 Project: CLI Data Tool | Done |
| 14 | Week 2 Review | Done |

### Week 3: AWS + Docker + Project 1 Start

| Day | Topic | Status |
|-----|-------|--------|
| 15 | Advanced Git + Code Review | Done |
| 16 | AWS Account Setup (IAM, CLI) | Done |
| 17 | S3 Fundamentals | Done |
| 18 | Docker Fundamentals | Done |
| 19 | Project 1: Credit Markets Pipeline - Core | Done |
| 20 | Project 1: Credit Markets Pipeline - Reference Data | Done |
| 21 | Project 1: Credit Markets Pipeline - Parallel Processing | Done |

### Week 4: Project 1 Deployment + CI/CD

| Day | Topic | Status |
|-----|-------|--------|
| 22 | AWS Lambda Deployment | Done |
| 23 | GitHub Actions CI/CD (pytest + Docker) | Done |
| 24 | Airflow DAG Setup (Local) | Done |
| 25 | Airflow Integration (Lambda + S3 Sensors) | Done |
| 26 | Monitoring + Alerting (CloudWatch, Slack) | Done |
| 27 | Data Quality with Great Expectations | Done |
| 28 | Project 1 Documentation + Architecture Diagrams | Done |

### Week 5: SQL Deep Dive

**Depth bar:** Each day = go deep: 3+ practice problems, edge cases, "when to use / when not," interview angle.

| Day | Topic | Status |
|-----|-------|--------|
| 29 | Window Functions (ROW_NUMBER, RANK, LEAD/LAG, NTILE) | Done |
| 30 | Advanced Aggregations (GROUPING SETS, CUBE, ROLLUP) | Done |
| 31 | CTEs + Recursive CTEs | Done |
| 32 | Query Optimization (EXPLAIN ANALYZE, Indexes) | Done |
| 33 | SQL Drilling (10 problems in-repo) | Done |
| 34 | SQL Drilling (10 problems in-repo, day34_sql_drill.sql) | Done |
| 35 | SQL Assessment + Review | Done |

### Week 6: Distributed Systems Theory

| Day | Topic | Status |
|-----|-------|--------|
| 36 | CAP Theorem Deep Dive | Done |
| 37 | Consistency Models (Eventual, Strong, Causal) | Done |
| 38 | Partitioning Strategies (Hash, Range, Composite) | Done |
| 39 | Replication Patterns (Leader-Follower, Multi-Leader) | Done |
| 40 | Exactly-Once Semantics (Why It's Mostly a Myth) | Done |
| 41 | Data Modeling at Scale (Star Schema, SCDs) | Done |
| 42 | Phase 1 Review + Project 1 Final Polish | Done |

---

## MONTH 2: DBT + SPARK + PROJECT 2

**Project:** Fraud Detection Pipeline
**Stack:** Python, Spark, dbt, Snowflake/Databricks, Kafka, Streamlit

**Certification:** dbt Analytics Engineering (Day 74)

### Week 7: dbt Fundamentals

*Palantir angle: dbt staging → marts and docs map conceptually to Foundry datasets, transforms, lineage, and ontology-like semantic layer.*

| Day | Topic | Status |
|-----|-------|--------|
| 43 | dbt Project Setup, Models, Refs | Done |
| 44 | Materializations (Table, View, Incremental, Ephemeral) |  |
| 45 | Staging → Intermediate → Marts Pattern |  |
| 46 | Sources, Seeds, Snapshots |  |
| 47 | dbt Testing (Schema + Data Tests) |  |
| 48 | Macros and Jinja Templating |  |
| 49 | dbt Packages + Documentation Generation |  |

### Week 7b: Palantir Foundry & Ontology (Palantir-tailored)

| Day | Topic | Status |
|-----|-------|--------|
| 50 | Foundry Overview: Data Integration, Pipeline Builder vs Code Repositories, batch vs incremental vs streaming |  |
| 51 | Ontology: Object types, Properties, Link types; semantic layer (dataset/row/column/join → object type/object/property/link) |  |
| 52 | Pipelines in Code Repos (Python/SQL transforms, versioning, scheduling); data quality and governance (checks, RBAC, audit) |  |
| 53 | Foundry Data Engineer cert prep (syllabus, sample topics, practice) |  |

### Week 8: Spark Fundamentals

*Palantir angle: PySpark and Spark SQL are central to Foundry; Spark at scale in a platform (scheduling, observability) applies to Foundry Code Repos.*

| Day | Topic | Status |
|-----|-------|--------|
| 54 | Spark Architecture (Driver, Executors, Partitions) |  |
| 55 | PySpark DataFrames + Transformations |  |
| 56 | Spark SQL + Optimization (Catalyst, Tungsten) |  |
| 57 | Partitioning + Bucketing Strategies |  |
| 58 | Joins at Scale (Broadcast, Shuffle, Sort-Merge) |  |
| 59 | Spark on Databricks / Foundry Code Repos (platform context) |  |
| 60 | Spark Performance Tuning |  |

### Week 9: Project 2: Fraud Detection Pipeline - Part 1

| Day | Topic | Status |
|-----|-------|--------|
| 61 | Synthetic Transaction Data Generation (10M+) |  |
| 62 | Feature Engineering for Fraud Signals |  |
| 63 | Spark Ingestion + Transformation |  |
| 64 | dbt Staging Models |  |
| 65 | dbt Intermediate Models (Feature Aggregations) |  |
| 66 | dbt Marts (Fraud Risk Scores) |  |
| 67 | Real-Time Scoring Architecture Design |  |

### Week 10: Project 2: Fraud Detection Pipeline - Part 2

| Day | Topic | Status |
|-----|-------|--------|
| 68 | Streamlit Fraud Dashboard |  |
| 69 | dbt Testing + Data Quality Checks |  |
| 70 | CI/CD for dbt (GitHub Actions + dbt Cloud) |  |
| 71 | Documentation + System Design Writeup |  |
| 72 | dbt Certification Prep |  |
| 73 | dbt Certification Prep |  |
| 74 | dbt Analytics Engineering Certification Exam |  |

### Week 11: Kafka + Streaming Basics

*Palantir angle: streaming pipelines in Foundry vs self-managed Kafka; same concepts (topics, partitions, exactly-once).*

| Day | Topic | Status |
|-----|-------|--------|
| 75 | Kafka Architecture (Brokers, Topics, Partitions) |  |
| 76 | Kafka Producer/Consumer in Python |  |
| 77 | Stream Processing Concepts (Windowing, Watermarks) |  |
| 78 | Kafka Connect Basics |  |
| 79 | Add Streaming Component to Project 2 |  |
| 80 | Exactly-Once Semantics in Practice |  |
| 81 | Phase 2 Review |  |

---

## MONTH 3: PRODUCTION SYSTEMS + APPLICATIONS

**Project:** Real-Time Analytics Platform
**Stack:** Python, Spark, Kafka, Airflow, PostgreSQL, Redis, Great Expectations

**Certification:** AWS Solutions Architect Associate (Day 112)

### Week 12: Data Quality + Great Expectations

*Palantir angle: production-ready pipelines = ownership, documentation, quality checks, scheduling (Foundry language); GX and data contracts map to Foundry governance.*

| Day | Topic | Status |
|-----|-------|--------|
| 82 | Great Expectations Setup + Concepts |  |
| 83 | Expectation Suites Design |  |
| 84 | Integration with Airflow |  |
| 85 | Data Contracts Pattern |  |
| 86 | Alerting on Quality Failures |  |
| 87 | Quality Dashboards |  |
| 88 | Phase 3 Project Planning |  |

### Week 13: Project 3: Real-Time Analytics Platform - Part 1

| Day | Topic | Status |
|-----|-------|--------|
| 89 | Multi-Source Ingestion (APIs, Kafka, Files) |  |
| 90 | Lambda Architecture Implementation |  |
| 91 | Batch Layer (Spark + S3) |  |
| 92 | Speed Layer (Kafka + Real-Time Aggregations) |  |
| 93 | Serving Layer (PostgreSQL + Redis) |  |
| 94 | Airflow Orchestration (Complex DAGs) |  |
| 95 | Great Expectations Integration |  |

### Week 14: Project 3: Real-Time Analytics Platform - Part 2

| Day | Topic | Status |
|-----|-------|--------|
| 96 | Monitoring + Observability (Metrics, Logs, Traces) |  |
| 97 | Alerting + Incident Response Setup |  |
| 98 | Load Testing + Performance Optimization |  |
| 99 | Documentation + Runbooks |  |
| 100 | Resume Polish + LinkedIn Optimization |  |
| 101 | START APPLYING - First 10 Applications |  |
| 102 | Application Sprint (10 more) |  |

### Week 15: AWS Certification - Part 1

| Day | Topic | Status |
|-----|-------|--------|
| 103 | AWS S3 + Storage Deep Dive |  |
| 104 | AWS Compute (Lambda, EC2, ECS, EKS) |  |
| 105 | AWS Databases (RDS, Redshift, DynamoDB) |  |
| 106 | AWS Networking (VPC, Security Groups, IAM) |  |
| 107 | AWS Glue + Athena + Lake Formation |  |
| 108 | Applications + AWS Practice Exams |  |
| 109 | AWS Practice Exam Review |  |

### Week 16: AWS Certification - Part 2

| Day | Topic | Status |
|-----|-------|--------|
| 110 | AWS Weak Areas Deep Dive |  |
| 111 | AWS Practice Exam 2 |  |
| 112 | AWS Solutions Architect Associate Exam |  |
| 113 | Interview Prep: SQL Live Coding |  |
| 114 | Interview Prep: System Design Basics |  |
| 115 | Interview Prep: Python Coding |  |
| 116 | Phase 3 Review (40+ applications) |  |

---

## MONTH 4: INTERVIEW INTENSIVE

### Week 17: System Design Mastery - Part 1

| Day | Topic | Status |
|-----|-------|--------|
| 117 | System Design Framework (Requirements, Estimation, Design) |  |
| 118 | Design: Data Warehouse from Scratch |  |
| 119 | Design: Real-Time Analytics Platform |  |
| 120 | Design: ETL Pipeline at Scale (batch + incremental, quality, governance; Foundry-style) |  |
| 121 | Design: Data Lake Architecture |  |
| 122 | Design: Streaming Platform (Kafka-based) |  |
| 123 | Design: ML Feature Store |  |

### Week 18: System Design Mastery - Part 2

| Day | Topic | Status |
|-----|-------|--------|
| 124 | Active Interviewing + Applications (50+ total) |  |
| 125 | Mock System Design Interview 1 |  |
| 126 | Mock System Design Interview 2 |  |
| 127 | Design: CDC Pipeline |  |
| 128 | Design: Data Mesh Architecture |  |
| 129 | Design: Multi-Region Data Replication |  |
| 130 | System Design Review |  |

### Week 19: Technical Interview Drilling

| Day | Topic | Status |
|-----|-------|--------|
| 131 | SQL Window Functions Under Pressure |  |
| 132 | SQL Complex Aggregations Timed |  |
| 133 | SQL Optimization Problems |  |
| 134 | Python Data Structures for Interviews |  |
| 135 | Python Coding Problems (Data-Focused) |  |
| 136 | Active Interviewing (Phone Screens) |  |
| 137 | Mock Technical Interview 1 |  |

### Week 20: Behavioral + Mock Interviews

| Day | Topic | Status |
|-----|-------|--------|
| 138 | Mock Technical Interview 2 |  |
| 139 | Behavioral STAR Method Prep (ambiguous problems, cross-functional, stakeholder comms for Palantir) |  |
| 140 | Tell Me About Yourself Polish |  |
| 141 | Leadership + Conflict Stories |  |
| 142 | Failure + Growth Stories |  |
| 143 | Mock Behavioral Interview |  |
| 144 | Phase 4 Review (60+ applications) |  |

### Week 21: Final Interview Prep

| Day | Topic | Status |
|-----|-------|--------|
| 145 | Weak Area Drilling |  |
| 146 | Company-Specific Research (incl. Palantir Foundry, Ontology, cert syllabus) |  |
| 147 | Salary Research + Negotiation Prep |  |
| 148 | Final Mock Interview (Full Loop Simulation) |  |
| 149 | Rest + Mental Prep |  |
| 150 | Active Interviewing |  |
| 151 | Phase 4 Complete |  |

---

## MONTH 5: CLOSE OFFERS

### Week 22: Final Rounds

| Day | Topic | Status |
|-----|-------|--------|
| 152 | Final Round Prep |  |
| 153 | Final Interviews |  |
| 154 | Final Interviews |  |
| 155 | Final Interviews |  |
| 156 | Final Interviews |  |
| 157 | Final Interviews |  |
| 158 | Offer Comparison Framework |  |

### Week 23: Negotiate + Accept

| Day | Topic | Status |
|-----|-------|--------|
| 159 | Negotiation Strategy (Leverage Multiple Offers) |  |
| 160 | Counter-Offer Calls |  |
| 161 | Final Negotiations |  |
| 162 | Accept Best Offer |  |
| 163 | Give Notice |  |
| 164 | Celebrate |  |
| 165 | Transition Planning |  |

### Week 24: Launch

| Day | Topic | Status |
|-----|-------|--------|
| 166 | Knowledge Transfer |  |
| 167 | Finish Strong at Current Role |  |
| 168 | Study New Stack |  |
| 169 | Prep Day 1 |  |
| 170 | Last Day |  |
| 171 | Rest |  |
| 172 | New Chapter Begins |  |

---
