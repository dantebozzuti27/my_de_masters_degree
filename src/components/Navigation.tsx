'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Home, Calendar, BarChart3, Settings, BookOpen } from 'lucide-react';

const navItems = [
  { href: '/', label: 'Dashboard', icon: Home },
  { href: '/calendar', label: 'Calendar', icon: Calendar },
  { href: '/curriculum', label: 'Curriculum', icon: BookOpen },
  { href: '/stats', label: 'Statistics', icon: BarChart3 },
  { href: '/settings', label: 'Settings', icon: Settings },
];

export function Navigation() {
  const pathname = usePathname();

  return (
    <nav className="fixed bottom-0 left-0 right-0 bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-800 md:static md:border-t-0 md:border-r md:h-screen md:w-64 z-50">
      {/* Desktop header */}
      <div className="hidden md:block p-6 border-b border-gray-200 dark:border-gray-800">
        <h1 className="text-xl font-bold text-gray-900 dark:text-white">
          SDE Tracker
        </h1>
        <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
          Your path to $200k+
        </p>
      </div>

      {/* Navigation items */}
      <div className="flex md:flex-col md:p-4">
        {navItems.map(({ href, label, icon: Icon }) => {
          const isActive = pathname === href;
          
          return (
            <Link
              key={href}
              href={href}
              className={`flex-1 md:flex-none flex flex-col md:flex-row items-center md:gap-3 p-3 md:px-4 md:py-3 md:rounded-lg transition-colors ${
                isActive
                  ? 'text-blue-600 dark:text-blue-400 md:bg-blue-50 md:dark:bg-blue-900/20'
                  : 'text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white md:hover:bg-gray-100 md:dark:hover:bg-gray-800'
              }`}
            >
              <Icon className="w-6 h-6" />
              <span className="text-xs md:text-sm font-medium mt-1 md:mt-0">{label}</span>
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
