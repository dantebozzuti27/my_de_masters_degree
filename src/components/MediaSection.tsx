'use client';

import { getDayMedia, RECOMMENDED_PODCASTS, DailyVideo, WeeklyPodcast } from '@/lib/media-resources';
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
      
      {/* Weekly Podcasts */}
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
                  ? "New episodes for this week - listen during commute or gym" 
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
                
                <div className="flex items-center justify-between flex-wrap gap-2">
                  <span className="flex items-center gap-1 text-sm text-green-200">
                    <Clock className="w-4 h-4" />
                    {podcast.duration}
                  </span>
                  
                  <div className="flex gap-2">
                    <a
                      href={podcast.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-2 bg-white text-green-600 px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-green-50 transition-colors"
                    >
                      Website
                      <ExternalLink className="w-3 h-3" />
                    </a>
                    <a
                      href={podcast.spotifySearch}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="inline-flex items-center gap-2 bg-green-800 text-white px-3 py-1.5 rounded-lg text-sm font-medium hover:bg-green-900 transition-colors"
                    >
                      <Music className="w-4 h-4" />
                      Find on Spotify
                    </a>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
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
          <div
            key={idx}
            className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
          >
            <div className="flex items-center justify-between flex-wrap gap-2">
              <div className="flex-1 min-w-0">
                <h4 className="font-semibold text-gray-900 dark:text-white">{podcast.name}</h4>
                <p className="text-sm text-gray-600 dark:text-gray-400">{podcast.description}</p>
                <p className="text-xs text-gray-500 dark:text-gray-500 mt-1">{podcast.frequency}</p>
              </div>
              <div className="flex gap-2">
                <a
                  href={podcast.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-sm text-blue-600 hover:text-blue-700"
                >
                  Website
                  <ExternalLink className="w-3 h-3" />
                </a>
                <a
                  href={podcast.spotifySearch}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-sm text-green-600 hover:text-green-700"
                >
                  <Music className="w-4 h-4" />
                  Spotify
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
