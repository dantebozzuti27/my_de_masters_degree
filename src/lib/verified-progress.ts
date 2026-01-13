// Verified Progress - Based on actual workspace files, not manual clicks
// This reads from workspace-manifest.json which is generated at build time

import manifestData from './workspace-manifest.json';

export interface WorkspaceManifest {
  generatedAt: string;
  quarters: {
    [key: string]: {
      folder: string;
      weeks: {
        [key: string]: {
          exercises: {
            [key: string]: {
              complete: boolean;
              path?: string;
              incompletePatterns?: number;
            };
          };
        };
      };
    };
  };
  summary: {
    totalExercises: number;
    completedExercises: number;
    completionRate: number;
  };
  dayStatus: {
    [key: string]: {
      complete: boolean;
      file?: string;
    };
  };
}

// Type assertion for the imported JSON
const manifest = manifestData as WorkspaceManifest;

/**
 * Check if a specific day's exercise is verified complete
 * (based on actual code in workspace, not manual clicks)
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
    completed: manifest.summary.completedExercises,
    total: manifest.summary.totalExercises,
    percentage: manifest.summary.completionRate,
    generatedAt: manifest.generatedAt
  };
}

/**
 * Get exercise status for a specific quarter and week
 */
export function getWeekExercises(quarterNum: number, weekNum: number) {
  return manifest.quarters[quarterNum]?.weeks[weekNum]?.exercises ?? {};
}

/**
 * Get all quarters with their completion status
 */
export function getQuarterProgress() {
  const result: { quarter: number; completed: number; total: number }[] = [];
  
  for (const [qNum, quarter] of Object.entries(manifest.quarters)) {
    let completed = 0;
    let total = 0;
    
    for (const [_, week] of Object.entries(quarter.weeks)) {
      for (const [_, exercise] of Object.entries(week.exercises)) {
        total++;
        if (exercise.complete) completed++;
      }
    }
    
    result.push({
      quarter: parseInt(qNum),
      completed,
      total
    });
  }
  
  return result;
}

/**
 * Get the raw manifest (for debugging)
 */
export function getManifest(): WorkspaceManifest {
  return manifest;
}
