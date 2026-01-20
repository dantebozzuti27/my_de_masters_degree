// Curriculum data for the Aggressive 6-Month Data Engineer Transition Plan
// Goal: Land $160-170k Role by July 2026

import { Quarter, WeekTopics } from './types';

// Using 'Quarter' type for backward compatibility, but semantically these are MONTHS
export const QUARTERS: Quarter[] = [
  {
    id: 1,
    name: "Foundations + Production Skills",
    shortName: "Month 1: Foundation",
    weeks: [1, 6],
    startDate: "2026-01-12",
    endDate: "2026-02-28",
    goal: "Python fundamentals (Days 1-8 COMPLETE), then production Python, Git/GitHub, AWS basics, Docker. Complete Project 1.",
    project: "Real-Time Stock Market Pipeline (AWS Lambda, S3, PostgreSQL, Airflow, Streamlit)"
  },
  {
    id: 2,
    name: "dbt Mastery + Project 2",
    shortName: "Month 2: dbt",
    weeks: [7, 10],
    startDate: "2026-03-01",
    endDate: "2026-03-31",
    goal: "Deep dbt expertise, analytics engineering patterns, Snowflake. Complete Project 2: NBA Analytics Platform.",
    project: "NBA Analytics Platform (Snowflake, dbt, Streamlit)",
    certification: "dbt Analytics Engineering"
  },
  {
    id: 3,
    name: "Airflow + Project 3 + Apply",
    shortName: "Month 3: Airflow",
    weeks: [11, 14],
    startDate: "2026-04-01",
    endDate: "2026-04-30",
    goal: "Master Airflow orchestration, data quality with Great Expectations. Complete Project 3. START APPLYING.",
    project: "Multi-Source Financial Data Quality Platform (Airflow, Great Expectations, PostgreSQL)"
  },
  {
    id: 4,
    name: "AWS Certification + Applications",
    shortName: "Month 4: AWS Cert",
    weeks: [15, 18],
    startDate: "2026-05-01",
    endDate: "2026-05-31",
    goal: "AWS Solutions Architect Associate certification. 25-30 applications submitted. Start getting interviews.",
    project: "AWS Certification Labs",
    certification: "AWS Solutions Architect Associate"
  },
  {
    id: 5,
    name: "Interview Prep + Interviewing",
    shortName: "Month 5: Interviews",
    weeks: [19, 22],
    startDate: "2026-06-01",
    endDate: "2026-06-30",
    goal: "System design practice, SQL interviews, Python challenges, behavioral prep. Heavy interviewing.",
    project: "Interview Practice Portfolio"
  },
  {
    id: 6,
    name: "Close Offers",
    shortName: "Month 6: Close",
    weeks: [23, 24],
    startDate: "2026-07-01",
    endDate: "2026-07-31",
    goal: "Final interviews, negotiate aggressively, close deal at $160-170k.",
    project: "Final Portfolio Polish"
  }
];

export const WEEKLY_CURRICULUM: WeekTopics[] = [
  // ============================================================================
  // FOUNDATION (Already Complete - Days 1-8)
  // ============================================================================
  
  // Week 1: Python Foundations Part 1 (COMPLETE)
  { week: 1, topics: [
    "Development Environment Setup",           // Day 1 - COMPLETE
    "Python Variables & Syntax",               // Day 2 - COMPLETE  
    "Functions & Control Flow",                // Day 3 - COMPLETE
    "Data Structures (Lists, Dicts)"           // Day 4 - COMPLETE
  ]},
  
  // Week 2: Python Foundations Part 2 (COMPLETE)
  { week: 2, topics: [
    "List Comprehensions",                     // Day 5 - COMPLETE
    "Dictionaries & JSON",                     // Day 6 - COMPLETE
    "File I/O & Context Managers",             // Day 7 - COMPLETE
    "Error Handling & Defensive Code"          // Day 8 - COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 1: Production Skills + Project 1 (Weeks 3-6)
  // ============================================================================
  
  // Week 3: Production Python + Git
  { week: 3, topics: [
    "Python Classes & OOP for Production",     // Day 9
    "Logging & Configuration Management",      // Day 10
    "Git Fundamentals (branching, commits)",   // Day 11
    "GitHub PRs & Professional Workflows"      // Day 12
  ]},
  
  // Week 4: AWS + Docker Basics
  { week: 4, topics: [
    "AWS Account Setup (IAM, CLI)",            // Day 13
    "S3 Fundamentals & Best Practices",        // Day 14
    "Docker Fundamentals",                     // Day 15
    "Docker for Data Engineering"              // Day 16
  ]},
  
  // Week 5: Project 1 - Real-Time Stock Pipeline (Part 1)
  { week: 5, topics: [
    "Alpha Vantage API Integration",           // Day 17
    "AWS Lambda Deployment",                   // Day 18
    "S3 Storage + Data Partitioning",          // Day 19
    "PostgreSQL Setup + Schema Design"         // Day 20
  ]},
  
  // Week 6: Project 1 - Real-Time Stock Pipeline (Part 2)
  { week: 6, topics: [
    "Data Transformation Pipeline",            // Day 21
    "Airflow DAG Basics",                      // Day 22
    "Streamlit Dashboard",                     // Day 23
    "Project 1 Polish + Documentation"         // Day 24 - MONTH 1 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 2: DBT MASTERY + PROJECT 2 (Weeks 7-10)
  // ============================================================================
  
  // Week 7: dbt Fundamentals
  { week: 7, topics: [
    "dbt Fundamentals (models, refs)",         // Day 25
    "dbt Materializations",                    // Day 26
    "Staging → Intermediate → Marts",          // Day 27
    "dbt Sources and Seeds"                    // Day 28
  ]},
  
  // Week 8: dbt Testing & Macros
  { week: 8, topics: [
    "dbt Testing (schema + data tests)",       // Day 29
    "Custom dbt Tests",                        // Day 30
    "dbt Macros and Jinja",                    // Day 31
    "dbt Packages + Documentation"             // Day 32
  ]},
  
  // Week 9: Project 2 - NBA Analytics Platform (Part 1)
  { week: 9, topics: [
    "NBA API Data Ingestion",                  // Day 33
    "Snowflake Setup",                         // Day 34
    "dbt Staging Models",                      // Day 35
    "dbt Intermediate Models"                  // Day 36
  ]},
  
  // Week 10: Project 2 - NBA Analytics Platform (Part 2)
  { week: 10, topics: [
    "dbt Marts + Dimensional Modeling",        // Day 37
    "dbt Test Coverage + Docs",                // Day 38
    "Streamlit Dashboard",                     // Day 39
    "dbt Cert Prep + Project Polish"           // Day 40 - MONTH 2 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 3: AIRFLOW + PROJECT 3 + START APPLYING (Weeks 11-14)
  // ============================================================================
  
  // Week 11: Airflow Fundamentals
  { week: 11, topics: [
    "Airflow Architecture Deep Dive",          // Day 41
    "DAG Design Patterns",                     // Day 42
    "Operators and TaskFlow API",              // Day 43
    "Task Dependencies + XComs"                // Day 44
  ]},
  
  // Week 12: Airflow Production + Start Applying
  { week: 12, topics: [
    "Airflow Testing + Monitoring",            // Day 45
    "Error Handling in DAGs",                  // Day 46
    "Resume + LinkedIn Polish",                // Day 47 - START APPLYING
    "First 10 Applications Submitted"          // Day 48
  ]},
  
  // Week 13: Project 3 - Financial Data Quality (Part 1)
  { week: 13, topics: [
    "Multi-Source Ingestion DAGs",             // Day 49
    "Great Expectations Setup",                // Day 50
    "Data Quality Framework",                  // Day 51
    "Applications: Keep Applying"              // Day 52
  ]},
  
  // Week 14: Project 3 - Financial Data Quality (Part 2)
  { week: 14, topics: [
    "Monitoring + Alerting",                   // Day 53
    "Final Polish + Deployment",               // Day 54
    "Project 3 Documentation",                 // Day 55
    "30+ Applications Submitted"               // Day 56 - MONTH 3 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 4: AWS CERTIFICATION + HEAVY APPLICATIONS (Weeks 15-18)
  // ============================================================================
  
  // Week 15: AWS SAA Prep - Compute & Storage
  { week: 15, topics: [
    "AWS SAA: S3 Deep Dive",                   // Day 57
    "AWS SAA: EC2 + Lambda Advanced",          // Day 58
    "AWS SAA: RDS + Redshift",                 // Day 59
    "Continue Applications (7/week)"           // Day 60
  ]},
  
  // Week 16: AWS SAA Prep - Networking & Security
  { week: 16, topics: [
    "AWS SAA: VPC + Networking",               // Day 61
    "AWS SAA: IAM Deep Dive",                  // Day 62
    "AWS SAA: Glue + Athena",                  // Day 63
    "Continue Applications (7/week)"           // Day 64
  ]},
  
  // Week 17: AWS SAA Prep - Practice Exams
  { week: 17, topics: [
    "AWS SAA: Practice Exam 1",                // Day 65
    "AWS SAA: Review Weak Areas",              // Day 66
    "AWS SAA: Practice Exam 2",                // Day 67
    "First Interviews Scheduled"               // Day 68
  ]},
  
  // Week 18: AWS Certification Week
  { week: 18, topics: [
    "AWS SAA: Final Review",                   // Day 69
    "AWS SAA: TAKE EXAM",                      // Day 70
    "Interview Prep Begins",                   // Day 71
    "5-10 Interviews Scheduled"                // Day 72 - MONTH 4 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 5: INTERVIEW PREP + HEAVY INTERVIEWING (Weeks 19-22)
  // ============================================================================
  
  // Week 19: System Design Practice
  { week: 19, topics: [
    "System Design: Data Pipelines",           // Day 73
    "System Design: Data Warehouses",          // Day 74
    "System Design: Streaming Systems",        // Day 75
    "Continue Interviewing"                    // Day 76
  ]},
  
  // Week 20: Technical Interview Practice
  { week: 20, topics: [
    "SQL Interview Questions",                 // Day 77
    "Python Coding Challenges",                // Day 78
    "Data Modeling Questions",                 // Day 79
    "Continue Interviewing"                    // Day 80
  ]},
  
  // Week 21: Behavioral + Mock Interviews
  { week: 21, topics: [
    "Behavioral Prep (STAR Method)",           // Day 81
    "Mock Interview 1",                        // Day 82
    "Mock Interview 2",                        // Day 83
    "Continue Interviewing"                    // Day 84
  ]},
  
  // Week 22: Interview Refinement
  { week: 22, topics: [
    "Refine Your Story",                       // Day 85
    "Technical Deep Dives",                    // Day 86
    "Negotiation Prep",                        // Day 87
    "Multiple Offers in Play"                  // Day 88 - MONTH 5 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 6: CLOSE OFFERS (Weeks 23-24)
  // ============================================================================
  
  // Week 23: Final Push
  { week: 23, topics: [
    "Final Round Prep",                        // Day 89
    "Final Interviews",                        // Day 90
    "Compare Offers",                          // Day 91
    "Negotiate Aggressively"                   // Day 92
  ]},
  
  // Week 24: Launch
  { week: 24, topics: [
    "Accept Offer ($160-170k)",                // Day 93
    "Give Notice",                             // Day 94
    "Prep for New Role",                       // Day 95
    "NEW CHAPTER BEGINS!"                      // Day 96 - PROGRAM COMPLETE
  ]}
];

export const CERTIFICATIONS = [
  { name: "dbt Analytics Engineering", quarter: 2, targetDate: "2026-03-31" },
  { name: "AWS Solutions Architect Associate", quarter: 4, targetDate: "2026-05-31" }
];

export const TARGET_COMPANIES = {
  tier1: [
    { name: "dbt Labs", role: "Analytics Engineer", salary: "$140-170k" },
    { name: "Ramp", role: "Analytics Engineer / DE", salary: "$150-180k" },
    { name: "Brex", role: "Data Engineer", salary: "$150-170k" }
  ],
  tier2: [
    { name: "Datadog", role: "Data Engineer", salary: "$150-180k" },
    { name: "Plaid", role: "Data Engineer", salary: "$160-180k" },
    { name: "Affirm", role: "Analytics Engineer", salary: "$150-170k" }
  ],
  tier3: [
    { name: "Stripe", role: "Data Engineer", salary: "$170-200k" },
    { name: "Capital One", role: "Data Engineer", salary: "$140-160k" },
    { name: "Two Sigma", role: "Data Infrastructure", salary: "$160-200k" },
    { name: "Robinhood", role: "Data Engineer", salary: "$150-180k" }
  ]
};

export const SKILL_BASELINE = {
  python: { start: 2, target: 4 },
  sql: { start: 3, target: 5 },
  dbt: { start: 0, target: 4 },
  airflow: { start: 0, target: 3 },
  aws: { start: 1, target: 4 },
  systemDesign: { start: 1, target: 3 }
};
