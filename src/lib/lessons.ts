// Complete Lesson Plans for 2-Year Senior Data Engineer Program
// AI-ENHANCED CURRICULUM - Updated January 2026
// Focus: Use AI tools to accelerate learning, understand concepts over syntax

export interface Lesson {
  dayNumber: number;
  week: number;
  topic: string;
  subtitle: string;
  
  // Learning objectives - specific, measurable outcomes
  objectives: string[];
  
  // AI Integration - How AI tools are used in this lesson
  aiIntegration: {
    toolsUsed: ('copilot' | 'chatgpt' | 'claude' | 'cursor' | 'none')[];
    focusArea: 'learn-with-ai' | 'debug-ai-code' | 'prompt-engineering' | 'ai-review' | 'manual-practice';
    aiTip: string;
    warningWhenNotToUseAI?: string;
  };
  
  // Session structure (120 minutes / 2 hours total) - supports both old and new formats
  sessionPlan: SessionPlanItem[] | {
    warmup: {
      duration: number;
      activity: string;
    };
    theory: {
      duration: number;
      content: string[];
      keyConceptes: string[];
    };
    practice: {
      duration: number;
      exercises: Exercise[];
    };
    review: {
      duration: number;
      activities: string[];
    };
  };
  
  // Resources - supports both old flat array and new categorized format
  resources: LessonResource[] | {
    required?: SimpleResource[];
    optional?: SimpleResource[];
  };
  
  // Exercises with full instructions
  exercises: Exercise[];
  
  // Success criteria
  successCriteria: string[];
  
  // Notes for work application
  workApplication?: string;
  
  // Weekly checkpoint (only on Thursdays)
  weeklyCheckpoint?: WeeklyCheckpoint;
  
  // Prerequisite knowledge
  prerequisites?: string[];
  
  // Key terms to know
  keyTerms?: KeyTerm[];
  
  // Common mistakes to avoid - supports both string[] and object[] formats
  commonMistakes?: string[] | CommonMistake[];
  
  // Future-proofing note
  futureProofNote?: string;
}

export interface LessonResource {
  title: string;
  url: string;
  type: 'video' | 'article' | 'documentation' | 'tutorial' | 'practice' | 'book' | 'course';
  duration?: string;
  priority: 'required' | 'recommended' | 'optional';
  notes?: string;
}

export interface Exercise {
  title: string;
  difficulty?: 'beginner' | 'intermediate' | 'advanced';
  estimatedTime?: number;
  instructions?: string[];
  description?: string; // Alternative to instructions for simpler format
  aiApproach?: string; // How to use AI for this exercise
  hints?: string[];
  solution?: string;
  deliverable?: string;
}

export interface WeeklyCheckpoint {
  title: string;
  description: string;
  deliverables: string[];
  selfAssessment: string[];
}

export interface KeyTerm {
  term: string;
  definition: string;
}

export interface SessionPlanItem {
  time: string;
  activity: string;
  type: 'video' | 'learn' | 'practice' | 'exercise' | 'review';
}

export interface SimpleResource {
  title: string;
  url: string;
  type: 'video' | 'article' | 'docs' | 'tutorial' | 'interactive' | 'reference' | 'tool';
  duration?: string;
}

export interface CommonMistake {
  mistake: string;
  fix: string;
}

// ============================================================================
// QUARTER 1: PYTHON & SQL FOUNDATIONS (Weeks 1-13)
// AI-ENHANCED CURRICULUM
// ============================================================================

export const Q1_LESSONS: Lesson[] = [
  // ============================================================================
  // WEEK 1: Development Environment & AI-Assisted Learning Setup
  // ============================================================================
  {
    dayNumber: 1,
    week: 1,
    topic: "Development Environment + AI Tools Setup",
    subtitle: "Building Your AI-Enhanced Data Engineering Workstation",
    
    objectives: [
      "Install Python 3.11+, VS Code, and Git",
      "Set up GitHub Copilot for AI-assisted coding",
      "Configure Cursor IDE as an alternative AI-native editor",
      "Create virtual environments using venv",
      "Understand when AI helps vs when to code manually"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'cursor'],
      focusArea: 'learn-with-ai',
      aiTip: "Install Copilot TODAY. Every exercise from now on should be done WITH AI assistance. The goal is to understand the code AI generates, not to memorize syntax.",
      warningWhenNotToUseAI: "For initial environment setup (installing Python, VS Code), follow manual steps. AI can't click buttons for you."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Check your current development setup. Do you have any AI coding tools installed? After today, you will."
      },
      theory: {
        duration: 20,
        content: [
          "Why AI tools are essential for modern data engineering",
          "GitHub Copilot: Your AI pair programmer",
          "The new skill: Understanding and reviewing AI-generated code",
          "When NOT to trust AI (security, business logic, edge cases)"
        ],
        keyConceptes: [
          "AI-assisted development",
          "Code review skills",
          "Prompt engineering basics",
          "Human-AI collaboration"
        ]
      },
      practice: {
        duration: 55,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Verify Copilot is generating suggestions",
          "Practice accepting/rejecting AI suggestions",
          "Commit your setup to git"
        ]
      }
    },
    
    resources: [
      {
        title: "GitHub Copilot Setup Guide",
        url: "https://docs.github.com/en/copilot/getting-started-with-github-copilot",
        type: "documentation",
        duration: "15 min",
        priority: "required",
        notes: "Free for students, or $10/month - WORTH IT for 10x productivity"
      },
      {
        title: "Cursor IDE",
        url: "https://cursor.sh/",
        type: "documentation",
        duration: "10 min",
        priority: "recommended",
        notes: "AI-native code editor, alternative to VS Code + Copilot"
      },
      {
        title: "Real Python: Setting Up Python",
        url: "https://realpython.com/installing-python/",
        type: "article",
        duration: "20 min read",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "Install Development Environment",
        difficulty: "beginner",
        estimatedTime: 20,
        instructions: [
          "Download Python 3.11+ from python.org - CHECK 'Add Python to PATH'",
          "Install VS Code from code.visualstudio.com",
          "Install extensions: Python, Pylance, GitLens, GitHub Copilot",
          "Verify: python --version shows 3.11+",
          "Create folder: mkdir sde-learning && cd sde-learning",
          "Create venv: python -m venv venv && source venv/bin/activate"
        ],
        aiApproach: "Don't use AI for installation. This is manual setup that AI can't do for you.",
        deliverable: "Screenshot showing Python 3.11+ and activated venv"
      },
      {
        title: "Configure GitHub Copilot",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Sign up at github.com/features/copilot (free trial or student/paid)",
          "Install GitHub Copilot extension in VS Code",
          "Sign in when prompted",
          "Create a test.py file and start typing: def calculate_average(",
          "Watch Copilot suggest the function body - press Tab to accept"
        ],
        aiApproach: "This IS the AI setup. After this, Copilot will be your constant companion.",
        deliverable: "Screenshot of Copilot suggesting code"
      },
      {
        title: "First AI-Assisted Code",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Create a file: ai_test.py",
          "Type this comment: # Function to check if a number is prime",
          "Let Copilot generate the function",
          "READ and UNDERSTAND the generated code",
          "Add a comment explaining what each line does",
          "Test it: print(is_prime(17)) should be True"
        ],
        aiApproach: "Let Copilot write the code, but YOU must understand it. Add comments explaining each line.",
        hints: [
          "If Copilot's suggestion isn't good, press Ctrl+Enter to see alternatives",
          "Don't just accept - read and verify the logic"
        ],
        deliverable: "is_prime function with YOUR explanatory comments"
      },
      {
        title: "Git Setup",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Install Git if needed",
          "git config --global user.name 'Your Name'",
          "git config --global user.email 'you@example.com'",
          "git init",
          "Create .gitignore (type: 'gitignore python' - let Copilot complete)",
          "git add . && git commit -m 'Initial commit with AI tools'"
        ],
        aiApproach: "Copilot can generate .gitignore content. Just type the comment and let it complete.",
        deliverable: "Git repo with first commit"
      }
    ],
    
    successCriteria: [
      "Python 3.11+ installed and in PATH",
      "GitHub Copilot active and suggesting code",
      "Can explain what Copilot-generated code does",
      "Virtual environment created and activated",
      "Git repository initialized"
    ],
    
    keyTerms: [
      { term: "GitHub Copilot", definition: "AI pair programmer that suggests code as you type, trained on billions of lines of code" },
      { term: "Prompt Engineering", definition: "The skill of writing comments/instructions that help AI generate better code" },
      { term: "AI Code Review", definition: "Reading and verifying AI-generated code before using it - YOUR key skill" },
      { term: "Virtual Environment", definition: "Isolated Python installation with its own packages" }
    ],
    
    commonMistakes: [
      "Blindly accepting AI suggestions without understanding them",
      "Not installing Copilot - you'll be 10x slower without it",
      "Trusting AI for security-sensitive code without review",
      "Forgetting to activate venv before installing packages"
    ],
    
    futureProofNote: "By 2028, AI-assisted coding will be the norm. Starting with these tools now means you're learning the future workflow, not outdated practices."
  },
  
  // Day 2
  {
    dayNumber: 2,
    week: 1,
    topic: "Python Fundamentals with AI",
    subtitle: "Variables, Types, and AI-Assisted Learning",
    
    objectives: [
      "Understand Python's core data types through AI-generated examples",
      "Use Copilot to generate code, then explain what it does",
      "Learn to write effective prompts for code generation",
      "Debug AI-generated code when it has issues",
      "Know when AI gets it wrong and how to fix it"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Write descriptive comments FIRST, then let Copilot complete. The better your comment, the better the code.",
      warningWhenNotToUseAI: "For the first exercise of each concept, try writing it yourself first. Then compare with AI's version."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Open VS Code, activate venv. Type: '# Create variables for name, age, height' and see what Copilot suggests."
      },
      theory: {
        duration: 15,
        content: [
          "Python data types: int, float, str, bool",
          "Dynamic typing vs static typing",
          "How to READ code (more important than writing in AI era)",
          "Type hints: helping AI generate better code"
        ],
        keyConceptes: [
          "Dynamic typing",
          "Type inference",
          "f-strings",
          "Type hints"
        ]
      },
      practice: {
        duration: 60,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review all AI-generated code",
          "Ensure you can explain every line",
          "Commit with message: 'Day 2: Python fundamentals'"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Official Tutorial: Introduction",
        url: "https://docs.python.org/3/tutorial/introduction.html",
        type: "documentation",
        duration: "20 min read",
        priority: "required",
        notes: "Skim for concepts - AI will handle syntax details"
      },
      {
        title: "Copilot Tips for Python",
        url: "https://github.blog/developer-skills/programming-languages-and-frameworks/how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/",
        type: "article",
        duration: "10 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "Manual First: Variables Without AI",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "DISABLE Copilot temporarily (Ctrl+Shift+P > Copilot: Disable)",
          "Create my_name, my_age, my_height, is_learning variables",
          "Print each with its type",
          "RE-ENABLE Copilot when done"
        ],
        aiApproach: "Do this WITHOUT AI first to establish baseline understanding.",
        deliverable: "variables_manual.py with your own code"
      },
      {
        title: "AI-Assisted: String Operations",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Create a new file: strings_ai.py",
          "Write comment: # Function that takes a string and returns uppercase, lowercase, title case, length, word count",
          "Accept Copilot's suggestion",
          "Add YOUR comments explaining each line",
          "Test with: string_operations('hello world')"
        ],
        aiApproach: "Write the comment, let Copilot generate, then YOU add explanatory comments.",
        hints: [
          "If Copilot suggests something different, that's okay - there are multiple valid approaches",
          "The key is understanding what it generated"
        ],
        deliverable: "strings_ai.py with AI code + your explanations"
      },
      {
        title: "Debug AI Code",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Ask Copilot: # Function to divide two numbers safely",
          "If it forgets to handle division by zero, fix it yourself",
          "Add test cases that might break the function",
          "Document what you fixed"
        ],
        aiApproach: "Intentionally look for bugs in AI code. AI often forgets edge cases.",
        deliverable: "safe_divide function with YOUR bug fixes"
      },
      {
        title: "Type Hints Practice",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Write: def greet(name: str, times: int) -> str:",
          "Notice Copilot gives BETTER suggestions with type hints",
          "Create 3 more functions with full type hints",
          "Compare suggestions with vs without type hints"
        ],
        aiApproach: "Type hints help AI understand your intent. Always use them.",
        deliverable: "typed_functions.py showing type hints improve AI suggestions"
      },
      {
        title: "Ask ChatGPT to Explain",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Copy one of Copilot's generated functions",
          "Paste into ChatGPT: 'Explain this Python code line by line:'",
          "Compare ChatGPT's explanation with your understanding",
          "Ask follow-up questions about anything unclear"
        ],
        aiApproach: "Use ChatGPT as a tutor. Copilot writes code, ChatGPT explains it.",
        deliverable: "Notes from ChatGPT explanation"
      }
    ],
    
    successCriteria: [
      "Can write basic Python without AI (proves understanding)",
      "Can read and explain AI-generated code",
      "Know how to write comments that generate good code",
      "Can identify and fix bugs in AI code",
      "Understand type hints help AI"
    ],
    
    keyTerms: [
      { term: "Type Hint", definition: "Annotations like def func(x: int) -> str that help both AI and humans understand code" },
      { term: "Prompt", definition: "The comment or context you provide to help AI generate better code" },
      { term: "Edge Case", definition: "Unusual inputs AI often forgets (empty strings, zero, None, etc.)" },
      { term: "Code Review", definition: "Reading code to verify it works correctly - now includes reviewing AI code" }
    ],
    
    commonMistakes: [
      "Accepting AI code without understanding it",
      "Not writing descriptive comments (prompts)",
      "Forgetting type hints - they help AI a lot",
      "Not testing edge cases AI might miss"
    ],
    
    futureProofNote: "Reading and reviewing code is MORE important than writing it in 2028. AI writes, you verify. Master this skill."
  },
  
  // Day 3
  {
    dayNumber: 3,
    week: 1,
    topic: "Control Flow with AI Assistance",
    subtitle: "Conditionals, Loops, and AI Debugging",
    
    objectives: [
      "Write conditional logic and loops with AI assistance",
      "Learn to debug AI-generated loops (common source of bugs)",
      "Use AI to generate test cases for your code",
      "Understand loop patterns AI uses (and why)"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often generates working loops but with subtle bugs. Always trace through with sample inputs.",
      warningWhenNotToUseAI: "For FizzBuzz, try it yourself first. It's the classic test of basic programming understanding."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "WITHOUT AI, write code to print numbers 1-10. Then see how AI would do it."
      },
      theory: {
        duration: 15,
        content: [
          "Boolean logic AI sometimes gets wrong",
          "Loop patterns: for vs while (AI chooses for you, but know the difference)",
          "AI-generated code often has off-by-one errors",
          "Using AI to generate test cases"
        ],
        keyConceptes: [
          "Boolean operators (and, or, not)",
          "Loop control (break, continue)",
          "Off-by-one errors",
          "Test-driven debugging"
        ]
      },
      practice: {
        duration: 60,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review all loops for off-by-one errors",
          "Verify edge cases work",
          "Commit code"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Control Flow",
        url: "https://docs.python.org/3/tutorial/controlflow.html",
        type: "documentation",
        duration: "20 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "FizzBuzz Without AI (Then Compare)",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "DISABLE Copilot",
          "Write fizzbuzz(n) yourself from scratch",
          "Then ENABLE Copilot and ask it to write FizzBuzz",
          "Compare approaches - what's different?"
        ],
        aiApproach: "Prove to yourself you understand the logic. Then see AI's version.",
        deliverable: "Two versions of FizzBuzz with comparison notes"
      },
      {
        title: "AI-Generated Loop Debugging",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Ask Copilot: # Function to find all prime numbers up to n",
          "Trace through with n=10 manually",
          "Look for: off-by-one errors, incorrect range, edge cases",
          "Document any bugs you find and fix them"
        ],
        aiApproach: "AI loops often have subtle bugs. Your job is to find them.",
        hints: [
          "Does it handle n=1 correctly?",
          "Does it handle n=2 correctly?",
          "Check the range() bounds carefully"
        ],
        deliverable: "primes.py with documented bug fixes"
      },
      {
        title: "Use AI to Generate Test Cases",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "For your FizzBuzz function, ask ChatGPT:",
          "'Generate 10 test cases for a FizzBuzz function, including edge cases'",
          "Run all test cases against your function",
          "Fix any failures"
        ],
        aiApproach: "AI is GREAT at generating test cases. Use it for this.",
        deliverable: "test_fizzbuzz.py with AI-generated test cases"
      },
      {
        title: "Loop Optimization with AI",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Write a slow nested loop solution to a problem",
          "Ask Copilot: # Optimize this loop",
          "Compare performance of both versions",
          "Understand WHY the optimized version is faster"
        ],
        aiApproach: "AI knows optimization patterns. Learn from what it suggests.",
        deliverable: "Two versions with timing comparison"
      }
    ],
    
    successCriteria: [
      "Can write FizzBuzz without AI (baseline skill)",
      "Can identify off-by-one errors in AI loops",
      "Know how to use AI to generate test cases",
      "Understand for vs while loop use cases"
    ],
    
    commonMistakes: [
      "Trusting AI loops without tracing through",
      "Off-by-one errors in range()",
      "Not testing edge cases (0, 1, negative numbers)",
      "Using while when for is cleaner"
    ],
    
    futureProofNote: "AI generates loops easily but often with bugs. The human skill is finding those bugs. This becomes even more critical at scale."
  },
  
  // Day 4
  {
    dayNumber: 4,
    week: 1,
    topic: "Functions & Data Structures",
    subtitle: "Building Blocks with AI Collaboration",
    
    objectives: [
      "Define functions with proper type hints for AI",
      "Use lists, dicts, tuples, sets with AI assistance",
      "Understand when AI chooses each data structure",
      "Build a small project combining all concepts"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "When you see AI choose a data structure, ask yourself: why that one? Understanding the choice is the skill.",
      warningWhenNotToUseAI: "For the data structure quiz, test yourself first."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Quiz yourself: When would you use a list vs dict vs set? Write down your answers."
      },
      theory: {
        duration: 20,
        content: [
          "Lists, tuples, dicts, sets - when to use each",
          "How AI chooses data structures (and when it's wrong)",
          "Nested data structures for real-world data",
          "Time complexity basics (why sets are fast for lookups)"
        ],
        keyConceptes: [
          "Mutability",
          "Hash tables (dicts, sets)",
          "Time complexity O(1) vs O(n)",
          "Choosing the right structure"
        ]
      },
      practice: {
        duration: 55,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Create Week 1 summary document",
          "Push all code to GitHub",
          "Complete weekly checkpoint"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Data Structures",
        url: "https://docs.python.org/3/tutorial/datastructures.html",
        type: "documentation",
        duration: "25 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "Data Structure Selection Challenge",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "For each scenario, choose the best data structure BEFORE asking AI:",
          "1. Store unique user IDs",
          "2. Map user IDs to usernames",
          "3. Store ordered list of transactions",
          "4. Store immutable coordinates (x, y)",
          "Then ask ChatGPT: 'What data structure for each?' and compare"
        ],
        aiApproach: "Test your understanding first, then verify with AI.",
        deliverable: "Your answers vs AI answers with explanations"
      },
      {
        title: "Database Schema as Nested Dicts",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Write a comment describing a database with users, orders, products tables",
          "Let Copilot generate the nested data structure",
          "Add functions to: find user by ID, get user's orders, calculate total spent",
          "Verify AI's data structure choice makes sense"
        ],
        aiApproach: "Describe what you need in plain English. AI will structure it.",
        deliverable: "database_model.py with nested structure and query functions"
      },
      {
        title: "Week 1 Mini-Project: Contact Manager",
        difficulty: "intermediate",
        estimatedTime: 30,
        instructions: [
          "Build a contact manager with AI assistance:",
          "- Add contact (name, email, phone)",
          "- Search by name",
          "- List all contacts",
          "- Delete contact",
          "Write the REQUIREMENTS as comments, let AI implement",
          "Review and fix any issues"
        ],
        aiApproach: "Write detailed requirements as comments. AI implements. You review.",
        deliverable: "contact_manager.py - fully functional"
      }
    ],
    
    successCriteria: [
      "Can explain when to use each data structure",
      "Can read and understand AI-generated data structures",
      "Completed mini-project with AI assistance",
      "Week 1 code pushed to GitHub"
    ],
    
    weeklyCheckpoint: {
      title: "Week 1: AI-Assisted Python Foundations",
      description: "You should now be comfortable coding WITH AI, not just copying from it.",
      deliverables: [
        "GitHub repo with all Week 1 code",
        "Copilot installed and actively suggesting",
        "At least 5 files with YOUR explanatory comments on AI code",
        "Contact manager mini-project working",
        "Notes on what AI got right vs wrong"
      ],
      selfAssessment: [
        "Can I write a simple function WITHOUT AI? (baseline)",
        "Can I explain what AI-generated code does?",
        "Do I know when AI might be wrong?",
        "Am I faster coding with AI than without?"
      ]
    },
    
    keyTerms: [
      { term: "List", definition: "Ordered, mutable - use for sequences" },
      { term: "Dictionary", definition: "Key-value pairs - use for lookups" },
      { term: "Set", definition: "Unique elements - use for deduplication" },
      { term: "Tuple", definition: "Immutable sequence - use for fixed data" },
      { term: "Time Complexity", definition: "How fast operations are: O(1) constant, O(n) linear" }
    ],
    
    commonMistakes: [
      "Using lists when sets would be faster for lookups",
      "Not understanding AI's data structure choice",
      "Forgetting that dict keys must be immutable",
      "Not reviewing AI's implementation choices"
    ],
    
    futureProofNote: "Data structure selection is a HUMAN decision AI helps with but doesn't fully solve. Understanding trade-offs remains your job."
  },
  
  // ============================================================================
  // WEEK 2: Control Flow & AI-Powered Debugging
  // ============================================================================
  {
    dayNumber: 5,
    week: 2,
    topic: "List Comprehensions & AI Patterns",
    subtitle: "Pythonic Code with AI Guidance",
    
    objectives: [
      "Master list comprehensions through AI examples",
      "Recognize when AI uses comprehensions vs loops",
      "Convert loops to comprehensions (a common AI suggestion)",
      "Understand generator expressions for memory efficiency"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "AI loves list comprehensions. Learn to read them - they're everywhere in AI-generated Python.",
      warningWhenNotToUseAI: "Try converting a few loops manually first to understand the pattern."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Write a for loop to square numbers 1-10. Then ask AI to make it 'more Pythonic'."
      },
      theory: {
        duration: 15,
        content: [
          "List comprehension syntax: [expr for item in iterable if condition]",
          "When comprehensions are clearer vs when loops are better",
          "Generator expressions: () instead of [] for memory",
          "Why AI prefers comprehensions"
        ],
        keyConceptes: [
          "List comprehension",
          "Generator expression",
          "Lazy evaluation",
          "Pythonic code"
        ]
      },
      practice: {
        duration: 60,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Compare readability of loops vs comprehensions",
          "Commit with message 'Day 5: List comprehensions'"
        ]
      }
    },
    
    resources: [
      {
        title: "Corey Schafer: List Comprehensions",
        url: "https://www.youtube.com/watch?v=3dt4OGnU5sM",
        type: "video",
        duration: "18 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "Loop to Comprehension Conversion",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Write 5 simple loops (squares, evens, string transformations)",
          "Ask Copilot to convert each to a list comprehension",
          "Understand the transformation pattern",
          "Write the comprehension yourself, then compare to AI"
        ],
        aiApproach: "Use AI to show you the pattern, then practice it yourself.",
        deliverable: "loops_vs_comprehensions.py showing both versions"
      },
      {
        title: "Complex Comprehensions",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Ask AI: # Nested list comprehension to create multiplication table",
          "Ask AI: # Dict comprehension mapping words to their lengths",
          "Ask AI: # Set comprehension for unique first letters",
          "Add comments explaining each"
        ],
        aiApproach: "Let AI generate complex comprehensions, you decode them.",
        deliverable: "complex_comprehensions.py with explanations"
      },
      {
        title: "Generator vs List Performance",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Create a list of 1 million numbers",
          "Compare memory usage: list comprehension vs generator",
          "Use sys.getsizeof() to measure",
          "Document when to use each"
        ],
        aiApproach: "Ask AI to show memory comparison code.",
        deliverable: "generator_performance.py with memory comparison"
      }
    ],
    
    successCriteria: [
      "Can read list comprehensions fluently",
      "Know when loops are clearer than comprehensions",
      "Understand generator expressions for large data",
      "Can convert between loops and comprehensions"
    ],
    
    futureProofNote: "AI generates comprehensions constantly. Being able to read them quickly is essential for reviewing AI code."
  },
  
  {
    dayNumber: 6,
    week: 2,
    topic: "Dictionaries & JSON",
    subtitle: "Data Engineering's Core Data Format",
    
    objectives: [
      "Master dict operations with AI assistance",
      "Parse and generate JSON (critical for data engineering)",
      "Use AI to transform between data formats",
      "Handle nested JSON structures"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "JSON is the language of APIs. AI is excellent at JSON transformations. Focus on understanding the structure.",
      warningWhenNotToUseAI: "Parse a simple JSON manually first to understand the structure."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Create a dict representing yourself. What keys would you include?"
      },
      theory: {
        duration: 15,
        content: [
          "Dictionaries as the foundation of data records",
          "JSON: JavaScript Object Notation (but we use it in Python)",
          "API responses are JSON - you'll work with this daily",
          "Schema inference from JSON (AI is great at this)"
        ],
        keyConceptes: [
          "Key-value pairs",
          "JSON serialization",
          "Nested structures",
          "API responses"
        ]
      },
      practice: {
        duration: 60,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review JSON parsing code",
          "Commit changes"
        ]
      }
    },
    
    resources: [
      {
        title: "Real Python: Working with JSON",
        url: "https://realpython.com/python-json/",
        type: "article",
        duration: "20 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "API Response Parsing",
        difficulty: "intermediate",
        estimatedTime: 25,
        instructions: [
          "Use this sample API response: https://jsonplaceholder.typicode.com/users",
          "Ask AI to write code to fetch and parse it",
          "Extract: all names, all emails, users in specific city",
          "Handle potential errors (network, parsing)"
        ],
        aiApproach: "AI writes the fetch/parse code. You understand the structure.",
        deliverable: "api_parser.py fetching real data"
      },
      {
        title: "JSON to Different Formats",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Given a list of user dicts, ask AI to:",
          "- Convert to CSV format",
          "- Convert to SQL INSERT statements",
          "- Convert to markdown table",
          "Understand each transformation"
        ],
        aiApproach: "Data format transformation is an AI strength. Learn the patterns.",
        deliverable: "format_conversions.py with multiple output formats"
      },
      {
        title: "Nested JSON Flattening",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Create deeply nested JSON (user with addresses with cities)",
          "Ask AI: # Flatten this nested JSON to a flat dict",
          "Understand the recursive solution",
          "Discuss: When is flattening needed? (Data warehouses!)"
        ],
        aiApproach: "Flattening is tricky - let AI show the pattern, then understand it.",
        deliverable: "json_flatten.py with before/after examples"
      }
    ],
    
    successCriteria: [
      "Can parse JSON from APIs",
      "Understand nested JSON structures",
      "Can transform between JSON and other formats",
      "Know when to flatten vs keep nested"
    ],
    
    futureProofNote: "JSON handling is fundamental to data engineering. AI makes the transformation code easy; understanding what transformation to do is your job."
  },
  
  {
    dayNumber: 7,
    week: 2,
    topic: "File I/O & Context Managers",
    subtitle: "Reading and Writing Data Files",
    
    objectives: [
      "Read/write text, CSV, JSON files with AI",
      "Understand context managers (with statement)",
      "Handle file encoding issues",
      "Process large files efficiently"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "File I/O patterns are repetitive - perfect for AI. Focus on error handling and encoding.",
      warningWhenNotToUseAI: "Understand the 'with' statement - it's crucial for resource management."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "What happens if you forget to close a file? Why does 'with' solve this?"
      },
      theory: {
        duration: 15,
        content: [
          "Context managers and resource cleanup",
          "File modes: r, w, a, r+, rb, wb",
          "Encoding issues (UTF-8 vs Latin-1)",
          "Memory-efficient reading of large files"
        ],
        keyConceptes: [
          "Context manager",
          "File modes",
          "Character encoding",
          "Streaming reads"
        ]
      },
      practice: {
        duration: 60,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review file handling code",
          "Test with different file sizes"
        ]
      }
    },
    
    resources: [
      {
        title: "Corey Schafer: File Objects",
        url: "https://www.youtube.com/watch?v=Uh2ebFW8OYM",
        type: "video",
        duration: "24 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "CSV Processing Pipeline",
        difficulty: "intermediate",
        estimatedTime: 25,
        instructions: [
          "Create a CSV with sample data (or use a public dataset)",
          "Ask AI to write: read CSV, transform data, write new CSV",
          "Add error handling for missing files, bad data",
          "Process the file line-by-line (memory efficient)"
        ],
        aiApproach: "AI generates the pipeline. You add error handling.",
        deliverable: "csv_pipeline.py with robust error handling"
      },
      {
        title: "Log File Parser",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Create a sample log file (or use /var/log/system.log)",
          "Ask AI: Parse log, extract errors, count by type",
          "Handle encoding issues if they occur",
          "Output summary statistics"
        ],
        aiApproach: "Log parsing is messy - let AI handle regex, you verify results.",
        deliverable: "log_parser.py extracting insights from logs"
      },
      {
        title: "Large File Processing",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Generate a 100MB text file (or use any large file)",
          "Write code to process it WITHOUT loading into memory",
          "Compare: reading all at once vs line-by-line",
          "Measure memory usage for both approaches"
        ],
        aiApproach: "Ask AI for 'memory-efficient' approach specifically.",
        deliverable: "large_file_processor.py with memory comparison"
      }
    ],
    
    successCriteria: [
      "Always use 'with' for file operations",
      "Can handle CSV, JSON, text files",
      "Know how to process large files efficiently",
      "Can handle encoding issues"
    ],
    
    futureProofNote: "File I/O is being replaced by cloud storage APIs in modern data engineering. But the concepts (streaming, encoding, error handling) remain critical."
  },
  
  {
    dayNumber: 8,
    week: 2,
    topic: "Error Handling & Defensive Code",
    subtitle: "Making Code Robust with AI",
    
    objectives: [
      "Write proper try/except blocks",
      "Understand Python's exception hierarchy",
      "Use AI to identify potential failure points",
      "Create custom exceptions for clarity"
    ],
    
    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often writes the 'happy path' and forgets error handling. Ask: 'Add error handling to this code'",
      warningWhenNotToUseAI: "Understand exception flow yourself - it's crucial for debugging."
    },
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "What happens when you divide by zero? What about accessing a missing dict key?"
      },
      theory: {
        duration: 20,
        content: [
          "Exception types in Python",
          "try/except/else/finally flow",
          "Catching specific vs generic exceptions",
          "When to raise vs handle exceptions"
        ],
        keyConceptes: [
          "Exception handling",
          "Exception hierarchy",
          "Custom exceptions",
          "Defensive programming"
        ]
      },
      practice: {
        duration: 55,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review Week 2 error handling patterns",
          "Complete weekly checkpoint"
        ]
      }
    },
    
    resources: [
      {
        title: "Corey Schafer: Exception Handling",
        url: "https://www.youtube.com/watch?v=NIWwJbo-9_8",
        type: "video",
        duration: "18 min",
        priority: "required"
      }
    ],
    
    exercises: [
      {
        title: "Add Error Handling to AI Code",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Take any AI-generated code from this week",
          "Identify all potential failure points",
          "Add appropriate try/except blocks",
          "Log errors meaningfully"
        ],
        aiApproach: "Ask AI: 'What can go wrong with this code?' Then add handling.",
        deliverable: "robust_code.py with comprehensive error handling"
      },
      {
        title: "Custom Exception Classes",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Create custom exceptions for a data pipeline:",
          "DataValidationError, SourceConnectionError, TransformationError",
          "Raise them in appropriate places",
          "Catch and handle them differently"
        ],
        aiApproach: "AI can generate exception classes. You decide when to raise them.",
        deliverable: "custom_exceptions.py with usage examples"
      },
      {
        title: "Retry Pattern Implementation",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Write a function that might fail (simulate network call)",
          "Implement retry logic: try 3 times with exponential backoff",
          "Ask AI: 'Use the tenacity library for retries'",
          "Compare manual vs library approach"
        ],
        aiApproach: "Let AI show you the tenacity library - it's what professionals use.",
        deliverable: "retry_patterns.py with both implementations"
      }
    ],
    
    successCriteria: [
      "Always catch specific exceptions, not bare except",
      "Know when to handle vs raise exceptions",
      "Can add error handling to existing code",
      "Understand retry patterns for unreliable operations"
    ],
    
    weeklyCheckpoint: {
      title: "Week 2: AI-Assisted Python Deepening",
      description: "You should now write more Pythonic code with AI help and handle errors robustly.",
      deliverables: [
        "All week 2 code in GitHub",
        "Examples of loops converted to comprehensions",
        "JSON parsing code for at least one real API",
        "Code with comprehensive error handling",
        "Notes on AI-generated code you had to fix"
      ],
      selfAssessment: [
        "Can I read list comprehensions fluently?",
        "Do I understand JSON structure deeply?",
        "Can I identify where AI forgets error handling?",
        "Am I writing defensive code by habit?"
      ]
    },
    
    futureProofNote: "Error handling is critical in production systems. AI helps write it, but understanding WHY you handle each error is the human skill."
  },

  // ============================================================================
  // WEEK 3: Production Python + Git (Days 9-12)
  // ============================================================================

  {
    dayNumber: 9,
    week: 2,
    topic: "Python Classes & OOP for Production",
    subtitle: "Build production-ready code with proper structure",

    objectives: [
      "Master class design for data engineering",
      "Understand when to use classes vs functions",
      "Implement __init__, __str__, __repr__",
      "Build reusable data pipeline components"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask AI to explain when classes add value vs just using functions. Understanding this design decision is key.",
      warningWhenNotToUseAI: "Don't over-engineer. Simple functions are often better than classes with one method."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python OOP Basics - Corey Schafer", type: "video" },
      { time: "0:15-0:35", activity: "Class design patterns: when OOP helps vs hurts", type: "learn" },
      { time: "0:35-0:55", activity: "Exercise 1-2: Basic classes + __str__/__repr__", type: "exercise" },
      { time: "0:55-1:15", activity: "Exercise 3: Properties - computed attributes", type: "exercise" },
      { time: "1:15-1:35", activity: "Exercise 4: Class methods and static methods", type: "exercise" },
      { time: "1:35-1:55", activity: "Exercise 5-6: DataExtractor, DataValidator, composition", type: "exercise" },
      { time: "1:55-2:00", activity: "Run tests, review patterns learned", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - OOP Tutorial", url: "https://www.youtube.com/watch?v=ZDa-Z5JzLYM", type: "video" }
      ],
      optional: [
        { title: "Real Python: OOP Guide", url: "https://realpython.com/python3-object-oriented-programming/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Basic Class Design",
        description: "DataRecord and User classes with __init__ and methods",
        estimatedTime: 20,
        deliverable: "Completed DataRecord and User classes"
      },
      {
        title: "Exercise 2: __str__ and __repr__",
        description: "Control how objects display - Pipeline and APIResponse classes",
        estimatedTime: 15,
        deliverable: "Proper string representations"
      },
      {
        title: "Exercise 3: Properties",
        description: "DataBatch and Connection with computed properties",
        estimatedTime: 20,
        deliverable: "Classes with @property decorators"
      },
      {
        title: "Exercise 4: Class & Static Methods",
        description: "Config and DataLoader with factory methods",
        estimatedTime: 20,
        deliverable: "Factory patterns with @classmethod"
      },
      {
        title: "Exercise 5: DataExtractor Pattern",
        description: "Production-ready data extractor class",
        estimatedTime: 25,
        deliverable: "Complete DataExtractor with state management"
      },
      {
        title: "Exercise 6: Composition",
        description: "DataPipeline using Logger - composition over inheritance",
        estimatedTime: 20,
        deliverable: "Pipeline with injected dependencies"
      }
    ],

    keyTerms: [
      { term: "__init__", definition: "Constructor method - called when creating an instance" },
      { term: "__str__", definition: "Human-readable string representation" },
      { term: "__repr__", definition: "Unambiguous string for debugging - should be valid Python" },
      { term: "@property", definition: "Decorator that makes a method act like an attribute" },
      { term: "@classmethod", definition: "Method that receives class as first argument - for factory methods" },
      { term: "Composition", definition: "Building objects by combining other objects (has-a relationship)" }
    ],

    commonMistakes: [
      "Creating classes when simple functions would work better",
      "Forgetting self in method definitions",
      "Using inheritance when composition is cleaner",
      "Not implementing __repr__ for debugging"
    ],

    successCriteria: [
      "Can design classes for pipeline components",
      "Understand when OOP adds value vs overhead",
      "All exercises pass tests",
      "Classes are well-documented with docstrings"
    ],

    futureProofNote: "Most data engineering libraries use OOP. Understanding classes helps you use Pandas, SQLAlchemy, Airflow effectively."
  },

  // Day 10: Logging & Configuration
  {
    dayNumber: 10,
    week: 2,
    topic: "Logging & Configuration Management",
    subtitle: "Production-ready logging and config patterns",

    objectives: [
      "Implement structured logging with Python's logging module",
      "Create configuration management patterns",
      "Use environment variables and config files",
      "Build observable, debuggable code"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to generate logging boilerplate, but understand log levels and when to use each.",
      warningWhenNotToUseAI: "Understand what you're logging and why - security-sensitive data should never be logged."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Python logging module - levels, handlers, formatters", type: "learn" },
      { time: "0:20-0:40", activity: "Exercise 1: Basic logger setup", type: "exercise" },
      { time: "0:40-1:05", activity: "Exercise 2: Structured (JSON) logging", type: "exercise" },
      { time: "1:05-1:25", activity: "Exercise 3: Environment-based configuration", type: "exercise" },
      { time: "1:25-1:45", activity: "Exercise 4: File-based configuration", type: "exercise" },
      { time: "1:45-2:00", activity: "Exercise 5: Complete configurable pipeline", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "Python Logging Tutorial", url: "https://docs.python.org/3/howto/logging.html", type: "docs" },
        { title: "12-Factor App Config", url: "https://12factor.net/config", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Basic Logger Setup",
        description: "Create loggers with console and file handlers",
        estimatedTime: 20,
        deliverable: "setup_basic_logger and setup_file_logger functions"
      },
      {
        title: "Exercise 2: Structured Logger",
        description: "JSON-formatted logs for production systems",
        estimatedTime: 25,
        deliverable: "StructuredLogger class with level filtering"
      },
      {
        title: "Exercise 3: Environment Config",
        description: "Load config from environment variables with type conversion",
        estimatedTime: 20,
        deliverable: "EnvConfig class with get_bool, get_int, get_list"
      },
      {
        title: "Exercise 4: File Config",
        description: "Load config from JSON files with nested access",
        estimatedTime: 20,
        deliverable: "FileConfig class with get_nested and merge"
      },
      {
        title: "Exercise 5: Configurable Pipeline",
        description: "Complete pipeline with logging and configuration",
        estimatedTime: 30,
        deliverable: "ConfigurablePipeline class with full observability"
      }
    ],

    keyTerms: [
      { term: "Log Level", definition: "Severity of message: DEBUG < INFO < WARNING < ERROR < CRITICAL" },
      { term: "Handler", definition: "Destination for log messages (console, file, network)" },
      { term: "Formatter", definition: "Controls the output format of log messages" },
      { term: "Structured Logging", definition: "JSON-formatted logs for machine parsing" },
      { term: "12-Factor App", definition: "Methodology for building cloud-native apps - config via env vars" }
    ],

    commonMistakes: [
      "Logging sensitive data (passwords, tokens)",
      "Using print() instead of logging",
      "Hardcoding configuration instead of using environment variables",
      "Not setting appropriate log levels for different environments"
    ],

    successCriteria: [
      "Proper log levels (DEBUG, INFO, WARNING, ERROR)",
      "Configuration from environment variables",
      "Structured JSON logs working",
      "No sensitive data in logs"
    ],

    futureProofNote: "Good logging is essential for debugging production systems. This is a senior-level skill."
  },

  // Day 11: Git Fundamentals
  {
    dayNumber: 11,
    week: 2,
    topic: "Git Fundamentals",
    subtitle: "Version control for professional development",

    objectives: [
      "Master Git branching and merging",
      "Write meaningful commit messages",
      "Handle merge conflicts confidently",
      "Use Git for collaboration"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'manual-practice',
      aiTip: "Git commands should become muscle memory. Practice manually, use AI only to explain concepts.",
      warningWhenNotToUseAI: "Don't use AI for Git commands - you need to understand exactly what you're doing."
    },

    sessionPlan: [
      { time: "0:00-0:10", activity: "Exercise 1: Repository setup and first commits", type: "exercise" },
      { time: "0:10-0:30", activity: "Exercise 2: Branching practice - feature branches", type: "exercise" },
      { time: "0:30-0:50", activity: "Exercise 3: Merging and conflict resolution", type: "exercise" },
      { time: "0:50-1:10", activity: "Exercise 4: Commit message conventions", type: "exercise" },
      { time: "1:10-1:25", activity: "Exercise 5: Viewing history and blame", type: "exercise" },
      { time: "1:25-1:40", activity: "Exercise 6: Undoing changes safely", type: "exercise" },
      { time: "1:40-1:55", activity: "Exercise 7: Git stash", type: "exercise" },
      { time: "1:55-2:00", activity: "Take Git quiz, verify exercises", type: "review" }
    ],

    resources: {
      required: [
        { title: "Learn Git Branching", url: "https://learngitbranching.js.org/", type: "interactive" }
      ],
      optional: [
        { title: "Atlassian Git Tutorial", url: "https://www.atlassian.com/git/tutorials", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Repository Setup",
        description: "Initialize repo, create initial commits with proper structure",
        estimatedTime: 10,
        deliverable: "Git repo with README and .gitignore"
      },
      {
        title: "Exercise 2: Branching Practice",
        description: "Create feature branches, switch between them, make changes",
        estimatedTime: 20,
        deliverable: "Multiple branches with commits"
      },
      {
        title: "Exercise 3: Merging Practice",
        description: "Merge branches, resolve conflicts when they occur",
        estimatedTime: 20,
        deliverable: "Clean merged history"
      },
      {
        title: "Exercise 4: Commit Messages",
        description: "Practice conventional commit format (Add:, Fix:, etc.)",
        estimatedTime: 20,
        deliverable: "Well-formatted commit history"
      },
      {
        title: "Exercise 5: History Exploration",
        description: "Use git log, git show, git diff, git blame",
        estimatedTime: 15,
        deliverable: "Understanding of history commands"
      },
      {
        title: "Exercise 6: Undoing Changes",
        description: "Practice reset, revert, checkout safely",
        estimatedTime: 15,
        deliverable: "Safely undone changes"
      },
      {
        title: "Exercise 7: Git Stash",
        description: "Save work in progress, switch branches, restore",
        estimatedTime: 10,
        deliverable: "Stash workflow mastered"
      }
    ],

    keyTerms: [
      { term: "Branch", definition: "Independent line of development" },
      { term: "Merge", definition: "Combine changes from different branches" },
      { term: "Conflict", definition: "When same lines changed in both branches" },
      { term: "Stash", definition: "Temporarily save uncommitted changes" },
      { term: "HEAD", definition: "Pointer to current commit/branch" }
    ],

    commonMistakes: [
      "Committing directly to main instead of using branches",
      "Vague commit messages like 'fixed stuff'",
      "Force pushing without understanding consequences",
      "Not pulling before starting work"
    ],

    successCriteria: [
      "Can create and merge branches",
      "Handle merge conflicts confidently",
      "Write clear commit messages",
      "Use stash for work-in-progress"
    ],

    futureProofNote: "Git proficiency is non-negotiable for any engineering role."
  },

  // Day 12: GitHub PRs & Workflows
  {
    dayNumber: 12,
    week: 2,
    topic: "GitHub PRs & Professional Workflows",
    subtitle: "Collaborate like a professional engineer",

    objectives: [
      "Create professional Pull Requests",
      "Write effective PR descriptions",
      "Review code effectively",
      "Use GitHub Actions basics"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'ai-review',
      aiTip: "Use AI to help write PR descriptions and review your own code before submitting.",
      warningWhenNotToUseAI: "You need to understand the code review process personally."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Exercise 1: Create GitHub repository", type: "exercise" },
      { time: "0:15-0:35", activity: "Exercise 2: Feature branch workflow", type: "exercise" },
      { time: "0:35-0:55", activity: "Exercise 3: Create a Pull Request", type: "exercise" },
      { time: "0:55-1:20", activity: "Exercise 4: Code review practice", type: "exercise" },
      { time: "1:20-1:40", activity: "Exercise 5: Handle review feedback", type: "exercise" },
      { time: "1:40-1:55", activity: "Exercise 6-7: Merge strategies & Issues", type: "exercise" },
      { time: "1:55-2:00", activity: "Week 3 checkpoint review", type: "review" }
    ],

    resources: {
      required: [
        { title: "GitHub Pull Requests", url: "https://docs.github.com/en/pull-requests", type: "docs" }
      ],
      optional: [
        { title: "GitHub Actions Quickstart", url: "https://docs.github.com/en/actions/quickstart", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: GitHub Repository",
        description: "Create a new repository on GitHub with README and .gitignore",
        estimatedTime: 15,
        deliverable: "Public repository for portfolio"
      },
      {
        title: "Exercise 2: Feature Branch Workflow",
        description: "Create branch, push, see 'Compare & pull request' button",
        estimatedTime: 20,
        deliverable: "Branch pushed to GitHub"
      },
      {
        title: "Exercise 3: Create Pull Request",
        description: "Write professional PR with summary, changes, testing",
        estimatedTime: 20,
        deliverable: "PR with proper description"
      },
      {
        title: "Exercise 4: Code Review",
        description: "Practice reviewing code - add comments, suggest changes",
        estimatedTime: 25,
        deliverable: "Review comments on PR"
      },
      {
        title: "Exercise 5: Handle Feedback",
        description: "Make requested changes, push updates, respond to comments",
        estimatedTime: 20,
        deliverable: "Updated PR ready to merge"
      },
      {
        title: "Exercise 6: Merge Strategies",
        description: "Understand merge, squash, and rebase options",
        estimatedTime: 15,
        deliverable: "Successfully merged PR"
      },
      {
        title: "Exercise 7: Issues",
        description: "Create and reference issues in commits",
        estimatedTime: 15,
        deliverable: "Issue linked to PR"
      }
    ],

    keyTerms: [
      { term: "Pull Request", definition: "Request to merge changes into a branch" },
      { term: "Code Review", definition: "Examining code changes for quality and issues" },
      { term: "Squash Merge", definition: "Combine all commits into one when merging" },
      { term: "GitHub Actions", definition: "CI/CD automation built into GitHub" }
    ],

    commonMistakes: [
      "PRs that are too large - break into smaller pieces",
      "Missing PR description",
      "Not responding to review comments",
      "Merging without approval"
    ],

    successCriteria: [
      "PRs have clear descriptions",
      "Can give and receive code review",
      "Understand merge strategies"
    ],

    weeklyCheckpoint: {
      title: "Week 3: Production Python + Git",
      description: "You now write production-quality Python and can collaborate using Git.",
      deliverables: [
        "DataExtractor class with logging",
        "Clean Git repository with branches",
        "At least one merged PR"
      ],
      selfAssessment: [
        "Is my code production-ready?",
        "Can I collaborate using Git?",
        "Are my PRs professional?"
      ]
    },

    futureProofNote: "GitHub proficiency is essential for any modern engineering job."
  },

  // Day 13: Advanced Git + Code Review (Friday)
  {
    dayNumber: 13,
    week: 2,
    topic: "Advanced Git + Code Review Practice",
    subtitle: "Deep dive into Git workflows and reviewing code",

    objectives: [
      "Master interactive rebase and history rewriting",
      "Understand Git hooks and automation",
      "Practice reviewing code effectively",
      "Build muscle memory for common Git operations"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'manual-practice',
      aiTip: "Use AI to explain complex Git concepts, but practice the commands manually.",
      warningWhenNotToUseAI: "Git operations need muscle memory - don't rely on AI for daily commands."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Interactive rebase practice", type: "exercise" },
      { time: "0:20-0:40", activity: "Git bisect for debugging", type: "exercise" },
      { time: "0:40-1:00", activity: "Cherry-pick and reverting", type: "exercise" },
      { time: "1:00-1:20", activity: "Git hooks and pre-commit", type: "learn" },
      { time: "1:20-1:40", activity: "Code review best practices", type: "learn" },
      { time: "1:40-2:00", activity: "Review a real open source PR", type: "exercise" },
      { time: "2:00-2:30", activity: "Practice reviewing your own code", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "Git Rebase Tutorial", url: "https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase", type: "tutorial" },
        { title: "How to Review Code", url: "https://google.github.io/eng-practices/review/reviewer/", type: "article" }
      ],
      optional: [
        { title: "pre-commit Docs", url: "https://pre-commit.com/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Interactive Rebase",
        description: "Reorder, squash, and edit commits in your practice repo",
        estimatedTime: 20,
        deliverable: "Clean commit history after rebase"
      },
      {
        title: "Exercise 2: Git Bisect",
        description: "Use bisect to find when a bug was introduced",
        estimatedTime: 20,
        deliverable: "Found the buggy commit"
      },
      {
        title: "Exercise 3: Cherry-pick & Revert",
        description: "Practice moving commits between branches and undoing",
        estimatedTime: 20,
        deliverable: "Successfully cherry-picked and reverted"
      },
      {
        title: "Exercise 4: Pre-commit Hooks",
        description: "Set up pre-commit with black, flake8, and mypy",
        estimatedTime: 20,
        deliverable: "Working pre-commit config"
      },
      {
        title: "Exercise 5: Review Practice",
        description: "Review an open source PR and write comments",
        estimatedTime: 20,
        deliverable: "Thoughtful review comments written"
      },
      {
        title: "Exercise 6: Self-Review",
        description: "Review your own code from this week",
        estimatedTime: 30,
        deliverable: "Improvements identified and applied"
      }
    ],

    keyTerms: [
      { term: "Interactive Rebase", definition: "Rewrite commit history - reorder, squash, edit" },
      { term: "Git Bisect", definition: "Binary search through commits to find bugs" },
      { term: "Cherry-pick", definition: "Apply a specific commit to another branch" },
      { term: "Pre-commit Hook", definition: "Script that runs before each commit" },
      { term: "Code Review", definition: "Examining code changes for quality, bugs, and style" }
    ],

    commonMistakes: [
      "Rebasing commits that have been pushed (dangerous!)",
      "Not testing after rebase",
      "Being too harsh or too lenient in code reviews",
      "Forgetting to pull before starting work"
    ],

    successCriteria: [
      "Can use interactive rebase confidently",
      "Understand when to rebase vs merge",
      "Can give constructive code review feedback",
      "Pre-commit hooks working"
    ],

    weeklyCheckpoint: {
      title: "Week 2: Production Python + Git",
      description: "You now write production-quality Python and collaborate professionally with Git.",
      deliverables: [
        "DataExtractor and DataValidator classes",
        "Logging and configuration setup",
        "Git repository with clean history",
        "At least one merged PR",
        "Pre-commit hooks configured"
      ],
      selfAssessment: [
        "Is my Python code production-ready?",
        "Can I use Git confidently for any workflow?",
        "Can I give and receive code review?"
      ]
    },

    futureProofNote: "Advanced Git skills separate senior engineers from juniors. Master these."
  },

  // ============================================================================
  // WEEK 3: AWS + Docker Basics (Days 16-22)
  // ============================================================================

  {
    dayNumber: 16,
    week: 3,
    topic: "AWS Account Setup & IAM",
    subtitle: "Your first steps into cloud infrastructure",

    objectives: [
      "Set up AWS account with proper security",
      "Understand IAM users, roles, and policies",
      "Configure AWS CLI",
      "Implement least-privilege access"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to explain AWS concepts, but NEVER share credentials or account details.",
      warningWhenNotToUseAI: "Security configuration must be understood - don't blindly copy IAM policies."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Exercise 1: AWS account creation (if needed)", type: "exercise" },
      { time: "0:20-0:30", activity: "Exercise 2: Enable MFA on root account", type: "exercise" },
      { time: "0:30-0:50", activity: "Exercise 3: Create IAM admin user", type: "exercise" },
      { time: "0:50-1:05", activity: "Exercise 4: Configure AWS CLI", type: "exercise" },
      { time: "1:05-1:25", activity: "Exercise 5: Understanding IAM policies", type: "learn" },
      { time: "1:25-1:45", activity: "Exercise 6: Create data engineering role", type: "exercise" },
      { time: "1:45-2:00", activity: "Exercise 7: Set up billing alerts + quiz", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "AWS IAM Getting Started", url: "https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html", type: "docs" },
        { title: "AWS Free Tier", url: "https://aws.amazon.com/free/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: AWS Account Setup",
        description: "Create AWS account if you don't have one",
        estimatedTime: 20,
        deliverable: "Active AWS account"
      },
      {
        title: "Exercise 2: Root Account MFA",
        description: "Enable MFA on root account - CRITICAL security step",
        estimatedTime: 10,
        deliverable: "MFA enabled on root"
      },
      {
        title: "Exercise 3: IAM Admin User",
        description: "Create IAM user for daily work with admin access",
        estimatedTime: 20,
        deliverable: "IAM user with MFA"
      },
      {
        title: "Exercise 4: AWS CLI Setup",
        description: "Install and configure AWS CLI with access keys",
        estimatedTime: 15,
        deliverable: "aws sts get-caller-identity works"
      },
      {
        title: "Exercise 5: IAM Policies",
        description: "Read and understand IAM policy structure",
        estimatedTime: 20,
        deliverable: "Can read and write basic policies"
      },
      {
        title: "Exercise 6: Data Pipeline Role",
        description: "Create IAM role for Lambda/data pipelines",
        estimatedTime: 20,
        deliverable: "data-pipeline-role created"
      },
      {
        title: "Exercise 7: Billing Alerts",
        description: "Set up billing alerts to avoid surprise charges",
        estimatedTime: 15,
        deliverable: "CloudWatch billing alarm"
      }
    ],

    keyTerms: [
      { term: "IAM", definition: "Identity and Access Management - controls who can do what" },
      { term: "Policy", definition: "JSON document defining permissions" },
      { term: "Role", definition: "Identity for services/apps, not humans" },
      { term: "MFA", definition: "Multi-Factor Authentication - extra security layer" },
      { term: "Least Privilege", definition: "Only grant permissions actually needed" }
    ],

    commonMistakes: [
      "Not enabling MFA on root account",
      "Using root account for daily work",
      "Committing access keys to Git",
      "Overly permissive IAM policies"
    ],

    successCriteria: [
      "AWS CLI working",
      "IAM user with least-privilege",
      "MFA enabled on root account",
      "Billing alerts configured"
    ],

    futureProofNote: "AWS skills are highly valued. This is the foundation for cloud data engineering."
  },

  {
    dayNumber: 17,
    week: 3,
    topic: "S3 Fundamentals & Best Practices",
    subtitle: "Cloud storage for data engineering",

    objectives: [
      "Create and manage S3 buckets",
      "Understand storage classes and lifecycle policies",
      "Implement proper data organization",
      "Use boto3 for S3 operations"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to generate boto3 code, but understand the S3 concepts behind it."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Exercise 1: Create S3 bucket with proper naming", type: "exercise" },
      { time: "0:15-0:35", activity: "Exercise 2: Data lake folder structure", type: "exercise" },
      { time: "0:35-0:55", activity: "Exercise 3: Upload/download with CLI and Python", type: "exercise" },
      { time: "0:55-1:10", activity: "Exercise 4: S3 Select - query in place", type: "exercise" },
      { time: "1:10-1:25", activity: "Exercise 5: Lifecycle policies", type: "exercise" },
      { time: "1:25-1:45", activity: "Exercise 6: Bucket policies", type: "exercise" },
      { time: "1:45-2:00", activity: "Exercise 7: Event notifications + verify", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "AWS S3 User Guide", url: "https://docs.aws.amazon.com/s3/", type: "docs" },
        { title: "boto3 S3 Docs", url: "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Create Bucket",
        description: "Create bucket with proper naming (globally unique)",
        estimatedTime: 15,
        deliverable: "S3 bucket created"
      },
      {
        title: "Exercise 2: Folder Structure",
        description: "Create raw/processed/curated/archive structure",
        estimatedTime: 20,
        deliverable: "Data lake structure in place"
      },
      {
        title: "Exercise 3: Upload/Download",
        description: "Use AWS CLI and boto3 for S3 operations",
        estimatedTime: 20,
        deliverable: "Files uploaded and downloaded"
      },
      {
        title: "Exercise 4: S3 Select",
        description: "Query JSON data in S3 without full download",
        estimatedTime: 15,
        deliverable: "S3 Select query working"
      },
      {
        title: "Exercise 5: Lifecycle Policies",
        description: "Set up automatic transitions to cheaper storage",
        estimatedTime: 15,
        deliverable: "Lifecycle rule for archive folder"
      },
      {
        title: "Exercise 6: Bucket Policies",
        description: "Control access at bucket level",
        estimatedTime: 20,
        deliverable: "Bucket policy allowing specific role"
      },
      {
        title: "Exercise 7: Event Notifications",
        description: "Trigger actions when files arrive",
        estimatedTime: 15,
        deliverable: "Event notification configured"
      }
    ],

    keyTerms: [
      { term: "Bucket", definition: "Container for objects in S3" },
      { term: "Object", definition: "File stored in S3 (up to 5TB)" },
      { term: "Prefix", definition: "Folder-like path in S3 (s3://bucket/prefix/file)" },
      { term: "Storage Class", definition: "Tier determining cost/access speed" },
      { term: "Lifecycle Policy", definition: "Rules for automatic data management" }
    ],

    commonMistakes: [
      "Not using partitioning for large datasets",
      "Public buckets (major security risk)",
      "Forgetting about data transfer costs",
      "Not enabling versioning for important data"
    ],

    successCriteria: [
      "S3 bucket created with proper structure",
      "Can upload/download with boto3",
      "Understand lifecycle policies",
      "Bucket policies configured"
    ],

    futureProofNote: "S3 is fundamental to AWS data engineering. Master it."
  },

  {
    dayNumber: 18,
    week: 3,
    topic: "Docker Fundamentals",
    subtitle: "Containerize your applications",

    objectives: [
      "Understand containers vs VMs",
      "Write Dockerfiles",
      "Build and run Docker images",
      "Use Docker Compose basics"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to generate Dockerfiles, but understand each instruction."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Exercise 1: Docker installation verification", type: "exercise" },
      { time: "0:15-0:30", activity: "Exercise 2: Images vs containers concepts", type: "learn" },
      { time: "0:30-0:55", activity: "Exercise 3: Your first Dockerfile", type: "exercise" },
      { time: "0:55-1:20", activity: "Exercise 4: Dockerfile with dependencies", type: "exercise" },
      { time: "1:20-1:40", activity: "Exercise 5: Volumes - persisting data", type: "exercise" },
      { time: "1:40-1:55", activity: "Exercise 6: Networking - exposing ports", type: "exercise" },
      { time: "1:55-2:00", activity: "Docker quiz + verify", type: "review" }
    ],

    resources: {
      required: [
        { title: "Docker Getting Started", url: "https://docs.docker.com/get-started/", type: "docs" }
      ],
      optional: [
        { title: "Docker Curriculum", url: "https://docker-curriculum.com/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Docker Installation",
        description: "Install Docker Desktop, run hello-world",
        estimatedTime: 15,
        deliverable: "Docker installed and running"
      },
      {
        title: "Exercise 2: Images & Containers",
        description: "Pull images, list, run containers",
        estimatedTime: 15,
        deliverable: "Understanding of image vs container"
      },
      {
        title: "Exercise 3: First Dockerfile",
        description: "Create simple Python app Dockerfile",
        estimatedTime: 25,
        deliverable: "Working Docker image"
      },
      {
        title: "Exercise 4: Dependencies",
        description: "Dockerfile with requirements.txt, proper layering",
        estimatedTime: 25,
        deliverable: "Image with Python dependencies"
      },
      {
        title: "Exercise 5: Volumes",
        description: "Mount directories for persistent data",
        estimatedTime: 20,
        deliverable: "Container with volume mount"
      },
      {
        title: "Exercise 6: Port Mapping",
        description: "Expose ports for web applications",
        estimatedTime: 15,
        deliverable: "Container with exposed port"
      }
    ],

    keyTerms: [
      { term: "Image", definition: "Read-only template for creating containers" },
      { term: "Container", definition: "Running instance of an image" },
      { term: "Dockerfile", definition: "Text file with instructions to build image" },
      { term: "Volume", definition: "Persistent storage for container data" },
      { term: "Layer", definition: "Each instruction in Dockerfile creates a cached layer" }
    ],

    commonMistakes: [
      "Using :latest tag (not reproducible)",
      "Not leveraging layer caching (copy deps first)",
      "Running as root in production",
      "Large images (use slim/alpine bases)"
    ],

    successCriteria: [
      "Can write Dockerfiles",
      "Can build and run containers",
      "Understand volumes and port mapping"
    ],

    futureProofNote: "Docker is standard for modern deployment. Essential skill."
  },

  {
    dayNumber: 19,
    week: 3,
    topic: "Docker for Data Engineering",
    subtitle: "Production Docker patterns",

    objectives: [
      "Multi-stage builds for smaller images",
      "Docker Compose for multi-container apps",
      "Environment management in Docker",
      "Docker best practices"
    ],

    aiIntegration: {
      toolsUsed: ['copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to optimize Dockerfiles, but verify the optimizations make sense."
    },

    sessionPlan: [
      { time: "0:00-0:30", activity: "Exercise 1: Containerized data pipeline", type: "exercise" },
      { time: "0:30-1:10", activity: "Exercise 2: Local data stack with Docker Compose", type: "exercise" },
      { time: "1:10-1:30", activity: "Exercise 3: Database init scripts", type: "exercise" },
      { time: "1:30-1:55", activity: "Exercise 4-5: Python app with database + workflow", type: "exercise" },
      { time: "1:55-2:00", activity: "Week 4 checkpoint + verify stack", type: "review" }
    ],

    resources: {
      required: [
        { title: "Docker Compose Docs", url: "https://docs.docker.com/compose/", type: "docs" }
      ],
      optional: [
        { title: "Awesome Compose Examples", url: "https://github.com/docker/awesome-compose", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Exercise 1: Data Pipeline Container",
        description: "Build complete data extraction pipeline in Docker",
        estimatedTime: 30,
        deliverable: "Containerized extractor with volume mounts"
      },
      {
        title: "Exercise 2: Local Data Stack",
        description: "Docker Compose with Postgres, MinIO, Redis, Adminer",
        estimatedTime: 40,
        deliverable: "Full local development environment"
      },
      {
        title: "Exercise 3: Database Init",
        description: "Auto-create tables on first container start",
        estimatedTime: 20,
        deliverable: "Init scripts that run automatically"
      },
      {
        title: "Exercise 4: App with Database",
        description: "Python app connecting to Postgres in Docker",
        estimatedTime: 25,
        deliverable: "End-to-end data flow working"
      },
      {
        title: "Exercise 5: Dev Workflow",
        description: "Hot reload, mounted volumes, interactive debugging",
        estimatedTime: 10,
        deliverable: "Efficient development workflow"
      }
    ],

    keyTerms: [
      { term: "Docker Compose", definition: "Tool for defining multi-container applications" },
      { term: "Service", definition: "One container configuration in docker-compose.yml" },
      { term: "depends_on", definition: "Define service startup order" },
      { term: "healthcheck", definition: "Verify service is ready before dependent starts" },
      { term: "Named Volume", definition: "Docker-managed persistent storage" }
    ],

    commonMistakes: [
      "Not waiting for database to be ready",
      "Hardcoding connection strings (use environment vars)",
      "Not using named volumes for data",
      "Forgetting to rebuild after Dockerfile changes"
    ],

    successCriteria: [
      "Docker Compose stack running",
      "Postgres, MinIO accessible",
      "Python app connects to database"
    ],

    weeklyCheckpoint: {
      title: "Week 4: AWS + Docker",
      description: "You now have cloud and containerization fundamentals.",
      deliverables: [
        "AWS account with proper IAM",
        "S3 bucket with data structure",
        "Dockerized Python application",
        "Docker Compose setup"
      ],
      selfAssessment: [
        "Can I deploy to AWS?",
        "Can I containerize any Python app?",
        "Do I understand cloud security basics?"
      ]
    },

    futureProofNote: "AWS + Docker are the foundation of modern data infrastructure."
  },

  // ============================================================================
  // WEEKS 5-6: PROJECT 1 - Real-Time Stock Pipeline (Days 17-24)
  // ============================================================================

  {
    dayNumber: 17,
    week: 5,
    topic: "Project 1: Alpha Vantage API Integration",
    subtitle: "Start building your showcase project",

    objectives: [
      "Understand the Alpha Vantage API",
      "Build data extraction code",
      "Handle API rate limits and errors",
      "Structure raw data for storage"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'cursor'],
      focusArea: 'learn-with-ai',
      aiTip: "Use AI to help with API integration boilerplate, but design the error handling yourself."
    },

    sessionPlan: [
      { time: "0:00-0:30", activity: "API exploration and design", type: "learn" },
      { time: "0:30-1:15", activity: "Build extraction code", type: "exercise" },
      { time: "1:15-1:30", activity: "Test with real API", type: "review" }
    ],

    resources: {
      required: [
        { title: "Alpha Vantage API Docs", url: "https://www.alphavantage.co/documentation/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Stock Data Extractor",
        description: "Build a robust API client for stock data",
        deliverable: "stock_extractor.py with error handling"
      }
    ],

    successCriteria: [
      "API integration working",
      "Proper error handling",
      "Rate limiting handled"
    ],

    futureProofNote: "API integration is core to data engineering. This project proves you can do it."
  },

  {
    dayNumber: 18, week: 5, topic: "Project 1: AWS Lambda Deployment",
    subtitle: "Deploy extraction to serverless", objectives: ["Create Lambda function", "Configure triggers", "Handle Lambda limitations", "Deploy with AWS CLI/SAM"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Use AI for Lambda boilerplate but understand the execution model." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Lambda development and deployment", type: "exercise" }],
    resources: { required: [{ title: "AWS Lambda Docs", url: "https://docs.aws.amazon.com/lambda/", type: "docs" }] },
    exercises: [{ title: "Lambda Deployment", description: "Deploy stock extractor to Lambda", deliverable: "Working Lambda function" }],
    successCriteria: ["Lambda deployed", "Triggers configured", "Logs visible in CloudWatch"],
    futureProofNote: "Serverless is a key pattern for cost-effective data pipelines."
  },

  {
    dayNumber: 19, week: 5, topic: "Project 1: S3 Storage & Partitioning",
    subtitle: "Structure data for analytics", objectives: ["Design S3 partition strategy", "Implement data landing zone", "Handle data formats", "Build transformation layer"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Use AI to generate S3 code, you design the partition strategy." },
    sessionPlan: [{ time: "0:00-1:30", activity: "S3 storage implementation", type: "exercise" }],
    resources: { required: [{ title: "S3 Best Practices", url: "https://docs.aws.amazon.com/s3/", type: "docs" }] },
    exercises: [{ title: "S3 Data Lake", description: "Implement partitioned storage", deliverable: "S3 structure with proper partitions" }],
    successCriteria: ["Data partitioned by date", "Raw and processed zones", "Proper file formats"],
    futureProofNote: "Good data organization is essential for scalable analytics."
  },

  {
    dayNumber: 20, week: 5, topic: "Project 1: PostgreSQL Setup",
    subtitle: "Build the analytics database", objectives: ["Design star schema", "Create tables and indexes", "Load data from S3", "Query optimization"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'ai-review', aiTip: "Use AI for SQL generation, you design the schema." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Database setup and loading", type: "exercise" }],
    resources: { required: [{ title: "PostgreSQL Docs", url: "https://www.postgresql.org/docs/", type: "docs" }] },
    exercises: [{ title: "Analytics Database", description: "Create and populate PostgreSQL schema", deliverable: "Working database with stock data" }],
    successCriteria: ["Schema designed", "Data loaded", "Queries optimized"],
    futureProofNote: "Database design is fundamental. This demonstrates your SQL skills."
  },

  {
    dayNumber: 21, week: 6, topic: "Project 1: Data Transformation Pipeline",
    subtitle: "Build the transformation layer", objectives: ["Implement data cleaning", "Calculate technical indicators", "Handle data quality issues", "Build idempotent transformations"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'ai-review', aiTip: "AI helps with calculations, you ensure data quality." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Transformation development", type: "exercise" }],
    resources: { required: [] },
    exercises: [{ title: "Transformation Pipeline", description: "Clean and transform stock data", deliverable: "transformation.py with full pipeline" }],
    successCriteria: ["Transformations correct", "Idempotent operations", "Quality checks in place"],
    futureProofNote: "Transformation logic is where domain knowledge meets code."
  },

  {
    dayNumber: 22, week: 6, topic: "Project 1: Airflow DAG Basics",
    subtitle: "Orchestrate the pipeline", objectives: ["Create first Airflow DAG", "Define task dependencies", "Implement basic scheduling", "Handle errors in DAGs"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Use AI for DAG boilerplate, understand the execution model." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Airflow DAG development", type: "exercise" }],
    resources: { required: [{ title: "Airflow Docs", url: "https://airflow.apache.org/docs/", type: "docs" }] },
    exercises: [{ title: "Stock Pipeline DAG", description: "Create Airflow DAG for stock pipeline", deliverable: "stock_pipeline_dag.py" }],
    successCriteria: ["DAG runs successfully", "Dependencies correct", "Error handling works"],
    futureProofNote: "Airflow is industry standard. This is essential experience."
  },

  {
    dayNumber: 23, week: 6, topic: "Project 1: Streamlit Dashboard",
    subtitle: "Build the visualization layer", objectives: ["Create interactive dashboard", "Display real-time data", "Add user controls", "Deploy dashboard"],
    aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Streamlit is perfect for AI-assisted development. Let it help." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Dashboard development", type: "exercise" }],
    resources: { required: [{ title: "Streamlit Docs", url: "https://docs.streamlit.io/", type: "docs" }] },
    exercises: [{ title: "Stock Dashboard", description: "Create interactive stock dashboard", deliverable: "streamlit_app.py deployed" }],
    successCriteria: ["Dashboard deployed", "Shows real-time data", "Interactive controls"],
    futureProofNote: "Visualization skills make you a complete data engineer."
  },

  {
    dayNumber: 24, week: 6, topic: "Project 1: Polish & Documentation",
    subtitle: "Complete your showcase project", objectives: ["Polish code to portfolio quality", "Write comprehensive README", "Create architecture diagram", "Record demo"],
    aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Use AI for documentation drafts, make it your voice." },
    sessionPlan: [{ time: "0:00-1:30", activity: "Project finalization", type: "exercise" }],
    resources: { required: [] },
    exercises: [{ title: "Project 1 Completion", description: "Finalize and document the project", deliverable: "Complete GitHub repository" }],
    successCriteria: ["Code polished", "README complete", "Architecture diagram done"],
    weeklyCheckpoint: { title: "Month 1 Complete: Project 1 Done", description: "You've built a complete data pipeline. This is interview-ready.", deliverables: ["Live pipeline running", "GitHub with professional README", "Architecture diagram", "Streamlit dashboard"], selfAssessment: ["Can I explain every component?", "Is this portfolio-ready?", "Would I be proud to show this?"] },
    futureProofNote: "PROJECT 1 COMPLETE. This alone shows you can build production data pipelines."
  },

  // ============================================================================
  // WEEKS 7-10: DBT + PROJECT 2 (Days 25-40) - Streamlined
  // ============================================================================

  { dayNumber: 25, week: 7, topic: "dbt Fundamentals", subtitle: "Modern analytics engineering", objectives: ["Understand dbt philosophy", "Create first dbt project", "Write models with refs", "Run and test models"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "dbt + AI is a powerful combo. Use it." }, sessionPlan: [{ time: "0:00-1:30", activity: "dbt fundamentals", type: "learn" }], resources: { required: [{ title: "dbt Learn", url: "https://courses.getdbt.com/", type: "tutorial" }] }, exercises: [{ title: "First dbt Project", deliverable: "Working dbt project" }], successCriteria: ["dbt project running", "Models building"], futureProofNote: "dbt is essential for modern data stacks." },

  { dayNumber: 26, week: 7, topic: "dbt Materializations", subtitle: "Tables, views, incremental", objectives: ["Understand materialization types", "Choose right materialization", "Configure materializations"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Let AI explain materializations with examples." }, sessionPlan: [{ time: "0:00-1:30", activity: "Materialization practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Materialization Practice", deliverable: "Models with different materializations" }], successCriteria: ["Correct materializations chosen"], futureProofNote: "Materialization choice is a key interview topic." },

  { dayNumber: 27, week: 7, topic: "dbt Staging → Marts Pattern", subtitle: "Professional dbt architecture", objectives: ["Understand staging layer", "Build intermediate models", "Create mart models"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "This pattern is fundamental - learn it well." }, sessionPlan: [{ time: "0:00-1:30", activity: "dbt architecture", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Layer Architecture", deliverable: "staging/intermediate/marts folders" }], successCriteria: ["Clean separation of layers"], futureProofNote: "This pattern is industry standard." },

  { dayNumber: 28, week: 7, topic: "dbt Sources & Seeds", subtitle: "Define your data sources", objectives: ["Configure sources", "Create seed files", "Document sources"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Sources and seeds are simple - get them right." }, sessionPlan: [{ time: "0:00-1:30", activity: "Sources and seeds", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Source Configuration", deliverable: "sources.yml and seeds" }], successCriteria: ["Sources documented", "Seeds loading"], futureProofNote: "Proper source configuration is professional practice." },

  { dayNumber: 29, week: 8, topic: "dbt Testing", subtitle: "Data quality in dbt", objectives: ["Built-in tests", "Custom tests", "Test coverage strategy"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Testing is where dbt shines. Learn it well." }, sessionPlan: [{ time: "0:00-1:30", activity: "dbt testing", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Test Coverage", deliverable: "Comprehensive test suite" }], successCriteria: ["100% model coverage"], futureProofNote: "Testing is a certification topic." },

  { dayNumber: 30, week: 8, topic: "Custom dbt Tests", subtitle: "Advanced data validation", objectives: ["Write custom schema tests", "Data tests for business rules", "Test macros"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Custom tests show advanced skills." }, sessionPlan: [{ time: "0:00-1:30", activity: "Custom tests", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Custom Tests", deliverable: "Custom test macros" }], successCriteria: ["Custom tests working"], futureProofNote: "Custom tests demonstrate mastery." },

  { dayNumber: 31, week: 8, topic: "dbt Macros & Jinja", subtitle: "DRY principles in dbt", objectives: ["Write macros", "Use Jinja templating", "Create reusable code"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Macros are powerful - AI helps write them." }, sessionPlan: [{ time: "0:00-1:30", activity: "Macros practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Macro Library", deliverable: "Reusable macros" }], successCriteria: ["Macros working"], futureProofNote: "Macro skills are valued." },

  { dayNumber: 32, week: 8, topic: "dbt Packages & Docs", subtitle: "Ecosystem and documentation", objectives: ["Use dbt packages", "Generate documentation", "Deploy dbt docs"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Documentation is your friend in interviews." }, sessionPlan: [{ time: "0:00-1:30", activity: "Packages and docs", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "dbt Docs Site", deliverable: "Deployed dbt docs" }], successCriteria: ["Docs deployed"], futureProofNote: "Good documentation is professional." },

  { dayNumber: 33, week: 9, topic: "Project 2: NBA API Integration", subtitle: "Start analytics platform", objectives: ["Explore NBA APIs", "Build ingestion pipeline", "Handle multiple endpoints"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "API integration patterns from Project 1 apply here." }, sessionPlan: [{ time: "0:00-1:30", activity: "NBA data ingestion", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "NBA Ingestion", deliverable: "nba_ingestion.py" }], successCriteria: ["Data flowing"], futureProofNote: "Second project reinforces skills." },

  { dayNumber: 34, week: 9, topic: "Project 2: Snowflake Setup", subtitle: "Cloud data warehouse", objectives: ["Set up Snowflake", "Load data", "Configure dbt connection"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Snowflake is industry standard - learn it." }, sessionPlan: [{ time: "0:00-1:30", activity: "Snowflake setup", type: "exercise" }], resources: { required: [{ title: "Snowflake Docs", url: "https://docs.snowflake.com/", type: "docs" }] }, exercises: [{ title: "Snowflake Environment", deliverable: "Working Snowflake with data" }], successCriteria: ["Snowflake running", "dbt connected"], futureProofNote: "Snowflake experience is highly valued." },

  { dayNumber: 35, week: 9, topic: "Project 2: dbt Staging Models", subtitle: "Build the foundation", objectives: ["Create staging models", "Clean NBA data", "Add tests"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Apply dbt patterns from training." }, sessionPlan: [{ time: "0:00-1:30", activity: "Staging development", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Staging Layer", deliverable: "Complete staging models" }], successCriteria: ["Staging complete"], futureProofNote: "Clean staging is the foundation." },

  { dayNumber: 36, week: 9, topic: "Project 2: Intermediate Models", subtitle: "Business logic layer", objectives: ["Build intermediate transformations", "Join data sources", "Calculate metrics"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Intermediate layer is where business logic lives." }, sessionPlan: [{ time: "0:00-1:30", activity: "Intermediate development", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Intermediate Layer", deliverable: "Intermediate models" }], successCriteria: ["Intermediate complete"], futureProofNote: "This layer shows domain understanding." },

  { dayNumber: 37, week: 10, topic: "Project 2: Marts & Dimensional Model", subtitle: "Analytics-ready data", objectives: ["Build dimension tables", "Create fact tables", "Optimize for analytics"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Dimensional modeling is a key interview skill." }, sessionPlan: [{ time: "0:00-1:30", activity: "Marts development", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Marts Layer", deliverable: "Dimensional model" }], successCriteria: ["Star schema complete"], futureProofNote: "Dimensional modeling is essential." },

  { dayNumber: 38, week: 10, topic: "Project 2: Test Coverage", subtitle: "Quality assurance", objectives: ["Add comprehensive tests", "Create data quality checks", "Document models"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'ai-review', aiTip: "Test coverage shows professional practice." }, sessionPlan: [{ time: "0:00-1:30", activity: "Testing", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Full Test Suite", deliverable: "100% test coverage" }], successCriteria: ["All tests passing"], futureProofNote: "Testing is expected." },

  { dayNumber: 39, week: 10, topic: "Project 2: Dashboard", subtitle: "Visualization layer", objectives: ["Build NBA dashboard", "Interactive analysis", "Deploy dashboard"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Dashboard makes the project tangible." }, sessionPlan: [{ time: "0:00-1:30", activity: "Dashboard development", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "NBA Dashboard", deliverable: "Deployed dashboard" }], successCriteria: ["Dashboard live"], futureProofNote: "Visualization completes the story." },

  { dayNumber: 40, week: 10, topic: "Project 2: Polish + dbt Cert Prep", subtitle: "Complete Month 2", objectives: ["Polish project", "Prepare for dbt certification", "Document everything"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Use AI for cert prep questions." }, sessionPlan: [{ time: "0:00-1:30", activity: "Project completion", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Project 2 Complete", deliverable: "Portfolio-ready project" }], successCriteria: ["Project complete", "Cert prep started"], weeklyCheckpoint: { title: "Month 2 Complete: dbt Master", description: "Two projects complete. dbt certification ready.", deliverables: ["NBA Analytics Platform", "dbt project with 20+ models", "Snowflake experience"], selfAssessment: ["Ready for dbt cert?", "Two strong portfolio pieces?"] }, futureProofNote: "MONTH 2 COMPLETE. Two portfolio projects done." },

  // ============================================================================
  // WEEKS 11-14: AIRFLOW + PROJECT 3 + START APPLYING (Days 41-56)
  // ============================================================================

  { dayNumber: 41, week: 11, topic: "Airflow Architecture", subtitle: "Deep dive into orchestration", objectives: ["Understand Airflow components", "Scheduler, workers, metadata DB", "Deployment options"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Understand architecture before coding." }, sessionPlan: [{ time: "0:00-1:30", activity: "Airflow architecture", type: "learn" }], resources: { required: [{ title: "Airflow Concepts", url: "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html", type: "docs" }] }, exercises: [{ title: "Architecture Diagram", deliverable: "Airflow architecture notes" }], successCriteria: ["Understand all components"], futureProofNote: "Architecture understanding is senior-level." },

  { dayNumber: 42, week: 11, topic: "DAG Design Patterns", subtitle: "Professional DAG design", objectives: ["DAG best practices", "Idempotency patterns", "Error handling"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Good DAG design is crucial for production." }, sessionPlan: [{ time: "0:00-1:30", activity: "DAG patterns", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "DAG Patterns", deliverable: "Pattern examples" }], successCriteria: ["Understand patterns"], futureProofNote: "DAG design is an interview topic." },

  { dayNumber: 43, week: 11, topic: "TaskFlow API & Operators", subtitle: "Modern Airflow development", objectives: ["TaskFlow API", "Common operators", "Custom operators intro"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "TaskFlow is modern Airflow - learn it." }, sessionPlan: [{ time: "0:00-1:30", activity: "TaskFlow development", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "TaskFlow DAG", deliverable: "Modern DAG implementation" }], successCriteria: ["TaskFlow working"], futureProofNote: "Modern Airflow skills." },

  { dayNumber: 44, week: 11, topic: "XComs & Dependencies", subtitle: "Task communication", objectives: ["XCom patterns", "Complex dependencies", "Branching logic"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "XComs are important for complex pipelines." }, sessionPlan: [{ time: "0:00-1:30", activity: "XCom practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "XCom Pipeline", deliverable: "DAG with XComs" }], successCriteria: ["XComs working"], futureProofNote: "Complex DAG skills." },

  { dayNumber: 45, week: 12, topic: "Airflow Testing", subtitle: "Test your DAGs", objectives: ["Unit testing DAGs", "Integration testing", "CI/CD for Airflow"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "DAG testing is professional practice." }, sessionPlan: [{ time: "0:00-1:30", activity: "DAG testing", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "DAG Tests", deliverable: "Test suite for DAGs" }], successCriteria: ["Tests passing"], futureProofNote: "Testing is expected." },

  { dayNumber: 46, week: 12, topic: "Error Handling in DAGs", subtitle: "Production error patterns", objectives: ["Retry logic", "Alerting", "Dead letter patterns"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Error handling makes or breaks production." }, sessionPlan: [{ time: "0:00-1:30", activity: "Error handling", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Robust DAG", deliverable: "DAG with full error handling" }], successCriteria: ["Errors handled gracefully"], futureProofNote: "Production error handling is senior-level." },

  { dayNumber: 47, week: 12, topic: "Resume & LinkedIn Polish", subtitle: "START APPLYING", objectives: ["Update resume with projects", "Polish LinkedIn", "Start job applications"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Use AI to review resume bullets." }, sessionPlan: [{ time: "0:00-1:30", activity: "Resume work + applications", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Application Ready", deliverable: "Polished resume, 5 applications" }], successCriteria: ["Resume ready", "5 apps submitted"], futureProofNote: "START APPLYING NOW." },

  { dayNumber: 48, week: 12, topic: "Applications Sprint", subtitle: "Apply to 10 companies", objectives: ["Submit 10 applications", "Tailor each application", "Track in spreadsheet"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "AI helps customize cover letters." }, sessionPlan: [{ time: "0:00-1:30", activity: "Application submission", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "10 Applications", deliverable: "10 submitted applications" }], successCriteria: ["10 apps submitted"], futureProofNote: "Volume matters. Keep applying." },

  { dayNumber: 49, week: 13, topic: "Project 3: Multi-Source DAGs", subtitle: "Complex orchestration", objectives: ["Build multi-API DAGs", "Parallel extraction", "Data consolidation"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Project 3 shows orchestration mastery." }, sessionPlan: [{ time: "0:00-1:30", activity: "Multi-source DAG", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Multi-Source Pipeline", deliverable: "Complex DAG structure" }], successCriteria: ["Multiple sources working"], futureProofNote: "Complexity showcase." },

  { dayNumber: 50, week: 13, topic: "Project 3: Great Expectations", subtitle: "Data quality framework", objectives: ["Set up Great Expectations", "Create expectations", "Integrate with DAGs"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "GX is industry standard for data quality." }, sessionPlan: [{ time: "0:00-1:30", activity: "Great Expectations setup", type: "exercise" }], resources: { required: [{ title: "Great Expectations Docs", url: "https://docs.greatexpectations.io/", type: "docs" }] }, exercises: [{ title: "GX Integration", deliverable: "Working GX suite" }], successCriteria: ["Expectations running"], futureProofNote: "Data quality is essential." },

  { dayNumber: 51, week: 13, topic: "Project 3: Quality Framework", subtitle: "Build comprehensive checks", objectives: ["Define quality rules", "Automated validation", "Quarantine layer"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Quality framework shows maturity." }, sessionPlan: [{ time: "0:00-1:30", activity: "Quality framework", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Quality Rules", deliverable: "Complete quality framework" }], successCriteria: ["Framework complete"], futureProofNote: "Data quality is a senior focus." },

  { dayNumber: 52, week: 13, topic: "Applications: Keep Applying", subtitle: "Continue job search", objectives: ["Submit 7 applications", "Follow up on previous", "Refine approach"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Track everything in spreadsheet." }, sessionPlan: [{ time: "0:00-1:30", activity: "Applications", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "7 More Applications", deliverable: "7 new applications" }], successCriteria: ["7 apps submitted"], futureProofNote: "Consistency in applying." },

  { dayNumber: 53, week: 14, topic: "Project 3: Monitoring", subtitle: "Observable pipelines", objectives: ["Build monitoring dashboard", "Set up alerting", "Track SLAs"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Monitoring shows production thinking." }, sessionPlan: [{ time: "0:00-1:30", activity: "Monitoring setup", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Monitoring Dashboard", deliverable: "Pipeline dashboard" }], successCriteria: ["Monitoring live"], futureProofNote: "Observability is senior-level." },

  { dayNumber: 54, week: 14, topic: "Project 3: Deployment", subtitle: "Production deployment", objectives: ["Containerize project", "Deploy to cloud", "Production configuration"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'learn-with-ai', aiTip: "Deployment shows end-to-end skill." }, sessionPlan: [{ time: "0:00-1:30", activity: "Deployment", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Production Deploy", deliverable: "Deployed project" }], successCriteria: ["Project deployed"], futureProofNote: "Deployment is essential." },

  { dayNumber: 55, week: 14, topic: "Project 3: Documentation", subtitle: "Complete the project", objectives: ["Write documentation", "Create architecture diagram", "Record demo"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Documentation makes portfolio shine." }, sessionPlan: [{ time: "0:00-1:30", activity: "Documentation", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Complete Documentation", deliverable: "Portfolio-ready docs" }], successCriteria: ["Docs complete"], futureProofNote: "Documentation is professional." },

  { dayNumber: 56, week: 14, topic: "30+ Applications Milestone", subtitle: "Month 3 complete", objectives: ["Hit 30 applications", "Review responses", "Adjust strategy"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Analyze what's working." }, sessionPlan: [{ time: "0:00-1:30", activity: "Application review", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "30 App Milestone", deliverable: "30+ applications submitted" }], successCriteria: ["30+ apps", "Strategy refined"], weeklyCheckpoint: { title: "Month 3 Complete: Three Projects + Applying", description: "Portfolio complete. Applications flowing.", deliverables: ["Three portfolio projects", "30+ applications", "Interview readiness"], selfAssessment: ["Portfolio strong?", "Application response rate?"] }, futureProofNote: "MONTH 3 COMPLETE. Portfolio done, now close." },

  // ============================================================================
  // WEEKS 15-18: AWS CERTIFICATION (Days 57-72) - Condensed
  // ============================================================================

  { dayNumber: 57, week: 15, topic: "AWS SAA: S3 Deep Dive", subtitle: "Storage mastery", objectives: ["S3 storage classes", "Lifecycle policies", "Cross-region replication"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "S3 is ~10% of exam." }, sessionPlan: [{ time: "0:00-1:30", activity: "S3 study", type: "learn" }], resources: { required: [] }, exercises: [{ title: "S3 Practice", deliverable: "S3 practice questions" }], successCriteria: ["S3 concepts clear"], futureProofNote: "AWS cert proves cloud skills." },

  { dayNumber: 58, week: 15, topic: "AWS SAA: EC2 + Lambda", subtitle: "Compute services", objectives: ["EC2 instance types", "Lambda patterns", "Pricing models"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Compute is major exam topic." }, sessionPlan: [{ time: "0:00-1:30", activity: "Compute study", type: "learn" }], resources: { required: [] }, exercises: [{ title: "Compute Practice", deliverable: "Practice questions" }], successCriteria: ["Compute clear"], futureProofNote: "Compute knowledge essential." },

  { dayNumber: 59, week: 15, topic: "AWS SAA: RDS + Redshift", subtitle: "Database services", objectives: ["RDS features", "Redshift architecture", "Aurora"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Databases are key for DE." }, sessionPlan: [{ time: "0:00-1:30", activity: "Database study", type: "learn" }], resources: { required: [] }, exercises: [{ title: "Database Practice", deliverable: "Practice questions" }], successCriteria: ["Database clear"], futureProofNote: "AWS database knowledge." },

  { dayNumber: 60, week: 15, topic: "Applications: 7 This Week", subtitle: "Keep momentum", objectives: ["Submit 7 applications", "Track responses"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Balance study with applying." }, sessionPlan: [{ time: "0:00-1:30", activity: "Applications", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Weekly Applications", deliverable: "7 apps" }], successCriteria: ["7 apps submitted"], futureProofNote: "Keep applying." },

  { dayNumber: 61, week: 16, topic: "AWS SAA: VPC + Networking", subtitle: "Network architecture", objectives: ["VPC design", "Security groups", "Route tables"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Networking is critical." }, sessionPlan: [{ time: "0:00-1:30", activity: "Networking study", type: "learn" }], resources: { required: [] }, exercises: [{ title: "VPC Practice", deliverable: "Practice questions" }], successCriteria: ["VPC clear"], futureProofNote: "Network security essential." },

  { dayNumber: 62, week: 16, topic: "AWS SAA: IAM Deep Dive", subtitle: "Security fundamentals", objectives: ["IAM policies", "Roles and federation", "Organizations"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "IAM is always on the exam." }, sessionPlan: [{ time: "0:00-1:30", activity: "IAM study", type: "learn" }], resources: { required: [] }, exercises: [{ title: "IAM Practice", deliverable: "Practice questions" }], successCriteria: ["IAM clear"], futureProofNote: "Security knowledge critical." },

  { dayNumber: 63, week: 16, topic: "AWS SAA: Glue + Athena", subtitle: "Data services", objectives: ["Glue ETL", "Athena queries", "Data catalog"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Data services for DE." }, sessionPlan: [{ time: "0:00-1:30", activity: "Data services", type: "learn" }], resources: { required: [] }, exercises: [{ title: "Glue Practice", deliverable: "Practice questions" }], successCriteria: ["Data services clear"], futureProofNote: "AWS data services." },

  { dayNumber: 64, week: 16, topic: "Applications + Interviews", subtitle: "Interview prep starts", objectives: ["7 applications", "Prep for interviews"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Interviews may start coming." }, sessionPlan: [{ time: "0:00-1:30", activity: "Apps + prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interview Prep", deliverable: "7 apps + prep" }], successCriteria: ["Ready for interviews"], futureProofNote: "Interview mode starting." },

  { dayNumber: 65, week: 17, topic: "AWS SAA: Practice Exam 1", subtitle: "First mock exam", objectives: ["Take practice exam", "Identify weak areas"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Practice exams show readiness." }, sessionPlan: [{ time: "0:00-1:30", activity: "Practice exam", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Practice Exam 1", deliverable: "Score and analysis" }], successCriteria: ["70%+ score"], futureProofNote: "Practice exams essential." },

  { dayNumber: 66, week: 17, topic: "AWS SAA: Review Weak Areas", subtitle: "Targeted study", objectives: ["Review missed topics", "Deep dive weak areas"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Focus on weak areas." }, sessionPlan: [{ time: "0:00-1:30", activity: "Review", type: "learn" }], resources: { required: [] }, exercises: [{ title: "Weak Area Review", deliverable: "Improved understanding" }], successCriteria: ["Weak areas addressed"], futureProofNote: "Targeted study effective." },

  { dayNumber: 67, week: 17, topic: "AWS SAA: Practice Exam 2", subtitle: "Second mock exam", objectives: ["Take second practice", "Validate improvement"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Should see improvement." }, sessionPlan: [{ time: "0:00-1:30", activity: "Practice exam 2", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Practice Exam 2", deliverable: "Score improvement" }], successCriteria: ["80%+ score"], futureProofNote: "Improvement shows readiness." },

  { dayNumber: 68, week: 17, topic: "First Interviews", subtitle: "Interview season", objectives: ["Conduct first interviews", "Learn from each one"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Debrief after each interview." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interviews", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interview Debrief", deliverable: "Interview notes" }], successCriteria: ["Interviews happening"], futureProofNote: "Each interview is practice." },

  { dayNumber: 69, week: 18, topic: "AWS SAA: Final Review", subtitle: "Last prep day", objectives: ["Final review", "Rest before exam"], aiIntegration: { toolsUsed: ['chatgpt'], focusArea: 'learn-with-ai', aiTip: "Light review, don't cram." }, sessionPlan: [{ time: "0:00-1:30", activity: "Final review", type: "learn" }], resources: { required: [] }, exercises: [{ title: "Final Review", deliverable: "Ready for exam" }], successCriteria: ["Confident for exam"], futureProofNote: "Ready to certify." },

  { dayNumber: 70, week: 18, topic: "AWS SAA: TAKE EXAM", subtitle: "Certification day", objectives: ["Take AWS SAA exam", "PASS"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "No AI in exams!" }, sessionPlan: [{ time: "0:00-1:30", activity: "EXAM DAY", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Take Exam", deliverable: "AWS SAA Certification" }], successCriteria: ["CERTIFIED"], futureProofNote: "AWS SAA on resume." },

  { dayNumber: 71, week: 18, topic: "Interview Prep Intensifies", subtitle: "Full interview mode", objectives: ["System design practice", "Behavioral prep"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Practice system design." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interview prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interview Practice", deliverable: "Practice sessions" }], successCriteria: ["Ready for interviews"], futureProofNote: "Interview mode." },

  { dayNumber: 72, week: 18, topic: "5-10 Interviews Scheduled", subtitle: "Month 4 complete", objectives: ["Have interviews scheduled", "Pipeline building"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Keep pipeline full." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interview scheduling", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interview Pipeline", deliverable: "5-10 interviews scheduled" }], successCriteria: ["Pipeline full"], weeklyCheckpoint: { title: "Month 4 Complete: AWS Certified + Interviewing", description: "AWS certified. Interview pipeline active.", deliverables: ["AWS SAA Certification", "5-10 interviews scheduled"], selfAssessment: ["Certified?", "Interviews happening?"] }, futureProofNote: "MONTH 4 COMPLETE. Now close." },

  // ============================================================================
  // WEEKS 19-22: INTERVIEW PREP + INTERVIEWING (Days 73-88) - Condensed
  // ============================================================================

  { dayNumber: 73, week: 19, topic: "System Design: Data Pipelines", subtitle: "Design interviews", objectives: ["Pipeline design patterns", "Scalability discussion"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Practice explaining designs." }, sessionPlan: [{ time: "0:00-1:30", activity: "System design", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Pipeline Design", deliverable: "Design practice" }], successCriteria: ["Can design pipelines"], futureProofNote: "System design is senior-level." },

  { dayNumber: 74, week: 19, topic: "System Design: Data Warehouses", subtitle: "Warehouse architecture", objectives: ["Warehouse design", "Schema decisions"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Know trade-offs." }, sessionPlan: [{ time: "0:00-1:30", activity: "Warehouse design", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Warehouse Design", deliverable: "Design practice" }], successCriteria: ["Can design warehouses"], futureProofNote: "Warehouse knowledge essential." },

  { dayNumber: 75, week: 19, topic: "System Design: Streaming", subtitle: "Real-time systems", objectives: ["Streaming architecture", "Event processing"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Know when to use streaming." }, sessionPlan: [{ time: "0:00-1:30", activity: "Streaming design", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Streaming Design", deliverable: "Design practice" }], successCriteria: ["Can discuss streaming"], futureProofNote: "Streaming shows breadth." },

  { dayNumber: 76, week: 19, topic: "Continue Interviewing", subtitle: "Interview execution", objectives: ["Conduct interviews", "Improve with each"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Debrief after each." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interviews", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interviews", deliverable: "Interview notes" }], successCriteria: ["Interviews happening"], futureProofNote: "Every interview is practice." },

  { dayNumber: 77, week: 20, topic: "SQL Interview Questions", subtitle: "Technical prep", objectives: ["Complex SQL patterns", "Window functions", "Optimization"], aiIntegration: { toolsUsed: ['copilot'], focusArea: 'manual-practice', aiTip: "Practice SQL without AI." }, sessionPlan: [{ time: "0:00-1:30", activity: "SQL practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "SQL Practice", deliverable: "SQL solutions" }], successCriteria: ["SQL sharp"], futureProofNote: "SQL always tested." },

  { dayNumber: 78, week: 20, topic: "Python Coding Challenges", subtitle: "Coding prep", objectives: ["Data structures", "Algorithm practice"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "No AI for coding practice." }, sessionPlan: [{ time: "0:00-1:30", activity: "Python practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Python Practice", deliverable: "Coding solutions" }], successCriteria: ["Python sharp"], futureProofNote: "Coding always tested." },

  { dayNumber: 79, week: 20, topic: "Data Modeling Questions", subtitle: "Modeling interviews", objectives: ["Dimensional modeling", "Schema design"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Know modeling patterns." }, sessionPlan: [{ time: "0:00-1:30", activity: "Modeling practice", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Modeling Practice", deliverable: "Design examples" }], successCriteria: ["Modeling confident"], futureProofNote: "Modeling expected." },

  { dayNumber: 80, week: 20, topic: "Continue Interviewing", subtitle: "Keep momentum", objectives: ["More interviews", "Refine approach"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "You're improving." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interviews", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Interviews", deliverable: "Progress" }], successCriteria: ["Improving"], futureProofNote: "Getting better." },

  { dayNumber: 81, week: 21, topic: "Behavioral Prep (STAR)", subtitle: "Soft skills", objectives: ["STAR method", "Story library", "Leadership examples"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Prepare 5-7 stories." }, sessionPlan: [{ time: "0:00-1:30", activity: "Behavioral prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Story Library", deliverable: "STAR stories" }], successCriteria: ["Stories ready"], futureProofNote: "Behavioral always asked." },

  { dayNumber: 82, week: 21, topic: "Mock Interview 1", subtitle: "Full practice", objectives: ["Complete mock interview", "Get feedback"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Practice with friend or AI." }, sessionPlan: [{ time: "0:00-1:30", activity: "Mock interview", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Mock Interview", deliverable: "Feedback notes" }], successCriteria: ["Got feedback"], futureProofNote: "Mocks improve performance." },

  { dayNumber: 83, week: 21, topic: "Mock Interview 2", subtitle: "Second mock", objectives: ["Apply feedback", "Improve delivery"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Focus on weak areas." }, sessionPlan: [{ time: "0:00-1:30", activity: "Mock interview", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Mock Interview 2", deliverable: "Improved performance" }], successCriteria: ["Better than first"], futureProofNote: "Iteration improves." },

  { dayNumber: 84, week: 21, topic: "Continue Interviewing", subtitle: "Getting close", objectives: ["Final round interviews", "Closing conversations"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Start talking offers." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interviews", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Final Rounds", deliverable: "Progress to offers" }], successCriteria: ["Final rounds happening"], futureProofNote: "Getting close." },

  { dayNumber: 85, week: 22, topic: "Refine Your Story", subtitle: "Polish narrative", objectives: ["Refine career narrative", "Project stories"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Your story is your brand." }, sessionPlan: [{ time: "0:00-1:30", activity: "Story refinement", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Career Story", deliverable: "Polished narrative" }], successCriteria: ["Story compelling"], futureProofNote: "Narrative matters." },

  { dayNumber: 86, week: 22, topic: "Technical Deep Dives", subtitle: "Expert mode", objectives: ["Deep technical discussions", "Architecture explanations"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Know your projects deeply." }, sessionPlan: [{ time: "0:00-1:30", activity: "Technical prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Project Deep Dive", deliverable: "Expert explanations" }], successCriteria: ["Expert level"], futureProofNote: "Deep knowledge impresses." },

  { dayNumber: 87, week: 22, topic: "Negotiation Prep", subtitle: "Get what you're worth", objectives: ["Negotiation strategy", "Research compensation"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Know your number and walk away point." }, sessionPlan: [{ time: "0:00-1:30", activity: "Negotiation prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Negotiation Strategy", deliverable: "Negotiation plan" }], successCriteria: ["Strategy ready"], futureProofNote: "Negotiation gets you $10-20k more." },

  { dayNumber: 88, week: 22, topic: "Multiple Offers in Play", subtitle: "Month 5 complete", objectives: ["Multiple offers or close", "Compare opportunities"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Leverage multiple offers." }, sessionPlan: [{ time: "0:00-1:30", activity: "Offer comparison", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Offer Analysis", deliverable: "Comparison matrix" }], successCriteria: ["Offers in hand or coming"], weeklyCheckpoint: { title: "Month 5 Complete: Final Stretch", description: "Offers coming. Negotiation time.", deliverables: ["Multiple interview processes", "Negotiation ready"], selfAssessment: ["Offers coming?", "Ready to negotiate?"] }, futureProofNote: "MONTH 5 COMPLETE. Close it." },

  // ============================================================================
  // WEEKS 23-24: CLOSE OFFERS (Days 89-96)
  // ============================================================================

  { dayNumber: 89, week: 23, topic: "Final Round Prep", subtitle: "Close strong", objectives: ["Final round preparation", "Executive presence"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Final rounds are about fit." }, sessionPlan: [{ time: "0:00-1:30", activity: "Final prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Final Round Ready", deliverable: "Prepared" }], successCriteria: ["Ready to close"], futureProofNote: "Final rounds decide offers." },

  { dayNumber: 90, week: 23, topic: "Final Interviews", subtitle: "Execute", objectives: ["Conduct final interviews", "Show your best"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "Trust your preparation." }, sessionPlan: [{ time: "0:00-1:30", activity: "Interviews", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Final Interviews", deliverable: "Completed finals" }], successCriteria: ["Finals done"], futureProofNote: "You've got this." },

  { dayNumber: 91, week: 23, topic: "Compare Offers", subtitle: "Make the right choice", objectives: ["Analyze offers", "Consider total comp", "Evaluate culture"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Consider more than just salary." }, sessionPlan: [{ time: "0:00-1:30", activity: "Offer analysis", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Offer Comparison", deliverable: "Decision framework" }], successCriteria: ["Clear preference"], futureProofNote: "Right choice matters long-term." },

  { dayNumber: 92, week: 23, topic: "Negotiate Aggressively", subtitle: "Get what you're worth", objectives: ["Execute negotiation", "Counter-offer strategy"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Always negotiate. Always." }, sessionPlan: [{ time: "0:00-1:30", activity: "Negotiation", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Negotiate", deliverable: "Improved offer" }], successCriteria: ["Better offer secured"], futureProofNote: "Negotiation is expected." },

  { dayNumber: 93, week: 24, topic: "Accept Offer ($160-170k)", subtitle: "YOU DID IT", objectives: ["Accept the offer", "Get everything in writing"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "Read the contract carefully." }, sessionPlan: [{ time: "0:00-1:30", activity: "Accept offer", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Accept Offer", deliverable: "SIGNED OFFER" }], successCriteria: ["OFFER ACCEPTED"], futureProofNote: "GOAL ACHIEVED." },

  { dayNumber: 94, week: 24, topic: "Give Notice", subtitle: "Professional exit", objectives: ["Resign professionally", "Plan transition"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "Leave on good terms." }, sessionPlan: [{ time: "0:00-1:30", activity: "Resignation", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Give Notice", deliverable: "Notice given" }], successCriteria: ["Resigned professionally"], futureProofNote: "Reputation matters." },

  { dayNumber: 95, week: 24, topic: "Prep for New Role", subtitle: "Get ready", objectives: ["Prepare for day 1", "Research company deeply"], aiIntegration: { toolsUsed: ['claude'], focusArea: 'ai-review', aiTip: "Be ready to contribute." }, sessionPlan: [{ time: "0:00-1:30", activity: "Day 1 prep", type: "exercise" }], resources: { required: [] }, exercises: [{ title: "Day 1 Ready", deliverable: "Prep complete" }], successCriteria: ["Ready to start"], futureProofNote: "First impression matters." },

  { dayNumber: 96, week: 24, topic: "NEW CHAPTER BEGINS!", subtitle: "PROGRAM COMPLETE", objectives: ["Celebrate", "Start new role", "Pay it forward"], aiIntegration: { toolsUsed: ['none'], focusArea: 'manual-practice', aiTip: "You earned this." }, sessionPlan: [{ time: "0:00-1:30", activity: "CELEBRATE", type: "review" }], resources: { required: [] }, exercises: [{ title: "CELEBRATE", deliverable: "NEW JOB STARTED" }], successCriteria: ["$160-170k DATA ENGINEER"], weeklyCheckpoint: { title: "PROGRAM COMPLETE", description: "You did it. From BofA BA to $160-170k Data Engineer in 6 months.", deliverables: ["New job started", "Three portfolio projects", "AWS + dbt certified", "$60-70k raise achieved"], selfAssessment: ["Did I achieve my goal?", "YES."] }, futureProofNote: "CONGRATULATIONS. Your new chapter begins now." }
];

// ============================================================================
// HELPER FUNCTIONS
// ============================================================================

// Get lesson by day number
export function getLessonByDay(dayNumber: number): Lesson | undefined {
  return Q1_LESSONS.find(l => l.dayNumber === dayNumber);
}

// Get all lessons for a week
export function getLessonsByWeek(weekNumber: number): Lesson[] {
  return Q1_LESSONS.filter(l => l.week === weekNumber);
}

// Export the full curriculum (all 96 lessons)
export const ALL_LESSONS: Lesson[] = [
  ...Q1_LESSONS,
];
