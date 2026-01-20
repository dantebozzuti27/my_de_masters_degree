// Session generation utilities for 6-Month Aggressive Plan
// NO DATE DEPENDENCIES - Complete lessons at your own pace (2 hours each)

import { StudySession } from './types';
import { QUARTERS, WEEKLY_CURRICULUM } from './curriculum';

const TOTAL_WEEKS = 24; // 6 months = 24 weeks
const SESSIONS_PER_WEEK = 4; // 4 sessions per week
const TOTAL_SESSIONS = TOTAL_WEEKS * SESSIONS_PER_WEEK; // 96 total sessions

function getQuarterForWeek(weekNumber: number): number {
  for (const quarter of QUARTERS) {
    if (weekNumber >= quarter.weeks[0] && weekNumber <= quarter.weeks[1]) {
      return quarter.id;
    }
  }
  return 6; // Default to last month
}

function getTopicsForWeek(weekNumber: number): [string, string, string, string] {
  const weekData = WEEKLY_CURRICULUM.find(w => w.week === weekNumber);
  return weekData?.topics ?? ["Study Session", "Study Session", "Study Session", "Study Session"];
}

export function generateAllSessions(): StudySession[] {
  const sessions: StudySession[] = [];

  // Generate 96 sessions (24 weeks × 4 sessions per week)
  for (let dayNumber = 1; dayNumber <= TOTAL_SESSIONS; dayNumber++) {
    const weekNumber = Math.ceil(dayNumber / SESSIONS_PER_WEEK);
    const dayInWeek = ((dayNumber - 1) % SESSIONS_PER_WEEK) as 0 | 1 | 2 | 3;
    
    const topics = getTopicsForWeek(weekNumber);
    const quarterId = getQuarterForWeek(weekNumber);
    
    const session: StudySession = {
      id: `session-${dayNumber}`,
      dayNumber,
      weekNumber,
      quarterId,
      // No date - complete at your own pace
      topic: topics[dayInWeek],
      objectives: [],
      resources: []
    };
    
    sessions.push(session);
  }

  return sessions;
}

// Pre-generate all sessions
let _allSessions: StudySession[] | null = null;

export function getAllSessions(): StudySession[] {
  if (!_allSessions) {
    _allSessions = generateAllSessions();
  }
  return _allSessions;
}

export function getSessionById(id: string): StudySession | undefined {
  return getAllSessions().find(s => s.id === id);
}

export function getSessionByDay(dayNumber: number): StudySession | undefined {
  return getAllSessions().find(s => s.dayNumber === dayNumber);
}

export function getSessionsByWeek(weekNumber: number): StudySession[] {
  return getAllSessions().filter(s => s.weekNumber === weekNumber);
}

export function getSessionsByQuarter(quarterId: number): StudySession[] {
  return getAllSessions().filter(s => s.quarterId === quarterId);
}

export function getNextIncompleteSession(completedIds: Set<string>): StudySession | undefined {
  return getAllSessions().find(s => !completedIds.has(s.id));
}

export function getNextIncompleteSessions(completedIds: Set<string>, count: number = 5): StudySession[] {
  return getAllSessions()
    .filter(s => !completedIds.has(s.id))
    .slice(0, count);
}

export function getCurrentWeekSessions(completedIds: Set<string>): StudySession[] {
  const nextSession = getNextIncompleteSession(completedIds);
  if (!nextSession) {
    // All done - return last week
    return getSessionsByWeek(TOTAL_WEEKS);
  }
  return getSessionsByWeek(nextSession.weekNumber);
}

export function getProgress(completedSessionIds: Set<string>): {
  completed: number;
  total: number;
  percentage: number;
  currentDay: number;
  nextDay: number;
} {
  const allSessions = getAllSessions();
  const completed = completedSessionIds.size;
  const total = allSessions.length;
  const percentage = Math.round((completed / total) * 100);
  const currentDay = completed;
  const nextDay = completed + 1;

  return { completed, total, percentage, currentDay, nextDay };
}

export function getDayLabel(dayInWeek: 0 | 1 | 2 | 3): string {
  const labels = ['Session 1', 'Session 2', 'Session 3', 'Session 4'];
  return labels[dayInWeek];
}

export function getShortDayLabel(dayInWeek: 0 | 1 | 2 | 3): string {
  const labels = ['S1', 'S2', 'S3', 'S4'];
  return labels[dayInWeek];
}

// Get program summary
export function getProgramSummary() {
  const sessions = getAllSessions();
  return {
    totalWeeks: TOTAL_WEEKS,
    totalSessions: sessions.length,
    sessionsPerWeek: SESSIONS_PER_WEEK,
    hoursPerSession: 2,
    totalHours: sessions.length * 2,
    months: 6
  };
}
