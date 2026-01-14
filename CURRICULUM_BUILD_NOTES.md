# Curriculum Build Notes

This document contains notes for building the remaining quarters (Q2-Q8) of the AI-enhanced Data Engineering curriculum.

## Completed

### Q1: Python & SQL Mastery (Weeks 1-13, Days 1-52) ✅
- All 52 days complete with AI-enhanced approach
- Each lesson includes:
  - `aiIntegration` field with `toolsUsed`, `focusArea`, `aiTip`, `warningWhenNotToUseAI`
  - `futureProofNote` explaining why the skill matters despite AI
  - Session plans with specific activities
  - Exercises with AI approach guidance
  - Key terms, common mistakes, and success criteria

## Remaining Quarters

### Q2: Cloud Fundamentals & Infrastructure (Weeks 14-26, Days 53-104)

**Focus Areas:**
- AWS Core Services (S3, EC2, IAM, VPC)
- Infrastructure as Code (Terraform basics)
- Docker fundamentals
- Cloud data services (RDS, Redshift intro)

**AI Integration Approach:**
- **Weeks 14-17 (AWS Basics):** Focus on "learn-with-ai" - AI is excellent at explaining cloud concepts and generating CLI commands
- **Weeks 18-20 (Docker):** Focus on "debug-ai-code" - AI generates Dockerfiles but often with subtle issues
- **Weeks 21-23 (Terraform):** Focus on "prompt-engineering" - Describe infrastructure in plain English, get IaC
- **Weeks 24-26 (Integration):** Focus on "ai-review" - Have AI review your cloud architecture

**Key Future-Proof Notes to Include:**
- Cloud architecture decisions require business context AI lacks
- Security configurations should never be blindly copied from AI
- Cost optimization requires understanding actual usage patterns
- Understanding cloud fundamentals helps you debug AI-suggested solutions

**Sample Lesson Topics:**
- Day 53: AWS Account Setup & IAM Fundamentals
- Day 54: S3 Deep Dive - Storage Classes, Lifecycle Policies
- Day 55: AWS CLI & Boto3 Introduction
- Day 56: S3 Data Lake Patterns
- Day 57: EC2 Basics & SSH Access
- Day 58: VPC Fundamentals
- Day 59: Security Groups & Network ACLs
- Day 60: RDS Setup & Management
... (continue through Day 104)

---

### Q3: Orchestration & Workflow Automation (Weeks 27-39, Days 105-156)

**Focus Areas:**
- Apache Airflow fundamentals
- DAG design patterns
- Dagster introduction (modern alternative)
- Workflow monitoring and alerting

**AI Integration Approach:**
- **Weeks 27-30 (Airflow Basics):** Focus on "learn-with-ai" - AI explains operators and concepts well
- **Weeks 31-33 (DAG Patterns):** Focus on "debug-ai-code" - AI generates DAGs with subtle dependency issues
- **Weeks 34-36 (Dagster):** Focus on "learn-with-ai" - Less training data, so explain concepts carefully
- **Weeks 37-39 (Production Patterns):** Focus on "manual-practice" - Production patterns need deep understanding

**Key Future-Proof Notes to Include:**
- Understanding task dependencies is critical - AI often gets them wrong
- Idempotency patterns require business logic understanding
- Debugging failed DAGs requires reading logs and understanding state
- Orchestration is about reliability - AI can't test for edge cases you'll hit in production

**Sample Lesson Topics:**
- Day 105: Airflow Architecture & Concepts
- Day 106: Your First DAG
- Day 107: Operators Deep Dive
- Day 108: XComs & Task Communication
... (continue through Day 156)

---

### Q4: dbt & Modern Data Stack (Weeks 40-52, Days 157-208)

**Focus Areas:**
- dbt Core fundamentals
- SQL transformations at scale
- Testing & documentation
- dbt Cloud / orchestration integration

**AI Integration Approach:**
- **Weeks 40-43 (dbt Basics):** Focus on "learn-with-ai" - AI is excellent at dbt model generation
- **Weeks 44-47 (Advanced dbt):** Focus on "ai-review" - Have AI review your models for best practices
- **Weeks 48-50 (Testing):** Focus on "prompt-engineering" - Describe data quality rules, get tests
- **Weeks 51-52 (Integration):** Focus on "manual-practice" - End-to-end understanding required

**Key Future-Proof Notes to Include:**
- dbt is increasingly AI-enhanced (dbt Assist) - learn the fundamentals
- Data modeling decisions require business understanding
- Testing strategy requires knowing what can go wrong
- Documentation is for humans - make it valuable

**Sample Lesson Topics:**
- Day 157: dbt Philosophy & Setup
- Day 158: Your First dbt Model
- Day 159: ref() & source() Functions
- Day 160: Incremental Models
... (continue through Day 208)

---

### Q5: System Design & Architecture (Weeks 53-65, Days 209-260)

**Focus Areas:**
- Data platform architecture patterns
- Batch vs streaming trade-offs
- Data lake vs data warehouse
- Scalability & performance

**AI Integration Approach:**
- **All weeks:** Primarily "learn-with-ai" and "ai-review"
- System design is about trade-offs - use AI to explore options
- AI is excellent at explaining distributed systems concepts
- Always verify AI suggestions against your specific requirements

**Key Future-Proof Notes to Include:**
- System design is THE senior skill - requires judgment AI can't replicate
- Trade-offs depend on business context AI doesn't have
- Architecture decisions have long-term consequences
- Understanding "why" is more important than "how"

---

### Q6: Data Quality & Governance (Weeks 66-78, Days 261-312)

**Focus Areas:**
- Data quality frameworks (Great Expectations, etc.)
- Data lineage & cataloging
- Privacy & compliance (GDPR, etc.)
- Metadata management

**AI Integration Approach:**
- Mix of all focus areas
- Quality rules require business understanding
- Compliance requires human judgment
- AI can help implement, but rules come from requirements

**Key Future-Proof Notes to Include:**
- Data quality is a competitive advantage
- Governance decisions are organizational, not technical
- Compliance mistakes are expensive - verify AI suggestions
- Data trust is earned through consistent quality

---

### Q7: Advanced Topics & Specialization (Weeks 79-91, Days 313-364)

**Focus Areas:**
- Streaming (Kafka, Spark Streaming)
- ML Platform basics
- Real-time analytics
- Choose-your-specialization weeks

**AI Integration Approach:**
- Advanced topics benefit from AI explanation
- Streaming has complex debugging - practice manually
- ML platform work is increasingly AI-assisted

**Key Future-Proof Notes to Include:**
- Specialization makes you valuable
- Deep expertise beats broad shallow knowledge
- Pick areas where AI augments, not replaces

---

### Q8: Interview Prep & Career Launch (Weeks 92-104, Days 365-416)

**Focus Areas:**
- System design interviews
- Coding interviews (Python, SQL)
- Behavioral preparation
- Portfolio presentation

**AI Integration Approach:**
- Use AI for practice problems
- Get AI feedback on solutions
- But do mock interviews with humans
- AI can't simulate interview pressure

**Key Future-Proof Notes to Include:**
- Interviewers test understanding, not memorization
- Explaining your thought process matters most
- Your portfolio shows what you can actually build
- Soft skills differentiate candidates

---

## Lesson Template

Use this template for all future lessons:

```typescript
{
  dayNumber: X,
  week: Y,
  topic: "Topic Name",
  subtitle: "Compelling one-liner about the topic",

  objectives: [
    "Specific, measurable objective 1",
    "Specific, measurable objective 2",
    "Specific, measurable objective 3",
    "Specific, measurable objective 4"
  ],

  aiIntegration: {
    toolsUsed: ['copilot' | 'chatgpt' | 'claude' | 'cursor' | 'none'],
    focusArea: 'learn-with-ai' | 'debug-ai-code' | 'prompt-engineering' | 'ai-review' | 'manual-practice',
    aiTip: "Specific advice on how AI helps with this topic",
    warningWhenNotToUseAI: "When to be careful with AI for this topic"
  },

  sessionPlan: [
    { time: "0:00-0:15", activity: "Activity description", type: "video" | "learn" | "practice" | "exercise" | "review" },
    // ... more activities to fill 90 minutes
  ],

  resources: {
    required: [
      { title: "Resource name", url: "URL", type: "video" | "article" | "docs" | "tutorial" | "interactive", duration: "X min" }
    ],
    optional: [
      { title: "Resource name", url: "URL", type: "type" }
    ]
  },

  exercises: [
    {
      title: "Exercise Name",
      description: "What to build",
      hints: ["Hint 1", "Hint 2", "Hint 3"],
      aiApproach: "How to use AI effectively for this exercise",
      deliverable: "filename.ext with description"
    }
  ],

  successCriteria: [
    "Criterion 1",
    "Criterion 2",
    "Criterion 3"
  ],

  // Optional fields as needed:
  prerequisites: ["Day X - Topic"],
  
  keyTerms: [
    { term: "Term", definition: "Definition" }
  ],
  
  commonMistakes: [
    { mistake: "Common mistake", fix: "How to fix it" }
  ],

  // Required for Day 4 of each week:
  weeklyCheckpoint: {
    title: "Week X: Topic Area",
    description: "Summary of what was learned",
    deliverables: ["Item 1", "Item 2"],
    selfAssessment: ["Question 1?", "Question 2?"]
  },

  futureProofNote: "Why this skill matters despite AI advances"
}
```

## Focus Area Guidelines

### learn-with-ai
Use when the topic is conceptual and AI explains well:
- Cloud concepts
- Framework introductions
- System design concepts

### debug-ai-code
Use when AI typically generates buggy code:
- Complex configurations (Docker, Terraform)
- DAG dependencies
- Pagination logic

### prompt-engineering
Use when describing the problem gets good results:
- Data transformations
- SQL queries
- Documentation generation

### ai-review
Use when you should code first, then get feedback:
- Architecture designs
- Code quality
- Documentation

### manual-practice
Use when fundamentals must be internalized:
- Basic SQL aggregations
- Core Python patterns
- Debugging skills

## Resource Guidelines

- Prefer YouTube videos from established educators (Corey Schafer, freeCodeCamp, etc.)
- Include direct links to specific videos, not playlists
- Official documentation for reference
- Interactive tutorials when available (SQLBolt, etc.)
- Podcasts: Data Engineering Podcast, Software Engineering Daily (data episodes)
- Audiobooks: Designing Data-Intensive Applications, The Pragmatic Programmer

## Exercise Guidelines

- Every exercise should produce a deliverable file
- Files should be testable (the scan-workspace.js script looks for completion markers)
- Include enough context that the exercise is completable in the session
- AI approach should be specific, not generic

## Building the Remaining Quarters

When building Q2-Q8:
1. Follow the template above exactly
2. Ensure `aiIntegration` is thoughtful and specific
3. Include `futureProofNote` on every lesson
4. Resources should be verified and working
5. Exercises should map to workspace folder structure:
   - `workspace/q2-cloud/week-14/exercises/`
   - `workspace/q3-orchestration/week-27/exercises/`
   - etc.
