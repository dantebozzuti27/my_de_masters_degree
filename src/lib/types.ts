// Types for the SDE Study Tracker
// Aggressive 6-Month Plan: Feb 2026 - July 2026

// Note: "Quarter" is kept for backward compatibility but represents MONTHS in the 6-mo plan
export interface Quarter {
  id: number;
  name: string;
  shortName: string;
  weeks: [number, number];
  startDate: string;
  endDate: string;
  goal: string;
  project: string;
  certification?: string;
}

// Alias for clarity
export type Month = Quarter;

export interface WeekTopics {
  week: number;
  topics: [string, string, string, string]; // Mon, Tue, Wed, Thu
}

export interface StudySession {
  id: string;
  dayNumber: number;
  weekNumber: number;
  quarterId: number;
  date?: string; // Optional - not tied to specific dates
  dayOfWeek?: 0 | 1 | 2 | 3; // Optional - complete at your own pace
  topic: string;
  objectives: string[];
  resources: Resource[];
  exercises?: string;
  workApplication?: string;
  weeklyCheckpoint?: string;
}

export interface Resource {
  title: string;
  url: string;
  type: 'video' | 'article' | 'documentation' | 'practice' | 'course';
}

export interface SessionProgress {
  sessionId: string;
  completed: boolean;
  completedAt?: string;
  timeSpent?: number; // minutes
  notes?: string;
  rating?: 1 | 2 | 3 | 4 | 5;
}

export interface ProgressStats {
  totalSessions: number;
  completedSessions: number;
  currentStreak: number;
  longestStreak: number;
  totalTimeSpent: number;
  averageRating: number;
  completionRate: number;
  nextSession: number;
}

export interface UserProgress {
  sessions: Record<string, SessionProgress>;
  lastUpdated: string;
  startDate: string;
}

export type ViewMode = 'day' | 'week' | 'month' | 'quarter';
