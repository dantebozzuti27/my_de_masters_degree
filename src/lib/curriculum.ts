// Curriculum data for the Aggressive 6-Month Data Engineer Transition Plan
// Goal: Land $160-170k Role by July 2026

import { Quarter, WeekTopics } from './types';

// Using 'Quarter' type for backward compatibility, but semantically these are MONTHS
export const QUARTERS: Quarter[] = [
  {
    id: 1,
    name: "Foundations + Production Skills",
    shortName: "Month 1: Foundation",
    weeks: [1, 5],  // Weeks 1-5 = Days 1-35
    startDate: "2026-02-01",
    endDate: "2026-02-28",
    goal: "Python fundamentals, production Python, Git/GitHub, AWS basics, Docker. Complete Project 1.",
    project: "Real-Time Stock Market Pipeline (AWS Lambda, S3, PostgreSQL, Airflow, Streamlit)"
  },
  {
    id: 2,
    name: "dbt Mastery + Project 2",
    shortName: "Month 2: dbt",
    weeks: [6, 9],  // Weeks 6-9 = Days 36-63
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
    weeks: [10, 13],  // Weeks 10-13 = Days 64-91
    startDate: "2026-04-01",
    endDate: "2026-04-30",
    goal: "Master Airflow orchestration, data quality with Great Expectations. Complete Project 3. START APPLYING.",
    project: "Multi-Source Financial Data Quality Platform (Airflow, Great Expectations, PostgreSQL)"
  },
  {
    id: 4,
    name: "AWS Certification + Applications",
    shortName: "Month 4: AWS Cert",
    weeks: [14, 17],  // Weeks 14-17 = Days 92-119
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
    weeks: [18, 21],  // Weeks 18-21 = Days 120-147
    startDate: "2026-06-01",
    endDate: "2026-06-30",
    goal: "System design practice, SQL interviews, Python challenges, behavioral prep. Heavy interviewing.",
    project: "Interview Practice Portfolio"
  },
  {
    id: 6,
    name: "Close Offers",
    shortName: "Month 6: Close",
    weeks: [22, 24],  // Weeks 22-24 = Days 148-168
    startDate: "2026-07-01",
    endDate: "2026-07-31",
    goal: "Final interviews, negotiate aggressively, close deal at $160-170k.",
    project: "Final Portfolio Polish"
  }
];

export const WEEKLY_CURRICULUM: WeekTopics[] = [
  // ============================================================================
  // WEEK 1: Python Foundations (Days 1-7) - COMPLETE
  // ============================================================================
  { week: 1, topics: [
    "Development Environment Setup",           // Day 1 - COMPLETE (Mon)
    "Python Variables & Syntax",               // Day 2 - COMPLETE (Tue)
    "Functions & Control Flow",                // Day 3 - COMPLETE (Wed)
    "Data Structures (Lists, Dicts)",          // Day 4 - COMPLETE (Thu)
    "List Comprehensions",                     // Day 5 - COMPLETE (Fri)
    "Dictionaries & JSON",                     // Day 6 - COMPLETE (Sat)
    "File I/O & Context Managers"              // Day 7 - COMPLETE (Sun)
  ]},
  
  // ============================================================================
  // WEEK 2: Error Handling + Production Python (Days 8-14)
  // ============================================================================
  { week: 2, topics: [
    "Error Handling & Defensive Code",         // Day 8 - Mon - COMPLETE
    "Python Classes & OOP for Production",     // Day 9 - Tue (2-2.5h hands-on)
    "Logging & Configuration Management",      // Day 10 - Wed
    "Git Fundamentals (branching, commits)",   // Day 11 - Thu
    "GitHub PRs & Professional Workflows",     // Day 12 - Fri
    "Week 2 Project: Build CLI Data Tool",     // Day 13 - Sat (6-7h project)
    "Review + Plan Week 3"                     // Day 14 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 3: Advanced Git + AWS Basics (Days 15-21)
  // ============================================================================
  { week: 3, topics: [
    "Advanced Git + Code Review Practice",     // Day 15 - Mon
    "AWS Account Setup (IAM, CLI)",            // Day 16 - Tue
    "S3 Fundamentals & Best Practices",        // Day 17 - Wed
    "Docker Fundamentals",                     // Day 18 - Thu
    "Docker for Data Engineering",             // Day 19 - Fri
    "Week 3 Project: Containerized Pipeline",  // Day 20 - Sat (6-7h project)
    "Review + Plan Week 4"                     // Day 21 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 4: Docker Compose + Project 1 Start (Days 22-28)
  // ============================================================================
  { week: 4, topics: [
    "Docker Compose + Local Dev Stack",        // Day 22 - Mon
    "Alpha Vantage API Integration",           // Day 23 - Tue
    "AWS Lambda Deployment",                   // Day 24 - Wed
    "S3 Storage + Data Partitioning",          // Day 25 - Thu
    "PostgreSQL Setup + Schema Design",        // Day 26 - Fri
    "Project 1 Deep Work Session",             // Day 27 - Sat (6-7h project)
    "Review + Debug Session"                   // Day 28 - Sun (3-4h)
  ]},
  
  // ============================================================================
  // WEEK 5: Project 1 Part 2 - Complete (Days 29-35)
  // ============================================================================
  { week: 5, topics: [
    "Data Transformation Pipeline",            // Day 29 - Mon
    "Airflow DAG Basics",                      // Day 30 - Tue
    "Connect Airflow to Lambda + S3",          // Day 31 - Wed
    "Streamlit Dashboard Basics",              // Day 32 - Thu
    "Dashboard Data Integration",              // Day 33 - Fri
    "Project 1 Polish + Documentation",        // Day 34 - Sat (6-7h)
    "Month 1 Review + Planning"                // Day 35 - Sun - MONTH 1 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 2: DBT MASTERY + PROJECT 2 (Weeks 6-9, Days 36-63)
  // ============================================================================
  
  // Week 6: dbt Fundamentals (Days 36-42)
  { week: 6, topics: [
    "dbt Fundamentals (models, refs)",         // Day 36 - Mon
    "dbt Materializations",                    // Day 37 - Tue
    "Staging → Intermediate → Marts",          // Day 38 - Wed
    "dbt Sources and Seeds",                   // Day 39 - Thu
    "dbt Practice: Transform Stock Data",      // Day 40 - Fri
    "dbt Deep Dive: Build Full Project",       // Day 41 - Sat (6-7h)
    "dbt Review + Testing Intro"               // Day 42 - Sun (3-4h)
  ]},
  
  // Week 7: dbt Testing & Macros (Days 43-49)
  { week: 7, topics: [
    "dbt Testing (schema + data tests)",       // Day 43 - Mon
    "Custom dbt Tests",                        // Day 44 - Tue
    "dbt Macros and Jinja",                    // Day 45 - Wed
    "dbt Packages + Documentation",            // Day 46 - Thu
    "dbt Advanced Patterns",                   // Day 47 - Fri
    "dbt Mastery Practice",                    // Day 48 - Sat (6-7h)
    "dbt Cert Prep Start"                      // Day 49 - Sun (3-4h)
  ]},
  
  // Week 8: Project 2 Part 1 - NBA Analytics (Days 50-56)
  { week: 8, topics: [
    "NBA API Data Ingestion",                  // Day 50 - Mon
    "Snowflake Setup",                         // Day 51 - Tue
    "dbt Staging Models for NBA",              // Day 52 - Wed
    "dbt Intermediate Models",                 // Day 53 - Thu
    "dbt Marts + Dimensional Modeling",        // Day 54 - Fri
    "Project 2 Deep Work",                     // Day 55 - Sat (6-7h)
    "Project 2 Testing"                        // Day 56 - Sun (3-4h)
  ]},
  
  // Week 9: Project 2 Complete + dbt Cert (Days 57-63)
  { week: 9, topics: [
    "dbt Test Coverage + Docs",                // Day 57 - Mon
    "Streamlit Dashboard for NBA",             // Day 58 - Tue
    "Dashboard Advanced Features",             // Day 59 - Wed
    "Project 2 Polish",                        // Day 60 - Thu
    "dbt Certification Final Prep",            // Day 61 - Fri
    "dbt Cert Exam Attempt",                   // Day 62 - Sat (exam day)
    "Month 2 Review"                           // Day 63 - Sun - MONTH 2 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 3: AIRFLOW + PROJECT 3 + START APPLYING (Weeks 10-13, Days 64-91)
  // ============================================================================
  
  // Week 10: Airflow Fundamentals (Days 64-70)
  { week: 10, topics: [
    "Airflow Architecture Deep Dive",          // Day 64 - Mon
    "DAG Design Patterns",                     // Day 65 - Tue
    "Operators and TaskFlow API",              // Day 66 - Wed
    "Task Dependencies + XComs",               // Day 67 - Thu
    "Airflow Connections + Hooks",             // Day 68 - Fri
    "Airflow Lab: Build Complex DAG",          // Day 69 - Sat (6-7h)
    "Airflow Testing Intro"                    // Day 70 - Sun (3-4h)
  ]},
  
  // Week 11: Airflow Production + Apply (Days 71-77)
  { week: 11, topics: [
    "Airflow Testing + Monitoring",            // Day 71 - Mon
    "Error Handling in DAGs",                  // Day 72 - Tue
    "Resume + LinkedIn Polish",                // Day 73 - Wed - START APPLYING
    "First 5 Applications",                    // Day 74 - Thu
    "More Applications + Airflow Practice",    // Day 75 - Fri
    "Application Sprint (10 apps)",            // Day 76 - Sat (apply + study)
    "Week Review + Application Tracking"       // Day 77 - Sun (3-4h)
  ]},
  
  // Week 12: Project 3 Part 1 - Financial Data Quality (Days 78-84)
  { week: 12, topics: [
    "Multi-Source Ingestion DAGs",             // Day 78 - Mon
    "Great Expectations Setup",                // Day 79 - Tue
    "Data Quality Framework",                  // Day 80 - Wed
    "Quality Checks Integration",              // Day 81 - Thu
    "Applications + Project Work",             // Day 82 - Fri
    "Project 3 Deep Work",                     // Day 83 - Sat (6-7h)
    "Project 3 Debug + Review"                 // Day 84 - Sun (3-4h)
  ]},
  
  // Week 13: Project 3 Part 2 - Complete (Days 85-91)
  { week: 13, topics: [
    "Monitoring + Alerting Setup",             // Day 85 - Mon
    "Final Polish + Deployment",               // Day 86 - Tue
    "Project 3 Documentation",                 // Day 87 - Wed
    "Applications (25+ total)",                // Day 88 - Thu
    "More Applications",                       // Day 89 - Fri
    "Application Sprint + Portfolio",          // Day 90 - Sat
    "Month 3 Review (30+ apps)"                // Day 91 - Sun - MONTH 3 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 4: AWS CERTIFICATION + HEAVY APPLICATIONS (Weeks 14-17, Days 92-119)
  // ============================================================================
  
  // Week 14: AWS SAA Prep - Compute & Storage (Days 92-98)
  { week: 14, topics: [
    "AWS SAA: S3 Deep Dive",                   // Day 92 - Mon
    "AWS SAA: EC2 + Lambda Advanced",          // Day 93 - Tue
    "AWS SAA: RDS + Redshift",                 // Day 94 - Wed
    "Applications (7/week pace)",              // Day 95 - Thu
    "AWS SAA: EBS + Storage",                  // Day 96 - Fri
    "AWS Lab Day + Applications",              // Day 97 - Sat (6-7h)
    "AWS Review + Flashcards"                  // Day 98 - Sun (3-4h)
  ]},
  
  // Week 15: AWS SAA Prep - Networking (Days 99-105)
  { week: 15, topics: [
    "AWS SAA: VPC + Networking",               // Day 99 - Mon
    "AWS SAA: IAM Deep Dive",                  // Day 100 - Tue
    "AWS SAA: Glue + Athena",                  // Day 101 - Wed
    "Applications + Interview Prep",           // Day 102 - Thu
    "AWS SAA: CloudWatch + Monitoring",        // Day 103 - Fri
    "AWS Practice Exam 1",                     // Day 104 - Sat
    "Review Weak Areas"                        // Day 105 - Sun (3-4h)
  ]},
  
  // Week 16: AWS SAA Final Prep (Days 106-112)
  { week: 16, topics: [
    "AWS SAA: Practice Exam 2",                // Day 106 - Mon
    "AWS SAA: Deep Dive Weak Areas",           // Day 107 - Tue
    "AWS SAA: Practice Exam 3",                // Day 108 - Wed
    "First Interviews This Week",              // Day 109 - Thu
    "AWS SAA: Final Review",                   // Day 110 - Fri
    "AWS SAA: TAKE EXAM",                      // Day 111 - Sat
    "Celebrate + Interview Prep"               // Day 112 - Sun
  ]},
  
  // Week 17: Interview Ramp Up (Days 113-119)
  { week: 17, topics: [
    "Interview Prep: SQL Deep Dive",           // Day 113 - Mon
    "Interview Prep: Python Challenges",       // Day 114 - Tue
    "Interview Prep: System Design Intro",     // Day 115 - Wed
    "Active Interviewing",                     // Day 116 - Thu
    "Interview Prep + Applications",           // Day 117 - Fri
    "Mock Interview Day",                      // Day 118 - Sat
    "Month 4 Review (5-10 interviews)"         // Day 119 - Sun - MONTH 4 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 5: INTERVIEW PREP + HEAVY INTERVIEWING (Weeks 18-21, Days 120-147)
  // ============================================================================
  
  // Week 18: System Design Practice (Days 120-126)
  { week: 18, topics: [
    "System Design: Data Pipelines",           // Day 120 - Mon
    "System Design: Data Warehouses",          // Day 121 - Tue
    "System Design: Streaming Systems",        // Day 122 - Wed
    "Active Interviewing",                     // Day 123 - Thu
    "System Design: Real-time Analytics",      // Day 124 - Fri
    "System Design Deep Practice",             // Day 125 - Sat (6-7h)
    "Interview Debrief + Prep"                 // Day 126 - Sun (3-4h)
  ]},
  
  // Week 19: Technical Interview Practice (Days 127-133)
  { week: 19, topics: [
    "SQL Interview: Window Functions",         // Day 127 - Mon
    "SQL Interview: CTEs + Subqueries",        // Day 128 - Tue
    "Python: Data Structures",                 // Day 129 - Wed
    "Active Interviewing",                     // Day 130 - Thu
    "Data Modeling Questions",                 // Day 131 - Fri
    "Full Mock Interview Day",                 // Day 132 - Sat
    "Interview Prep + Review"                  // Day 133 - Sun (3-4h)
  ]},
  
  // Week 20: Behavioral + Mock Interviews (Days 134-140)
  { week: 20, topics: [
    "Behavioral Prep (STAR Method)",           // Day 134 - Mon
    "Tell Me About Yourself",                  // Day 135 - Tue
    "Leadership + Conflict Questions",         // Day 136 - Wed
    "Active Interviewing",                     // Day 137 - Thu
    "Mock Interview 1",                        // Day 138 - Fri
    "Mock Interview 2 + Feedback",             // Day 139 - Sat
    "Refine Interview Answers"                 // Day 140 - Sun (3-4h)
  ]},
  
  // Week 21: Interview Refinement (Days 141-147)
  { week: 21, topics: [
    "Refine Your Story",                       // Day 141 - Mon
    "Technical Deep Dives",                    // Day 142 - Tue
    "Negotiation Research",                    // Day 143 - Wed
    "Active Interviewing",                     // Day 144 - Thu
    "Final Round Prep",                        // Day 145 - Fri
    "Practice Final Rounds",                   // Day 146 - Sat
    "Month 5 Review (multiple offers)"         // Day 147 - Sun - MONTH 5 COMPLETE
  ]},
  
  // ============================================================================
  // MONTH 6: CLOSE OFFERS (Weeks 22-24, Days 148-168)
  // ============================================================================
  
  // Week 22: Final Push (Days 148-154)
  { week: 22, topics: [
    "Final Round Prep",                        // Day 148 - Mon
    "Final Interviews",                        // Day 149 - Tue
    "Final Interviews",                        // Day 150 - Wed
    "Compare Offers",                          // Day 151 - Thu
    "Negotiation Strategy",                    // Day 152 - Fri
    "Negotiate Aggressively",                  // Day 153 - Sat
    "Review Offer Details"                     // Day 154 - Sun (3-4h)
  ]},
  
  // Week 23: Negotiate + Accept (Days 155-161)
  { week: 23, topics: [
    "Counter-Offer Calls",                     // Day 155 - Mon
    "Final Negotiations",                      // Day 156 - Tue
    "Accept Best Offer ($160-170k)",           // Day 157 - Wed
    "Give Notice",                             // Day 158 - Thu
    "Transition Planning",                     // Day 159 - Fri
    "Celebrate!",                              // Day 160 - Sat
    "Prep for New Role"                        // Day 161 - Sun (3-4h)
  ]},
  
  // Week 24: Launch (Days 162-168)
  { week: 24, topics: [
    "Knowledge Transfer at Current Job",       // Day 162 - Mon
    "Finish Strong at Current Job",            // Day 163 - Tue
    "Study New Company Stack",                 // Day 164 - Wed
    "Prep Day 1 Questions",                    // Day 165 - Thu
    "Last Day Current Job",                    // Day 166 - Fri
    "Rest + Celebrate",                        // Day 167 - Sat
    "NEW CHAPTER BEGINS!"                      // Day 168 - Sun - PROGRAM COMPLETE
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
