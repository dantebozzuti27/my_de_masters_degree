'use client';

import { getDayMedia, Audiobook } from '@/lib/media-resources';
import { Play, Headphones, ExternalLink, Clock, Youtube, BookOpen } from 'lucide-react';

interface MediaSectionProps {
  dayNumber: number;
}

export function MediaSection({ dayNumber }: MediaSectionProps) {
  const { video, podcasts, audiobooks, isNewPodcastDay, isFirstDayOfQuarter } = getDayMedia(dayNumber);
  const weekNumber = Math.ceil(dayNumber / 4);
  
  return (
    <div className="space-y-6">
      {/* Daily Video */}
      {video && (
        <div className="bg-gradient-to-r from-red-600 to-red-700 rounded-xl p-6 text-white">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-2 bg-white/20 rounded-lg">
              <Youtube className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-bold">Today's Video</h3>
              <p className="text-red-100 text-sm">Watch before or during your session</p>
            </div>
          </div>
          
          <div className="bg-white/10 rounded-lg p-4">
            <h4 className="font-semibold text-lg mb-2">{video.title}</h4>
            <p className="text-red-100 text-sm mb-3">{video.description}</p>
            
            <div className="flex items-center gap-4 text-sm text-red-200 mb-4">
              <span className="flex items-center gap-1">
                <Clock className="w-4 h-4" />
                {video.duration}
              </span>
              <span>{video.channel}</span>
            </div>
            
            <a
              href={video.url}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 bg-white text-red-600 px-4 py-2 rounded-lg font-medium hover:bg-red-50 transition-colors"
            >
              <Play className="w-5 h-5" />
              Watch on YouTube
              <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </div>
      )}
      
      {/* Weekly Podcasts - Specific Episodes */}
      {podcasts.length > 0 && (
        <div className="bg-gradient-to-r from-purple-600 to-purple-700 rounded-xl p-6 text-white">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-2 bg-white/20 rounded-lg">
              <Headphones className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-bold">Week {weekNumber} Podcast Episodes</h3>
              <p className="text-purple-100 text-sm">
                {isNewPodcastDay 
                  ? "New episodes for this week - listen during commute or gym" 
                  : "Continue listening to this week's episodes"}
              </p>
            </div>
          </div>
          
          <div className="space-y-3">
            {podcasts.map((podcast, idx) => (
              <div key={idx} className="bg-white/10 rounded-lg p-4">
                <div className="flex items-start justify-between gap-3 mb-2">
                  <h4 className="font-semibold">{podcast.title}</h4>
                  {podcast.episodeNumber && (
                    <span className="text-xs bg-white/20 px-2 py-1 rounded">{podcast.episodeNumber}</span>
                  )}
                </div>
                <p className="text-purple-200 text-sm mb-2">{podcast.show}</p>
                <p className="text-purple-100 text-sm mb-3">{podcast.description}</p>
                
                <div className="flex items-center justify-between flex-wrap gap-2">
                  <span className="flex items-center gap-1 text-sm text-purple-200">
                    <Clock className="w-4 h-4" />
                    {podcast.duration}
                  </span>
                  
                  <div className="flex gap-2">
                    <a
                      href={podcast.episodeUrl}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-2 bg-white text-purple-600 px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-purple-50 transition-colors"
                    >
                      <Play className="w-4 h-4" />
                      Listen
                      <ExternalLink className="w-3 h-3" />
                    </a>
                    {podcast.appleUrl && (
                      <a
                        href={podcast.appleUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-2 bg-purple-800 text-white px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-purple-900 transition-colors"
                      >
                        Apple
                        <ExternalLink className="w-3 h-3" />
                      </a>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      {/* Audiobooks - Show on first day of quarter or always available */}
      {audiobooks.length > 0 && (
        <div className="bg-gradient-to-r from-amber-600 to-amber-700 rounded-xl p-6 text-white">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-2 bg-white/20 rounded-lg">
              <BookOpen className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-bold">Recommended Audiobooks</h3>
              <p className="text-amber-100 text-sm">Listen during commute, gym, or walks</p>
            </div>
          </div>
          
          <div className="space-y-3">
            {audiobooks.map((book, idx) => (
              <div key={idx} className="bg-white/10 rounded-lg p-4">
                <h4 className="font-semibold mb-1">{book.title}</h4>
                <p className="text-amber-200 text-sm mb-2">by {book.author}</p>
                <p className="text-amber-100 text-sm mb-2">{book.description}</p>
                <p className="text-amber-200 text-xs mb-3 italic">{book.whenToListen}</p>
                
                <div className="flex items-center justify-between flex-wrap gap-2">
                  <span className="flex items-center gap-1 text-sm text-amber-200">
                    <Clock className="w-4 h-4" />
                    {book.duration}
                  </span>
                  
                  <a
                    href={book.audibleUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 bg-white text-amber-600 px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-amber-50 transition-colors"
                  >
                    Listen on Audible
                    <ExternalLink className="w-3 h-3" />
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

// Standalone audiobook recommendations component
export function AudiobookRecommendations({ quarterNumber }: { quarterNumber: number }) {
  const { audiobooks } = getDayMedia((quarterNumber - 1) * 52 + 1);
  
  if (audiobooks.length === 0) return null;
  
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
      <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
        <BookOpen className="w-6 h-6 text-amber-500" />
        Quarter {quarterNumber} Audiobooks
      </h3>
      <p className="text-gray-600 dark:text-gray-400 mb-4">
        Listen during commute, workouts, or downtime to supplement your learning.
      </p>
      
      <div className="space-y-4">
        {audiobooks.map((book, idx) => (
          <div
            key={idx}
            className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
          >
            <h4 className="font-semibold text-gray-900 dark:text-white">{book.title}</h4>
            <p className="text-sm text-gray-500 dark:text-gray-400">by {book.author} - {book.duration}</p>
            <p className="text-sm text-gray-600 dark:text-gray-300 mt-2">{book.description}</p>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1 italic">{book.whenToListen}</p>
            
            <div className="mt-3">
              <a
                href={book.audibleUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-amber-600 hover:text-amber-700 flex items-center gap-1"
              >
                Listen on Audible <ExternalLink className="w-3 h-3" />
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
