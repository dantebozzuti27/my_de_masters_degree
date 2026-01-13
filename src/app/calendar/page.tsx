'use client';

import { useState } from 'react';
import { CalendarGrid } from '@/components/CalendarGrid';
import { SessionCard } from '@/components/SessionCard';
import { StudySession } from '@/lib/types';
import { X } from 'lucide-react';

export default function CalendarPage() {
  const [selectedSession, setSelectedSession] = useState<StudySession | null>(null);

  return (
    <div className="p-6 max-w-6xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Calendar
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          View and track all 416 study sessions
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Calendar */}
        <div className="lg:col-span-2">
          <CalendarGrid onSelectSession={setSelectedSession} />
        </div>

        {/* Selected Session */}
        <div>
          <h2 className="text-lg font-bold text-gray-900 dark:text-white mb-4">
            Session Details
          </h2>
          
          {selectedSession ? (
            <div className="relative">
              <button
                onClick={() => setSelectedSession(null)}
                className="absolute -top-2 -right-2 p-1 bg-gray-200 dark:bg-gray-700 rounded-full hover:bg-gray-300 dark:hover:bg-gray-600 z-10"
              >
                <X className="w-4 h-4 text-gray-600 dark:text-gray-400" />
              </button>
              <SessionCard session={selectedSession} variant="full" />
            </div>
          ) : (
            <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-8 text-center">
              <p className="text-gray-500 dark:text-gray-400">
                Click on a study day to view session details
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
