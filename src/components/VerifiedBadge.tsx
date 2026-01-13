'use client';

import { CheckCircle2, Circle, ShieldCheck, ShieldX } from 'lucide-react';
import { isDayVerifiedComplete } from '@/lib/verified-progress';

interface VerifiedBadgeProps {
  dayNumber: number;
  showLabel?: boolean;
  size?: 'sm' | 'md' | 'lg';
}

/**
 * Shows verified completion status based on actual workspace code
 * NOT manual checkboxes - this reflects real work done
 */
export function VerifiedBadge({ dayNumber, showLabel = true, size = 'md' }: VerifiedBadgeProps) {
  const isComplete = isDayVerifiedComplete(dayNumber);
  
  const sizeClasses = {
    sm: 'w-4 h-4',
    md: 'w-5 h-5',
    lg: 'w-6 h-6'
  };
  
  const iconSize = sizeClasses[size];
  
  if (isComplete) {
    return (
      <div className="flex items-center gap-1.5">
        <ShieldCheck className={`${iconSize} text-green-500`} />
        {showLabel && (
          <span className="text-sm font-medium text-green-600 dark:text-green-400">
            Verified Complete
          </span>
        )}
      </div>
    );
  }
  
  return (
    <div className="flex items-center gap-1.5">
      <Circle className={`${iconSize} text-gray-300 dark:text-gray-600`} />
      {showLabel && (
        <span className="text-sm text-gray-500 dark:text-gray-400">
          Not Yet Complete
        </span>
      )}
    </div>
  );
}

interface VerifiedProgressBarProps {
  completed: number;
  total: number;
  showNumbers?: boolean;
}

export function VerifiedProgressBar({ completed, total, showNumbers = true }: VerifiedProgressBarProps) {
  const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;
  
  return (
    <div className="w-full">
      <div className="flex items-center justify-between mb-1">
        <span className="flex items-center gap-1.5 text-sm font-medium text-gray-700 dark:text-gray-300">
          <ShieldCheck className="w-4 h-4 text-green-500" />
          Verified Progress
        </span>
        {showNumbers && (
          <span className="text-sm text-gray-500 dark:text-gray-400">
            {completed}/{total} ({percentage}%)
          </span>
        )}
      </div>
      <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
        <div
          className="h-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500"
          style={{ width: `${percentage}%` }}
        />
      </div>
    </div>
  );
}
