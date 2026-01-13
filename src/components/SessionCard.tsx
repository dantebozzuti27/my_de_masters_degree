'use client';

import { StudySession } from '@/lib/types';
import { QUARTERS } from '@/lib/curriculum';
import { getDayLabel } from '@/lib/sessions';
import { useProgress } from '@/hooks/useProgress';
import { format, parseISO } from 'date-fns';
import { CheckCircle2, Circle, Calendar, Target, BookOpen, Star } from 'lucide-react';
import { useState } from 'react';

interface SessionCardProps {
  session: StudySession;
  variant?: 'compact' | 'full';
  showDate?: boolean;
}

export function SessionCard({ session, variant = 'full', showDate = true }: SessionCardProps) {
  const { progress, toggleSession, setRating, setNotes } = useProgress();
  const [showNotes, setShowNotes] = useState(false);
  const [noteText, setNoteText] = useState(progress.sessions[session.id]?.notes || '');
  
  const isCompleted = progress.sessions[session.id]?.completed ?? false;
  const sessionProgress = progress.sessions[session.id];
  const quarter = QUARTERS.find(q => q.id === session.quarterId);
  
  const handleToggle = () => {
    toggleSession(session.id);
  };

  const handleRating = (rating: 1 | 2 | 3 | 4 | 5) => {
    setRating(session.id, rating);
  };

  const handleNoteSave = () => {
    setNotes(session.id, noteText);
    setShowNotes(false);
  };

  if (variant === 'compact') {
    return (
      <div 
        className={`flex items-center gap-3 p-3 rounded-lg border transition-all cursor-pointer hover:shadow-md ${
          isCompleted 
            ? 'bg-green-50 border-green-200 dark:bg-green-900/20 dark:border-green-800' 
            : 'bg-white border-gray-200 dark:bg-gray-800 dark:border-gray-700'
        }`}
        onClick={handleToggle}
      >
        {isCompleted ? (
          <CheckCircle2 className="w-5 h-5 text-green-500 flex-shrink-0" />
        ) : (
          <Circle className="w-5 h-5 text-gray-400 flex-shrink-0" />
        )}
        <div className="flex-1 min-w-0">
          <p className={`font-medium truncate ${isCompleted ? 'text-green-700 dark:text-green-300' : 'text-gray-900 dark:text-white'}`}>
            {session.topic}
          </p>
          {showDate && (
            <p className="text-sm text-gray-500 dark:text-gray-400">
              {getDayLabel(session.dayOfWeek)} • {format(parseISO(session.date), 'MMM d, yyyy')}
            </p>
          )}
        </div>
        <span className="text-xs font-medium text-gray-500 dark:text-gray-400">
          Day {session.dayNumber}
        </span>
      </div>
    );
  }

  return (
    <div className={`rounded-xl border-2 p-6 transition-all ${
      isCompleted 
        ? 'bg-green-50 border-green-300 dark:bg-green-900/20 dark:border-green-700' 
        : 'bg-white border-gray-200 dark:bg-gray-800 dark:border-gray-700'
    }`}>
      {/* Header */}
      <div className="flex items-start justify-between mb-4">
        <div>
          <div className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-1">
            <Calendar className="w-4 h-4" />
            <span>{getDayLabel(session.dayOfWeek)}, {format(parseISO(session.date), 'MMMM d, yyyy')}</span>
          </div>
          <h3 className="text-xl font-bold text-gray-900 dark:text-white">
            {session.topic}
          </h3>
        </div>
        <button
          onClick={handleToggle}
          className={`p-2 rounded-full transition-colors ${
            isCompleted 
              ? 'bg-green-100 text-green-600 hover:bg-green-200 dark:bg-green-800 dark:text-green-300' 
              : 'bg-gray-100 text-gray-400 hover:bg-gray-200 dark:bg-gray-700 dark:hover:bg-gray-600'
          }`}
        >
          {isCompleted ? (
            <CheckCircle2 className="w-8 h-8" />
          ) : (
            <Circle className="w-8 h-8" />
          )}
        </button>
      </div>

      {/* Meta info */}
      <div className="flex flex-wrap gap-2 mb-4">
        <span className="px-3 py-1 bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300 rounded-full text-sm font-medium">
          Day {session.dayNumber} of 416
        </span>
        <span className="px-3 py-1 bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300 rounded-full text-sm font-medium">
          Week {session.weekNumber}
        </span>
        <span className="px-3 py-1 bg-orange-100 text-orange-700 dark:bg-orange-900 dark:text-orange-300 rounded-full text-sm font-medium">
          {quarter?.shortName}
        </span>
      </div>

      {/* Quarter info */}
      <div className="bg-gray-50 dark:bg-gray-900 rounded-lg p-4 mb-4">
        <div className="flex items-start gap-2">
          <Target className="w-5 h-5 text-gray-500 mt-0.5" />
          <div>
            <p className="text-sm font-medium text-gray-700 dark:text-gray-300">Quarter Goal</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">{quarter?.goal}</p>
          </div>
        </div>
        <div className="flex items-start gap-2 mt-3">
          <BookOpen className="w-5 h-5 text-gray-500 mt-0.5" />
          <div>
            <p className="text-sm font-medium text-gray-700 dark:text-gray-300">Side Project</p>
            <p className="text-sm text-gray-600 dark:text-gray-400">{quarter?.project}</p>
          </div>
        </div>
      </div>

      {/* Rating */}
      {isCompleted && (
        <div className="mb-4">
          <p className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">How was this session?</p>
          <div className="flex gap-1">
            {[1, 2, 3, 4, 5].map((star) => (
              <button
                key={star}
                onClick={() => handleRating(star as 1 | 2 | 3 | 4 | 5)}
                className="p-1 transition-transform hover:scale-110"
              >
                <Star
                  className={`w-6 h-6 ${
                    (sessionProgress?.rating ?? 0) >= star
                      ? 'fill-yellow-400 text-yellow-400'
                      : 'text-gray-300 dark:text-gray-600'
                  }`}
                />
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Notes */}
      <div>
        <button
          onClick={() => setShowNotes(!showNotes)}
          className="text-sm text-blue-600 hover:text-blue-700 dark:text-blue-400 font-medium"
        >
          {showNotes ? 'Hide Notes' : (sessionProgress?.notes ? 'Edit Notes' : 'Add Notes')}
        </button>
        
        {showNotes && (
          <div className="mt-3">
            <textarea
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              placeholder="Add your notes, learnings, or reflections..."
              className="w-full p-3 border border-gray-300 dark:border-gray-600 rounded-lg text-sm bg-white dark:bg-gray-900 text-gray-900 dark:text-white resize-none"
              rows={4}
            />
            <div className="flex gap-2 mt-2">
              <button
                onClick={handleNoteSave}
                className="px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700"
              >
                Save Notes
              </button>
              <button
                onClick={() => setShowNotes(false)}
                className="px-4 py-2 bg-gray-200 text-gray-700 dark:bg-gray-700 dark:text-gray-300 rounded-lg text-sm font-medium hover:bg-gray-300 dark:hover:bg-gray-600"
              >
                Cancel
              </button>
            </div>
          </div>
        )}
        
        {!showNotes && sessionProgress?.notes && (
          <p className="mt-2 text-sm text-gray-600 dark:text-gray-400 italic">
            "{sessionProgress.notes.substring(0, 100)}{sessionProgress.notes.length > 100 ? '...' : ''}"
          </p>
        )}
      </div>
    </div>
  );
}
