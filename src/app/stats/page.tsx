'use client';

import { useProgress } from '@/hooks/useProgress';
import { getAllSessions, getProgress, getSessionsByQuarter } from '@/lib/sessions';
import { QUARTERS, SKILL_BASELINE, CERTIFICATIONS } from '@/lib/curriculum';
import { StatsCard } from '@/components/StatsCard';
import { ProgressRing } from '@/components/ProgressRing';
import { 
  Calendar, 
  CheckCircle2, 
  Flame, 
  Clock, 
  Star,
  TrendingUp,
  Award,
  Target,
  BookOpen,
  Zap
} from 'lucide-react';
import { format, parseISO, differenceInDays, differenceInWeeks } from 'date-fns';

export default function StatsPage() {
  const { completedIds, streak, progress } = useProgress();
  
  const allSessions = getAllSessions();
  const progressData = getProgress(completedIds);
  
  // Calculate various stats
  const startDate = new Date(2026, 0, 12);
  const endDate = new Date(2028, 0, 8);
  const today = new Date();
  
  const totalDays = differenceInDays(endDate, startDate);
  const daysElapsed = Math.max(0, differenceInDays(today, startDate));
  const daysRemaining = Math.max(0, differenceInDays(endDate, today));
  
  // Calculate average rating
  const ratingsArr = Object.values(progress.sessions)
    .filter(s => s.rating)
    .map(s => s.rating as number);
  const avgRating = ratingsArr.length > 0
    ? (ratingsArr.reduce((a, b) => a + b, 0) / ratingsArr.length).toFixed(1)
    : 'N/A';
  
  // Calculate total time spent (assuming 90 min per completed session)
  const totalMinutes = completedIds.size * 90;
  const totalHours = Math.round(totalMinutes / 60);
  
  // Calculate skill progress (linear interpolation based on progress)
  const skillProgress = (baseline: { start: number; target: number }) => {
    const progressPct = progressData.percentage / 100;
    return baseline.start + (baseline.target - baseline.start) * progressPct;
  };

  // Completion by quarter
  const quarterStats = QUARTERS.map(quarter => {
    const sessions = getSessionsByQuarter(quarter.id);
    const completed = sessions.filter(s => completedIds.has(s.id)).length;
    return {
      ...quarter,
      completed,
      total: sessions.length,
      percentage: Math.round((completed / sessions.length) * 100)
    };
  });

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Statistics
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          Track your progress and performance
        </p>
      </div>

      {/* Overall Progress Card */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-8 text-white mb-8">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-bold">Overall Progress</h2>
            <p className="text-blue-100 mt-1">
              {progressData.completed} of {progressData.total} sessions completed
            </p>
            
            <div className="mt-6 grid grid-cols-3 gap-6">
              <div>
                <p className="text-3xl font-bold">{daysElapsed}</p>
                <p className="text-blue-100 text-sm">Days Elapsed</p>
              </div>
              <div>
                <p className="text-3xl font-bold">{daysRemaining}</p>
                <p className="text-blue-100 text-sm">Days Remaining</p>
              </div>
              <div>
                <p className="text-3xl font-bold">{totalHours}h</p>
                <p className="text-blue-100 text-sm">Time Invested</p>
              </div>
            </div>
          </div>
          
          <ProgressRing progress={progressData.percentage} size={150} strokeWidth={10}>
            <div className="text-center">
              <p className="text-4xl font-bold">{progressData.percentage}%</p>
              <p className="text-blue-100 text-sm">Complete</p>
            </div>
          </ProgressRing>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <StatsCard
          title="Current Streak"
          value={`${streak.current} days`}
          subtitle={`Longest: ${streak.longest} days`}
          icon={Flame}
          color="orange"
        />
        <StatsCard
          title="Average Rating"
          value={avgRating}
          subtitle={`${ratingsArr.length} rated sessions`}
          icon={Star}
          color="purple"
        />
        <StatsCard
          title="Pace Status"
          value={progressData.daysAhead >= 0 ? `+${progressData.daysAhead}` : progressData.daysAhead}
          subtitle={progressData.daysAhead >= 0 ? "Days ahead" : "Days behind"}
          icon={TrendingUp}
          color={progressData.daysAhead >= 0 ? "green" : "red"}
        />
        <StatsCard
          title="Sessions with Notes"
          value={Object.values(progress.sessions).filter(s => s.notes).length}
          icon={BookOpen}
          color="blue"
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Skill Progress */}
        <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
          <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-6">
            Skill Progress
          </h3>
          
          <div className="space-y-6">
            {Object.entries(SKILL_BASELINE).map(([skill, baseline]) => {
              const current = skillProgress(baseline);
              const percentage = ((current - 1) / 4) * 100;
              
              return (
                <div key={skill}>
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-medium text-gray-700 dark:text-gray-300 capitalize">
                      {skill}
                    </span>
                    <div className="flex items-center gap-2">
                      <span className="text-sm text-gray-500 dark:text-gray-400">
                        {baseline.start}/5
                      </span>
                      <span className="text-gray-400">→</span>
                      <span className="text-sm font-bold text-blue-600 dark:text-blue-400">
                        {current.toFixed(1)}/5
                      </span>
                      <span className="text-gray-400">→</span>
                      <span className="text-sm text-gray-500 dark:text-gray-400">
                        {baseline.target}/5
                      </span>
                    </div>
                  </div>
                  <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-blue-500 to-blue-600 transition-all duration-500"
                      style={{ width: `${percentage}%` }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Certifications */}
        <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
          <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-6">
            Certifications
          </h3>
          
          <div className="space-y-4">
            {CERTIFICATIONS.map(cert => {
              const targetDate = parseISO(cert.targetDate);
              const isPast = targetDate < today;
              const daysUntil = differenceInDays(targetDate, today);
              
              return (
                <div
                  key={cert.name}
                  className={`p-4 rounded-lg border-2 ${
                    isPast
                      ? 'border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900'
                      : 'border-orange-200 dark:border-orange-800 bg-orange-50 dark:bg-orange-900/20'
                  }`}
                >
                  <div className="flex items-center gap-3">
                    <Award className={`w-8 h-8 ${
                      isPast ? 'text-gray-400' : 'text-orange-500'
                    }`} />
                    <div className="flex-1">
                      <h4 className="font-semibold text-gray-900 dark:text-white">
                        {cert.name}
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        Q{cert.quarter} • Target: {format(targetDate, 'MMMM yyyy')}
                      </p>
                    </div>
                    {!isPast && (
                      <div className="text-right">
                        <p className="text-lg font-bold text-orange-600 dark:text-orange-400">
                          {daysUntil}
                        </p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">days</p>
                      </div>
                    )}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Quarter Progress Breakdown */}
      <div className="mt-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-6">
          Progress by Quarter
        </h3>
        
        <div className="space-y-4">
          {quarterStats.map(quarter => (
            <div key={quarter.id} className="flex items-center gap-4">
              <div className="w-32 shrink-0">
                <p className="font-medium text-gray-900 dark:text-white text-sm">
                  Q{quarter.id}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400 truncate">
                  {quarter.shortName.split(': ')[1]}
                </p>
              </div>
              
              <div className="flex-1">
                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
                  <div
                    className={`h-full transition-all duration-500 ${
                      quarter.percentage === 100
                        ? 'bg-green-500'
                        : 'bg-blue-500'
                    }`}
                    style={{ width: `${quarter.percentage}%` }}
                  />
                </div>
              </div>
              
              <div className="w-20 text-right">
                <span className="font-bold text-gray-900 dark:text-white">
                  {quarter.percentage}%
                </span>
                <span className="text-gray-400 text-sm ml-1">
                  ({quarter.completed}/{quarter.total})
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
