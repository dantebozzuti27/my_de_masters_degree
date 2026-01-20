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
  // WEEK 1: Python Foundations (Days 1-8) - COMPLETE
  // Special 8-day bootcamp week
  // ============================================================================
  { week: 1, topics: [
    "Development Environment Setup",           // Day 1 - COMPLETE (Mon)
    "Python Variables & Syntax",               // Day 2 - COMPLETE (Tue)
    "Functions & Control Flow",                // Day 3 - COMPLETE (Wed)
    "Data Structures (Lists, Dicts)",          // Day 4 - COMPLETE (Thu)
    "List Comprehensions",                     // Day 5 - COMPLETE (Fri)
    "Dictionaries & JSON",                     // Day 6 - COMPLETE (Sat)
    "File I/O & Context Managers"              // Day 7 - COMPLETE (Sun)
    // Day 8 was bonus: Error Handling - also COMPLETE
  ]},
  
  // ============================================================================
  // WEEK 2: Production Python + Git (Days 9-15)
  // ============================================================================
  { week: 2, topics: [
    "Python Classes & OOP for Production",     // Day 9 - Mon (2-2.5h hands-on)
    "Logging & Configuration Management",      // Day 10 - Tue
    "Git Fundamentals (branching, commits)",   // Day 11 - Wed
    "GitHub PRs & Professional Workflows",     // Day 12 - Thu
    "Advanced Git + Code Review Practice",     // Day 13 - Fri
    "Week 2 Project: Build CLI Data Tool",     // Day 14 - Sat (6-7h project)
    "Review + Plan Week 3"                     // Day 15 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 3: AWS + Docker Basics (Days 16-22)
  // ============================================================================
  { week: 3, topics: [
    "AWS Account Setup (IAM, CLI)",            // Day 16 - Mon
    "S3 Fundamentals & Best Practices",        // Day 17 - Tue
    "Docker Fundamentals",                     // Day 18 - Wed
    "Docker for Data Engineering",             // Day 19 - Thu
    "Docker Compose + Local Dev Stack",        // Day 20 - Fri
    "Week 3 Project: Containerized Pipeline",  // Day 21 - Sat (6-7h project)
    "Review + Plan Week 4"                     // Day 22 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 4: Project 1 Part 1 - Stock Pipeline (Days 23-29)
  // ============================================================================
  { week: 4, topics: [
    "Alpha Vantage API Integration",           // Day 23 - Mon
    "AWS Lambda Deployment",                   // Day 24 - Tue
    "S3 Storage + Data Partitioning",          // Day 25 - Wed
    "PostgreSQL Setup + Schema Design",        // Day 26 - Thu
    "Data Transformation Pipeline",            // Day 27 - Fri
    "Project 1 Deep Work Session",             // Day 28 - Sat (6-7h project)
    "Review + Debug Session"                   // Day 29 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 5: Project 1 Part 2 - Complete (Days 30-36)
  // ============================================================================
  { week: 5, topics: [
    "Airflow DAG Basics",                      // Day 30 - Mon
    "Connect Airflow to Lambda + S3",          // Day 31 - Tue
    "Streamlit Dashboard Basics",              // Day 32 - Wed
    "Dashboard Data Integration",              // Day 33 - Thu
    "Project 1 Testing + Debugging",           // Day 34 - Fri
    "Project 1 Polish + Documentation",        // Day 35 - Sat (6-7h)
    "Month 1 Review + Planning"                // Day 36 - Sun - MONTH 1 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 2: DBT MASTERY + PROJECT 2 (Weeks 6-9)
  // ============================================================================
  
  // Week 6: dbt Fundamentals (Days 37-43)
  { week: 6, topics: [
    "dbt Fundamentals (models, refs)",         // Day 37 - Mon
    "dbt Materializations",                    // Day 38 - Tue
    "Staging → Intermediate → Marts",          // Day 39 - Wed
    "dbt Sources and Seeds",                   // Day 40 - Thu
    "dbt Practice: Transform Stock Data",      // Day 41 - Fri
    "dbt Deep Dive: Build Full Project",       // Day 42 - Sat (6-7h)
    "dbt Review + Testing Intro"               // Day 43 - Sun (3-4h)
  ]},
  
  // Week 7: dbt Testing & Macros (Days 44-50)
  { week: 7, topics: [
    "dbt Testing (schema + data tests)",       // Day 44 - Mon
    "Custom dbt Tests",                        // Day 45 - Tue
    "dbt Macros and Jinja",                    // Day 46 - Wed
    "dbt Packages + Documentation",            // Day 47 - Thu
    "dbt Advanced Patterns",                   // Day 48 - Fri
    "dbt Mastery Practice",                    // Day 49 - Sat (6-7h)
    "dbt Cert Prep Start"                      // Day 50 - Sun (3-4h)
  ]},
  
  // Week 8: Project 2 Part 1 - NBA Analytics (Days 51-57)
  { week: 8, topics: [
    "NBA API Data Ingestion",                  // Day 51 - Mon
    "Snowflake Setup",                         // Day 52 - Tue
    "dbt Staging Models for NBA",              // Day 53 - Wed
    "dbt Intermediate Models",                 // Day 54 - Thu
    "dbt Marts + Dimensional Modeling",        // Day 55 - Fri
    "Project 2 Deep Work",                     // Day 56 - Sat (6-7h)
    "Project 2 Testing"                        // Day 57 - Sun (3-4h)
  ]},
  
  // Week 9: Project 2 Part 2 - Complete (Days 58-64)
  { week: 9, topics: [
    "dbt Test Coverage + Docs",                // Day 58 - Mon
    "Streamlit Dashboard for NBA",             // Day 59 - Tue
    "Dashboard Advanced Features",             // Day 60 - Wed
    "Project 2 Polish",                        // Day 61 - Thu
    "dbt Certification Final Prep",            // Day 62 - Fri
    "dbt Cert Exam Attempt",                   // Day 63 - Sat (exam day)
    "Month 2 Review"                           // Day 64 - Sun - MONTH 2 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 3: AIRFLOW + PROJECT 3 + START APPLYING (Weeks 10-13)
  // ============================================================================
  
  // Week 10: Airflow Fundamentals (Days 65-71)
  { week: 10, topics: [
    "Airflow Architecture Deep Dive",          // Day 65 - Mon
    "DAG Design Patterns",                     // Day 66 - Tue
    "Operators and TaskFlow API",              // Day 67 - Wed
    "Task Dependencies + XComs",               // Day 68 - Thu
    "Airflow Connections + Hooks",             // Day 69 - Fri
    "Airflow Lab: Build Complex DAG",          // Day 70 - Sat (6-7h)
    "Airflow Testing Intro"                    // Day 71 - Sun (3-4h)
  ]},
  
  // Week 11: Airflow Production + Apply (Days 72-78)
  { week: 11, topics: [
    "Airflow Testing + Monitoring",            // Day 72 - Mon
    "Error Handling in DAGs",                  // Day 73 - Tue
    "Resume + LinkedIn Polish",                // Day 74 - Wed - START APPLYING
    "First 5 Applications",                    // Day 75 - Thu
    "More Applications + Airflow Practice",    // Day 76 - Fri
    "Application Sprint (10 apps)",            // Day 77 - Sat (apply + study)
    "Week Review + Application Tracking"       // Day 78 - Sun (3-4h)
  ]},
  
  // Week 12: Project 3 Part 1 - Financial Data Quality (Days 79-85)
  { week: 12, topics: [
    "Multi-Source Ingestion DAGs",             // Day 79 - Mon
    "Great Expectations Setup",                // Day 80 - Tue
    "Data Quality Framework",                  // Day 81 - Wed
    "Quality Checks Integration",              // Day 82 - Thu
    "Applications + Project Work",             // Day 83 - Fri
    "Project 3 Deep Work",                     // Day 84 - Sat (6-7h)
    "Project 3 Debug + Review"                 // Day 85 - Sun (3-4h)
  ]},
  
  // Week 13: Project 3 Part 2 - Complete (Days 86-92)
  { week: 13, topics: [
    "Monitoring + Alerting Setup",             // Day 86 - Mon
    "Final Polish + Deployment",               // Day 87 - Tue
    "Project 3 Documentation",                 // Day 88 - Wed
    "Applications (25+ total)",                // Day 89 - Thu
    "More Applications",                       // Day 90 - Fri
    "Application Sprint + Portfolio",          // Day 91 - Sat
    "Month 3 Review (30+ apps)"                // Day 92 - Sun - MONTH 3 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 4: AWS CERTIFICATION + HEAVY APPLICATIONS (Weeks 14-17)
  // ============================================================================
  
  // Week 14: AWS SAA Prep - Compute & Storage (Days 93-99)
  { week: 14, topics: [
    "AWS SAA: S3 Deep Dive",                   // Day 93 - Mon
    "AWS SAA: EC2 + Lambda Advanced",          // Day 94 - Tue
    "AWS SAA: RDS + Redshift",                 // Day 95 - Wed
    "Applications (7/week pace)",              // Day 96 - Thu
    "AWS SAA: EBS + Storage",                  // Day 97 - Fri
    "AWS Lab Day + Applications",              // Day 98 - Sat (6-7h)
    "AWS Review + Flashcards"                  // Day 99 - Sun (3-4h)
  ]},
  
  // Week 15: AWS SAA Prep - Networking (Days 100-106)
  { week: 15, topics: [
    "AWS SAA: VPC + Networking",               // Day 100 - Mon
    "AWS SAA: IAM Deep Dive",                  // Day 101 - Tue
    "AWS SAA: Glue + Athena",                  // Day 102 - Wed
    "Applications + Interview Prep",           // Day 103 - Thu
    "AWS SAA: CloudWatch + Monitoring",        // Day 104 - Fri
    "AWS Practice Exam 1",                     // Day 105 - Sat
    "Review Weak Areas"                        // Day 106 - Sun (3-4h)
  ]},
  
  // Week 16: AWS SAA Final Prep (Days 107-113)
  { week: 16, topics: [
    "AWS SAA: Practice Exam 2",                // Day 107 - Mon
    "AWS SAA: Deep Dive Weak Areas",           // Day 108 - Tue
    "AWS SAA: Practice Exam 3",                // Day 109 - Wed
    "First Interviews This Week",              // Day 110 - Thu
    "AWS SAA: Final Review",                   // Day 111 - Fri
    "AWS SAA: TAKE EXAM",                      // Day 112 - Sat
    "Celebrate + Interview Prep"               // Day 113 - Sun
  ]},
  
  // Week 17: Interview Ramp Up (Days 114-120)
  { week: 17, topics: [
    "Interview Prep: SQL Deep Dive",           // Day 114 - Mon
    "Interview Prep: Python Challenges",       // Day 115 - Tue
    "Interview Prep: System Design Intro",     // Day 116 - Wed
    "Active Interviewing",                     // Day 117 - Thu
    "Interview Prep + Applications",           // Day 118 - Fri
    "Mock Interview Day",                      // Day 119 - Sat
    "Month 4 Review (5-10 interviews)"         // Day 120 - Sun - MONTH 4 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 5: INTERVIEW PREP + HEAVY INTERVIEWING (Weeks 18-21)
  // ============================================================================
  
  // Week 18: System Design Practice (Days 121-127)
  { week: 18, topics: [
    "System Design: Data Pipelines",           // Day 121 - Mon
    "System Design: Data Warehouses",          // Day 122 - Tue
    "System Design: Streaming Systems",        // Day 123 - Wed
    "Active Interviewing",                     // Day 124 - Thu
    "System Design: Real-time Analytics",      // Day 125 - Fri
    "System Design Deep Practice",             // Day 126 - Sat (6-7h)
    "Interview Debrief + Prep"                 // Day 127 - Sun (3-4h)
  ]},
  
  // Week 19: Technical Interview Practice (Days 128-134)
  { week: 19, topics: [
    "SQL Interview: Window Functions",         // Day 128 - Mon
    "SQL Interview: CTEs + Subqueries",        // Day 129 - Tue
    "Python: Data Structures",                 // Day 130 - Wed
    "Active Interviewing",                     // Day 131 - Thu
    "Data Modeling Questions",                 // Day 132 - Fri
    "Full Mock Interview Day",                 // Day 133 - Sat
    "Interview Prep + Review"                  // Day 134 - Sun (3-4h)
  ]},
  
  // Week 20: Behavioral + Mock Interviews (Days 135-141)
  { week: 20, topics: [
    "Behavioral Prep (STAR Method)",           // Day 135 - Mon
    "Tell Me About Yourself",                  // Day 136 - Tue
    "Leadership + Conflict Questions",         // Day 137 - Wed
    "Active Interviewing",                     // Day 138 - Thu
    "Mock Interview 1",                        // Day 139 - Fri
    "Mock Interview 2 + Feedback",             // Day 140 - Sat
    "Refine Interview Answers"                 // Day 141 - Sun (3-4h)
  ]},
  
  // Week 21: Interview Refinement (Days 142-148)
  { week: 21, topics: [
    "Refine Your Story",                       // Day 142 - Mon
    "Technical Deep Dives",                    // Day 143 - Tue
    "Negotiation Research",                    // Day 144 - Wed
    "Active Interviewing",                     // Day 145 - Thu
    "Final Round Prep",                        // Day 146 - Fri
    "Practice Final Rounds",                   // Day 147 - Sat
    "Month 5 Review (multiple offers)"         // Day 148 - Sun - MONTH 5 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 6: CLOSE OFFERS (Weeks 22-24)
  // ============================================================================
  
  // Week 22: Final Push (Days 149-155)
  { week: 22, topics: [
    "Final Round Prep",                        // Day 149 - Mon
    "Final Interviews",                        // Day 150 - Tue
    "Final Interviews",                        // Day 151 - Wed
    "Compare Offers",                          // Day 152 - Thu
    "Negotiation Strategy",                    // Day 153 - Fri
    "Negotiate Aggressively",                  // Day 154 - Sat
    "Review Offer Details"                     // Day 155 - Sun (3-4h)
  ]},
  
  // Week 23: Negotiate + Accept (Days 156-162)
  { week: 23, topics: [
    "Counter-Offer Calls",                     // Day 156 - Mon
    "Final Negotiations",                      // Day 157 - Tue
    "Accept Best Offer ($160-170k)",           // Day 158 - Wed
    "Give Notice",                             // Day 159 - Thu
    "Transition Planning",                     // Day 160 - Fri
    "Celebrate!",                              // Day 161 - Sat
    "Prep for New Role"                        // Day 162 - Sun (3-4h)
  ]},
  
  // Week 24: Launch (Days 163-169)
  { week: 24, topics: [
    "Knowledge Transfer at Current Job",       // Day 163 - Mon
    "Finish Strong at Current Job",            // Day 164 - Tue
    "Study New Company Stack",                 // Day 165 - Wed
    "Prep Day 1 Questions",                    // Day 166 - Thu
    "Last Day Current Job",                    // Day 167 - Fri
    "Rest + Celebrate",                        // Day 168 - Sat
    "NEW CHAPTER BEGINS!"                      // Day 169 - Sun - PROGRAM COMPLETE
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
