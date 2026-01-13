'use client';

import { useState } from 'react';
import { 
  FolderOpen, 
  FileCode, 
  CheckCircle2, 
  ExternalLink,
  Github,
  Code,
  BookOpen,
  Trophy
} from 'lucide-react';
import Link from 'next/link';

// Workspace structure - will be dynamically populated
const WORKSPACE_STRUCTURE = {
  quarters: [
    {
      id: 'q1',
      name: 'Q1: Python & SQL Foundations',
      folder: 'q1-python-sql',
      weeks: 13,
      status: 'active',
      deliverables: [
        'Python exercises (50+)',
        'SQL window function queries',
        'ETL Generator v0 scaffolding'
      ]
    },
    {
      id: 'q2',
      name: 'Q2: ETL Patterns & Data Quality',
      folder: 'q2-etl-quality',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'ETL pipeline implementations',
        'Data quality framework',
        'dbt models'
      ]
    },
    {
      id: 'q3',
      name: 'Q3: dbt Mastery',
      folder: 'q3-dbt-mastery',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'Complete dbt project',
        'dbt Analytics Engineering Cert',
        'Testing framework'
      ]
    },
    {
      id: 'q4',
      name: 'Q4: AWS Foundations',
      folder: 'q4-aws-foundations',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'AWS Cloud Practitioner Cert',
        'Terraform configurations',
        'Cloud-deployed ETL'
      ]
    },
    {
      id: 'q5',
      name: 'Q5: Orchestration',
      folder: 'q5-orchestration',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'Airflow DAGs',
        'Dagster pipelines',
        'Orchestrated data platform'
      ]
    },
    {
      id: 'q6',
      name: 'Q6: AWS Advanced',
      folder: 'q6-aws-advanced',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'AWS Data Engineer Cert',
        'Serverless data pipelines',
        'Cloud-native platform'
      ]
    },
    {
      id: 'q7',
      name: 'Q7: System Design',
      folder: 'q7-system-design',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'System design documents',
        'Architecture diagrams',
        'Governance framework'
      ]
    },
    {
      id: 'q8',
      name: 'Q8: Interview Prep',
      folder: 'q8-interview-prep',
      weeks: 13,
      status: 'upcoming',
      deliverables: [
        'Resume & portfolio',
        'Mock interviews',
        '$200k+ offer'
      ]
    }
  ]
};

export default function PortfolioPage() {
  const [selectedQuarter, setSelectedQuarter] = useState('q1');

  const quarter = WORKSPACE_STRUCTURE.quarters.find(q => q.id === selectedQuarter);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
          <Trophy className="w-8 h-8 text-yellow-500" />
          My Portfolio
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          Your completed work lives in <code className="bg-gray-100 dark:bg-gray-800 px-2 py-1 rounded">workspace/</code>
        </p>
      </div>

      {/* GitHub Link */}
      <a
        href="https://github.com/dantebozzuti27/my_de_masters_degree"
        target="_blank"
        rel="noopener noreferrer"
        className="flex items-center gap-3 p-4 bg-gray-900 dark:bg-gray-800 text-white rounded-xl mb-8 hover:bg-gray-800 dark:hover:bg-gray-700 transition-colors"
      >
        <Github className="w-8 h-8" />
        <div className="flex-1">
          <p className="font-semibold">View on GitHub</p>
          <p className="text-sm text-gray-400">dantebozzuti27/my_de_masters_degree</p>
        </div>
        <ExternalLink className="w-5 h-5" />
      </a>

      {/* Workspace Overview */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden mb-8">
        <div className="p-6 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
            <FolderOpen className="w-6 h-6 text-blue-500" />
            Workspace Structure
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mt-1">
            All your code, exercises, and projects are organized here
          </p>
        </div>

        <div className="p-6">
          <div className="font-mono text-sm bg-gray-50 dark:bg-gray-900 rounded-lg p-4 overflow-x-auto">
            <pre className="text-gray-700 dark:text-gray-300">{`workspace/
├── q1-python-sql/           # ← You are here
│   ├── week-01/
│   │   ├── exercises/
│   │   │   ├── day1_verify_setup.py
│   │   │   ├── day2_variables.py
│   │   │   ├── day3_functions.py
│   │   │   └── day4_data_structures.py
│   │   ├── notes.md
│   │   └── README.md
│   ├── week-02/
│   │   └── exercises/
│   └── ... (weeks 3-13)
├── q2-etl-quality/
├── q3-dbt-mastery/
├── q4-aws-foundations/
├── q5-orchestration/
├── q6-aws-advanced/
├── q7-system-design/
├── q8-interview-prep/
└── projects/
    └── etl-generator/       # Your side project`}</pre>
          </div>
        </div>
      </div>

      {/* Quarter Tabs */}
      <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
        {WORKSPACE_STRUCTURE.quarters.map(q => (
          <button
            key={q.id}
            onClick={() => setSelectedQuarter(q.id)}
            className={`px-4 py-2 rounded-lg font-medium whitespace-nowrap transition-colors ${
              selectedQuarter === q.id
                ? 'bg-blue-600 text-white'
                : q.status === 'active'
                ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 hover:bg-blue-200 dark:hover:bg-blue-800'
                : 'bg-gray-100 text-gray-500 dark:bg-gray-800 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-700'
            }`}
          >
            {q.id.toUpperCase()}
          </button>
        ))}
      </div>

      {/* Selected Quarter Detail */}
      {quarter && (
        <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden">
          <div className={`p-6 border-b border-gray-200 dark:border-gray-700 ${
            quarter.status === 'active' 
              ? 'bg-blue-50 dark:bg-blue-900/20' 
              : 'bg-gray-50 dark:bg-gray-900'
          }`}>
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                  {quarter.name}
                </h3>
                <p className="text-gray-600 dark:text-gray-400 mt-1">
                  {quarter.weeks} weeks • Folder: <code className="bg-gray-200 dark:bg-gray-700 px-2 py-0.5 rounded">{quarter.folder}/</code>
                </p>
              </div>
              {quarter.status === 'active' && (
                <span className="px-3 py-1 bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300 rounded-full text-sm font-medium">
                  In Progress
                </span>
              )}
            </div>
          </div>

          <div className="p-6">
            <h4 className="font-semibold text-gray-900 dark:text-white mb-3">
              Key Deliverables
            </h4>
            <ul className="space-y-2">
              {quarter.deliverables.map((item, i) => (
                <li key={i} className="flex items-center gap-3 text-gray-700 dark:text-gray-300">
                  <CheckCircle2 className="w-5 h-5 text-gray-300 dark:text-gray-600" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* How to Use Instructions */}
      <div className="mt-8 bg-gradient-to-r from-purple-600 to-blue-600 rounded-xl p-6 text-white">
        <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
          <Code className="w-6 h-6" />
          How Your Work Shows Up Here
        </h3>
        
        <div className="grid md:grid-cols-3 gap-4">
          <div className="bg-white/10 rounded-lg p-4">
            <p className="font-semibold mb-2">1. Do the Work</p>
            <p className="text-sm text-blue-100">
              Complete exercises in <code className="bg-white/20 px-1 rounded">workspace/</code> folders
            </p>
          </div>
          <div className="bg-white/10 rounded-lg p-4">
            <p className="font-semibold mb-2">2. Commit & Push</p>
            <p className="text-sm text-blue-100">
              <code className="bg-white/20 px-1 rounded">git add . && git commit && git push</code>
            </p>
          </div>
          <div className="bg-white/10 rounded-lg p-4">
            <p className="font-semibold mb-2">3. Auto-Deploy</p>
            <p className="text-sm text-blue-100">
              Vercel rebuilds automatically. Your work is live!
            </p>
          </div>
        </div>
      </div>

      {/* Quick Start for Today */}
      <div className="mt-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-green-500" />
          Quick Start for Today
        </h3>
        
        <div className="font-mono text-sm bg-gray-900 text-gray-100 rounded-lg p-4 overflow-x-auto">
          <pre>{`# Navigate to your workspace
cd /Users/dantebozzuti/cursor/Projects/Business/SDE_PATH/sde-tracker/workspace

# Go to this week's folder
cd q1-python-sql/week-01/exercises

# Open VS Code
code .

# Complete the exercise
# Then commit your work:
git add .
git commit -m "Complete Day 1 exercises"
git push`}</pre>
        </div>
      </div>
    </div>
  );
}
