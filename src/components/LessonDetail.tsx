'use client';

import { useState } from 'react';
import { Lesson, getLessonByDay } from '@/lib/lessons';
import { StudySession } from '@/lib/types';
import { useProgress } from '@/hooks/useProgress';
import { 
  Target, 
  Clock, 
  BookOpen, 
  Code, 
  CheckCircle2, 
  Circle,
  ChevronDown,
  ChevronRight,
  ExternalLink,
  Star,
  Lightbulb,
  AlertTriangle,
  Briefcase
} from 'lucide-react';
import { MediaSection } from '@/components/MediaSection';
import { VerifiedBadge } from '@/components/VerifiedBadge';

interface LessonDetailProps {
  session: StudySession;
}

export function LessonDetail({ session }: LessonDetailProps) {
  const { progress, toggleSession, setRating, setNotes } = useProgress();
  const [expandedSections, setExpandedSections] = useState<Set<string>>(
    new Set(['objectives', 'session-plan', 'resources', 'exercises'])
  );
  const [showNotes, setShowNotes] = useState(false);
  const [noteText, setNoteText] = useState(progress.sessions[session.id]?.notes || '');
  
  const lesson = getLessonByDay(session.dayNumber);
  const isCompleted = progress.sessions[session.id]?.completed ?? false;
  const sessionProgress = progress.sessions[session.id];
  
  const toggleSection = (section: string) => {
    const newExpanded = new Set(expandedSections);
    if (newExpanded.has(section)) {
      newExpanded.delete(section);
    } else {
      newExpanded.add(section);
    }
    setExpandedSections(newExpanded);
  };

  const handleToggleComplete = () => {
    toggleSession(session.id);
  };

  const handleRating = (rating: 1 | 2 | 3 | 4 | 5) => {
    setRating(session.id, rating);
  };

  const handleNoteSave = () => {
    setNotes(session.id, noteText);
    setShowNotes(false);
  };

  if (!lesson) {
    return (
      <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 p-6">
        <p className="text-gray-500 dark:text-gray-400">
          Detailed lesson content coming soon for Day {session.dayNumber}.
        </p>
      </div>
    );
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-gray-700 overflow-hidden">
      {/* Header */}
      <div className={`p-6 border-b border-gray-200 dark:border-gray-700 ${
        isCompleted ? 'bg-green-50 dark:bg-green-900/20' : 'bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20'
      }`}>
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <div className="flex items-center gap-2 text-sm text-gray-500 dark:text-gray-400 mb-2">
              <span className="px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 rounded font-medium">
                Day {session.dayNumber}
              </span>
              <span className="px-2 py-1 bg-purple-100 dark:bg-purple-900 text-purple-700 dark:text-purple-300 rounded font-medium">
                Week {session.weekNumber}
              </span>
            </div>
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
              {lesson.topic}
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mt-1">
              {lesson.subtitle}
            </p>
          </div>
          <button
            onClick={handleToggleComplete}
            className={`p-3 rounded-full transition-all ${
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

        {/* Rating (if completed) */}
        {isCompleted && (
          <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
            <p className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              How was this session?
            </p>
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
      </div>

      {/* Verified Progress Status */}
      <div className="p-4 border-b border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900">
        <VerifiedBadge dayNumber={session.dayNumber} size="md" />
        <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
          Complete the exercise in your workspace to verify progress
        </p>
      </div>

      {/* Daily Video & Podcasts */}
      <div className="p-6 border-b border-gray-200 dark:border-gray-700">
        <MediaSection dayNumber={session.dayNumber} />
      </div>

      {/* Learning Objectives */}
      <CollapsibleSection
        title="Learning Objectives"
        icon={Target}
        isExpanded={expandedSections.has('objectives')}
        onToggle={() => toggleSection('objectives')}
        color="blue"
      >
        <ul className="space-y-2">
          {lesson.objectives.map((obj, i) => (
            <li key={i} className="flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-blue-500 mt-0.5 flex-shrink-0" />
              <span className="text-gray-700 dark:text-gray-300">{obj}</span>
            </li>
          ))}
        </ul>
      </CollapsibleSection>

      {/* Session Plan */}
      <CollapsibleSection
        title="Session Plan (90 minutes)"
        icon={Clock}
        isExpanded={expandedSections.has('session-plan')}
        onToggle={() => toggleSection('session-plan')}
        color="purple"
      >
        <div className="space-y-3">
          {Object.entries(lesson.sessionPlan).map(([phase, content]) => (
            <div key={phase} className="flex gap-4 p-3 bg-gray-50 dark:bg-gray-900 rounded-lg">
              <div className="w-24 flex-shrink-0">
                <span className={`px-2 py-1 rounded text-xs font-bold uppercase ${
                  phase === 'warmup' ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300' :
                  phase === 'theory' ? 'bg-blue-100 text-blue-700 dark:bg-blue-900 dark:text-blue-300' :
                  phase === 'practice' ? 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300' :
                  'bg-purple-100 text-purple-700 dark:bg-purple-900 dark:text-purple-300'
                }`}>
                  {phase}
                </span>
              </div>
              <div className="flex-1">
                {typeof content === 'string' ? (
                  <p className="text-gray-700 dark:text-gray-300">{content}</p>
                ) : (
                  <div>
                    <p className="text-gray-700 dark:text-gray-300 mb-2">
                      {(content as any).duration} min - {(content as any).activity || (content as any).content?.join(', ') || ''}
                    </p>
                    {(content as any).keyConceptes && (
                      <div className="flex flex-wrap gap-2 mt-2">
                        {(content as any).keyConceptes.map((concept: string, i: number) => (
                          <span key={i} className="px-2 py-1 bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 rounded text-xs">
                            {concept}
                          </span>
                        ))}
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>
      </CollapsibleSection>

      {/* Resources */}
      <CollapsibleSection
        title="Resources"
        icon={BookOpen}
        isExpanded={expandedSections.has('resources')}
        onToggle={() => toggleSection('resources')}
        color="green"
      >
        <div className="space-y-2">
          {lesson.resources.map((resource, i) => (
            <a
              key={i}
              href={resource.url}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-900 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors group"
            >
              <div className="flex items-center gap-3">
                <span className={`px-2 py-1 rounded text-xs font-medium ${
                  resource.priority === 'required' 
                    ? 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300' 
                    : resource.priority === 'recommended'
                    ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300'
                    : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300'
                }`}>
                  {resource.priority}
                </span>
                <div>
                  <p className="font-medium text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400">
                    {resource.title}
                  </p>
                  {resource.duration && (
                    <p className="text-sm text-gray-500 dark:text-gray-400">
                      {resource.duration}
                    </p>
                  )}
                </div>
              </div>
              <ExternalLink className="w-4 h-4 text-gray-400 group-hover:text-blue-500" />
            </a>
          ))}
        </div>
      </CollapsibleSection>

      {/* Exercises */}
      <CollapsibleSection
        title="Exercises"
        icon={Code}
        isExpanded={expandedSections.has('exercises')}
        onToggle={() => toggleSection('exercises')}
        color="orange"
      >
        <div className="space-y-4">
          {lesson.exercises.map((exercise, i) => (
            <ExerciseCard key={i} exercise={exercise} index={i + 1} />
          ))}
        </div>
      </CollapsibleSection>

      {/* Success Criteria */}
      <CollapsibleSection
        title="Success Criteria"
        icon={CheckCircle2}
        isExpanded={expandedSections.has('success')}
        onToggle={() => toggleSection('success')}
        color="green"
      >
        <ul className="space-y-2">
          {lesson.successCriteria.map((criterion, i) => (
            <li key={i} className="flex items-start gap-3">
              <input
                type="checkbox"
                className="mt-1 w-4 h-4 rounded border-gray-300 text-green-600 focus:ring-green-500"
              />
              <span className="text-gray-700 dark:text-gray-300">{criterion}</span>
            </li>
          ))}
        </ul>
      </CollapsibleSection>

      {/* Key Terms */}
      {lesson.keyTerms && (
        <CollapsibleSection
          title="Key Terms"
          icon={Lightbulb}
          isExpanded={expandedSections.has('terms')}
          onToggle={() => toggleSection('terms')}
          color="yellow"
        >
          <div className="space-y-3">
            {lesson.keyTerms.map((item, i) => (
              <div key={i} className="p-3 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg border border-yellow-200 dark:border-yellow-800">
                <p className="font-semibold text-yellow-800 dark:text-yellow-200">
                  {item.term}
                </p>
                <p className="text-yellow-700 dark:text-yellow-300 text-sm mt-1">
                  {item.definition}
                </p>
              </div>
            ))}
          </div>
        </CollapsibleSection>
      )}

      {/* Common Mistakes */}
      {lesson.commonMistakes && (
        <CollapsibleSection
          title="Common Mistakes to Avoid"
          icon={AlertTriangle}
          isExpanded={expandedSections.has('mistakes')}
          onToggle={() => toggleSection('mistakes')}
          color="red"
        >
          <ul className="space-y-2">
            {lesson.commonMistakes.map((mistake, i) => (
              <li key={i} className="flex items-start gap-3 text-red-700 dark:text-red-300">
                <AlertTriangle className="w-5 h-5 mt-0.5 flex-shrink-0" />
                <span>{mistake}</span>
              </li>
            ))}
          </ul>
        </CollapsibleSection>
      )}

      {/* Work Application */}
      {lesson.workApplication && (
        <CollapsibleSection
          title="Work Application"
          icon={Briefcase}
          isExpanded={expandedSections.has('work')}
          onToggle={() => toggleSection('work')}
          color="indigo"
        >
          <div className="p-4 bg-indigo-50 dark:bg-indigo-900/20 rounded-lg border border-indigo-200 dark:border-indigo-800">
            <p className="text-indigo-700 dark:text-indigo-300">
              {lesson.workApplication}
            </p>
          </div>
        </CollapsibleSection>
      )}

      {/* Notes Section */}
      <div className="p-6 border-t border-gray-200 dark:border-gray-700">
        <button
          onClick={() => setShowNotes(!showNotes)}
          className="text-blue-600 hover:text-blue-700 dark:text-blue-400 font-medium"
        >
          {showNotes ? 'Hide Notes' : (sessionProgress?.notes ? 'Edit Notes' : '+ Add Notes')}
        </button>
        
        {showNotes && (
          <div className="mt-4">
            <textarea
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              placeholder="Add your notes, learnings, questions, or reflections..."
              className="w-full p-4 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-900 text-gray-900 dark:text-white resize-none"
              rows={5}
            />
            <div className="flex gap-2 mt-3">
              <button
                onClick={handleNoteSave}
                className="px-4 py-2 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700"
              >
                Save Notes
              </button>
              <button
                onClick={() => setShowNotes(false)}
                className="px-4 py-2 bg-gray-200 text-gray-700 dark:bg-gray-700 dark:text-gray-300 rounded-lg font-medium hover:bg-gray-300 dark:hover:bg-gray-600"
              >
                Cancel
              </button>
            </div>
          </div>
        )}
        
        {!showNotes && sessionProgress?.notes && (
          <div className="mt-3 p-4 bg-gray-50 dark:bg-gray-900 rounded-lg">
            <p className="text-gray-700 dark:text-gray-300 whitespace-pre-wrap">
              {sessionProgress.notes}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

// Collapsible Section Component
interface CollapsibleSectionProps {
  title: string;
  icon: React.ComponentType<{ className?: string }>;
  isExpanded: boolean;
  onToggle: () => void;
  color: 'blue' | 'purple' | 'green' | 'orange' | 'red' | 'yellow' | 'indigo';
  children: React.ReactNode;
}

function CollapsibleSection({ 
  title, 
  icon: Icon, 
  isExpanded, 
  onToggle, 
  color,
  children 
}: CollapsibleSectionProps) {
  const colorClasses = {
    blue: 'text-blue-600 dark:text-blue-400',
    purple: 'text-purple-600 dark:text-purple-400',
    green: 'text-green-600 dark:text-green-400',
    orange: 'text-orange-600 dark:text-orange-400',
    red: 'text-red-600 dark:text-red-400',
    yellow: 'text-yellow-600 dark:text-yellow-400',
    indigo: 'text-indigo-600 dark:text-indigo-400'
  };

  return (
    <div className="border-t border-gray-200 dark:border-gray-700">
      <button
        onClick={onToggle}
        className="w-full p-4 flex items-center justify-between hover:bg-gray-50 dark:hover:bg-gray-700/50 transition-colors"
      >
        <div className="flex items-center gap-3">
          <Icon className={`w-5 h-5 ${colorClasses[color]}`} />
          <h3 className="font-semibold text-gray-900 dark:text-white">{title}</h3>
        </div>
        {isExpanded ? (
          <ChevronDown className="w-5 h-5 text-gray-400" />
        ) : (
          <ChevronRight className="w-5 h-5 text-gray-400" />
        )}
      </button>
      {isExpanded && (
        <div className="px-6 pb-6">
          {children}
        </div>
      )}
    </div>
  );
}

// Exercise Card Component
interface ExerciseCardProps {
  exercise: any;
  index: number;
}

function ExerciseCard({ exercise, index }: ExerciseCardProps) {
  const [showSolution, setShowSolution] = useState(false);

  return (
    <div className="border border-gray-200 dark:border-gray-700 rounded-lg overflow-hidden">
      <div className="p-4 bg-gray-50 dark:bg-gray-900">
        <div className="flex items-center justify-between">
          <h4 className="font-semibold text-gray-900 dark:text-white">
            Exercise {index}: {exercise.title}
          </h4>
          <div className="flex items-center gap-2">
            <span className={`px-2 py-1 rounded text-xs font-medium ${
              exercise.difficulty === 'beginner' 
                ? 'bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300'
                : exercise.difficulty === 'intermediate'
                ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900 dark:text-yellow-300'
                : 'bg-red-100 text-red-700 dark:bg-red-900 dark:text-red-300'
            }`}>
              {exercise.difficulty}
            </span>
            <span className="text-sm text-gray-500 dark:text-gray-400">
              ~{exercise.estimatedTime} min
            </span>
          </div>
        </div>
      </div>
      
      <div className="p-4">
        <h5 className="font-medium text-gray-700 dark:text-gray-300 mb-2">Instructions:</h5>
        <ul className="space-y-1 mb-4">
          {exercise.instructions.map((instruction: string, i: number) => (
            <li key={i} className="text-gray-600 dark:text-gray-400 text-sm flex items-start gap-2">
              <span className="text-blue-500 mt-1">•</span>
              <span>{instruction}</span>
            </li>
          ))}
        </ul>

        {exercise.hints && (
          <div className="mb-4">
            <h5 className="font-medium text-gray-700 dark:text-gray-300 mb-2">Hints:</h5>
            <ul className="space-y-1">
              {exercise.hints.map((hint: string, i: number) => (
                <li key={i} className="text-gray-500 dark:text-gray-400 text-sm italic">
                  {hint}
                </li>
              ))}
            </ul>
          </div>
        )}

        {exercise.solution && (
          <div>
            <button
              onClick={() => setShowSolution(!showSolution)}
              className="text-blue-600 hover:text-blue-700 dark:text-blue-400 text-sm font-medium"
            >
              {showSolution ? 'Hide Solution' : 'Show Solution'}
            </button>
            
            {showSolution && (
              <pre className="mt-3 p-4 bg-gray-900 text-gray-100 rounded-lg overflow-x-auto text-sm">
                <code>{exercise.solution}</code>
              </pre>
            )}
          </div>
        )}

        {exercise.deliverable && (
          <div className="mt-4 p-3 bg-green-50 dark:bg-green-900/20 rounded-lg border border-green-200 dark:border-green-800">
            <p className="text-sm text-green-700 dark:text-green-300">
              <strong>Deliverable:</strong> {exercise.deliverable}
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
