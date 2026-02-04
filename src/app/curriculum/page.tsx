'use client';

import { useState } from 'react';
import { QUARTERS, WEEKLY_CURRICULUM } from '@/lib/curriculum';
import { getSessionsByQuarter, getSessionsByWeek } from '@/lib/sessions';
import { useProgress } from '@/hooks/useProgress';
import { SessionCard } from '@/components/SessionCard';
import { WeekView } from '@/components/WeekView';
import { ChevronDown, ChevronRight, CheckCircle2, Award, BookOpen } from 'lucide-react';

export default function CurriculumPage() {
  const { completedIds } = useProgress();
  const [expandedQuarter, setExpandedQuarter] = useState<number | null>(1);
  const [expandedWeek, setExpandedWeek] = useState<number | null>(null);

  const toggleQuarter = (id: number) => {
    setExpandedQuarter(expandedQuarter === id ? null : id);
    setExpandedWeek(null);
  };

  const toggleWeek = (week: number) => {
    setExpandedWeek(expandedWeek === week ? null : week);
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          6-Month Aggressive Plan
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          24 weeks • 168 days • Goal: Data Engineer by July 2026
        </p>
      </div>

      {/* Progress Summary */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-6 text-white mb-8">
        <div className="flex items-center gap-4">
          <BookOpen className="w-12 h-12" />
          <div>
            <h2 className="text-xl font-bold">6-Month Aggressive Transition</h2>
            <p className="text-blue-100">
              {completedIds.size} of 168 days completed ({Math.round((completedIds.size / 168) * 100)}%)
            </p>
          </div>
        </div>
      </div>

      {/* Quarters Accordion */}
      <div className="space-y-4">
        {QUARTERS.map(quarter => {
          const sessions = getSessionsByQuarter(quarter.id);
          const completedCount = sessions.filter(s => completedIds.has(s.id)).length;
          const percentage = Math.round((completedCount / sessions.length) * 100);
          const isExpanded = expandedQuarter === quarter.id;
          const isComplete = completedCount === sessions.length;

          // Get weeks for this quarter
          const weeks = WEEKLY_CURRICULUM.filter(
            w => w.week >= quarter.weeks[0] && w.week <= quarter.weeks[1]
          );

          return (
            <div
              key={quarter.id}
              className={`bg-white dark:bg-gray-800 rounded-xl border overflow-hidden transition-all ${
                isComplete
                  ? 'border-green-300 dark:border-green-700'
                  : 'border-gray-200 dark:border-gray-700'
              }`}
            >
              {/* Quarter Header */}
              <button
                onClick={() => toggleQuarter(quarter.id)}
                className={`w-full p-6 flex items-center justify-between text-left transition-colors ${
                  isComplete
                    ? 'bg-green-50 dark:bg-green-900/20 hover:bg-green-100 dark:hover:bg-green-900/30'
                    : 'hover:bg-gray-50 dark:hover:bg-gray-700/50'
                }`}
              >
                <div className="flex items-center gap-4">
                  {isComplete ? (
                    <CheckCircle2 className="w-8 h-8 text-green-500" />
                  ) : (
                    <span className="w-8 h-8 flex items-center justify-center text-xl font-bold text-gray-400 dark:text-gray-500 bg-gray-100 dark:bg-gray-700 rounded-full">
                      {quarter.id}
                    </span>
                  )}
                  <div>
                    <h3 className="text-lg font-bold text-gray-900 dark:text-white">
                      {quarter.name}
                    </h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      Weeks {quarter.weeks[0]}-{quarter.weeks[1]} • {quarter.startDate} – {quarter.endDate}
                    </p>
                  </div>
                </div>
                
                <div className="flex items-center gap-4">
                  <div className="text-right">
                    <p className="text-lg font-bold text-gray-900 dark:text-white">{percentage}%</p>
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {completedCount}/{sessions.length}
                    </p>
                  </div>
                  {isExpanded ? (
                    <ChevronDown className="w-5 h-5 text-gray-400" />
                  ) : (
                    <ChevronRight className="w-5 h-5 text-gray-400" />
                  )}
                </div>
              </button>

              {/* Quarter Content */}
              {isExpanded && (
                <div className="border-t border-gray-200 dark:border-gray-700">
                  {/* Quarter Meta */}
                  <div className="p-6 bg-gray-50 dark:bg-gray-900 border-b border-gray-200 dark:border-gray-700">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      <div>
                        <h4 className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-1">
                          Goal
                        </h4>
                        <p className="text-gray-900 dark:text-white">{quarter.goal}</p>
                      </div>
                      <div>
                        <h4 className="text-sm font-medium text-gray-500 dark:text-gray-400 mb-1">
                          Side Project
                        </h4>
                        <p className="text-gray-900 dark:text-white">{quarter.project}</p>
                      </div>
                    </div>
                    
                    {quarter.certification && (
                      <div className="mt-4 flex items-center gap-2 text-orange-600 dark:text-orange-400">
                        <Award className="w-5 h-5" />
                        <span className="font-medium">Certification: {quarter.certification}</span>
                      </div>
                    )}
                  </div>

                  {/* Weeks List */}
                  <div className="p-6 space-y-3">
                    {weeks.map(weekData => {
                      const weekSessions = getSessionsByWeek(weekData.week);
                      const weekCompleted = weekSessions.filter(s => completedIds.has(s.id)).length;
                      const isWeekExpanded = expandedWeek === weekData.week;
                      const isWeekComplete = weekCompleted === weekSessions.length;

                      return (
                        <div key={weekData.week}>
                          <button
                            onClick={() => toggleWeek(weekData.week)}
                            className={`w-full p-4 rounded-lg flex items-center justify-between text-left transition-colors ${
                              isWeekComplete
                                ? 'bg-green-50 dark:bg-green-900/20'
                                : 'bg-gray-100 dark:bg-gray-700'
                            } hover:opacity-80`}
                          >
                            <div className="flex items-center gap-3">
                              {isWeekComplete ? (
                                <CheckCircle2 className="w-5 h-5 text-green-500" />
                              ) : (
                                <span className="w-5 h-5 flex items-center justify-center text-xs font-bold text-gray-500 dark:text-gray-400">
                                  {weekData.week}
                                </span>
                              )}
                              <div>
                                <p className="font-medium text-gray-900 dark:text-white">
                                  Week {weekData.week}
                                </p>
                                <p className="text-sm text-gray-500 dark:text-gray-400">
                                  {weekData.topics.join(' • ')}
                                </p>
                              </div>
                            </div>
                            <div className="flex items-center gap-2">
                              <span className="text-sm font-medium text-gray-500 dark:text-gray-400">
                                {weekCompleted}/{weekSessions.length}
                              </span>
                              {isWeekExpanded ? (
                                <ChevronDown className="w-4 h-4 text-gray-400" />
                              ) : (
                                <ChevronRight className="w-4 h-4 text-gray-400" />
                              )}
                            </div>
                          </button>

                          {isWeekExpanded && (
                            <div className="mt-3 ml-8 space-y-2">
                              {weekSessions.map(session => (
                                <SessionCard
                                  key={session.id}
                                  session={session}
                                  variant="compact"
                                />
                              ))}
                            </div>
                          )}
                        </div>
                      );
                    })}
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
