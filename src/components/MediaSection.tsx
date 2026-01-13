'use client';

import { getDayMedia, RECOMMENDED_PODCASTS, SPOTIFY_PLAYLISTS, DailyVideo, WeeklyPodcast } from '@/lib/media-resources';
import { Play, Headphones, ExternalLink, Clock, Youtube, Music } from 'lucide-react';

interface MediaSectionProps {
  dayNumber: number;
}

export function MediaSection({ dayNumber }: MediaSectionProps) {
  const { video, podcasts, isNewPodcastDay } = getDayMedia(dayNumber);
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
      
      {/* Weekly Podcasts - Show prominently on first day of week */}
      {podcasts.length > 0 && (
        <div className="bg-gradient-to-r from-green-600 to-green-700 rounded-xl p-6 text-white">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-2 bg-white/20 rounded-lg">
              <Headphones className="w-6 h-6" />
            </div>
            <div>
              <h3 className="text-lg font-bold">Week {weekNumber} Podcasts</h3>
              <p className="text-green-100 text-sm">
                {isNewPodcastDay 
                  ? "New episodes for this week! Listen during commute/gym" 
                  : "Continue listening to this week's episodes"}
              </p>
            </div>
          </div>
          
          <div className="space-y-3">
            {podcasts.map((podcast, idx) => (
              <div key={idx} className="bg-white/10 rounded-lg p-4">
                <h4 className="font-semibold mb-1">{podcast.title}</h4>
                <p className="text-green-200 text-sm mb-2">{podcast.show}</p>
                <p className="text-green-100 text-sm mb-3">{podcast.description}</p>
                
                <div className="flex items-center justify-between">
                  <span className="flex items-center gap-1 text-sm text-green-200">
                    <Clock className="w-4 h-4" />
                    {podcast.duration}
                  </span>
                  
                  <a
                    href={podcast.spotifyUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 bg-white text-green-600 px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-green-50 transition-colors"
                  >
                    <Music className="w-4 h-4" />
                    Open in Spotify
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
      
      {/* Focus Music Suggestion */}
      <div className="bg-gray-800 rounded-xl p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Music className="w-5 h-5 text-purple-400" />
            <div>
              <p className="text-white font-medium">Need focus music?</p>
              <p className="text-gray-400 text-sm">Play while coding</p>
            </div>
          </div>
          <div className="flex gap-2">
            <a
              href={SPOTIFY_PLAYLISTS.focusStudy.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-purple-400 hover:text-purple-300 underline"
            >
              Deep Focus
            </a>
            <span className="text-gray-600">|</span>
            <a
              href={SPOTIFY_PLAYLISTS.lofi.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-sm text-purple-400 hover:text-purple-300 underline"
            >
              Lo-Fi Beats
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

// Standalone component for recommended podcasts to subscribe to
export function PodcastRecommendations() {
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl p-6 shadow-sm">
      <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-4 flex items-center gap-2">
        <Headphones className="w-6 h-6 text-green-500" />
        Subscribe to These Podcasts
      </h3>
      <p className="text-gray-600 dark:text-gray-400 mb-4">
        Listen during your commute, workouts, or downtime to accelerate your learning.
      </p>
      
      <div className="space-y-3">
        {RECOMMENDED_PODCASTS.map((podcast, idx) => (
          <a
            key={idx}
            href={podcast.spotifyUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="block p-4 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 transition-colors"
          >
            <div className="flex items-center justify-between">
              <div>
                <h4 className="font-semibold text-gray-900 dark:text-white">{podcast.name}</h4>
                <p className="text-sm text-gray-600 dark:text-gray-400">{podcast.description}</p>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">{podcast.frequency}</p>
              </div>
              <div className="flex items-center gap-2 text-green-500">
                <Music className="w-5 h-5" />
                <ExternalLink className="w-4 h-4" />
              </div>
            </div>
          </a>
        ))}
      </div>
    </div>
  );
}
