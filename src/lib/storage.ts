// Local storage utilities for progress tracking

import { UserProgress, SessionProgress } from './types';

const STORAGE_KEY = 'sde-tracker-progress';

export function getStoredProgress(): UserProgress | null {
  if (typeof window === 'undefined') return null;
  
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (!stored) return null;
    return JSON.parse(stored) as UserProgress;
  } catch {
    return null;
  }
}

export function saveProgress(progress: UserProgress): void {
  if (typeof window === 'undefined') return;
  
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  } catch (e) {
    console.error('Failed to save progress:', e);
  }
}

export function initializeProgress(): UserProgress {
  return {
    sessions: {},
    lastUpdated: new Date().toISOString(),
    startDate: '2026-01-12'
  };
}

export function markSessionComplete(
  progress: UserProgress,
  sessionId: string,
  data?: Partial<SessionProgress>
): UserProgress {
  return {
    ...progress,
    sessions: {
      ...progress.sessions,
      [sessionId]: {
        sessionId,
        completed: true,
        completedAt: new Date().toISOString(),
        ...data
      }
    },
    lastUpdated: new Date().toISOString()
  };
}

export function markSessionIncomplete(
  progress: UserProgress,
  sessionId: string
): UserProgress {
  const newSessions = { ...progress.sessions };
  delete newSessions[sessionId];
  
  return {
    ...progress,
    sessions: newSessions,
    lastUpdated: new Date().toISOString()
  };
}

export function updateSessionNotes(
  progress: UserProgress,
  sessionId: string,
  notes: string
): UserProgress {
  const existingSession = progress.sessions[sessionId];
  
  return {
    ...progress,
    sessions: {
      ...progress.sessions,
      [sessionId]: {
        sessionId,
        completed: existingSession?.completed ?? false,
        completedAt: existingSession?.completedAt,
        notes,
        rating: existingSession?.rating,
        timeSpent: existingSession?.timeSpent
      }
    },
    lastUpdated: new Date().toISOString()
  };
}

export function updateSessionRating(
  progress: UserProgress,
  sessionId: string,
  rating: 1 | 2 | 3 | 4 | 5
): UserProgress {
  const existingSession = progress.sessions[sessionId];
  
  return {
    ...progress,
    sessions: {
      ...progress.sessions,
      [sessionId]: {
        sessionId,
        completed: existingSession?.completed ?? false,
        completedAt: existingSession?.completedAt,
        notes: existingSession?.notes,
        rating,
        timeSpent: existingSession?.timeSpent
      }
    },
    lastUpdated: new Date().toISOString()
  };
}

export function getCompletedSessionIds(progress: UserProgress): Set<string> {
  return new Set(
    Object.values(progress.sessions)
      .filter(s => s.completed)
      .map(s => s.sessionId)
  );
}

export function calculateStreak(progress: UserProgress, allSessionDates: string[]): {
  current: number;
  longest: number;
} {
  const completedDates = new Set(
    Object.values(progress.sessions)
      .filter(s => s.completed && s.completedAt)
      .map(s => s.completedAt!.split('T')[0])
  );

  let currentStreak = 0;
  let longestStreak = 0;
  let tempStreak = 0;

  // Sort session dates and check for consecutive completions
  const sortedDates = [...allSessionDates].sort();
  
  for (const date of sortedDates) {
    if (completedDates.has(date)) {
      tempStreak++;
      longestStreak = Math.max(longestStreak, tempStreak);
    } else {
      tempStreak = 0;
    }
  }

  // Calculate current streak from today backwards
  const today = new Date().toISOString().split('T')[0];
  const reversedDates = [...sortedDates].reverse();
  
  for (const date of reversedDates) {
    if (date > today) continue;
    if (completedDates.has(date)) {
      currentStreak++;
    } else {
      break;
    }
  }

  return { current: currentStreak, longest: longestStreak };
}

export function exportProgress(progress: UserProgress): string {
  return JSON.stringify(progress, null, 2);
}

export function importProgress(jsonString: string): UserProgress | null {
  try {
    const parsed = JSON.parse(jsonString);
    if (parsed.sessions && parsed.lastUpdated) {
      return parsed as UserProgress;
    }
    return null;
  } catch {
    return null;
  }
}
