'use client';

import { useState, useRef } from 'react';
import { useProgress } from '@/hooks/useProgress';
import { 
  Download, 
  Upload, 
  CheckCircle2,
  Copy,
  ExternalLink,
  ShieldCheck,
  Info
} from 'lucide-react';

export default function SettingsPage() {
  const { exportData, importData, completedIds, verifiedStats } = useProgress();
  const [importStatus, setImportStatus] = useState<'idle' | 'success' | 'error'>('idle');
  const [exportStatus, setExportStatus] = useState<'idle' | 'copied'>('idle');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleExport = () => {
    const data = exportData();
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `sde-tracker-notes-${new Date().toISOString().split('T')[0]}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const handleCopyToClipboard = async () => {
    const data = exportData();
    await navigator.clipboard.writeText(data);
    setExportStatus('copied');
    setTimeout(() => setExportStatus('idle'), 2000);
  };

  const handleImportClick = () => {
    fileInputRef.current?.click();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (event) => {
      const content = event.target?.result as string;
      const success = importData(content);
      setImportStatus(success ? 'success' : 'error');
      setTimeout(() => setImportStatus('idle'), 3000);
    };
    reader.readAsText(file);
    
    // Reset file input
    e.target.value = '';
  };

  return (
    <div className="p-6 max-w-2xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Settings
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-1">
          Manage your data and preferences
        </p>
      </div>

      {/* How Progress Works */}
      <div className="bg-green-50 dark:bg-green-900/20 rounded-xl border border-green-200 dark:border-green-800 p-6 mb-6">
        <div className="flex items-center gap-3 mb-3">
          <ShieldCheck className="w-6 h-6 text-green-600 dark:text-green-400" />
          <h2 className="text-lg font-bold text-green-800 dark:text-green-300">
            Verified Progress System
          </h2>
        </div>
        <p className="text-green-700 dark:text-green-400 text-sm mb-3">
          Your progress is tracked by analyzing the actual code in your workspace - no checkboxes needed. 
          Complete the exercises in your code editor, and your progress updates automatically at build time.
        </p>
        <div className="flex items-center gap-2 text-sm text-green-600 dark:text-green-500">
          <Info className="w-4 h-4" />
          <span>Progress syncs when you commit and deploy</span>
        </div>
      </div>

      {/* Current Status */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6 mb-6">
        <h2 className="text-lg font-bold text-gray-900 dark:text-white mb-4">
          Current Progress
        </h2>
        
        <div className="grid grid-cols-3 gap-4">
          <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
            <p className="text-sm text-green-600 dark:text-green-400">Verified Complete</p>
            <p className="text-2xl font-bold text-green-700 dark:text-green-300">{verifiedStats.completed}</p>
          </div>
          <div className="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
            <p className="text-sm text-blue-600 dark:text-blue-400">Total Sessions</p>
            <p className="text-2xl font-bold text-blue-700 dark:text-blue-300">416</p>
          </div>
          <div className="p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
            <p className="text-sm text-purple-600 dark:text-purple-400">Remaining</p>
            <p className="text-2xl font-bold text-purple-700 dark:text-purple-300">{416 - verifiedStats.completed}</p>
          </div>
        </div>
      </div>

      {/* Notes & Ratings Backup */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6 mb-6">
        <h2 className="text-lg font-bold text-gray-900 dark:text-white mb-4">
          Notes & Ratings Backup
        </h2>
        
        <p className="text-gray-600 dark:text-gray-400 mb-6">
          Your notes and ratings are stored locally. Export to back them up or transfer to another device.
        </p>

        <div className="space-y-4">
          {/* Export */}
          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">
            <div>
              <h3 className="font-medium text-gray-900 dark:text-white">Export Notes</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                Download your notes and ratings
              </p>
            </div>
            <div className="flex gap-2">
              <button
                onClick={handleCopyToClipboard}
                className="flex items-center gap-2 px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
              >
                {exportStatus === 'copied' ? (
                  <>
                    <CheckCircle2 className="w-4 h-4 text-green-500" />
                    Copied!
                  </>
                ) : (
                  <>
                    <Copy className="w-4 h-4" />
                    Copy
                  </>
                )}
              </button>
              <button
                onClick={handleExport}
                className="flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
              >
                <Download className="w-4 h-4" />
                Download
              </button>
            </div>
          </div>

          {/* Import */}
          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">
            <div>
              <h3 className="font-medium text-gray-900 dark:text-white">Import Notes</h3>
              <p className="text-sm text-gray-500 dark:text-gray-400">
                Restore notes from a backup file
              </p>
            </div>
            <div className="flex items-center gap-2">
              {importStatus === 'success' && (
                <span className="text-green-500 text-sm flex items-center gap-1">
                  <CheckCircle2 className="w-4 h-4" /> Imported!
                </span>
              )}
              {importStatus === 'error' && (
                <span className="text-red-500 text-sm">Invalid file</span>
              )}
              <button
                onClick={handleImportClick}
                className="flex items-center gap-2 px-4 py-2 bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
              >
                <Upload className="w-4 h-4" />
                Import
              </button>
              <input
                ref={fileInputRef}
                type="file"
                accept=".json"
                onChange={handleFileChange}
                className="hidden"
              />
            </div>
          </div>
        </div>
      </div>

      {/* Resources */}
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6 mb-6">
        <h2 className="text-lg font-bold text-gray-900 dark:text-white mb-4">
          Resources
        </h2>
        
        <div className="space-y-3">
          <a
            href="https://github.com/DataTalksClub/data-engineering-zoomcamp"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <span className="text-gray-900 dark:text-white">Data Engineering Zoomcamp (Free)</span>
            <ExternalLink className="w-4 h-4 text-gray-400" />
          </a>
          <a
            href="https://courses.getdbt.com/"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <span className="text-gray-900 dark:text-white">dbt Learn (Free)</span>
            <ExternalLink className="w-4 h-4 text-gray-400" />
          </a>
          <a
            href="https://skillbuilder.aws/"
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <span className="text-gray-900 dark:text-white">AWS Skill Builder (Free Tier)</span>
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>
      </div>

      {/* Footer */}
      <div className="mt-8 text-center text-sm text-gray-500 dark:text-gray-400">
        <p>SDE Tracker • 2-Year Senior Data Engineer Study Plan</p>
        <p className="mt-1">Built for the journey to $200k+</p>
      </div>
    </div>
  );
}
