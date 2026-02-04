'use client';

import { useState } from 'react';
import { useProgress } from '@/hooks/useProgress';
import { QUARTERS } from '@/lib/curriculum';
import { 
  FolderOpen, 
  FileCode, 
  CheckCircle2, 
  ExternalLink,
  Github,
  Code,
  BookOpen,
  Trophy,
  Clock
} from 'lucide-react';

export default function PortfolioPage() {
  const { completedIds, verifiedStats } = useProgress();
  const [selectedMonth, setSelectedMonth] = useState(1);

  const month = QUARTERS.find(q => q.id === selectedMonth);

  // Calculate progress per month
  const monthProgress = QUARTERS.map(m => {
    // Simplified: assume ~28 days per month for progress tracking
    const daysPerMonth = 28;
    const startDay = (m.id - 1) * daysPerMonth + 1;
    const endDay = m.id * daysPerMonth;
    
    let completed = 0;
    for (let d = startDay; d <= endDay; d++) {
      if (completedIds.has(`session-${d}`)) completed++;
    }
    
    return {
      ...m,
      completed,
      total: daysPerMonth,
      percentage: Math.round((completed / daysPerMonth) * 100)
    };
  });

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white flex items-center gap-3">
          <Trophy className="w-8 h-8 text-yellow-500" />
          My Portfolio
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          6-Month Aggressive Plan • Target: Data Engineer by July 2026
        </p>
      </div>

      {/* Verified Progress */}
      <div className="bg-gradient-to-r from-green-600 to-emerald-600 rounded-xl p-6 text-white mb-8">
        <div className="flex items-center gap-3 mb-4">
          <CheckCircle2 className="w-6 h-6" />
          <h2 className="text-xl font-bold">Verified Progress</h2>
        </div>
        <div className="grid grid-cols-3 gap-6">
          <div>
            <p className="text-3xl font-bold">{verifiedStats.completed}</p>
            <p className="text-green-100 text-sm">Days Complete</p>
          </div>
          <div>
            <p className="text-3xl font-bold">169</p>
            <p className="text-green-100 text-sm">Total Days</p>
          </div>
          <div>
            <p className="text-3xl font-bold">{Math.round((verifiedStats.completed / 169) * 100)}%</p>
            <p className="text-green-100 text-sm">Overall Progress</p>
          </div>
        </div>
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

      {/* Month Tabs */}
      <div className="flex gap-2 mb-6 overflow-x-auto pb-2">
        {monthProgress.map(m => (
          <button
            key={m.id}
            onClick={() => setSelectedMonth(m.id)}
            className={`px-4 py-2 rounded-lg font-medium whitespace-nowrap transition-colors relative ${
              selectedMonth === m.id
                ? 'bg-blue-600 text-white'
                : m.percentage > 0
                ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 hover:bg-blue-200 dark:hover:bg-blue-800'
                : 'bg-gray-100 text-gray-500 dark:bg-gray-800 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-700'
            }`}
          >
            Month {m.id}
            {m.percentage > 0 && m.percentage < 100 && (
              <span className="ml-2 text-xs opacity-75">({m.percentage}%)</span>
            )}
            {m.percentage === 100 && (
              <CheckCircle2 className="inline-block ml-1 w-4 h-4" />
            )}
          </button>
        ))}
      </div>

      {/* Selected Month Detail */}
      {month && (
        <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden mb-8">
          <div className={`p-6 border-b border-gray-200 dark:border-gray-700 ${
            monthProgress.find(m => m.id === month.id)?.percentage! > 0
              ? 'bg-blue-50 dark:bg-blue-900/20' 
              : 'bg-gray-50 dark:bg-gray-900'
          }`}>
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-xl font-bold text-gray-900 dark:text-white">
                  {month.name}
                </h3>
                <p className="text-gray-600 dark:text-gray-400 mt-1">
                  Weeks {month.weeks[0]}-{month.weeks[1]} • {month.goal}
                </p>
              </div>
              {month.certification && (
                <span className="px-3 py-1 bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300 rounded-full text-sm font-medium">
                  🎓 {month.certification}
                </span>
              )}
            </div>
          </div>

          <div className="p-6">
            <h4 className="font-semibold text-gray-900 dark:text-white mb-3">
              Key Project
            </h4>
            <div className="flex items-center gap-3 text-gray-700 dark:text-gray-300 mb-6">
              <Code className="w-5 h-5 text-blue-500" />
              {month.project}
            </div>

            <h4 className="font-semibold text-gray-900 dark:text-white mb-3">
              Weekly Schedule
            </h4>
            <div className="grid grid-cols-7 gap-2 text-center text-sm">
              {['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].map((day, i) => (
                <div key={day} className="p-2 bg-gray-50 dark:bg-gray-900 rounded">
                  <p className="font-medium text-gray-900 dark:text-white">{day}</p>
                  <p className="text-xs text-gray-500 dark:text-gray-400">
                    {i < 5 ? '2-2.5h' : i === 5 ? '6-7h' : '3-4h'}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* Workspace Structure */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden mb-8">
        <div className="p-6 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
            <FolderOpen className="w-6 h-6 text-blue-500" />
            Workspace Structure
          </h2>
        </div>

        <div className="p-6">
          <div className="font-mono text-sm bg-gray-50 dark:bg-gray-900 rounded-lg p-4 overflow-x-auto">
            <pre className="text-gray-700 dark:text-gray-300">{`workspace/
├── month1-foundations/          # ← Current
│   ├── week-01/                 # Days 1-8 (COMPLETE)
│   ├── week-02/                 # Days 9-15
│   │   └── exercises/
│   │       ├── day9_classes_oop.py
│   │       ├── day10_logging_config.py
│   │       ├── day11_git_fundamentals.py
│   │       └── ...
│   ├── week-03/                 # Days 16-22
│   ├── week-04/                 # Days 23-29
│   └── week-05/                 # Days 30-36
├── month2-dbt-analytics/        # Weeks 6-9
├── month3-airflow-orchestration/ # Weeks 10-13
├── month4-aws-certification/    # Weeks 14-17
├── month5-interview-prep/       # Weeks 18-21
├── month6-close-offers/         # Weeks 22-24
└── projects/
    ├── project1-stock-pipeline/
    ├── project2-nba-analytics/
    └── project3-data-quality/`}</pre>
          </div>
        </div>
      </div>

      {/* How to Use */}
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-xl p-6 text-white">
        <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
          <BookOpen className="w-6 h-6" />
          Daily Schedule
        </h3>
        
        <div className="grid md:grid-cols-3 gap-4">
          <div className="bg-white/10 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Clock className="w-4 h-4" />
              <p className="font-semibold">Weekdays (Mon-Fri)</p>
            </div>
            <p className="text-sm text-blue-100">
              2-2.5h hands-on coding<br/>
              + 1-1.5h audiobooks/podcasts during commute
            </p>
          </div>
          <div className="bg-white/10 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <Code className="w-4 h-4" />
              <p className="font-semibold">Saturday</p>
            </div>
            <p className="text-sm text-blue-100">
              6-7h deep project work<br/>
              Build, debug, deploy
            </p>
          </div>
          <div className="bg-white/10 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <BookOpen className="w-4 h-4" />
              <p className="font-semibold">Sunday</p>
            </div>
            <p className="text-sm text-blue-100">
              3-4h light learning<br/>
              Review, plan, prep
            </p>
          </div>
        </div>
        
        <p className="text-center text-blue-100 mt-4 text-sm">
          27-30 hours/week total • Sustainable maximum intensity
        </p>
      </div>
    </div>
  );
}
