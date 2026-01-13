# SDE Tracker 🚀

**Your interactive companion for the 2-Year Senior Data Engineer Study Plan**

Track your progress through 416 study sessions designed to prepare you for $200k+ Senior Data Engineer roles.

![SDE Tracker Dashboard](https://img.shields.io/badge/Sessions-416-blue)
![Progress](https://img.shields.io/badge/Duration-2_Years-purple)
![Goal](https://img.shields.io/badge/Target-$200k+-green)

## Features

### 📊 Dashboard
- Today's session with full details and context
- Overall progress with visual indicators
- Current streak tracking
- Week-at-a-glance view
- Quarter progress overview

### 📅 Calendar
- Full calendar view of all 416 sessions
- Visual completion status
- Click any day to view session details
- Navigate between months

### 📚 Curriculum
- 8 quarters of structured learning
- 104 weeks broken down by topic
- Expandable week/quarter views
- Track completion at every level

### 📈 Statistics
- Skill progress tracking (SQL, Python, Cloud, Orchestration, dbt)
- Certification timeline and countdown
- Average session ratings
- Pace tracking (ahead/behind schedule)
- Time invested tracking

### ⚙️ Settings
- Export progress as JSON backup
- Import progress from backup
- Copy data to clipboard
- Reset progress (with confirmation)
- Quick links to learning resources

## Tech Stack

- **Framework:** Next.js 16 with App Router
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Icons:** Lucide React
- **Date Handling:** date-fns
- **State:** React Context + Local Storage

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sde-tracker.git
cd sde-tracker

# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
npm run build
npm start
```

## Deploy to Vercel

The easiest way to deploy this app is with [Vercel](https://vercel.com):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/sde-tracker)

Or deploy manually:

1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Import your GitHub repository
4. Click "Deploy"

That's it! Vercel will automatically detect Next.js and configure everything.

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

## Data Persistence

Your progress is stored in your browser's Local Storage. This means:

- ✅ Your data stays on your device
- ✅ No account needed
- ✅ Works offline
- ⚠️ Clearing browser data will erase progress
- 💡 Use the Export feature to backup your data!

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests

## License

MIT License - feel free to use this for your own learning journey!

---

Built with 💙 for the journey to $200k+
