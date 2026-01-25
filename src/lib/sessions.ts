// Session generation utilities for 6-Month Aggressive Plan
// 7 days per week with varying time allocations:
// - Mon-Fri: 2-2.5h hands-on work + 1-1.5h audiobooks/podcasts during commute
// - Saturday: 6-7h heavy project day
// - Sunday: 3-4h light learning + planning

import { StudySession, DayType, DAY_TIME_ALLOCATION } from './types';
import { QUARTERS, WEEKLY_CURRICULUM } from './curriculum';

const TOTAL_WEEKS = 24; // 6 months = 24 weeks
const SESSIONS_PER_WEEK = 7; // 7 days per week (Mon-Sun)
const TOTAL_SESSIONS = TOTAL_WEEKS * SESSIONS_PER_WEEK; // 24 * 7 = 168 days

// Day names for display
const DAY_NAMES = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] as const;
const SHORT_DAY_NAMES = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] as const;

function getQuarterForWeek(weekNumber: number): number {
  for (const quarter of QUARTERS) {
    if (weekNumber >= quarter.weeks[0] && weekNumber <= quarter.weeks[1]) {
      return quarter.id;
    }
  }
  return 6; // Default to last month
}

function getTopicsForWeek(weekNumber: number): string[] {
  const weekData = WEEKLY_CURRICULUM.find(w => w.week === weekNumber);
  if (!weekData) {
    return Array(7).fill("Study Session");
  }
  return weekData.topics;
}

// Get day type based on position in week (0=Mon, 6=Sun)
export function getDayType(dayInWeek: number): DayType {
  if (dayInWeek === 5) return 'saturday';
  if (dayInWeek === 6) return 'sunday';
  return 'weekday';
}

// Get time allocation for a day
export function getTimeForDay(dayInWeek: number): { handson: number; passive: number; total: number } {
  return DAY_TIME_ALLOCATION[getDayType(dayInWeek)];
}

export function generateAllSessions(): StudySession[] {
  const sessions: StudySession[] = [];

  // Generate all sessions: 24 weeks × 7 days = 168 days
  // Week 1: Days 1-7, Week 2: Days 8-14, etc.
  for (let dayNumber = 1; dayNumber <= TOTAL_SESSIONS; dayNumber++) {
    const weekNumber = Math.ceil(dayNumber / SESSIONS_PER_WEEK);
    const dayInWeek = (dayNumber - 1) % SESSIONS_PER_WEEK; // 0=Mon, 6=Sun
    
    const topics = getTopicsForWeek(weekNumber);
    const quarterId = getQuarterForWeek(weekNumber);
    
    const session: StudySession = {
      id: `session-${dayNumber}`,
      dayNumber,
      weekNumber,
      quarterId,
      dayOfWeek: dayInWeek as 0 | 1 | 2 | 3 | 4 | 5 | 6,
      topic: topics[dayInWeek] || `Day ${dayNumber} Study Session`,
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

export function getDayLabel(dayInWeek: number): string {
  return DAY_NAMES[dayInWeek % 7] || 'Session';
}

export function getShortDayLabel(dayInWeek: number): string {
  return SHORT_DAY_NAMES[dayInWeek % 7] || 'S';
}

// Get program summary with accurate time totals
export function getProgramSummary() {
  const sessions = getAllSessions();
  
  // Calculate total hours based on day types
  let totalMinutes = 0;
  let totalHandsonMinutes = 0;
  let totalPassiveMinutes = 0;
  
  sessions.forEach(session => {
    const dayInWeek = session.dayOfWeek ?? 0;
    const time = getTimeForDay(dayInWeek);
    totalMinutes += time.total;
    totalHandsonMinutes += time.handson;
    totalPassiveMinutes += time.passive;
  });
  
  return {
    totalWeeks: TOTAL_WEEKS,
    totalDays: sessions.length,
    sessionsPerWeek: SESSIONS_PER_WEEK,
    totalHours: Math.round(totalMinutes / 60),
    handsOnHours: Math.round(totalHandsonMinutes / 60),
    passiveHours: Math.round(totalPassiveMinutes / 60),
    avgHoursPerWeek: Math.round((totalMinutes / 60) / TOTAL_WEEKS),
    months: 6
  };
}
