'use client';

import { QUARTERS } from '@/lib/curriculum';
import { getSessionsByQuarter } from '@/lib/sessions';
import { useProgress } from '@/hooks/useProgress';
import { Award, CheckCircle2 } from 'lucide-react';

export function QuarterProgress() {
  const { completedIds } = useProgress();

  return (
    <div className="space-y-4">
      {QUARTERS.map(quarter => {
        const sessions = getSessionsByQuarter(quarter.id);
        const completedCount = sessions.filter(s => completedIds.has(s.id)).length;
        const percentage = Math.round((completedCount / sessions.length) * 100);
        const isComplete = completedCount === sessions.length;

        return (
          <div
            key={quarter.id}
            className={`p-4 rounded-xl border transition-all ${
              isComplete
                ? 'bg-green-50 border-green-200 dark:bg-green-900/20 dark:border-green-800'
                : 'bg-white border-gray-200 dark:bg-gray-800 dark:border-gray-700'
            }`}
          >
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-3">
                {isComplete ? (
                  <CheckCircle2 className="w-5 h-5 text-green-500" />
                ) : (
                  <span className="w-5 h-5 flex items-center justify-center text-sm font-bold text-gray-500 dark:text-gray-400">
                    {quarter.id}
                  </span>
                )}
                <div>
                  <h3 className="font-semibold text-gray-900 dark:text-white">
                    {quarter.name}
                  </h3>
                  <p className="text-xs text-gray-500 dark:text-gray-400">
                    {quarter.startDate} – {quarter.endDate}
                  </p>
                </div>
              </div>
              <div className="text-right">
                <p className="text-lg font-bold text-gray-900 dark:text-white">
                  {percentage}%
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400">
                  {completedCount}/{sessions.length}
                </p>
              </div>
            </div>

            {/* Progress bar */}
            <div className="h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
              <div
                className={`h-full transition-all duration-500 ${
                  isComplete ? 'bg-green-500' : 'bg-blue-500'
                }`}
                style={{ width: `${percentage}%` }}
              />
            </div>

            {/* Certification badge */}
            {quarter.certification && (
              <div className="mt-3 flex items-center gap-2">
                <Award className="w-4 h-4 text-orange-500" />
                <span className="text-sm text-orange-600 dark:text-orange-400 font-medium">
                  {quarter.certification}
                </span>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
