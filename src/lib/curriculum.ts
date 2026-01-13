// Curriculum data for the 2-Year Senior Data Engineer Study Plan

import { Quarter, WeekTopics } from './types';

export const QUARTERS: Quarter[] = [
  {
    id: 1,
    name: "Python & SQL Foundations",
    shortName: "Q1: Python & SQL",
    weeks: [1, 13],
    startDate: "2026-01-12",
    endDate: "2026-04-05",
    goal: "Build Python fundamentals from scratch, advance SQL to window functions and optimization, establish development environment and habits.",
    project: "Schema-Aware ETL Generator (v0) - scaffolding only"
  },
  {
    id: 2,
    name: "ETL Patterns & Data Quality",
    shortName: "Q2: ETL & Quality",
    weeks: [14, 26],
    startDate: "2026-04-06",
    endDate: "2026-06-28",
    goal: "Master ETL patterns, data quality frameworks, begin dbt.",
    project: "Schema-Aware ETL Generator (v1) - basic functionality"
  },
  {
    id: 3,
    name: "dbt Mastery & Testing",
    shortName: "Q3: dbt Mastery",
    weeks: [27, 39],
    startDate: "2026-06-29",
    endDate: "2026-09-20",
    goal: "Deep dbt expertise, analytics engineering certification, comprehensive testing.",
    project: "Schema-Aware ETL Generator (v2) - dbt integration",
    certification: "dbt Analytics Engineering"
  },
  {
    id: 4,
    name: "AWS Foundations & Cloud Data",
    shortName: "Q4: AWS Foundations",
    weeks: [40, 52],
    startDate: "2026-09-21",
    endDate: "2026-12-13",
    goal: "AWS Cloud Practitioner cert, core services mastery, cloud data patterns.",
    project: "Deploy ETL Generator to AWS",
    certification: "AWS Cloud Practitioner"
  },
  {
    id: 5,
    name: "Orchestration Deep Dive",
    shortName: "Q5: Orchestration",
    weeks: [53, 65],
    startDate: "2026-12-14",
    endDate: "2027-03-07",
    goal: "Master Airflow/Dagster, production orchestration patterns.",
    project: "Orchestrated Data Pipeline Platform"
  },
  {
    id: 6,
    name: "AWS Advanced & Data Engineering",
    shortName: "Q6: AWS Advanced",
    weeks: [66, 78],
    startDate: "2027-03-08",
    endDate: "2027-05-30",
    goal: "AWS Data Engineer Associate cert, advanced cloud architecture.",
    project: "Full cloud-native data platform",
    certification: "AWS Data Engineer Associate"
  },
  {
    id: 7,
    name: "System Design & Governance",
    shortName: "Q7: System Design",
    weeks: [79, 91],
    startDate: "2027-05-31",
    endDate: "2027-08-22",
    goal: "System design mastery, data governance, compliance frameworks.",
    project: "Enterprise-grade data platform with governance"
  },
  {
    id: 8,
    name: "Interview Prep & Career Launch",
    shortName: "Q8: Interview Prep",
    weeks: [92, 104],
    startDate: "2027-08-23",
    endDate: "2028-01-08",
    goal: "Interview preparation, portfolio polish, job search execution.",
    project: "Final portfolio presentation"
  }
];

export const WEEKLY_CURRICULUM: WeekTopics[] = [
  // Quarter 1: Python & SQL Foundations
  { week: 1, topics: ["Development Environment Setup", "Python Syntax Fundamentals", "Control Flow & Functions", "Data Types Deep Dive"] },
  { week: 2, topics: ["Lists and List Comprehensions", "Dictionaries and JSON", "File I/O and Context Managers", "Error Handling"] },
  { week: 3, topics: ["Classes and Objects Basics", "Class Methods and Static Methods", "Inheritance and Polymorphism", "Special Methods (Dunder)"] },
  { week: 4, topics: ["Modules and Imports", "Package Structure", "Virtual Environments Deep Dive", "Project Structure Best Practices"] },
  { week: 5, topics: ["SQL Window Functions Intro", "Aggregate Window Functions", "Advanced Window Functions (LAG/LEAD)", "CTE Mastery"] },
  { week: 6, topics: ["Understanding Execution Plans", "Indexing Fundamentals", "Index Types and Strategies", "Query Optimization Patterns"] },
  { week: 7, topics: ["Python Iterators", "Generators and Yield", "Decorators Part 1", "Decorators Part 2 + Functools"] },
  { week: 8, topics: ["Type Hints Fundamentals", "Advanced Type Hints (Generics)", "Dataclasses", "Pydantic Introduction"] },
  { week: 9, topics: ["Unit Testing with pytest", "Test Fixtures and Parametrize", "Mocking with unittest.mock", "Test-Driven Development"] },
  { week: 10, topics: ["SQL Schema Design Basics", "Normalization (1NF-3NF)", "Denormalization Strategies", "Dimensional Modeling Intro"] },
  { week: 11, topics: ["Star Schema Design", "Slowly Changing Dimensions", "Fact Table Patterns", "Schema Design Review"] },
  { week: 12, topics: ["Pandas Fundamentals", "Pandas Data Manipulation", "Pandas Aggregations and Joins", "Pandas Performance Tips"] },
  { week: 13, topics: ["Q1 Project: ETL Generator Setup", "Q1 Project: Schema Parser", "Q1 Project: Code Generator", "Q1 Review & Retrospective"] },
  
  // Quarter 2: ETL Patterns & Data Quality
  { week: 14, topics: ["ETL vs ELT Patterns", "Full Load Strategies", "Incremental Load Patterns", "Upsert/Merge Patterns"] },
  { week: 15, topics: ["Change Data Capture (CDC)", "CDC Implementation Patterns", "Checkpointing Strategies", "Idempotency in ETL"] },
  { week: 16, topics: ["Data Quality Fundamentals", "Data Quality Dimensions", "Quality Metrics and SLAs", "Quality Rule Patterns"] },
  { week: 17, topics: ["Great Expectations Intro", "Creating Expectations", "Data Docs and Validation", "GE in Pipelines"] },
  { week: 18, topics: ["dbt Fundamentals", "dbt Models and Refs", "dbt Sources and Seeds", "dbt Documentation"] },
  { week: 19, topics: ["dbt Tests: Built-in", "dbt Tests: Custom", "dbt-expectations Package", "dbt Data Quality Strategy"] },
  { week: 20, topics: ["Logging Fundamentals", "Structured Logging (JSON)", "Python Logging Best Practices", "Log Aggregation Concepts"] },
  { week: 21, topics: ["Error Handling Patterns", "Retry Strategies (tenacity)", "Dead Letter Queues", "Alerting Patterns"] },
  { week: 22, topics: ["Configuration Management", "YAML and PyYAML", "Config-Driven Pipelines", "Secrets Management Intro"] },
  { week: 23, topics: ["Schema Evolution", "Schema Drift Detection", "Backwards Compatibility", "Data Contracts Intro"] },
  { week: 24, topics: ["ETL Generator: Full Load", "ETL Generator: Incremental", "ETL Generator: Quality Checks", "ETL Generator: Config"] },
  { week: 25, topics: ["ETL Generator: Logging", "ETL Generator: Error Handling", "ETL Generator: Documentation", "Integration Testing"] },
  { week: 26, topics: ["Q2 Project Polish", "Q2 Code Review", "Q2 Documentation", "Q2 Review & Retrospective"] },
  
  // Quarter 3: dbt Mastery & Testing
  { week: 27, topics: ["dbt Project Structure", "dbt Macros Fundamentals", "Jinja Templating in dbt", "Custom Macros"] },
  { week: 28, topics: ["dbt Packages", "dbt-utils Package", "dbt-audit-helper", "Package Management"] },
  { week: 29, topics: ["dbt Snapshots", "Snapshot Strategies", "Historical Data Tracking", "SCD Type 2 with dbt"] },
  { week: 30, topics: ["dbt Incremental Models", "Incremental Strategies", "Incremental Optimization", "Incremental Edge Cases"] },
  { week: 31, topics: ["dbt Analytics Engineering Cert Prep", "Cert Practice Questions", "Cert Review Topics", "Mock Certification Exam"] },
  { week: 32, topics: ["Advanced dbt Testing", "Unit Tests in dbt", "Integration Tests", "Test Coverage Strategies"] },
  { week: 33, topics: ["dbt Cloud Intro", "dbt Cloud Jobs", "CI/CD with dbt Cloud", "dbt Cloud vs Core"] },
  { week: 34, topics: ["dbt Artifacts", "dbt docs generate", "Data Lineage in dbt", "Catalog Management"] },
  { week: 35, topics: ["dbt Performance", "Model Optimization", "Warehouse Optimization", "dbt Profiling"] },
  { week: 36, topics: ["dbt Project: Metrics Layer", "dbt Project: Semantic Layer", "dbt Project: BI Integration", "dbt Best Practices Review"] },
  { week: 37, topics: ["ETL Generator: dbt Integration", "ETL Generator: dbt Tests", "ETL Generator: dbt Docs", "Testing Strategy"] },
  { week: 38, topics: ["Full Pipeline Testing", "End-to-End Testing", "Performance Testing", "Load Testing Basics"] },
  { week: 39, topics: ["Q3 Certification Final Prep", "Q3 Portfolio Review", "Q3 GitHub Optimization", "Q3 Review & Retrospective"] },
  
  // Quarter 4: AWS Foundations & Cloud Data
  { week: 40, topics: ["AWS Overview & Account Setup", "AWS Console Navigation", "AWS CLI Setup", "IAM Fundamentals"] },
  { week: 41, topics: ["S3 Fundamentals", "S3 Storage Classes", "S3 Lifecycle Policies", "S3 Security and Encryption"] },
  { week: 42, topics: ["EC2 Basics", "EC2 Instance Types", "VPC Fundamentals", "Security Groups and NACLs"] },
  { week: 43, topics: ["Lambda Introduction", "Lambda Function Patterns", "Lambda Triggers", "Lambda Best Practices"] },
  { week: 44, topics: ["AWS Glue Introduction", "Glue ETL Jobs", "Glue Crawlers", "Glue Data Catalog"] },
  { week: 45, topics: ["Athena Introduction", "Athena Query Patterns", "Athena Performance", "Athena + S3 Best Practices"] },
  { week: 46, topics: ["Redshift Introduction", "Redshift Architecture", "Redshift Loading Data", "Redshift Optimization"] },
  { week: 47, topics: ["AWS Cloud Practitioner Prep", "CLF Practice Exam 1", "CLF Practice Exam 2", "CLF Review & Exam"] },
  { week: 48, topics: ["Terraform Introduction", "Terraform HCL Basics", "Terraform State", "Terraform Modules"] },
  { week: 49, topics: ["Infrastructure as Code Patterns", "Terraform for AWS", "Terraform Best Practices", "IaC in Data Engineering"] },
  { week: 50, topics: ["ETL Generator: S3 Integration", "ETL Generator: Lambda Deploy", "ETL Generator: Glue Jobs", "Cloud Testing"] },
  { week: 51, topics: ["Cost Optimization", "AWS Cost Explorer", "Resource Tagging", "Cost Monitoring"] },
  { week: 52, topics: ["Q4 AWS Review", "Q4 Terraform Review", "Q4 Portfolio Update", "Q4 Review & Retrospective"] },
  
  // Quarter 5: Orchestration Deep Dive
  { week: 53, topics: ["Orchestration Concepts", "Airflow Introduction", "Airflow Architecture", "Airflow Installation"] },
  { week: 54, topics: ["DAGs Fundamentals", "Operators Overview", "BashOperator and PythonOperator", "Task Dependencies"] },
  { week: 55, topics: ["TaskFlow API", "XCom Communication", "Dynamic DAGs", "DAG Factory Patterns"] },
  { week: 56, topics: ["Sensors in Airflow", "Custom Operators", "Custom Sensors", "Hooks and Connections"] },
  { week: 57, topics: ["Airflow Variables", "Airflow Connections", "Secrets Backends", "Configuration Management"] },
  { week: 58, topics: ["SubDAGs and TaskGroups", "Branching Logic", "Conditional Execution", "Error Handling in DAGs"] },
  { week: 59, topics: ["Airflow Testing", "DAG Integrity Tests", "Unit Testing Tasks", "Integration Testing"] },
  { week: 60, topics: ["Airflow REST API", "Triggering DAGs", "Monitoring via API", "Airflow Plugins"] },
  { week: 61, topics: ["Dagster Introduction", "Assets vs Tasks", "Dagster vs Airflow", "Dagster Concepts"] },
  { week: 62, topics: ["Dagster Ops and Jobs", "Dagster Resources", "Dagster Schedules", "Dagster Sensors"] },
  { week: 63, topics: ["Production Orchestration", "Scaling Airflow", "MWAA (Managed Airflow)", "Monitoring and Alerting"] },
  { week: 64, topics: ["Orchestrated Pipeline Project", "Multi-DAG Architecture", "Cross-DAG Dependencies", "Pipeline Documentation"] },
  { week: 65, topics: ["Q5 Orchestration Review", "Q5 Best Practices", "Q5 Portfolio Update", "Q5 Review & Retrospective"] },
  
  // Quarter 6: AWS Advanced & Data Engineering
  { week: 66, topics: ["AWS Data Engineer Cert Overview", "Data Engineering on AWS", "Lake House Architecture", "Data Lakes vs Warehouses"] },
  { week: 67, topics: ["Advanced S3 Patterns", "S3 Event Notifications", "S3 Replication", "Cross-Account Access"] },
  { week: 68, topics: ["Kinesis Introduction", "Kinesis Streams", "Kinesis Firehose", "Real-time Processing"] },
  { week: 69, topics: ["EMR Introduction", "Spark on EMR", "EMR Serverless", "Big Data Processing Patterns"] },
  { week: 70, topics: ["Step Functions", "State Machine Design", "Step Functions + Lambda", "Orchestration Comparison"] },
  { week: 71, topics: ["EventBridge Introduction", "Event-Driven Architecture", "EventBridge Patterns", "Serverless Orchestration"] },
  { week: 72, topics: ["Secrets Manager", "Parameter Store", "Security Best Practices", "Compliance Basics"] },
  { week: 73, topics: ["AWS DEA Cert Prep Week 1", "DEA Practice Questions", "DEA Lab Practice", "DEA Review Session"] },
  { week: 74, topics: ["AWS DEA Cert Prep Week 2", "DEA Mock Exam 1", "DEA Mock Exam 2", "DEA Final Review"] },
  { week: 75, topics: ["Advanced Terraform", "Terraform Workspaces", "Remote State", "Terraform CI/CD"] },
  { week: 76, topics: ["Multi-Environment Deployments", "Blue-Green Deployments", "Canary Releases", "Feature Flags"] },
  { week: 77, topics: ["Cloud Native Pipeline", "Serverless Data Pipeline", "Cost-Optimized Architecture", "Performance Tuning"] },
  { week: 78, topics: ["Q6 Project Completion", "Q6 Architecture Review", "Q6 Portfolio Update", "Q6 Review & Retrospective"] },
  
  // Quarter 7: System Design & Governance
  { week: 79, topics: ["System Design Fundamentals", "Scalability Concepts", "Reliability Engineering", "CAP Theorem"] },
  { week: 80, topics: ["Data System Design", "Batch Processing Design", "Stream Processing Design", "Lambda Architecture"] },
  { week: 81, topics: ["Kappa Architecture", "Hybrid Architectures", "Trade-off Analysis", "Design Documentation"] },
  { week: 82, topics: ["C4 Model", "Architecture Decision Records", "Technical Writing", "Design Reviews"] },
  { week: 83, topics: ["Data Governance Intro", "Data Catalogs", "Metadata Management", "Data Lineage"] },
  { week: 84, topics: ["PII Handling", "Data Masking", "Anonymization vs Pseudonymization", "Privacy by Design"] },
  { week: 85, topics: ["Access Control", "RBAC vs ABAC", "Row/Column Level Security", "AWS Lake Formation"] },
  { week: 86, topics: ["Compliance Frameworks", "GDPR Basics", "CCPA Basics", "Audit Logging"] },
  { week: 87, topics: ["CloudTrail Deep Dive", "CloudWatch Monitoring", "Compliance Monitoring", "Security Automation"] },
  { week: 88, topics: ["Threat Modeling", "STRIDE Framework", "Security in Data Pipelines", "Incident Response"] },
  { week: 89, topics: ["System Design Practice 1", "System Design Practice 2", "Mock Design Interview", "Feedback Review"] },
  { week: 90, topics: ["Enterprise Platform Design", "Governance Implementation", "Documentation Polish", "Architecture Review"] },
  { week: 91, topics: ["Q7 Governance Project", "Q7 Documentation", "Q7 Portfolio Final", "Q7 Review & Retrospective"] },
  
  // Quarter 8: Interview Prep & Career Launch
  { week: 92, topics: ["Resume Optimization", "LinkedIn Profile Polish", "GitHub Portfolio Review", "Personal Branding"] },
  { week: 93, topics: ["Job Search Strategy", "Target Company Research", "Networking Strategies", "Application Tracking"] },
  { week: 94, topics: ["System Design Interview Prep 1", "Common DE Design Questions", "Designing Data Pipelines", "Practice Session"] },
  { week: 95, topics: ["System Design Interview Prep 2", "Designing Data Warehouses", "Designing Data Lakes", "Mock Interview"] },
  { week: 96, topics: ["Coding Interview Prep 1", "Python Algorithms", "SQL Interview Questions", "Practice Problems"] },
  { week: 97, topics: ["Coding Interview Prep 2", "Data Structures Review", "Time Complexity", "Mock Coding Interview"] },
  { week: 98, topics: ["Behavioral Interview Prep", "STAR Method", "Leadership Principles", "Story Library Building"] },
  { week: 99, topics: ["Mock Full Interview 1", "Feedback Review", "Improvement Areas", "Practice Refinement"] },
  { week: 100, topics: ["Mock Full Interview 2", "Technical Deep Dive", "Communication Practice", "Confidence Building"] },
  { week: 101, topics: ["Offer Negotiation Prep", "Compensation Research", "Negotiation Strategies", "Counter-Offer Tactics"] },
  { week: 102, topics: ["Active Job Search Week 1", "Application Submissions", "Recruiter Outreach", "Interview Scheduling"] },
  { week: 103, topics: ["Active Job Search Week 2", "Interview Execution", "Follow-up Strategy", "Pipeline Management"] },
  { week: 104, topics: ["Final Review", "Journey Retrospective", "Next Steps Planning", "Celebration & Launch!"] }
];

export const CERTIFICATIONS = [
  { name: "dbt Analytics Engineering", quarter: 3, targetDate: "2026-09-20" },
  { name: "AWS Cloud Practitioner", quarter: 4, targetDate: "2026-12-13" },
  { name: "AWS Data Engineer Associate", quarter: 6, targetDate: "2027-05-30" }
];

export const SKILL_BASELINE = {
  sql: { start: 3, target: 5 },
  python: { start: 1, target: 4 },
  cloud: { start: 1, target: 4 },
  orchestration: { start: 1, target: 4 },
  dbt: { start: 1, target: 4 }
};
