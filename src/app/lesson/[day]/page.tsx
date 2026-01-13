'use client';

import { useParams, useRouter } from 'next/navigation';
import { getSessionById, getAllSessions } from '@/lib/sessions';
import { LessonDetail } from '@/components/LessonDetail';
import { ChevronLeft, ChevronRight } from 'lucide-react';
import Link from 'next/link';

export default function LessonPage() {
  const params = useParams();
  const router = useRouter();
  const dayNumber = parseInt(params.day as string);
  
  const allSessions = getAllSessions();
  const session = allSessions.find(s => s.dayNumber === dayNumber);
  
  if (!session) {
    return (
      <div className="p-6 max-w-4xl mx-auto">
        <div className="text-center py-12">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
            Session Not Found
          </h1>
          <p className="text-gray-600 dark:text-gray-400 mb-6">
            Day {dayNumber} doesn't exist in the curriculum.
          </p>
          <Link
            href="/curriculum"
            className="text-blue-600 hover:text-blue-700 dark:text-blue-400"
          >
            Back to Curriculum
          </Link>
        </div>
      </div>
    );
  }

  const prevSession = allSessions.find(s => s.dayNumber === dayNumber - 1);
  const nextSession = allSessions.find(s => s.dayNumber === dayNumber + 1);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      {/* Navigation */}
      <div className="flex items-center justify-between mb-6">
        <Link
          href="/curriculum"
          className="text-blue-600 hover:text-blue-700 dark:text-blue-400 flex items-center gap-1"
        >
          <ChevronLeft className="w-4 h-4" />
          Curriculum
        </Link>
        
        <div className="flex items-center gap-4">
          {prevSession && (
            <button
              onClick={() => router.push(`/lesson/${dayNumber - 1}`)}
              className="flex items-center gap-1 text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
            >
              <ChevronLeft className="w-4 h-4" />
              Day {dayNumber - 1}
            </button>
          )}
          
          <span className="text-gray-400">|</span>
          
          {nextSession && (
            <button
              onClick={() => router.push(`/lesson/${dayNumber + 1}`)}
              className="flex items-center gap-1 text-gray-600 hover:text-gray-900 dark:text-gray-400 dark:hover:text-white"
            >
              Day {dayNumber + 1}
              <ChevronRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </div>

      {/* Lesson Content */}
      <LessonDetail session={session} />

      {/* Bottom Navigation */}
      <div className="flex items-center justify-between mt-8 pt-6 border-t border-gray-200 dark:border-gray-700">
        {prevSession ? (
          <button
            onClick={() => router.push(`/lesson/${dayNumber - 1}`)}
            className="flex items-center gap-2 px-4 py-2 bg-gray-100 dark:bg-gray-800 rounded-lg hover:bg-gray-200 dark:hover:bg-gray-700 transition-colors"
          >
            <ChevronLeft className="w-5 h-5" />
            <div className="text-left">
              <p className="text-xs text-gray-500 dark:text-gray-400">Previous</p>
              <p className="font-medium text-gray-900 dark:text-white">Day {dayNumber - 1}</p>
            </div>
          </button>
        ) : <div />}
        
        {nextSession ? (
          <button
            onClick={() => router.push(`/lesson/${dayNumber + 1}`)}
            className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
          >
            <div className="text-right">
              <p className="text-xs text-blue-200">Next</p>
              <p className="font-medium">Day {dayNumber + 1}</p>
            </div>
            <ChevronRight className="w-5 h-5" />
          </button>
        ) : (
          <div className="px-4 py-2 bg-green-600 text-white rounded-lg">
            Curriculum Complete!
          </div>
        )}
      </div>
    </div>
  );
}
