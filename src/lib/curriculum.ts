// Curriculum data derived from workspace-manifest.json
// Single source of truth: data/curriculum.json + data/progress.json

import manifestData from './workspace-manifest.json';
import { Quarter, WeekTopics } from './types';

interface ManifestMonth {
  name: string;
  weeks: {
    [key: string]: {
      title: string;
      days: { day: number; topic: string; complete: boolean }[];
    };
  };
}

interface Manifest {
  generatedAt: string;
  meta: {
    title: string;
    goal: string;
    hoursPerWeek: number;
    totalDays: number;
    startDate: string;
  };
  summary: {
    totalDays: number;
    completedDays: number;
    completionRate: number;
  };
  months: { [key: string]: ManifestMonth };
  dayStatus: {
    [key: string]: {
      complete: boolean;
      topic: string;
      month: number;
      week: number;
    };
  };
}

const manifest = manifestData as Manifest;

// Month date ranges
const MONTH_DATES: { [key: number]: { start: string; end: string } } = {
  1: { start: '2026-02-01', end: '2026-02-28' },
  2: { start: '2026-03-01', end: '2026-03-31' },
  3: { start: '2026-04-01', end: '2026-04-30' },
  4: { start: '2026-05-01', end: '2026-05-31' },
  5: { start: '2026-06-01', end: '2026-06-30' },
  6: { start: '2026-07-01', end: '2026-07-31' }
};

// Month goals and projects
const MONTH_INFO: { [key: number]: { goal: string; project: string; certification?: string } } = {
  1: {
    goal: 'Python fundamentals, production Python, Git/GitHub, AWS basics, Docker. Complete Project 1.',
    project: 'Credit Markets Pipeline (AWS Lambda, S3, PostgreSQL, Airflow, Streamlit)'
  },
  2: {
    goal: 'Deep dbt expertise, analytics engineering patterns, Snowflake. Complete Project 2.',
    project: 'MLB Analytics Platform (Snowflake, dbt, Streamlit)',
    certification: 'dbt Analytics Engineering'
  },
  3: {
    goal: 'Master Airflow orchestration, data quality with Great Expectations. Complete Project 3. START APPLYING.',
    project: 'Data Quality Platform (Airflow, Great Expectations, PostgreSQL)'
  },
  4: {
    goal: 'AWS Solutions Architect Associate certification. 25-30 applications submitted.',
    project: 'AWS Certification Labs',
    certification: 'AWS Solutions Architect Associate'
  },
  5: {
    goal: 'System design practice, SQL interviews, Python challenges, behavioral prep. Heavy interviewing.',
    project: 'Interview Practice Portfolio'
  },
  6: {
    goal: 'Final interviews, negotiate aggressively, close deal at $160-170k.',
    project: 'Final Portfolio Polish'
  }
};

// Build QUARTERS (months) from manifest
export const QUARTERS: Quarter[] = Object.entries(manifest.months).map(([id, month]) => {
  const monthNum = parseInt(id);
  const weekNums = Object.keys(month.weeks).map(Number).sort((a, b) => a - b);
  const info = MONTH_INFO[monthNum] || { goal: '', project: '' };
  const dates = MONTH_DATES[monthNum] || { start: '', end: '' };

  return {
    id: monthNum,
    name: month.name,
    shortName: `Month ${monthNum}: ${month.name}`,
    weeks: [weekNums[0], weekNums[weekNums.length - 1]] as [number, number],
    startDate: dates.start,
    endDate: dates.end,
    goal: info.goal,
    project: info.project,
    certification: info.certification
  };
});

// Build WEEKLY_CURRICULUM from manifest
export const WEEKLY_CURRICULUM: WeekTopics[] = [];

for (const [monthId, month] of Object.entries(manifest.months)) {
  for (const [weekNum, week] of Object.entries(month.weeks)) {
    const topics = week.days.map(d => d.topic);
    // Ensure we have exactly 7 topics
    while (topics.length < 7) topics.push('');
    
    WEEKLY_CURRICULUM.push({
      week: parseInt(weekNum),
      topics: topics.slice(0, 7) as [string, string, string, string, string, string, string]
    });
  }
}

// Sort by week number
WEEKLY_CURRICULUM.sort((a, b) => a.week - b.week);

// Get completion stats for a week
export function getWeekProgress(weekNum: number): { completed: number; total: number } {
  for (const month of Object.values(manifest.months)) {
    const week = month.weeks[weekNum];
    if (week) {
      const completed = week.days.filter(d => d.complete).length;
      return { completed, total: week.days.length };
    }
  }
  return { completed: 0, total: 7 };
}

// Get completion stats for a month
export function getMonthProgress(monthNum: number): { completed: number; total: number } {
  const month = manifest.months[monthNum];
  if (!month) return { completed: 0, total: 0 };

  let completed = 0;
  let total = 0;

  for (const week of Object.values(month.weeks)) {
    for (const day of week.days) {
      total++;
      if (day.complete) completed++;
    }
  }

  return { completed, total };
}

// Check if a day is complete
export function isDayComplete(dayNum: number): boolean {
  return manifest.dayStatus[dayNum]?.complete ?? false;
}

// Get overall progress
export function getOverallProgress(): { completed: number; total: number; percentage: number } {
  return {
    completed: manifest.summary.completedDays,
    total: manifest.summary.totalDays,
    percentage: manifest.summary.completionRate
  };
}

// Legacy exports for backward compatibility
export const CERTIFICATIONS = [
  { name: 'dbt Analytics Engineering', quarter: 2, targetDate: '2026-03-31' },
  { name: 'AWS Solutions Architect Associate', quarter: 4, targetDate: '2026-05-31' }
];

export const TARGET_COMPANIES = {
  tier1: [
    { name: 'dbt Labs', role: 'Analytics Engineer', salary: '$140-170k' },
    { name: 'Ramp', role: 'Analytics Engineer / DE', salary: '$150-180k' },
    { name: 'Brex', role: 'Data Engineer', salary: '$150-170k' }
  ],
  tier2: [
    { name: 'Datadog', role: 'Data Engineer', salary: '$150-180k' },
    { name: 'Plaid', role: 'Data Engineer', salary: '$160-180k' },
    { name: 'Affirm', role: 'Analytics Engineer', salary: '$150-170k' }
  ],
  tier3: [
    { name: 'Stripe', role: 'Data Engineer', salary: '$170-200k' },
    { name: 'Capital One', role: 'Data Engineer', salary: '$140-160k' },
    { name: 'Two Sigma', role: 'Data Infrastructure', salary: '$160-200k' },
    { name: 'Robinhood', role: 'Data Engineer', salary: '$150-180k' }
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
