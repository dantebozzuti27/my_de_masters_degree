# SDE Tracker

**6-Month Data Engineer Learning Curriculum**

---

## Current Progress: 43/172 Days (25%)

| Week | Days | Focus | Status |
|------|------|-------|--------|
| 1 | 1-7 | Python Fundamentals | ✅ |
| 2 | 8-14 | Production Python + Git | ✅ |
| 3 | 15-21 | AWS + Docker + Project 1 Start | ✅ |
| 4 | 22-28 | Project 1 Deployment + CI/CD | ✅ |
| 5 | 29-35 | SQL Deep Dive | ✅ |
| 6 | 36-42 | Distributed Systems Theory | ✅ |
| 7 | 43-49 | dbt Fundamentals | 🔄 Day 43 complete |

**Latest:** Day 43 - dbt project setup, models, ref(); dbt run against Postgres. Next: Day 44 (materializations).

---

## Current Project: Credit Markets Pipeline

Production-grade data pipeline for treasury yields and SEC filings.

| Component | Status |
|-----------|--------|
| FRED/SEC Ingestion | ✅ |
| S3 Bronze Layer | ✅ |
| PostgreSQL Silver/Gold | ✅ |
| Parallel Processing | ✅ |
| AWS Lambda | ✅ |
| GitHub Actions CI | ✅ |
| Airflow DAG | ✅ |
| S3 Sensors + XCom | ✅ |
| Slack Alerts | ✅ |
| Great Expectations | ✅ |
| Documentation | ✅ |

---

## 6-Month Overview

| Month | Focus | Days | Key Deliverables |
|-------|-------|------|------------------|
| 1 | Foundations + Project 1 | 1-42 | Credit Markets Pipeline, SQL Deep Dive |
| 2 | dbt + Foundry + Spark + Project 2 | 43-81 | Foundry & Ontology, Fraud Detection, dbt Cert |
| 3 | Production Systems | 82-116 | Real-Time Analytics, AWS SAA Cert |
| 4-6 | Interview Prep | 117-172 | System Design, Mock Interviews |

---

## Week 4: Project 1 Deployment + CI/CD

| Day | Topic | Status |
|-----|-------|--------|
| 22 | AWS Lambda Deployment | ✅ |
| 23 | GitHub Actions CI/CD | ✅ |
| 24 | Airflow DAG Setup (Local) | ✅ |
| 25 | Airflow Integration (Lambda + S3 Sensors) | ✅ |
| 26 | Monitoring + Alerting (CloudWatch, Slack) | ✅ |
| 27 | Data Quality with Great Expectations | ✅ |
| 28 | Project 1 Documentation + Architecture Diagrams | ✅ |

---

## Week 5: SQL Deep Dive

*Go deep each day: 3+ problems, edge cases, when to use / when not, interview angle.*

| Day | Topic | Status |
|-----|-------|--------|
| 29 | Window Functions (ROW_NUMBER, RANK, LEAD/LAG, NTILE) | ✅ |
| 30 | Advanced Aggregations (GROUPING SETS, CUBE, ROLLUP) | ✅ |
| 31 | CTEs + Recursive CTEs | ✅ |
| 32 | Query Optimization (EXPLAIN ANALYZE, Indexes) | ✅ |
| 33 | SQL Drilling (10 problems in-repo) | ✅ |
| 34 | SQL Drilling (10 problems in-repo, day34_sql_drill.sql) | ✅ |
| 35 | SQL Assessment + Review | ✅ |

---

## Week 6: Distributed Systems Theory

| Day | Topic | Status |
|-----|-------|--------|
| 36 | CAP Theorem Deep Dive | ✅ |
| 37 | Consistency Models (Eventual, Strong, Causal) | ✅ |
| 38 | Partitioning Strategies (Hash, Range, Composite) | ✅ |
| 39 | Replication Patterns (Leader-Follower, Multi-Leader) | ✅ |
| 40 | Exactly-Once Semantics (Why It's Mostly a Myth) | ✅ |
| 41 | Data Modeling at Scale (Star Schema, SCDs) | ✅ |
| 42 | Phase 1 Review + Project 1 Final Polish | ✅ |

## Week 7: dbt Fundamentals (Current)

| Day | Topic | Status |
|-----|-------|--------|
| 43 | dbt Project Setup, Models, Refs | ✅ |
| 44 | Materializations (Table, View, Incremental, Ephemeral) | |
| 45 | Staging → Intermediate → Marts Pattern | |
| 46 | Sources, Seeds, Snapshots | |
| 47 | dbt Testing (Schema + Data Tests) | |
| 48 | Macros and Jinja Templating | |
| 49 | dbt Packages + Documentation Generation | |

---

## Certifications

| Certification | Target Day |
|--------------|------------|
| dbt Analytics Engineering | Day 74 |
| AWS Solutions Architect Associate | Day 112 |

**Target companies:** See `TARGETS.md` (e.g. Palantir Foundry tailoring in Week 7b and callouts).

---

## Data Files

- `data/curriculum.json` — Full curriculum (see CURRICULUM.md; 172 days with Palantir block)
- `data/progress.json` — Completed days and notes
