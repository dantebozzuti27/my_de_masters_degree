# DATA ENGINEERING MASTERS CURRICULUM V2
## 168-Day Elite Program for Top-Tier NYC Roles ($160-200k)

---

## DAILY STRUCTURE (3-4 hours total)

| Block | Duration | Activity |
|-------|----------|----------|
| **LEARN** | 60-90 min | Video course + reading (commute/lunch friendly) |
| **BUILD** | 2-2.5 hours | Hands-on coding, real projects |
| **REVIEW** | 15-30 min | Document learnings, commit code |

---

## TARGET COMPANIES (NYC Focus)

### Tier 1: Elite ($180-250k)
- Two Sigma, Citadel, Jane Street (quant finance)
- Bloomberg (data infrastructure)

### Tier 2: Top Tech ($160-200k)  
- Datadog, MongoDB, Cockroach Labs
- Stripe, Plaid, Ramp, Brex

### Tier 3: Strong ($140-180k)
- Capital One, Goldman Sachs tech
- Spotify, Netflix (if remote)
- HashiCorp, Confluent

---

## MONTH 1: FOUNDATIONS + PRODUCTION SKILLS (Days 1-35)

### Week 1: Python Mastery (Days 1-7) ✅ COMPLETE
Focus: Core Python for data engineering

### Week 2: Production Python + Git (Days 8-14) ✅ COMPLETE  
Focus: OOP, testing, version control

### Week 3: Cloud Fundamentals (Days 15-21) 🔄 IN PROGRESS
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) | Status |
|-----|-------|-------------------|-------------------|--------|
| 15 | Advanced Git | Zach Wilson: Git for DE (YT) | Rebase, bisect, hooks practice | ✅ |
| 16 | AWS IAM | AWS Skill Builder: IAM | MFA, users, policies, CLI | ✅ |
| 17 | S3 Deep Dive | "Fundamentals of DE" Ch 6 | Production pipeline to S3, lifecycle | ✅ |
| 18 | Docker Fundamentals | TechWorld Nana: Docker (YT) | Images, containers, Dockerfile | ✅ |
| 19 | Docker for DE | Seattle Data Guy: Docker DE | Multi-stage builds, optimization | 🔄 |
| 20 | **PROJECT DAY** | - | Containerized data pipeline | |
| 21 | Review + Prep | Review week, plan ahead | Document, commit, refactor | |

### Week 4: Lambda + PostgreSQL (Days 22-28)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 22 | Docker Compose | Docker docs + tutorials | Multi-container local stack |
| 23 | AWS Lambda | AWS Skill Builder: Lambda | Deploy Python Lambda |
| 24 | Lambda + S3 | AWS tutorials | Event-driven pipeline |
| 25 | PostgreSQL Basics | "Fundamentals of DE" Ch 8 | Schema design, queries |
| 26 | PostgreSQL Advanced | Mode SQL Tutorial (advanced) | Indexes, EXPLAIN, optimization |
| 27 | **PROJECT DAY** | - | Lambda → S3 → PostgreSQL pipeline |
| 28 | Review + Debug | - | Fix bugs, add tests, document |

### Week 5: Airflow Intro + Project 1 (Days 29-35)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 29 | Airflow Architecture | Astronomer Academy (free) | Local Airflow setup |
| 30 | DAG Fundamentals | Astronomer: DAG best practices | First DAG with dependencies |
| 31 | Airflow + AWS | - | Connect Lambda, S3 to Airflow |
| 32 | Streamlit Basics | Streamlit docs + tutorials | Simple dashboard |
| 33 | Dashboard + Data | - | Connect to PostgreSQL |
| 34 | **PROJECT 1 POLISH** | - | Stock pipeline end-to-end |
| 35 | Month 1 Review | "Fundamentals of DE" Ch 1-2 | Portfolio documentation |

---

## MONTH 2: DBT + ADVANCED SQL (Days 36-63)

### Week 6: dbt Fundamentals (Days 36-42)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 36 | dbt Introduction | dbt Learn (official, free) | dbt init, first models |
| 37 | Materializations | dbt Learn: Materializations | Tables, views, incremental |
| 38 | Staging/Marts | Advancing Analytics (YT) | Layered architecture |
| 39 | Sources + Seeds | dbt docs | Configure sources, load seeds |
| 40 | dbt + Jinja | dbt Learn: Jinja | Dynamic SQL with Jinja |
| 41 | **PROJECT DAY** | - | Full dbt project structure |
| 42 | Review + Testing Intro | dbt testing docs | Add schema tests |

### Week 7: dbt Advanced + SQL Deep Dive (Days 43-49)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 43 | dbt Testing | dbt Learn: Testing | Schema + data tests |
| 44 | Custom Tests + Macros | dbt docs: macros | Write custom tests, macros |
| 45 | **Advanced SQL: Windows** | Mode: Window Functions | 20+ window function exercises |
| 46 | **Advanced SQL: CTEs** | Mode: CTEs | Complex recursive queries |
| 47 | dbt Packages | dbt Hub: dbt-utils, codegen | Install and use packages |
| 48 | **SQL DEEP PRACTICE** | - | 50+ interview-style problems |
| 49 | dbt Cert Prep Start | dbt certification guide | Practice questions |

### Week 8: Data Modeling + Snowflake (Days 50-56)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 50 | Dimensional Modeling | "Data Warehouse Toolkit" Ch 1-2 | Design star schema |
| 51 | Kimball Deep Dive | "Data Warehouse Toolkit" Ch 3 | Fact vs dimension tables |
| 52 | Snowflake Setup | Snowflake quickstart | Account, warehouse, database |
| 53 | Snowflake + dbt | dbt + Snowflake docs | Connect and deploy |
| 54 | SCD Types | "Data Warehouse Toolkit" Ch 5 | Implement Type 2 SCD |
| 55 | **PROJECT 2 START** | - | NBA Analytics ingestion |
| 56 | Project 2 Modeling | - | dbt models for NBA data |

### Week 9: Project 2 Complete + Cert (Days 57-63)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 57 | Project 2 dbt | - | Staging → Marts pipeline |
| 58 | Streamlit + Snowflake | - | NBA analytics dashboard |
| 59 | Dashboard Polish | - | Charts, filters, interactivity |
| 60 | Testing + Docs | - | Full test coverage, docs |
| 61 | dbt Cert Final Prep | Practice exams | Review weak areas |
| 62 | **DBT CERTIFICATION** | - | Take the exam |
| 63 | Month 2 Review | - | Document, celebrate |

---

## MONTH 3: AIRFLOW MASTERY + SPARK INTRO (Days 64-91)

### Week 10: Airflow Deep Dive (Days 64-70)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 64 | Airflow Architecture | Astronomer: Architecture | Executor types, scaling |
| 65 | TaskFlow API | Astronomer: TaskFlow | Modern DAG patterns |
| 66 | Operators Deep Dive | Airflow docs | Python, Bash, Docker operators |
| 67 | XComs + Dependencies | - | Complex task communication |
| 68 | Connections + Hooks | - | AWS, Snowflake connections |
| 69 | **COMPLEX DAG DAY** | - | Multi-step orchestration |
| 70 | Airflow Testing | pytest-airflow | Unit and integration tests |

### Week 11: Airflow Production + Applying (Days 71-77)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 71 | Monitoring + Alerting | Datadog/CloudWatch | Observability setup |
| 72 | Error Handling | Astronomer: Error handling | Retries, callbacks, SLAs |
| 73 | **RESUME + LINKEDIN** | Review top DE resumes | Polish materials |
| 74 | **FIRST 5 APPLICATIONS** | Company research | Apply to 5 companies |
| 75 | Airflow + dbt | dbt Cloud or Cosmos | Orchestrate dbt with Airflow |
| 76 | **APPLICATION SPRINT** | - | 10 more applications |
| 77 | Week Review | - | Track applications |

### Week 12: Spark Introduction (Days 78-84)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 78 | Spark Overview | "Spark: Definitive Guide" Ch 1-2 | Local Spark setup |
| 79 | PySpark Basics | DataBricks free tutorials | DataFrames, transformations |
| 80 | Spark SQL | Spark docs | SQL on Spark |
| 81 | Spark + S3 | - | Read/write to S3 |
| 82 | Spark Optimization | "Spark: Definitive Guide" Ch 8 | Partitions, caching |
| 83 | **PROJECT 3 START** | - | Spark data processing |
| 84 | Project 3 Pipeline | - | Airflow + Spark |

### Week 13: Data Quality + Project 3 (Days 85-91)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 85 | Great Expectations | GE docs + tutorials | Setup, first expectations |
| 86 | Data Quality in Pipelines | - | Integrate GE with Airflow |
| 87 | Project 3 Quality | - | Add quality checks |
| 88 | Project 3 Polish | - | End-to-end testing |
| 89 | **MORE APPLICATIONS** | - | 10 more (35+ total) |
| 90 | Portfolio Review | - | All projects documented |
| 91 | Month 3 Review | - | 40+ applications out |

---

## MONTH 4: AWS CERTIFICATION + INTERVIEWS START (Days 92-119)

### Week 14: AWS Deep Dive - Compute/Storage (Days 92-98)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 92 | S3 Advanced | AWS Skill Builder | Storage classes, lifecycle, policies |
| 93 | EC2 + Lambda | AWS Skill Builder | Compute patterns |
| 94 | RDS + Redshift | AWS Skill Builder | Managed databases |
| 95 | **APPLICATIONS** | - | Weekly app goal |
| 96 | Kinesis + Streaming | AWS Skill Builder | Real-time data |
| 97 | **AWS LAB DAY** | - | Build full architecture |
| 98 | Review + Flashcards | - | Anki for AWS |

### Week 15: AWS Deep Dive - Networking/Analytics (Days 99-105)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 99 | VPC + Networking | AWS Skill Builder | Subnets, security groups |
| 100 | IAM Advanced | AWS Skill Builder | Roles, policies, federation |
| 101 | Glue + Athena | AWS Skill Builder | Serverless analytics |
| 102 | **INTERVIEW PREP** | - | SQL + Python practice |
| 103 | CloudWatch + Monitoring | AWS Skill Builder | Logs, metrics, alarms |
| 104 | **PRACTICE EXAM 1** | Tutorials Dojo | Full practice exam |
| 105 | Review Weak Areas | - | Focus study |

### Week 16: AWS Certification Week (Days 106-112)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 106 | Practice Exam 2 | Tutorials Dojo | Full exam |
| 107 | Deep Dive Gaps | - | Study weak areas |
| 108 | Practice Exam 3 | Tutorials Dojo | Full exam |
| 109 | **FIRST INTERVIEWS** | - | Phone screens |
| 110 | Final Review | - | Last cram session |
| 111 | **AWS SAA EXAM** | - | Take certification |
| 112 | Celebrate + Prep | - | Interview prep |

### Week 17: Interview Fundamentals (Days 113-119)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 113 | SQL Interviews | "Ace the Data Science Interview" | 30+ problems |
| 114 | Python Interviews | LeetCode (Easy/Medium) | Data structures problems |
| 115 | System Design Intro | "DDIA" Ch 1-2 | Basic patterns |
| 116 | **ACTIVE INTERVIEWING** | - | Phone/video screens |
| 117 | Behavioral Prep | - | STAR method stories |
| 118 | **MOCK INTERVIEW** | - | Practice with friend/service |
| 119 | Month 4 Review | - | 5-10 interviews completed |

---

## MONTH 5: INTERVIEW INTENSIVE (Days 120-147)

### Week 18: System Design (Days 120-126)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 120 | Data Pipelines | "DDIA" Ch 10-11 | Design batch pipeline |
| 121 | Data Warehouses | "DDIA" Ch 3 | Design DW architecture |
| 122 | Streaming Systems | "DDIA" Ch 11 | Design real-time system |
| 123 | **INTERVIEWS** | - | Active interviewing |
| 124 | Real-time Analytics | - | Design dashboard backend |
| 125 | **SYSTEM DESIGN PRACTICE** | - | 3 full designs |
| 126 | Review + Debrief | - | Learn from interviews |

### Week 19: Technical Deep Dive (Days 127-133)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 127 | SQL: Window Functions | - | 20 hard problems |
| 128 | SQL: Performance | - | EXPLAIN, optimization |
| 129 | Python: Algorithms | - | Medium/Hard LeetCode |
| 130 | **INTERVIEWS** | - | Technical rounds |
| 131 | Data Modeling Deep | - | Design schemas on whiteboard |
| 132 | **FULL MOCK INTERVIEW** | - | 4-hour simulation |
| 133 | Review + Adjust | - | Refine weak areas |

### Week 20: Behavioral + Final Prep (Days 134-140)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 134 | STAR Method | - | Write 10 stories |
| 135 | "Tell Me About Yourself" | - | Perfect your pitch |
| 136 | Leadership/Conflict | - | Prepare examples |
| 137 | **INTERVIEWS** | - | On-sites starting |
| 138 | Mock Interview 1 | - | Full behavioral |
| 139 | Mock Interview 2 | - | Full technical |
| 140 | Refine Everything | - | Polish answers |

### Week 21: Interview Mastery (Days 141-147)
| Day | Topic | Learn (60-90 min) | Build (2-2.5 hrs) |
|-----|-------|-------------------|-------------------|
| 141 | Refine Your Story | - | Tighten narrative |
| 142 | Technical Deep Dives | - | Practice explaining projects |
| 143 | Negotiation Prep | - | Research comp bands |
| 144 | **INTERVIEWS** | - | Final rounds |
| 145 | Final Round Prep | - | Company-specific prep |
| 146 | Practice Finals | - | Mock on-sites |
| 147 | Month 5 Review | - | Multiple offers expected |

---

## MONTH 6: CLOSE + TRANSITION (Days 148-168)

### Week 22: Final Interviews (Days 148-154)
| Day | Topic | Activity |
|-----|-------|----------|
| 148-150 | Final Rounds | Complete remaining interviews |
| 151 | Compare Offers | Analyze total comp |
| 152 | Negotiation Strategy | Plan approach |
| 153-154 | Negotiate | Push for top of band |

### Week 23: Accept + Notice (Days 155-161)
| Day | Topic | Activity |
|-----|-------|----------|
| 155-156 | Final Negotiations | Counter-offers |
| 157 | **ACCEPT OFFER** | Sign at $160-200k |
| 158 | Give Notice | Resign professionally |
| 159-161 | Transition | Knowledge transfer |

### Week 24: Launch (Days 162-168)
| Day | Topic | Activity |
|-----|-------|----------|
| 162-163 | Finish Strong | Complete handoff |
| 164-165 | Prep New Role | Study their stack |
| 166 | Last Day | Celebrate |
| 167-168 | Rest + Launch | New chapter begins |

---

## REQUIRED RESOURCES

### Books (Buy These)
1. **"Fundamentals of Data Engineering"** - Joe Reis & Matt Housley
2. **"Designing Data-Intensive Applications"** - Martin Kleppmann (THE bible)
3. **"The Data Warehouse Toolkit"** - Ralph Kimball
4. **"Spark: The Definitive Guide"** - Chambers & Zaharia

### Video Courses (Free)
- Zach Wilson's Data Engineering Bootcamp (YouTube)
- Seattle Data Guy (YouTube)
- Advancing Analytics - dbt (YouTube)
- Astronomer Academy (Airflow)
- AWS Skill Builder (free tier)
- dbt Learn (official, free)

### Video Courses (Paid - Optional)
- DataExpert.io by Zach Wilson ($)
- DataBricks Academy (Spark)

### Practice Platforms
- Mode Analytics (SQL)
- LeetCode (Python)
- Tutorials Dojo (AWS)
- StrataScratch (SQL interviews)

---

## CERTIFICATIONS

| Certification | Target Date | Purpose |
|---------------|-------------|---------|
| dbt Analytics Engineering | End of Month 2 | Validates dbt expertise |
| AWS Solutions Architect Associate | End of Month 4 | Industry standard |

---

## KEY DIFFERENCES FROM V1

1. **Added Spark/PySpark** (Week 12) - Required for 80% of senior roles
2. **Advanced SQL weeks** - Window functions, CTEs, optimization
3. **Data Modeling theory** - Kimball, dimensional modeling
4. **Streaming basics** - Kinesis introduction
5. **More rigorous daily structure** - Learn + Build + Review
6. **Specific resources per day** - Videos, books, docs
7. **Earlier job applications** - Start Month 3, not Month 4
8. **Interview prep integrated** - Not just crammed at end

---

*This curriculum is designed to make you overqualified for $160k+ roles at top NYC companies.*
