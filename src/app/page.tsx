'use client';

import { useProgress } from '@/hooks/useProgress';
import { getAllSessions, getCurrentWeekSessions } from '@/lib/sessions';
import { QUARTERS } from '@/lib/curriculum';
import { SessionCard } from '@/components/SessionCard';
import { StatsCard } from '@/components/StatsCard';
import { ProgressRing } from '@/components/ProgressRing';
import { WeekView } from '@/components/WeekView';
import { QuarterProgress } from '@/components/QuarterProgress';
import { format, differenceInDays } from 'date-fns';
import { 
  Calendar, 
  Clock, 
  ChevronRight,
  Zap,
  ShieldCheck
} from 'lucide-react';
import Link from 'next/link';

export default function Dashboard() {
  const { completedIds, verifiedStats, isLoading } = useProgress();
  
  const allSessions = getAllSessions();
  const currentWeekSessions = getCurrentWeekSessions();
  
  // Find the next incomplete session (for users who work ahead)
  const nextSession = allSessions.find(s => !completedIds.has(s.id));
  
  // Calculate days until end
  const endDate = new Date(2028, 0, 8);
  const daysRemaining = differenceInDays(endDate, new Date());
  
  // Calculate progress based on verified completion
  const totalSessions = allSessions.length;
  const completedCount = completedIds.size;
  const progressPercentage = Math.round((completedCount / totalSessions) * 100);
  
  // Find current quarter based on next session
  const currentQuarter = nextSession 
    ? QUARTERS.find(q => q.id === nextSession.quarterId)
    : QUARTERS[0];

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Welcome back
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          {format(new Date(), 'EEEE, MMMM d, yyyy')}
        </p>
      </div>

      {/* Verified Progress Banner */}
      <div className="mb-8 bg-gradient-to-r from-green-600 to-emerald-600 rounded-xl p-6 text-white">
        <div className="flex items-center gap-3 mb-4">
          <ShieldCheck className="w-8 h-8" />
          <div>
            <h2 className="text-xl font-bold">Verified Progress</h2>
            <p className="text-green-100 text-sm">Based on actual code in your workspace</p>
          </div>
        </div>
        
        <div className="grid grid-cols-3 gap-4 mb-4">
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <p className="text-3xl font-bold">{verifiedStats.completed}</p>
            <p className="text-green-100 text-sm">Days Complete</p>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <p className="text-3xl font-bold">{totalSessions}</p>
            <p className="text-green-100 text-sm">Total Sessions</p>
          </div>
          <div className="bg-white/10 rounded-lg p-3 text-center">
            <p className="text-3xl font-bold">{progressPercentage}%</p>
            <p className="text-green-100 text-sm">Complete</p>
          </div>
        </div>
        
        <div className="h-3 bg-white/20 rounded-full overflow-hidden">
          <div 
            className="h-full bg-white transition-all duration-500"
            style={{ width: `${progressPercentage}%` }}
          />
        </div>
      </div>

      {/* Progress Overview */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
        <div className="bg-white dark:bg-gray-800 rounded-xl p-6 border border-gray-200 dark:border-gray-700">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-500 dark:text-gray-400">Overall Progress</p>
              <p className="text-3xl font-bold text-gray-900 dark:text-white mt-1">
                {progressPercentage}%
              </p>
              <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
                {completedCount} of {totalSessions} sessions
              </p>
            </div>
            <ProgressRing progress={progressPercentage} size={80} strokeWidth={6}>
              <span className="text-lg font-bold text-gray-900 dark:text-white">
                {progressPercentage}%
              </span>
            </ProgressRing>
          </div>
        </div>
        
        <StatsCard
          title="Sessions This Week"
          value={`${currentWeekSessions.filter(s => completedIds.has(s.id)).length}/${currentWeekSessions.length}`}
          icon={Calendar}
          color="blue"
        />
        
        <StatsCard
          title="Days Remaining"
          value={daysRemaining}
          subtitle="Until program end"
          icon={Clock}
          color="purple"
        />
      </div>

      {/* Next Session */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
            <Zap className="w-5 h-5 text-yellow-500" />
            Next Up
          </h2>
          {nextSession && (
            <span className="text-sm text-gray-500 dark:text-gray-400">
              Day {nextSession.dayNumber} of {totalSessions}
            </span>
          )}
        </div>
        
        {nextSession ? (
          <SessionCard session={nextSession} variant="full" />
        ) : (
          <div className="bg-green-50 dark:bg-green-900/20 rounded-xl border border-green-200 dark:border-green-700 p-8 text-center">
            <ShieldCheck className="w-12 h-12 text-green-500 mx-auto mb-4" />
            <h3 className="text-lg font-semibold text-green-800 dark:text-green-300 mb-2">
              All Sessions Complete!
            </h3>
            <p className="text-green-600 dark:text-green-400">
              You've completed the entire 2-year program. Congratulations!
            </p>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* This Week */}
        <div className="lg:col-span-2">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-bold text-gray-900 dark:text-white">
              This Week
            </h2>
            <Link 
              href="/calendar"
              className="text-sm text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
            >
              View Calendar
              <ChevronRight className="w-4 h-4" />
            </Link>
          </div>
          
          <WeekView 
            sessions={currentWeekSessions}
            weekNumber={currentWeekSessions[0]?.weekNumber ?? 1}
          />
        </div>

        {/* Quarter Progress */}
        <div>
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-xl font-bold text-gray-900 dark:text-white">
              Quarters
            </h2>
            <Link 
              href="/curriculum"
              className="text-sm text-blue-600 dark:text-blue-400 hover:underline flex items-center gap-1"
            >
              View All
              <ChevronRight className="w-4 h-4" />
            </Link>
          </div>
          
          <QuarterProgress />
        </div>
      </div>

      {/* Next Sessions in Queue */}
      <div className="mt-8">
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold text-gray-900 dark:text-white">
            Coming Up Next
          </h2>
        </div>
        
        <div className="grid gap-3">
          {allSessions
            .filter(s => !completedIds.has(s.id))
            .slice(1, 6)
            .map(session => (
              <SessionCard
                key={session.id}
                session={session}
                variant="compact"
              />
            ))}
        </div>
      </div>

      {/* Current Quarter Info */}
      {currentQuarter && (
        <div className="mt-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl p-6 text-white">
          <div className="flex items-start justify-between">
            <div>
              <p className="text-blue-100 text-sm font-medium">Currently in</p>
              <h3 className="text-2xl font-bold mt-1">{currentQuarter.name}</h3>
              <p className="text-blue-100 mt-2">{currentQuarter.goal}</p>
              
              <div className="mt-4 flex flex-wrap gap-2">
                <span className="px-3 py-1 bg-white/20 rounded-full text-sm">
                  Project: {currentQuarter.project}
                </span>
                {currentQuarter.certification && (
                  <span className="px-3 py-1 bg-yellow-400/30 rounded-full text-sm">
                    Cert: {currentQuarter.certification}
                  </span>
                )}
              </div>
            </div>
            
            <div className="text-right">
              <p className="text-4xl font-bold">{daysRemaining}</p>
              <p className="text-blue-100 text-sm">days remaining</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
