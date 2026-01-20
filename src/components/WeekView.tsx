'use client';

import { StudySession } from '@/lib/types';
import { QUARTERS, WEEKLY_CURRICULUM } from '@/lib/curriculum';
import { useProgress } from '@/hooks/useProgress';
import { SessionCard } from './SessionCard';
import { CheckCircle2 } from 'lucide-react';

interface WeekViewProps {
  sessions: StudySession[];
  weekNumber: number;
}

export function WeekView({ sessions, weekNumber }: WeekViewProps) {
  const { completedIds } = useProgress();
  
  const weekData = WEEKLY_CURRICULUM.find(w => w.week === weekNumber);
  const quarter = sessions[0] ? QUARTERS.find(q => q.id === sessions[0].quarterId) : null;
  
  const completedCount = sessions.filter(s => completedIds.has(s.id)).length;
  const isWeekComplete = completedCount === sessions.length;

  // Calculate day range for this week
  const firstDay = sessions[0]?.dayNumber ?? 1;
  const lastDay = sessions[sessions.length - 1]?.dayNumber ?? 4;

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* Week Header */}
      <div className={`p-6 border-b border-gray-200 dark:border-gray-700 ${
        isWeekComplete ? 'bg-green-50 dark:bg-green-900/20' : 'bg-gray-50 dark:bg-gray-900'
      }`}>
        <div className="flex items-center justify-between">
          <div>
            <div className="flex items-center gap-3">
              <h2 className="text-xl font-bold text-gray-900 dark:text-white">
                Week {weekNumber}
              </h2>
              {isWeekComplete && (
                <span className="flex items-center gap-1 px-2 py-1 bg-green-100 dark:bg-green-800 text-green-700 dark:text-green-300 rounded-full text-sm font-medium">
                  <CheckCircle2 className="w-4 h-4" />
                  Complete
                </span>
              )}
            </div>
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
              Days {firstDay} - {lastDay} • 8 hours total
            </p>
          </div>
          <div className="text-right">
            <p className="text-2xl font-bold text-gray-900 dark:text-white">
              {completedCount}/{sessions.length}
            </p>
            <p className="text-sm text-gray-500 dark:text-gray-400">sessions</p>
          </div>
        </div>
        
        {quarter && (
          <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
            <span className="px-3 py-1 bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300 rounded-full text-sm font-medium">
              {quarter.shortName}
            </span>
          </div>
        )}
      </div>

      {/* Session List */}
      <div className="p-6">
        <div className="grid gap-3">
          {sessions.map(session => (
            <SessionCard
              key={session.id}
              session={session}
              variant="compact"
            />
          ))}
        </div>
      </div>
    </div>
  );
}
