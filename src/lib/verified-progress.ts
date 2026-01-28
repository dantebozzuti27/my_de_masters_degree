// Verified Progress - Based on data/progress.json
// This reads from workspace-manifest.json which is generated at build time

import manifestData from './workspace-manifest.json';

export interface DayStatus {
  complete: boolean;
  topic: string;
  month: number;
  week: number;
}

export interface WeekData {
  title: string;
  days: {
    day: number;
    topic: string;
    complete: boolean;
  }[];
}

export interface MonthData {
  name: string;
  weeks: {
    [key: string]: WeekData;
  };
}

export interface WorkspaceManifest {
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
  months: {
    [key: string]: MonthData;
  };
  dayStatus: {
    [key: string]: DayStatus;
  };
}

// Type assertion for the imported JSON
const manifest = manifestData as WorkspaceManifest;

/**
 * Check if a specific day is verified complete
 */
export function isDayVerifiedComplete(dayNumber: number): boolean {
  return manifest.dayStatus[dayNumber]?.complete ?? false;
}

/**
 * Get all verified completed day numbers
 */
export function getVerifiedCompletedDays(): number[] {
  return Object.entries(manifest.dayStatus)
    .filter(([_, status]) => status.complete)
    .map(([day, _]) => parseInt(day));
}

/**
 * Get verified progress summary
 */
export function getVerifiedProgress() {
  return {
    completed: manifest.summary.completedDays,
    total: manifest.summary.totalDays,
    percentage: manifest.summary.completionRate,
    generatedAt: manifest.generatedAt
  };
}

/**
 * Get days for a specific month and week
 */
export function getWeekDays(monthNum: number, weekNum: number) {
  return manifest.months[monthNum]?.weeks[weekNum]?.days ?? [];
}

/**
 * Get all months with their completion status
 */
export function getMonthProgress() {
  const result: { month: number; name: string; completed: number; total: number }[] = [];
  
  for (const [mNum, month] of Object.entries(manifest.months)) {
    let completed = 0;
    let total = 0;
    
    for (const [_, week] of Object.entries(month.weeks)) {
      for (const day of week.days) {
        total++;
        if (day.complete) completed++;
      }
    }
    
    result.push({
      month: parseInt(mNum),
      name: month.name,
      completed,
      total
    });
  }
  
  return result;
}

/**
 * Get the raw manifest
 */
export function getManifest(): WorkspaceManifest {
  return manifest;
}
