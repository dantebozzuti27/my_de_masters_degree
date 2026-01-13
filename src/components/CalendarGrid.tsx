'use client';

import { useState } from 'react';
import { StudySession } from '@/lib/types';
import { getSessionsForMonth, getSessionByDate, getDayLabel } from '@/lib/sessions';
import { useProgress } from '@/hooks/useProgress';
import { format, startOfMonth, endOfMonth, eachDayOfInterval, getDay, addMonths, subMonths, isToday, parseISO, isSameDay } from 'date-fns';
import { ChevronLeft, ChevronRight, CheckCircle2 } from 'lucide-react';

interface CalendarGridProps {
  onSelectSession?: (session: StudySession) => void;
}

export function CalendarGrid({ onSelectSession }: CalendarGridProps) {
  const [currentDate, setCurrentDate] = useState(new Date(2026, 0, 1)); // Start at Jan 2026
  const { completedIds } = useProgress();

  const monthStart = startOfMonth(currentDate);
  const monthEnd = endOfMonth(currentDate);
  const days = eachDayOfInterval({ start: monthStart, end: monthEnd });
  
  // Get sessions for this month
  const sessions = getSessionsForMonth(currentDate.getFullYear(), currentDate.getMonth());
  const sessionMap = new Map(sessions.map(s => [s.date, s]));

  // Calculate padding for start of month
  const startPadding = getDay(monthStart); // 0 = Sunday

  const goToPrevMonth = () => setCurrentDate(prev => subMonths(prev, 1));
  const goToNextMonth = () => setCurrentDate(prev => addMonths(prev, 1));
  const goToToday = () => setCurrentDate(new Date());

  const weekDays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
        <button
          onClick={goToPrevMonth}
          className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
        >
          <ChevronLeft className="w-5 h-5 text-gray-600 dark:text-gray-400" />
        </button>
        
        <div className="flex items-center gap-4">
          <h2 className="text-lg font-bold text-gray-900 dark:text-white">
            {format(currentDate, 'MMMM yyyy')}
          </h2>
          <button
            onClick={goToToday}
            className="px-3 py-1 text-sm bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 rounded-lg hover:bg-blue-200 dark:hover:bg-blue-800 transition-colors"
          >
            Today
          </button>
        </div>
        
        <button
          onClick={goToNextMonth}
          className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors"
        >
          <ChevronRight className="w-5 h-5 text-gray-600 dark:text-gray-400" />
        </button>
      </div>

      {/* Week day headers */}
      <div className="grid grid-cols-7 border-b border-gray-200 dark:border-gray-700">
        {weekDays.map(day => (
          <div
            key={day}
            className={`p-2 text-center text-sm font-medium ${
              day === 'Mon' || day === 'Tue' || day === 'Wed' || day === 'Thu'
                ? 'text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20'
                : 'text-gray-500 dark:text-gray-400'
            }`}
          >
            {day}
          </div>
        ))}
      </div>

      {/* Calendar grid */}
      <div className="grid grid-cols-7">
        {/* Empty cells for padding */}
        {Array.from({ length: startPadding }).map((_, i) => (
          <div key={`pad-${i}`} className="p-2 min-h-[80px] bg-gray-50 dark:bg-gray-900" />
        ))}
        
        {/* Day cells */}
        {days.map(day => {
          const dateStr = format(day, 'yyyy-MM-dd');
          const session = sessionMap.get(dateStr);
          const isCompleted = session && completedIds.has(session.id);
          const isTodayDate = isToday(day);
          const isStudyDay = session !== undefined;

          return (
            <div
              key={dateStr}
              onClick={() => session && onSelectSession?.(session)}
              className={`p-2 min-h-[80px] border-t border-r border-gray-200 dark:border-gray-700 transition-colors ${
                isStudyDay ? 'cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700' : ''
              } ${
                isTodayDate ? 'bg-blue-50 dark:bg-blue-900/30' : ''
              } ${
                isCompleted ? 'bg-green-50 dark:bg-green-900/20' : ''
              }`}
            >
              <div className="flex items-center justify-between">
                <span className={`text-sm font-medium ${
                  isTodayDate
                    ? 'w-6 h-6 flex items-center justify-center bg-blue-600 text-white rounded-full'
                    : 'text-gray-700 dark:text-gray-300'
                }`}>
                  {format(day, 'd')}
                </span>
                {isCompleted && (
                  <CheckCircle2 className="w-4 h-4 text-green-500" />
                )}
              </div>
              
              {session && (
                <div className={`mt-1 p-1 rounded text-xs truncate ${
                  isCompleted
                    ? 'bg-green-100 text-green-700 dark:bg-green-800 dark:text-green-300'
                    : 'bg-blue-100 text-blue-700 dark:bg-blue-800 dark:text-blue-300'
                }`}>
                  {session.topic}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Legend */}
      <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex gap-4 text-sm">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded bg-blue-100 dark:bg-blue-800" />
          <span className="text-gray-600 dark:text-gray-400">Study Day</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded bg-green-100 dark:bg-green-800" />
          <span className="text-gray-600 dark:text-gray-400">Completed</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-blue-600" />
          <span className="text-gray-600 dark:text-gray-400">Today</span>
        </div>
      </div>
    </div>
  );
}
