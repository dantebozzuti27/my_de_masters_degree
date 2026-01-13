'use client';

import React, { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';
import { UserProgress, SessionProgress } from '@/lib/types';
import {
  getStoredProgress,
  saveProgress,
  initializeProgress,
  markSessionComplete,
  markSessionIncomplete,
  updateSessionNotes,
  updateSessionRating,
  getCompletedSessionIds,
  calculateStreak,
  exportProgress,
  importProgress
} from '@/lib/storage';
import { getAllSessions } from '@/lib/sessions';

interface ProgressContextType {
  progress: UserProgress;
  isLoading: boolean;
  completedIds: Set<string>;
  streak: { current: number; longest: number };
  
  // Actions
  toggleSession: (sessionId: string) => void;
  completeSession: (sessionId: string, data?: Partial<SessionProgress>) => void;
  uncompleteSession: (sessionId: string) => void;
  setNotes: (sessionId: string, notes: string) => void;
  setRating: (sessionId: string, rating: 1 | 2 | 3 | 4 | 5) => void;
  
  // Import/Export
  exportData: () => string;
  importData: (json: string) => boolean;
  resetProgress: () => void;
}

const ProgressContext = createContext<ProgressContextType | null>(null);

export function ProgressProvider({ children }: { children: ReactNode }) {
  const [progress, setProgress] = useState<UserProgress>(initializeProgress());
  const [isLoading, setIsLoading] = useState(true);
  const [completedIds, setCompletedIds] = useState<Set<string>>(new Set());
  const [streak, setStreak] = useState({ current: 0, longest: 0 });

  // Load from localStorage on mount
  useEffect(() => {
    const stored = getStoredProgress();
    if (stored) {
      setProgress(stored);
      setCompletedIds(getCompletedSessionIds(stored));
      
      const allDates = getAllSessions().map(s => s.date);
      setStreak(calculateStreak(stored, allDates));
    }
    setIsLoading(false);
  }, []);

  // Save to localStorage whenever progress changes
  useEffect(() => {
    if (!isLoading) {
      saveProgress(progress);
      setCompletedIds(getCompletedSessionIds(progress));
      
      const allDates = getAllSessions().map(s => s.date);
      setStreak(calculateStreak(progress, allDates));
    }
  }, [progress, isLoading]);

  const toggleSession = useCallback((sessionId: string) => {
    setProgress(prev => {
      if (prev.sessions[sessionId]?.completed) {
        return markSessionIncomplete(prev, sessionId);
      } else {
        return markSessionComplete(prev, sessionId);
      }
    });
  }, []);

  const completeSession = useCallback((sessionId: string, data?: Partial<SessionProgress>) => {
    setProgress(prev => markSessionComplete(prev, sessionId, data));
  }, []);

  const uncompleteSession = useCallback((sessionId: string) => {
    setProgress(prev => markSessionIncomplete(prev, sessionId));
  }, []);

  const setNotes = useCallback((sessionId: string, notes: string) => {
    setProgress(prev => updateSessionNotes(prev, sessionId, notes));
  }, []);

  const setRating = useCallback((sessionId: string, rating: 1 | 2 | 3 | 4 | 5) => {
    setProgress(prev => updateSessionRating(prev, sessionId, rating));
  }, []);

  const exportData = useCallback(() => {
    return exportProgress(progress);
  }, [progress]);

  const importDataFn = useCallback((json: string): boolean => {
    const imported = importProgress(json);
    if (imported) {
      setProgress(imported);
      return true;
    }
    return false;
  }, []);

  const resetProgress = useCallback(() => {
    const fresh = initializeProgress();
    setProgress(fresh);
  }, []);

  return (
    <ProgressContext.Provider
      value={{
        progress,
        isLoading,
        completedIds,
        streak,
        toggleSession,
        completeSession,
        uncompleteSession,
        setNotes,
        setRating,
        exportData,
        importData: importDataFn,
        resetProgress
      }}
    >
      {children}
    </ProgressContext.Provider>
  );
}

export function useProgress() {
  const context = useContext(ProgressContext);
  if (!context) {
    throw new Error('useProgress must be used within a ProgressProvider');
  }
  return context;
}
