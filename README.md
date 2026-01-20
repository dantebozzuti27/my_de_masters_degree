# SDE Tracker 🚀

**Your interactive companion for the 2-Year Senior Data Engineer Study Plan**

Track your progress through 416 study sessions designed to prepare you for $200k+ Senior Data Engineer roles.

![SDE Tracker Dashboard](https://img.shields.io/badge/Sessions-416-blue)
![Progress](https://img.shields.io/badge/Duration-2_Years-purple)
![Goal](https://img.shields.io/badge/Target-$200k+-green)

## Current Progress

| Day | Topic | Status |
|-----|-------|--------|
| 1 | Development Environment + AI Tools | ✅ Complete |
| 2 | Python Variables & Data Types | ✅ Complete |
| 3 | Control Flow & Functions | ✅ Complete |
| 4 | Data Structures | ✅ Complete |
| 5 | Python Comprehensions | ✅ Complete |
| 6 | Dictionaries & JSON | ✅ Complete |
| 7 | File I/O & Context Managers | ✅ Complete |
| 8 | Error Handling & Defensive Code | 🔄 Next Up |

**Week 2, Day 3 of 104 weeks**

## Features

### 📊 Dashboard
- Next incomplete session with full details
- Overall progress with visual indicators
- Week-at-a-glance view
- Quarter progress overview

### 💻 Verified Progress (Portfolio)
- **Your code IS your progress** — no manual checkboxes
- Complete exercises in the `workspace/` folder
- Build-time scanner verifies completion
- Your solutions become your portfolio

### 📅 Calendar
- Full calendar view of all 416 sessions
- Visual completion status
- Click any day to view session details
- Navigate between months

### 📚 Curriculum
- 8 quarters of structured learning
- 104 weeks broken down by topic
- Expandable week/quarter views
- AI-enhanced lessons with practical exercises

### 📈 Statistics
- Skill progress tracking (SQL, Python, Cloud, Orchestration, dbt)
- Certification timeline and countdown
- Verified completion rates

## Workspace Structure

```
workspace/
├── q1-python-sql/
│   ├── week-01/
│   │   └── exercises/
│   │       ├── day1_verify_setup.py
│   │       ├── day2_variables.py
│   │       ├── day3_functions.py
│   │       └── day4_data_structures.py
│   ├── week-02/
│   │   └── exercises/
│   │       ├── day5_comprehensions.py
│   │       ├── day6_dicts_json.py
│   │       ├── day7_file_io.py
│   │       └── day8_error_handling.py
│   └── week-03/
│       └── exercises/
│           ├── day9_advanced_functions.py
│           ├── day10_functional.py
│           ├── day11_modules.py
│           └── day12_utility_library.py
```

Each exercise file includes:
- Docstrings explaining the concept
- Multiple functions to implement
- Built-in test suite (`python3 dayX_*.py`)

## Tech Stack

- **Framework:** Next.js 16 with App Router
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Icons:** Lucide React
- **Date Handling:** date-fns
- **Progress Verification:** Build-time workspace scanner

## Getting Started

### Prerequisites

- Node.js 18+ 
- Python 3.11+
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/dantebozzuti27/my_de_masters_degree.git
cd my_de_masters_degree/sde-tracker

# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Running Exercises

```bash
# Navigate to an exercise
cd workspace/q1-python-sql/week-02/exercises

# Run the exercise tests
python3 day7_file_io.py
```

### Build for Production

```bash
npm run build  # Also scans workspace for verified progress
npm start
```

## Study Plan Overview

| Quarter | Focus | Certification |
|---------|-------|---------------|
| Q1 (Jan-Apr 2026) | Python & SQL Foundations | — |
| Q2 (Apr-Jun 2026) | ETL Patterns & Data Quality | — |
| Q3 (Jul-Sep 2026) | dbt Mastery | **dbt Analytics Engineering** |
| Q4 (Sep-Dec 2026) | AWS Foundations | **AWS Cloud Practitioner** |
| Q5 (Dec-Mar 2027) | Orchestration (Airflow/Dagster) | — |
| Q6 (Mar-Jun 2027) | AWS Advanced | **AWS Data Engineer Associate** |
| Q7 (Jun-Aug 2027) | System Design & Governance | — |
| Q8 (Aug-Jan 2028) | Interview Prep & Career Launch | 🎯 **$200k+ Role** |

## How Progress Works

1. **Complete exercises** in the `workspace/` folder
2. **Run tests** to verify: `python3 dayX_*.py`
3. **Commit your code** to the repo
4. **Build triggers scanner** that verifies completion
5. **Dashboard updates** to show verified progress

No manual tracking needed — your code speaks for itself.

## Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/dantebozzuti27/my_de_masters_degree)

Or deploy manually:

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your GitHub repository
4. Click "Deploy"

## License

MIT License - feel free to use this for your own learning journey!

---

Built with 💙 for the journey to $200k+
