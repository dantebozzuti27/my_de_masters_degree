'use client';

import { useState } from 'react';
import { StudySession } from '@/lib/types';
import { getAllSessions, getSessionsByWeek } from '@/lib/sessions';
import { useProgress } from '@/hooks/useProgress';
import { ChevronLeft, ChevronRight, CheckCircle2 } from 'lucide-react';

interface CalendarGridProps {
  onSelectSession?: (session: StudySession) => void;
}

export function CalendarGrid({ onSelectSession }: CalendarGridProps) {
  const [currentWeekPage, setCurrentWeekPage] = useState(0); // Show weeks 4 at a time
  const { completedIds } = useProgress();
  const allSessions = getAllSessions();
  
  const WEEKS_PER_PAGE = 4;
  const TOTAL_WEEKS = 24;
  const totalPages = Math.ceil(TOTAL_WEEKS / WEEKS_PER_PAGE);
  
  const startWeek = currentWeekPage * WEEKS_PER_PAGE + 1;
  const endWeek = Math.min(startWeek + WEEKS_PER_PAGE - 1, TOTAL_WEEKS);
  
  const weeksToShow = Array.from(
    { length: endWeek - startWeek + 1 },
    (_, i) => startWeek + i
  );

  const goPrevPage = () => setCurrentWeekPage(prev => Math.max(0, prev - 1));
  const goNextPage = () => setCurrentWeekPage(prev => Math.min(totalPages - 1, prev + 1));

  const sessionLabels = ['Session 1', 'Session 2', 'Session 3', 'Session 4'];

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
        <button
          onClick={goPrevPage}
          disabled={currentWeekPage === 0}
          className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors disabled:opacity-30"
        >
          <ChevronLeft className="w-5 h-5 text-gray-600 dark:text-gray-400" />
        </button>
        
        <h2 className="text-lg font-bold text-gray-900 dark:text-white">
          Weeks {startWeek} - {endWeek} of {TOTAL_WEEKS}
        </h2>
        
        <button
          onClick={goNextPage}
          disabled={currentWeekPage >= totalPages - 1}
          className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg transition-colors disabled:opacity-30"
        >
          <ChevronRight className="w-5 h-5 text-gray-600 dark:text-gray-400" />
        </button>
      </div>

      {/* Session headers */}
      <div className="grid grid-cols-5 border-b border-gray-200 dark:border-gray-700">
        <div className="p-2 text-center text-sm font-medium text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-gray-900">
          Week
        </div>
        {sessionLabels.map(label => (
          <div
            key={label}
            className="p-2 text-center text-sm font-medium text-blue-600 dark:text-blue-400 bg-blue-50 dark:bg-blue-900/20"
          >
            {label}
          </div>
        ))}
      </div>

      {/* Week rows */}
      <div className="divide-y divide-gray-200 dark:divide-gray-700">
        {weeksToShow.map(weekNum => {
          const weekSessions = getSessionsByWeek(weekNum);
          const completedCount = weekSessions.filter(s => completedIds.has(s.id)).length;
          const allComplete = completedCount === 4;
          
          return (
            <div key={weekNum} className="grid grid-cols-5">
              {/* Week number cell */}
              <div className={`p-3 flex items-center justify-center ${
                allComplete ? 'bg-green-50 dark:bg-green-900/20' : 'bg-gray-50 dark:bg-gray-900'
              }`}>
                <span className="font-medium text-gray-700 dark:text-gray-300">
                  Week {weekNum}
                </span>
                {allComplete && (
                  <CheckCircle2 className="w-4 h-4 text-green-500 ml-2" />
                )}
              </div>
              
              {/* Session cells */}
              {weekSessions.map(session => {
                const isCompleted = completedIds.has(session.id);
                
                return (
                  <div
                    key={session.id}
                    onClick={() => onSelectSession?.(session)}
                    className={`p-3 cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors border-l border-gray-200 dark:border-gray-700 ${
                      isCompleted ? 'bg-green-50 dark:bg-green-900/20' : ''
                    }`}
                  >
                    <div className="flex items-center justify-between mb-1">
                      <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
                        Day {session.dayNumber}
                      </span>
                      {isCompleted && (
                        <CheckCircle2 className="w-4 h-4 text-green-500" />
                      )}
                    </div>
                    <div className={`text-xs truncate ${
                      isCompleted
                        ? 'text-green-700 dark:text-green-300'
                        : 'text-gray-700 dark:text-gray-300'
                    }`}>
                      {session.topic}
                    </div>
                  </div>
                );
              })}
            </div>
          );
        })}
      </div>

      {/* Legend & Summary */}
      <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex justify-between items-center text-sm">
        <div className="flex gap-4">
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded bg-blue-100 dark:bg-blue-800" />
            <span className="text-gray-600 dark:text-gray-400">Pending</span>
          </div>
          <div className="flex items-center gap-2">
            <div className="w-3 h-3 rounded bg-green-100 dark:bg-green-800" />
            <span className="text-gray-600 dark:text-gray-400">Completed</span>
          </div>
        </div>
        <div className="text-gray-600 dark:text-gray-400">
          {completedIds.size} / {allSessions.length} sessions (2 hours each)
        </div>
      </div>
    </div>
  );
}
