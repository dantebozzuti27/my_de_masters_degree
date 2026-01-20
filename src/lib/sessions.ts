// Session generation utilities for 6-Month Aggressive Plan

import { addDays, format, parseISO, isBefore, isAfter, isEqual, startOfDay } from 'date-fns';
import { StudySession } from './types';
import { QUARTERS, WEEKLY_CURRICULUM } from './curriculum';

// START: February 1, 2026 (aggressive 6-month plan)
const START_DATE = new Date(2026, 1, 1); // February 1, 2026
const TOTAL_WEEKS = 24; // 6 months = 24 weeks

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
  let currentDate = START_DATE;
  let dayNumber = 0;
  let weekNumber = 1;

  // Generate sessions for 24 weeks (Mon-Thu each week)
  while (weekNumber <= TOTAL_WEEKS) {
    const dayOfWeekJS = currentDate.getDay(); // 0=Sun, 1=Mon, ..., 6=Sat
    
    // Only Mon (1), Tue (2), Wed (3), Thu (4)
    if (dayOfWeekJS >= 1 && dayOfWeekJS <= 4) {
      dayNumber++;
      
      const dayOfWeek = (dayOfWeekJS - 1) as 0 | 1 | 2 | 3; // Convert to our 0-3 system
      const topics = getTopicsForWeek(weekNumber);
      const quarterId = getQuarterForWeek(weekNumber);
      
      const session: StudySession = {
        id: `session-${dayNumber}`,
        dayNumber,
        weekNumber,
        quarterId,
        date: format(currentDate, 'yyyy-MM-dd'),
        dayOfWeek,
        topic: topics[dayOfWeek],
        objectives: [],
        resources: []
      };
      
      sessions.push(session);
      
      // After Thursday, move to next week
      if (dayOfWeekJS === 4) {
        weekNumber++;
      }
    }
    
    currentDate = addDays(currentDate, 1);
    
    // Safety check to prevent infinite loop
    if (dayNumber > 150) break;
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

export function getSessionByDate(date: Date): StudySession | undefined {
  const dateStr = format(startOfDay(date), 'yyyy-MM-dd');
  return getAllSessions().find(s => s.date === dateStr);
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

export function getTodaySession(): StudySession | undefined {
  return getSessionByDate(new Date());
}

export function getCurrentWeekSessions(): StudySession[] {
  const today = getTodaySession();
  if (!today) {
    // If today isn't a study day, find the current week based on date
    const allSessions = getAllSessions();
    const todayDate = startOfDay(new Date());
    
    // Find the session that's closest to today
    for (let i = 0; i < allSessions.length; i++) {
      const sessionDate = parseISO(allSessions[i].date);
      if (isAfter(sessionDate, todayDate) || isEqual(sessionDate, todayDate)) {
        return getSessionsByWeek(allSessions[i].weekNumber);
      }
    }
    return getSessionsByWeek(1);
  }
  return getSessionsByWeek(today.weekNumber);
}

export function getNextIncompleteSession(completedIds: Set<string>): StudySession | undefined {
  return getAllSessions().find(s => !completedIds.has(s.id));
}

export function getUpcomingSessions(count: number = 5): StudySession[] {
  const today = startOfDay(new Date());
  return getAllSessions()
    .filter(s => {
      const sessionDate = parseISO(s.date);
      return isAfter(sessionDate, today) || isEqual(sessionDate, today);
    })
    .slice(0, count);
}

export function getPastSessions(count: number = 5): StudySession[] {
  const today = startOfDay(new Date());
  return getAllSessions()
    .filter(s => isBefore(parseISO(s.date), today))
    .slice(-count);
}

export function getSessionsForMonth(year: number, month: number): StudySession[] {
  return getAllSessions().filter(s => {
    const date = parseISO(s.date);
    return date.getFullYear() === year && date.getMonth() === month;
  });
}

export function getProgress(completedSessionIds: Set<string>): {
  completed: number;
  total: number;
  percentage: number;
  currentDay: number;
  expectedDay: number;
  daysAhead: number;
} {
  const allSessions = getAllSessions();
  const today = startOfDay(new Date());
  
  // Find expected progress (sessions up to today)
  const expectedSessions = allSessions.filter(s => 
    isBefore(parseISO(s.date), today) || isEqual(parseISO(s.date), today)
  );
  
  const completed = completedSessionIds.size;
  const total = allSessions.length;
  const percentage = Math.round((completed / total) * 100);
  const currentDay = completed;
  const expectedDay = expectedSessions.length;
  const daysAhead = completed - expectedDay;

  return { completed, total, percentage, currentDay, expectedDay, daysAhead };
}

export function getDayLabel(dayOfWeek: 0 | 1 | 2 | 3): string {
  const labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday'];
  return labels[dayOfWeek];
}

export function getShortDayLabel(dayOfWeek: 0 | 1 | 2 | 3): string {
  const labels = ['Mon', 'Tue', 'Wed', 'Thu'];
  return labels[dayOfWeek];
}

// Get the end date of the program
export function getProgramEndDate(): Date {
  return new Date(2026, 6, 31); // July 31, 2026
}

// Get program summary
export function getProgramSummary() {
  const sessions = getAllSessions();
  return {
    totalWeeks: TOTAL_WEEKS,
    totalSessions: sessions.length,
    startDate: START_DATE,
    endDate: getProgramEndDate(),
    months: 6
  };
}
