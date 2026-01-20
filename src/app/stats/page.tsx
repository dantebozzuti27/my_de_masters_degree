'use client';

import { useProgress } from '@/hooks/useProgress';
import { getAllSessions, getSessionsByQuarter, getProgramSummary, getTimeForDay } from '@/lib/sessions';
import { QUARTERS, SKILL_BASELINE, CERTIFICATIONS } from '@/lib/curriculum';
import { StatsCard } from '@/components/StatsCard';
import { ProgressRing } from '@/components/ProgressRing';
import { 
  Clock, 
  Star,
  TrendingUp,
  Award,
  BookOpen,
  ShieldCheck,
  Calendar,
  Target
} from 'lucide-react';

export default function StatsPage() {
  const { completedIds, verifiedStats, progress } = useProgress();
  
  const allSessions = getAllSessions();
  const programSummary = getProgramSummary();
  const completedCount = completedIds.size;
  const totalSessions = allSessions.length;
  const progressPercentage = Math.round((completedCount / totalSessions) * 100);
  
  // Calculate time invested based on completed sessions and their day types
  let totalMinutesInvested = 0;
  allSessions.forEach(session => {
    if (completedIds.has(session.id)) {
      const time = getTimeForDay(session.dayOfWeek ?? 0);
      totalMinutesInvested += time.handson;
    }
  });
  const totalHoursInvested = Math.round(totalMinutesInvested / 60);
  
  // Sessions remaining
  const sessionsRemaining = totalSessions - completedCount;
  
  // Calculate average rating
  const ratingsArr = Object.values(progress.sessions)
    .filter(s => s.rating)
    .map(s => s.rating as number);
  const avgRating = ratingsArr.length > 0
    ? (ratingsArr.reduce((a, b) => a + b, 0) / ratingsArr.length).toFixed(1)
    : 'N/A';
  
  // Calculate skill progress (linear interpolation based on progress)
  const skillProgress = (baseline: { start: number; target: number }) => {
    const progressPct = progressPercentage / 100;
    return baseline.start + (baseline.target - baseline.start) * progressPct;
  };

  // Completion by month
  const monthStats = QUARTERS.map(month => {
    const sessions = getSessionsByQuarter(month.id);
    const completed = sessions.filter(s => completedIds.has(s.id)).length;
    return {
      ...month,
      completed,
      total: sessions.length,
      percentage: sessions.length > 0 ? Math.round((completed / sessions.length) * 100) : 0
    };
  });

  // Weekly breakdown for current week
  const currentWeek = Math.ceil((completedCount + 1) / 7);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Statistics
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          6-Month Aggressive Plan Progress
        </p>
      </div>

      {/* Overall Progress Card */}
      <div className="bg-gradient-to-r from-green-600 to-emerald-600 rounded-xl p-8 text-white mb-8">
        <div className="flex items-center justify-between">
          <div>
            <div className="flex items-center gap-2 mb-2">
              <ShieldCheck className="w-6 h-6" />
              <h2 className="text-2xl font-bold">Verified Progress</h2>
            </div>
            <p className="text-green-100 mt-1">
              {completedCount} of {totalSessions} days completed
            </p>
            
            <div className="mt-6 grid grid-cols-3 gap-6">
              <div>
                <p className="text-3xl font-bold">{currentWeek}</p>
                <p className="text-green-100 text-sm">Current Week</p>
              </div>
              <div>
                <p className="text-3xl font-bold">{sessionsRemaining}</p>
                <p className="text-green-100 text-sm">Days Remaining</p>
              </div>
              <div>
                <p className="text-3xl font-bold">{totalHoursInvested}h</p>
                <p className="text-green-100 text-sm">Time Invested</p>
              </div>
            </div>
          </div>
          
          <ProgressRing progress={progressPercentage} size={150} strokeWidth={10}>
            <div className="text-center">
              <p className="text-4xl font-bold">{progressPercentage}%</p>
              <p className="text-green-100 text-sm">Complete</p>
            </div>
          </ProgressRing>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <StatsCard
          title="Verified Days"
          value={verifiedStats.completed}
          subtitle="With committed code"
          icon={ShieldCheck}
          color="green"
        />
        <StatsCard
          title="Average Rating"
          value={avgRating}
          subtitle={`${ratingsArr.length} rated sessions`}
          icon={Star}
          color="purple"
        />
        <StatsCard
          title="Total Hours"
          value={`${programSummary.totalHours}h`}
          subtitle={`${programSummary.handsOnHours}h hands-on`}
          icon={Clock}
          color="blue"
        />
        <StatsCard
          title="Weekly Pace"
          value={`${programSummary.avgHoursPerWeek}h/wk`}
          subtitle="27-30h sustainable"
          icon={TrendingUp}
          color="orange"
        />
      </div>

      {/* Weekly Time Breakdown */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6 mb-8">
        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
          <Calendar className="w-5 h-5 text-blue-500" />
          Weekly Time Breakdown
        </h3>
        
        <div className="grid grid-cols-7 gap-2">
          {[
            { day: 'Mon', hours: '3.5-4h', work: '2-2.5h', passive: '1-1.5h', type: 'Office' },
            { day: 'Tue', hours: '4h', work: '2-2.5h', passive: '1.5h', type: 'WFH' },
            { day: 'Wed', hours: '3.5-4h', work: '2-2.5h', passive: '1-1.5h', type: 'Office' },
            { day: 'Thu', hours: '4h', work: '2-2.5h', passive: '1.5h', type: 'WFH' },
            { day: 'Fri', hours: '3.5-4h', work: '2-2.5h', passive: '1-1.5h', type: 'Office' },
            { day: 'Sat', hours: '6-7h', work: '6-7h', passive: '-', type: 'Project' },
            { day: 'Sun', hours: '3-4h', work: '3-4h', passive: '-', type: 'Light' },
          ].map((d, i) => (
            <div 
              key={d.day} 
              className={`p-3 rounded-lg text-center ${
                i === 5 ? 'bg-purple-100 dark:bg-purple-900/30' :
                i === 6 ? 'bg-blue-100 dark:bg-blue-900/30' :
                'bg-gray-50 dark:bg-gray-900'
              }`}
            >
              <p className="font-bold text-gray-900 dark:text-white">{d.day}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400 mb-1">{d.type}</p>
              <p className="text-sm font-medium text-blue-600 dark:text-blue-400">{d.hours}</p>
              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                {d.work} work
              </p>
              {d.passive !== '-' && (
                <p className="text-xs text-gray-400">
                  {d.passive} audio
                </p>
              )}
            </div>
          ))}
        </div>
        
        <div className="mt-4 text-center text-sm text-gray-600 dark:text-gray-400">
          <span className="font-bold text-gray-900 dark:text-white">27-30 hours/week</span> • Sustainable maximum intensity
        </div>
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
                      {skill === 'systemDesign' ? 'System Design' : skill}
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
            Certification Targets
          </h3>
          
          <div className="space-y-4">
            {CERTIFICATIONS.map(cert => {
              const monthNum = cert.quarter;
              const monthData = QUARTERS.find(q => q.id === monthNum);
              
              return (
                <div
                  key={cert.name}
                  className="p-4 rounded-lg border-2 border-orange-200 dark:border-orange-800 bg-orange-50 dark:bg-orange-900/20"
                >
                  <div className="flex items-center gap-3">
                    <Award className="w-8 h-8 text-orange-500" />
                    <div className="flex-1">
                      <h4 className="font-semibold text-gray-900 dark:text-white">
                        {cert.name}
                      </h4>
                      <p className="text-sm text-gray-500 dark:text-gray-400">
                        Month {monthNum} • {monthData?.shortName}
                      </p>
                    </div>
                    <Target className="w-5 h-5 text-orange-400" />
                  </div>
                </div>
              );
            })}
          </div>
          
          <div className="mt-6 p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">
            <div className="flex items-center gap-2 mb-2">
              <Target className="w-5 h-5 text-green-500" />
              <h4 className="font-semibold text-gray-900 dark:text-white">
                End Goal
              </h4>
            </div>
            <p className="text-gray-600 dark:text-gray-400">
              Land <span className="font-bold text-green-600 dark:text-green-400">$160-170k</span> Data Engineer role by July 2026
            </p>
          </div>
        </div>
      </div>

      {/* Month Progress Breakdown */}
      <div className="mt-8 bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
        <h3 className="text-lg font-bold text-gray-900 dark:text-white mb-6">
          Progress by Month
        </h3>
        
        <div className="space-y-4">
          {monthStats.map(month => (
            <div key={month.id} className="flex items-center gap-4">
              <div className="w-32 shrink-0">
                <p className="font-medium text-gray-900 dark:text-white text-sm">
                  Month {month.id}
                </p>
                <p className="text-xs text-gray-500 dark:text-gray-400 truncate">
                  {month.shortName.split(': ')[1]}
                </p>
              </div>
              
              <div className="flex-1">
                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
                  <div
                    className={`h-full transition-all duration-500 ${
                      month.percentage === 100
                        ? 'bg-green-500'
                        : month.percentage > 0
                        ? 'bg-blue-500'
                        : 'bg-gray-300 dark:bg-gray-600'
                    }`}
                    style={{ width: `${Math.max(month.percentage, 2)}%` }}
                  />
                </div>
              </div>
              
              <div className="w-24 text-right">
                <span className="font-bold text-gray-900 dark:text-white">
                  {month.percentage}%
                </span>
                <span className="text-gray-400 text-sm ml-1">
                  ({month.completed}/{month.total})
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
