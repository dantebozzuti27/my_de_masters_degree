'use client';

import React, { createContext, useContext, useState, useEffect, useCallback, ReactNode } from 'react';
import { UserProgress, SessionProgress } from '@/lib/types';
import {
  getStoredProgress,
  saveProgress,
  initializeProgress,
  updateSessionNotes,
  updateSessionRating,
  exportProgress,
  importProgress
} from '@/lib/storage';
import { getAllSessions } from '@/lib/sessions';
import { getVerifiedCompletedDays, getVerifiedProgress } from '@/lib/verified-progress';

interface ProgressContextType {
  progress: UserProgress;
  isLoading: boolean;
  completedIds: Set<string>;
  completedDays: number[];
  verifiedStats: { completed: number; total: number; percentage: number };
  
  // Actions (notes/ratings only - completion is verified by code)
  setNotes: (sessionId: string, notes: string) => void;
  setRating: (sessionId: string, rating: 1 | 2 | 3 | 4 | 5) => void;
  
  // Import/Export (for notes/ratings)
  exportData: () => string;
  importData: (json: string) => boolean;
}

const ProgressContext = createContext<ProgressContextType | null>(null);

export function ProgressProvider({ children }: { children: ReactNode }) {
  const [progress, setProgress] = useState<UserProgress>(initializeProgress());
  const [isLoading, setIsLoading] = useState(true);
  
  // Verified progress is the source of truth
  const verifiedDays = getVerifiedCompletedDays();
  const verifiedStats = getVerifiedProgress();
  const completedIds = new Set(verifiedDays.map(day => `session-${day}`));

  // Load notes/ratings from localStorage on mount
  useEffect(() => {
    const stored = getStoredProgress();
    if (stored) {
      setProgress(stored);
    }
    setIsLoading(false);
  }, []);

  // Save notes/ratings to localStorage
  useEffect(() => {
    if (!isLoading) {
      saveProgress(progress);
    }
  }, [progress, isLoading]);

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

  return (
    <ProgressContext.Provider
      value={{
        progress,
        isLoading,
        completedIds,
        completedDays: verifiedDays,
        verifiedStats,
        setNotes,
        setRating,
        exportData,
        importData: importDataFn
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
