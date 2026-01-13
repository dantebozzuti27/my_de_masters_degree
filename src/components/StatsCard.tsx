'use client';

import { LucideIcon } from 'lucide-react';

interface StatsCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  icon: LucideIcon;
  color?: 'blue' | 'green' | 'purple' | 'orange' | 'red';
}

const colorClasses = {
  blue: 'bg-blue-100 text-blue-600 dark:bg-blue-900 dark:text-blue-300',
  green: 'bg-green-100 text-green-600 dark:bg-green-900 dark:text-green-300',
  purple: 'bg-purple-100 text-purple-600 dark:bg-purple-900 dark:text-purple-300',
  orange: 'bg-orange-100 text-orange-600 dark:bg-orange-900 dark:text-orange-300',
  red: 'bg-red-100 text-red-600 dark:bg-red-900 dark:text-red-300'
};

export function StatsCard({ title, value, subtitle, icon: Icon, color = 'blue' }: StatsCardProps) {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 border border-gray-200 dark:border-gray-700">
      <div className="flex items-center gap-4">
        <div className={`p-3 rounded-lg ${colorClasses[color]}`}>
          <Icon className="w-6 h-6" />
        </div>
        <div>
          <p className="text-sm text-gray-500 dark:text-gray-400">{title}</p>
          <p className="text-2xl font-bold text-gray-900 dark:text-white">{value}</p>
          {subtitle && (
            <p className="text-sm text-gray-500 dark:text-gray-400">{subtitle}</p>
          )}
        </div>
      </div>
    </div>
  );
}
