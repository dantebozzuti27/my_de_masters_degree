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
  
  // Session structure (90 minutes total) - supports both old and new formats
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

  // ============================================
  // WEEK 3: Functions Deep Dive & Modules
  // ============================================

  {
    dayNumber: 9,
    week: 3,
    topic: "Advanced Function Patterns",
    subtitle: "Default arguments, *args, **kwargs - the building blocks of flexible APIs",

    objectives: [
      "Master default argument patterns and common gotchas",
      "Understand *args for variable positional arguments",
      "Use **kwargs for flexible keyword arguments",
      "Combine argument types in proper order"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to explain the mutable default argument gotcha. This trips up even experienced developers and AI often generates buggy code with it.",
      warningWhenNotToUseAI: "Don't let AI write your function signatures without understanding why each parameter is designed that way."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Corey Schafer - Python args/kwargs", type: "video" },
      { time: "0:15-0:35", activity: "Default arguments - the mutable gotcha", type: "learn" },
      { time: "0:35-0:55", activity: "*args and **kwargs patterns", type: "practice" },
      { time: "0:55-1:20", activity: "Build a flexible logging function", type: "exercise" },
      { time: "1:20-1:30", activity: "AI review of your function design", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - *args and **kwargs", url: "https://www.youtube.com/watch?v=c0x5gxpINT0", type: "video", duration: "10 min" }
      ],
      optional: [
        { title: "Real Python - Python args kwargs", url: "https://realpython.com/python-kwargs-and-args/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Flexible Logger Function",
        description: "Build a logging function that accepts any number of items to log and optional formatting settings",
        hints: [
          "Use *args for variable log messages",
          "Use **kwargs for options like timestamp, level, prefix",
          "Never use mutable defaults like def func(data=[])"
        ],
        aiApproach: "Ask Copilot to generate it, then check if it made the mutable default mistake.",
        deliverable: "flexible_logger.py with various usage examples"
      }
    ],

    successCriteria: [
      "Can explain why def func(items=[]) is dangerous",
      "Know the order: positional, *args, keyword-only, **kwargs",
      "Can read and write functions with flexible signatures"
    ],

    prerequisites: ["Day 3 - Basic Functions"],

    keyTerms: [
      { term: "*args", definition: "Collects extra positional arguments into a tuple" },
      { term: "**kwargs", definition: "Collects extra keyword arguments into a dictionary" },
      { term: "Mutable default", definition: "A bug where default list/dict is shared across calls" }
    ],

    commonMistakes: [
      { mistake: "Using a mutable default argument", fix: "Use None as default, create new list/dict in function body" },
      { mistake: "Wrong parameter order", fix: "Order: positional, *args, keyword-only, **kwargs" }
    ],

    futureProofNote: "Understanding flexible function signatures is essential for API design. AI can write functions, but designing intuitive, maintainable APIs is a senior-level human skill."
  },

  {
    dayNumber: 10,
    week: 3,
    topic: "Lambda Functions & Functional Programming",
    subtitle: "Anonymous functions, map, filter, reduce - when (and when not) to use them",

    objectives: [
      "Write lambda functions for simple operations",
      "Use map() and filter() effectively",
      "Understand reduce() and when it's appropriate",
      "Know when lambdas hurt readability"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'ai-review',
      aiTip: "AI loves generating lambda/map/filter chains. Ask Claude to refactor complex lambdas into named functions - readability matters more than cleverness.",
      warningWhenNotToUseAI: "Don't use AI-generated lambdas you can't read. If it takes more than 5 seconds to understand, refactor it."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Lambda functions explained", type: "video" },
      { time: "0:15-0:30", activity: "Lambda syntax and use cases", type: "learn" },
      { time: "0:30-0:50", activity: "map(), filter(), reduce() practice", type: "practice" },
      { time: "0:50-1:15", activity: "Data transformation pipeline", type: "exercise" },
      { time: "1:15-1:30", activity: "Refactor lambdas to comprehensions", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - Lambda Functions", url: "https://www.youtube.com/watch?v=25ovCm9jKfA", type: "video", duration: "14 min" }
      ],
      optional: [
        { title: "Real Python - Functional Programming", url: "https://realpython.com/python-functional-programming/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Data Transformation Pipeline",
        description: "Process a list of user records using functional approaches, then refactor to comprehensions",
        hints: [
          "Start with filter() to remove invalid records",
          "Use map() to transform remaining records",
          "Compare readability with list comprehension version"
        ],
        aiApproach: "Have AI write both versions - functional and comprehension - then analyze which is clearer.",
        deliverable: "functional_vs_comprehensions.py with both approaches"
      }
    ],

    successCriteria: [
      "Can write simple lambdas for sorting key functions",
      "Know when comprehensions beat map/filter",
      "Can read and debug functional code"
    ],

    keyTerms: [
      { term: "Lambda", definition: "Anonymous function for simple, single-expression operations" },
      { term: "Higher-order function", definition: "A function that takes or returns other functions" },
      { term: "Pure function", definition: "A function with no side effects - same input always gives same output" }
    ],

    commonMistakes: [
      { mistake: "Complex multi-line logic in lambdas", fix: "Use a named function for anything complex" },
      { mistake: "Using reduce() when a simple loop is clearer", fix: "Prefer readability over functional purity" }
    ],

    futureProofNote: "Functional concepts are timeless. Understanding map/filter/reduce helps you work in any language and recognize patterns AI generates."
  },

  {
    dayNumber: 11,
    week: 3,
    topic: "Python Module System",
    subtitle: "Imports, packages, __init__.py - organizing code like a professional",

    objectives: [
      "Understand how Python finds and loads modules",
      "Master import syntax variations",
      "Create packages with __init__.py",
      "Handle circular import issues"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often generates import statements that work in isolation but cause circular imports in real projects. Always test imports in the actual project context.",
      warningWhenNotToUseAI: "Don't let AI restructure your package layout without understanding the import implications."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python imports explained", type: "video" },
      { time: "0:15-0:35", activity: "Import mechanics and sys.path", type: "learn" },
      { time: "0:35-0:55", activity: "Create a multi-file package", type: "practice" },
      { time: "0:55-1:20", activity: "Build a data_utils package", type: "exercise" },
      { time: "1:20-1:30", activity: "Debug circular import example", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - Modules and Packages", url: "https://www.youtube.com/watch?v=0oTh1CXRaQ0", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Real Python - Python Modules", url: "https://realpython.com/python-modules-packages/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Build data_utils Package",
        description: "Create a package with submodules for validation, transformation, and io operations",
        hints: [
          "Create data_utils/ directory with __init__.py",
          "Add validators.py, transformers.py, io.py",
          "Export key functions in __init__.py for clean imports"
        ],
        aiApproach: "Ask AI to generate the package structure, then manually verify all imports work correctly.",
        deliverable: "data_utils/ package with clean import interface"
      }
    ],

    successCriteria: [
      "Can create packages from scratch",
      "Know difference between relative and absolute imports",
      "Can debug and fix import errors"
    ],

    keyTerms: [
      { term: "__init__.py", definition: "File that marks a directory as a Python package" },
      { term: "sys.path", definition: "List of directories Python searches for modules" },
      { term: "Circular import", definition: "When two modules import each other, causing loading issues" }
    ],

    commonMistakes: [
      { mistake: "Running scripts from wrong directory", fix: "Always run from project root or set PYTHONPATH" },
      { mistake: "Circular imports between modules", fix: "Import inside functions or restructure code" }
    ],

    futureProofNote: "Clean package structure is the foundation of maintainable code. This is essential context for data pipeline organization."
  },

  {
    dayNumber: 12,
    week: 3,
    topic: "Building Your First Utility Library",
    subtitle: "Create reusable code you'll use throughout the program",

    objectives: [
      "Design a utility library for data engineering tasks",
      "Write functions with proper documentation",
      "Add type hints for better AI assistance",
      "Create a testing strategy"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude', 'cursor'],
      focusArea: 'prompt-engineering',
      aiTip: "Use Claude to help design the API surface first. Describe what you want the library to do, get suggestions, then implement. Good prompts lead to good architecture.",
      warningWhenNotToUseAI: "Don't skip the design phase. Jumping straight to AI-generated code often leads to poor APIs."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Review professional library examples", type: "learn" },
      { time: "0:15-0:35", activity: "Design your de_utils library", type: "practice" },
      { time: "0:35-1:00", activity: "Implement core functions", type: "exercise" },
      { time: "1:00-1:20", activity: "Add docstrings and type hints", type: "exercise" },
      { time: "1:20-1:30", activity: "Test and document usage", type: "review" }
    ],

    resources: {
      required: [
        { title: "NumPy Documentation Style Guide", url: "https://numpydoc.readthedocs.io/en/latest/format.html", type: "docs" }
      ],
      optional: [
        { title: "Google Python Style Guide", url: "https://google.github.io/styleguide/pyguide.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Create de_utils Library",
        description: "Build a reusable library with functions you'll use throughout the program",
        hints: [
          "Include: file readers (CSV, JSON, Parquet stubs)",
          "Include: data validators (schema checking)",
          "Include: string cleaners (normalize, strip, etc.)",
          "Add type hints to every function"
        ],
        aiApproach: "Prompt AI: 'Design a utility library for data engineering. What modules would it have?' Then implement the best ideas.",
        deliverable: "de_utils/ package with documentation"
      }
    ],

    successCriteria: [
      "Library is well-documented with docstrings",
      "All functions have type hints",
      "You can explain why each function exists"
    ],

    weeklyCheckpoint: {
      title: "Week 3: Functions & Modules Mastery",
      description: "You should now write professional-quality Python functions and organize code into packages.",
      deliverables: [
        "flexible_logger.py demonstrating *args/**kwargs",
        "functional_vs_comprehensions.py comparison",
        "data_utils/ package with working imports",
        "de_utils/ library you'll build upon"
      ],
      selfAssessment: [
        "Can I design flexible function signatures?",
        "Do I know when lambdas help vs hurt readability?",
        "Can I create packages without import errors?",
        "Am I writing documented, type-hinted code?"
      ]
    },

    futureProofNote: "Building reusable libraries is a core skill. AI helps write functions, but designing good abstractions requires understanding the problem domain deeply."
  },

  // ============================================
  // WEEK 4: Object-Oriented Python
  // ============================================

  {
    dayNumber: 13,
    week: 4,
    topic: "Classes and Objects Fundamentals",
    subtitle: "From functions to classes - when and why to use OOP",

    objectives: [
      "Understand when classes make sense vs functions",
      "Write classes with __init__ and instance methods",
      "Use self correctly throughout class methods",
      "Create multiple instances with different state"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to explain when to use a class vs a function with examples. Understanding this design decision is more valuable than memorizing syntax.",
      warningWhenNotToUseAI: "Don't let AI over-engineer. Simple functions are often better than classes with one method."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python OOP basics", type: "video" },
      { time: "0:15-0:35", activity: "Class syntax and __init__", type: "learn" },
      { time: "0:35-0:55", activity: "Instance methods and self", type: "practice" },
      { time: "0:55-1:20", activity: "Build a DataRecord class", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare to dict approach", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - OOP Tutorial 1", url: "https://www.youtube.com/watch?v=ZDa-Z5JzLYM", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Real Python - OOP in Python", url: "https://realpython.com/python3-object-oriented-programming/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "DataRecord Class",
        description: "Create a class to represent a data record with validation and transformation methods",
        hints: [
          "Store raw data in __init__",
          "Add validate() method to check required fields",
          "Add transform() method to clean data",
          "Add to_dict() method for export"
        ],
        aiApproach: "Write the basic class yourself, then ask AI to add edge case handling.",
        deliverable: "data_record.py with DataRecord class"
      }
    ],

    successCriteria: [
      "Can create classes with proper __init__",
      "Understand the difference between class and instance attributes",
      "Know when a class adds value vs just using a dict"
    ],

    keyTerms: [
      { term: "Instance", definition: "A specific object created from a class" },
      { term: "self", definition: "Reference to the current instance in methods" },
      { term: "Constructor", definition: "__init__ method that initializes new instances" }
    ],

    commonMistakes: [
      { mistake: "Forgetting self in method definitions", fix: "Every instance method needs self as first parameter" },
      { mistake: "Creating a class when a function would suffice", fix: "Use classes for state + behavior, functions for stateless operations" }
    ],

    futureProofNote: "Most data engineering libraries use OOP. Understanding classes helps you use Pandas, SQLAlchemy, Airflow, and read any professional codebase."
  },

  {
    dayNumber: 14,
    week: 4,
    topic: "Properties and Magic Methods",
    subtitle: "Make your classes Pythonic with @property and __dunder__ methods",

    objectives: [
      "Use @property for computed attributes",
      "Implement __str__ and __repr__ for debugging",
      "Understand __eq__, __lt__ for comparisons",
      "Know common magic methods and their purposes"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'ai-review',
      aiTip: "AI is great at generating magic methods. Ask it to add __str__, __repr__, __eq__ to your class, then verify the implementations make sense.",
      warningWhenNotToUseAI: "Don't add every possible magic method. Only implement what you actually need."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python properties and dunder methods", type: "video" },
      { time: "0:15-0:35", activity: "@property decorator deep dive", type: "learn" },
      { time: "0:35-0:55", activity: "Essential magic methods", type: "practice" },
      { time: "0:55-1:20", activity: "Enhance DataRecord with magic", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare before/after usability", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - Property Decorators", url: "https://www.youtube.com/watch?v=jCzT9XFZ5bw", type: "video", duration: "16 min" }
      ],
      optional: [
        { title: "Python Magic Methods Guide", url: "https://rszalski.github.io/magicmethods/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Pythonic DataRecord",
        description: "Enhance yesterday's DataRecord with properties and magic methods",
        hints: [
          "Add @property for computed fields (e.g., is_valid)",
          "Implement __str__ for user-friendly output",
          "Implement __repr__ for debugging",
          "Add __eq__ to compare records by ID"
        ],
        aiApproach: "Ask AI to make your class 'Pythonic' and review what it suggests.",
        deliverable: "pythonic_data_record.py with enhanced class"
      }
    ],

    successCriteria: [
      "Know when to use @property vs regular methods",
      "Can implement __str__ and __repr__ correctly",
      "Understand the difference between str() and repr()"
    ],

    keyTerms: [
      { term: "@property", definition: "Decorator that makes a method act like an attribute" },
      { term: "__repr__", definition: "String representation for developers/debugging" },
      { term: "__str__", definition: "String representation for end users" }
    ],

    commonMistakes: [
      { mistake: "Making __str__ and __repr__ identical", fix: "__repr__ should be unambiguous, __str__ should be readable" },
      { mistake: "Heavy computation in @property", fix: "Properties should be cheap to compute, cache if expensive" }
    ],

    futureProofNote: "Magic methods make Python feel like Python. Understanding them helps you create intuitive APIs and debug library code."
  },

  {
    dayNumber: 15,
    week: 4,
    topic: "Inheritance and Composition",
    subtitle: "Class relationships - when to inherit vs when to compose",

    objectives: [
      "Implement class inheritance with super()",
      "Understand method resolution order (MRO)",
      "Know when composition beats inheritance",
      "Design flexible class hierarchies"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often over-uses inheritance. Ask it to design a class hierarchy, then ask 'Could this use composition instead?' Compare both approaches.",
      warningWhenNotToUseAI: "Don't accept deep inheritance hierarchies. 'Favor composition over inheritance' is a key principle."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Inheritance in Python", type: "video" },
      { time: "0:15-0:35", activity: "Inheritance patterns and super()", type: "learn" },
      { time: "0:35-0:55", activity: "Composition patterns", type: "practice" },
      { time: "0:55-1:20", activity: "Build a data processor hierarchy", type: "exercise" },
      { time: "1:20-1:30", activity: "Refactor to composition", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - Inheritance", url: "https://www.youtube.com/watch?v=RSl87lqOXDE", type: "video", duration: "19 min" }
      ],
      optional: [
        { title: "Real Python - Inheritance and Composition", url: "https://realpython.com/inheritance-composition-python/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Data Processor Hierarchy",
        description: "Build processors for different data types using both inheritance and composition",
        hints: [
          "Create BaseProcessor with process() method",
          "Inherit CSVProcessor, JSONProcessor, ParquetProcessor",
          "Then refactor: use composition with separate Reader and Transformer classes"
        ],
        aiApproach: "Have AI generate inheritance version, then prompt it to refactor using composition. Compare complexity.",
        deliverable: "processor_inheritance.py and processor_composition.py"
      }
    ],

    successCriteria: [
      "Can implement inheritance correctly with super()",
      "Know when inheritance creates problems",
      "Can design using composition pattern"
    ],

    keyTerms: [
      { term: "Inheritance", definition: "Creating new classes that share behavior from parent classes" },
      { term: "Composition", definition: "Building complex objects from simpler component objects" },
      { term: "MRO", definition: "Method Resolution Order - how Python finds methods in inheritance chains" }
    ],

    commonMistakes: [
      { mistake: "Deep inheritance hierarchies", fix: "Keep inheritance shallow, prefer composition" },
      { mistake: "Inheriting just to reuse one method", fix: "That's what composition is for" }
    ],

    futureProofNote: "Most modern Python libraries use composition over inheritance. Understanding both helps you make good design decisions."
  },

  {
    dayNumber: 16,
    week: 4,
    topic: "Dataclasses and Type Hints",
    subtitle: "Modern Python patterns that make AI coding assistance better",

    objectives: [
      "Use @dataclass for simple data containers",
      "Add comprehensive type hints",
      "Understand how type hints improve AI suggestions",
      "Use TypedDict for dictionary schemas"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'cursor'],
      focusArea: 'prompt-engineering',
      aiTip: "Type hints dramatically improve AI code suggestions. Write the types first, then let Copilot fill in the implementation. This is modern development workflow.",
      warningWhenNotToUseAI: "Understand the types before adding them. Wrong types lead to wrong AI suggestions."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python dataclasses", type: "video" },
      { time: "0:15-0:35", activity: "Dataclass features and options", type: "learn" },
      { time: "0:35-0:55", activity: "Type hints and their benefits", type: "practice" },
      { time: "0:55-1:20", activity: "Build typed data pipeline classes", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare AI suggestions with/without types", type: "review" }
    ],

    resources: {
      required: [
        { title: "ArjanCodes - Dataclasses", url: "https://www.youtube.com/watch?v=vRVVyl9uaZc", type: "video", duration: "16 min" }
      ],
      optional: [
        { title: "Real Python - Dataclasses", url: "https://realpython.com/python-data-classes/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Typed Pipeline Components",
        description: "Create dataclasses for pipeline configuration and data models",
        hints: [
          "Create PipelineConfig dataclass with typed fields",
          "Create DataModel with validation in __post_init__",
          "Use Optional[], List[], Dict[] type hints",
          "Compare Copilot suggestions with and without types"
        ],
        aiApproach: "Write type signatures first, then let AI fill implementations. Note how much better the suggestions are.",
        deliverable: "typed_pipeline.py with dataclass-based components"
      }
    ],

    successCriteria: [
      "Can use @dataclass effectively",
      "Know when dataclass beats regular class",
      "Understand how type hints help AI and IDEs"
    ],

    weeklyCheckpoint: {
      title: "Week 4: Object-Oriented Python",
      description: "You should now design and implement classes using modern Python patterns.",
      deliverables: [
        "DataRecord class with full functionality",
        "Processor examples using both inheritance and composition",
        "Typed dataclass-based pipeline components",
        "Notes on when to use each OOP pattern"
      ],
      selfAssessment: [
        "Can I design classes that are intuitive to use?",
        "Do I know when to use inheritance vs composition?",
        "Am I using dataclasses and type hints consistently?",
        "Do my type hints improve AI assistance?"
      ]
    },

    keyTerms: [
      { term: "@dataclass", definition: "Decorator that auto-generates __init__, __repr__, __eq__ for data containers" },
      { term: "Type hint", definition: "Annotations that document expected types (def foo(x: int) -> str)" },
      { term: "TypedDict", definition: "Type hint for dictionaries with known keys and value types" }
    ],

    commonMistakes: [
      { mistake: "Using dataclass for classes with lots of methods", fix: "Dataclasses are for data-focused classes, not behavior-heavy classes" },
      { mistake: "Skipping type hints to save time", fix: "Type hints save more time than they cost via better AI assistance and error catching" }
    ],

    futureProofNote: "Type hints are the future of Python. They're required for modern tools and dramatically improve AI coding assistance. Invest in them now."
  },

  // ============================================
  // WEEK 5: File I/O and Data Formats
  // ============================================

  {
    dayNumber: 17,
    week: 5,
    topic: "File I/O and Context Managers",
    subtitle: "Reading and writing files safely in data pipelines",

    objectives: [
      "Master file operations with context managers",
      "Understand text vs binary modes",
      "Handle encoding issues (UTF-8, etc.)",
      "Use pathlib for cross-platform paths"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT about common encoding issues in data pipelines. Real-world data often has encoding problems that AI can help debug.",
      warningWhenNotToUseAI: "Always specify encoding explicitly. AI often forgets encoding parameters, causing production bugs."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: File handling in Python", type: "video" },
      { time: "0:15-0:35", activity: "Context managers and with statement", type: "learn" },
      { time: "0:35-0:55", activity: "Encoding and binary modes", type: "practice" },
      { time: "0:55-1:20", activity: "Build a robust file processor", type: "exercise" },
      { time: "1:20-1:30", activity: "Cross-platform path handling", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - File Handling", url: "https://www.youtube.com/watch?v=Uh2ebFW8OYM", type: "video", duration: "24 min" }
      ],
      optional: [
        { title: "Real Python - Working with Files", url: "https://realpython.com/working-with-files-in-python/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Robust File Processor",
        description: "Create functions that safely read/write files with proper error handling",
        hints: [
          "Always use 'with' for file operations",
          "Always specify encoding='utf-8'",
          "Use pathlib.Path instead of string paths",
          "Handle FileNotFoundError, PermissionError, UnicodeDecodeError"
        ],
        aiApproach: "Generate with AI, then check: Does it specify encoding? Does it use context managers? Does it handle errors?",
        deliverable: "file_processor.py with safe read/write functions"
      }
    ],

    successCriteria: [
      "Always use context managers for files",
      "Know the difference between text and binary modes",
      "Can debug encoding issues"
    ],

    keyTerms: [
      { term: "Context manager", definition: "Object that manages setup/teardown, used with 'with' statement" },
      { term: "Encoding", definition: "How text characters are converted to/from bytes (UTF-8, Latin-1, etc.)" },
      { term: "pathlib", definition: "Modern, cross-platform module for filesystem paths" }
    ],

    commonMistakes: [
      { mistake: "Forgetting to specify encoding", fix: "Always use encoding='utf-8' explicitly" },
      { mistake: "Using string paths with / or \\\\", fix: "Use pathlib.Path for cross-platform compatibility" }
    ],

    futureProofNote: "File I/O is fundamental to data engineering. Every pipeline reads and writes files. Robust file handling prevents data corruption."
  },

  {
    dayNumber: 18,
    week: 5,
    topic: "CSV and Excel Processing",
    subtitle: "Working with the most common business data formats",

    objectives: [
      "Read/write CSV with various configurations",
      "Handle messy CSV data (quotes, escapes, delimiters)",
      "Work with Excel files using openpyxl",
      "Know when to use csv module vs pandas"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often generates pandas code for CSV, but the csv module is lighter for simple tasks. Ask about trade-offs before accepting pandas suggestions.",
      warningWhenNotToUseAI: "Real CSV files are messy. AI generates ideal-case code. Always test with real data."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: CSV processing in Python", type: "video" },
      { time: "0:15-0:35", activity: "csv module deep dive", type: "learn" },
      { time: "0:35-0:55", activity: "Handling messy CSVs", type: "practice" },
      { time: "0:55-1:20", activity: "Build CSV cleaning pipeline", type: "exercise" },
      { time: "1:20-1:30", activity: "Excel basics with openpyxl", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - CSV Module", url: "https://www.youtube.com/watch?v=q5uM4VKywbA", type: "video", duration: "16 min" }
      ],
      optional: [
        { title: "Real Python - Reading/Writing CSV", url: "https://realpython.com/python-csv/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "CSV Cleaning Pipeline",
        description: "Process a messy CSV file with various data quality issues",
        hints: [
          "Handle different delimiters (comma, semicolon, tab)",
          "Handle quoted fields with embedded commas",
          "Handle missing values and inconsistent types",
          "Output clean, normalized CSV"
        ],
        aiApproach: "Ask AI to handle edge cases one at a time. Each messy scenario teaches you something.",
        deliverable: "csv_cleaner.py with before/after example files"
      }
    ],

    successCriteria: [
      "Can configure csv.reader/writer for various formats",
      "Know how to handle quoted fields and escapes",
      "Can decide between csv module and pandas"
    ],

    keyTerms: [
      { term: "Dialect", definition: "CSV format specification (delimiter, quoting, etc.)" },
      { term: "DictReader", definition: "Reads CSV rows as dictionaries with header keys" },
      { term: "Quoting", definition: "How CSV handles fields containing special characters" }
    ],

    commonMistakes: [
      { mistake: "Assuming all CSVs use commas", fix: "Check delimiter, especially for European data (semicolons)" },
      { mistake: "Ignoring encoding issues in CSV", fix: "Specify encoding when opening file" }
    ],

    futureProofNote: "CSV is the universal data exchange format. You'll process thousands of CSVs in your career. Master the edge cases now."
  },

  {
    dayNumber: 19,
    week: 5,
    topic: "JSON and API Data",
    subtitle: "The language of APIs and modern data interchange",

    objectives: [
      "Master json module for parsing and generation",
      "Handle nested JSON structures",
      "Work with JSON Lines format for large files",
      "Validate JSON against expected schemas"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Use ChatGPT to explain complex nested JSON structures. Paste real API responses and ask for parsing strategies.",
      warningWhenNotToUseAI: "AI can generate JSON parsers quickly, but understanding the data structure is the real skill."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: JSON in Python", type: "video" },
      { time: "0:15-0:35", activity: "Parsing and generating JSON", type: "learn" },
      { time: "0:35-0:55", activity: "Nested JSON navigation", type: "practice" },
      { time: "0:55-1:20", activity: "Parse real API responses", type: "exercise" },
      { time: "1:20-1:30", activity: "JSON Lines for large files", type: "review" }
    ],

    resources: {
      required: [
        { title: "Corey Schafer - JSON in Python", url: "https://www.youtube.com/watch?v=9N6a-VLBa2I", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Real Python - Working with JSON", url: "https://realpython.com/python-json/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "API Response Parser",
        description: "Build functions to extract data from complex nested JSON API responses",
        hints: [
          "Use .get() for safe key access",
          "Handle missing keys gracefully",
          "Flatten nested structures for analysis",
          "Write helper functions for common patterns"
        ],
        aiApproach: "Paste a complex JSON example and ask AI to write extraction functions. Then review and simplify.",
        deliverable: "json_parser.py with extraction functions and tests"
      }
    ],

    successCriteria: [
      "Can navigate deeply nested JSON confidently",
      "Know when to use json.loads() vs json.load()",
      "Can handle JSON Lines files efficiently"
    ],

    keyTerms: [
      { term: "JSON Lines", definition: "Format with one JSON object per line, for streaming large datasets" },
      { term: "json.dumps()", definition: "Serialize Python object to JSON string" },
      { term: "json.loads()", definition: "Parse JSON string to Python object" }
    ],

    commonMistakes: [
      { mistake: "Using [] instead of .get() for optional keys", fix: "dict.get('key', default) prevents KeyError" },
      { mistake: "Loading huge JSON files into memory", fix: "Use JSON Lines or streaming parsing for large files" }
    ],

    futureProofNote: "JSON is the format of web APIs, which are central to modern data engineering. Deep JSON skills are essential."
  },

  {
    dayNumber: 20,
    week: 5,
    topic: "Data Serialization: Pickle, YAML, and Parquet",
    subtitle: "Choosing the right format for the right job",

    objectives: [
      "Understand pickle for Python object serialization",
      "Know pickle security concerns",
      "Work with YAML for configuration",
      "Introduction to Parquet for analytics"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'ai-review',
      aiTip: "Ask AI to compare all serialization formats with pros/cons table. Understanding trade-offs is more valuable than memorizing APIs.",
      warningWhenNotToUseAI: "AI might suggest pickle for data storage. It's fine for caching but risky for data exchange due to security concerns."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Data serialization overview", type: "video" },
      { time: "0:15-0:35", activity: "Pickle: power and dangers", type: "learn" },
      { time: "0:35-0:55", activity: "YAML for configuration", type: "practice" },
      { time: "0:55-1:20", activity: "Parquet introduction", type: "exercise" },
      { time: "1:20-1:30", activity: "Format comparison summary", type: "review" }
    ],

    resources: {
      required: [
        { title: "Real Python - Serialization", url: "https://realpython.com/python-serialize-data/", type: "article" }
      ],
      optional: [
        { title: "Apache Parquet Documentation", url: "https://parquet.apache.org/docs/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Format Comparison Project",
        description: "Save and load the same dataset in multiple formats, compare characteristics",
        hints: [
          "Create sample dataset with mixed types",
          "Save as JSON, CSV, Pickle, YAML, Parquet",
          "Compare file sizes and load/save times",
          "Document when to use each format"
        ],
        aiApproach: "Ask AI to generate the benchmarking code, then run it and analyze results yourself.",
        deliverable: "format_comparison.py with benchmark results and recommendations"
      }
    ],

    successCriteria: [
      "Know security risks of unpickling untrusted data",
      "Can use YAML for configuration files",
      "Understand when Parquet is the right choice"
    ],

    weeklyCheckpoint: {
      title: "Week 5: File I/O & Data Formats",
      description: "You should now confidently work with all common data formats.",
      deliverables: [
        "file_processor.py with robust I/O",
        "csv_cleaner.py handling messy data",
        "json_parser.py for nested structures",
        "format_comparison.py with benchmarks"
      ],
      selfAssessment: [
        "Do I always use context managers for files?",
        "Can I handle encoding issues?",
        "Do I know which format to use when?",
        "Can I process real-world messy data files?"
      ]
    },

    keyTerms: [
      { term: "Pickle", definition: "Python-specific binary serialization format" },
      { term: "YAML", definition: "Human-readable data format often used for config files" },
      { term: "Parquet", definition: "Columnar storage format optimized for analytics workloads" }
    ],

    commonMistakes: [
      { mistake: "Using pickle for data exchange between systems", fix: "Use JSON or Parquet for interoperability" },
      { mistake: "Unpickling data from untrusted sources", fix: "Pickle can execute arbitrary code - never unpickle untrusted data" }
    ],

    futureProofNote: "Parquet is increasingly important for data engineering. It's the standard for data lakes and works well with Spark, Snowflake, and cloud data tools."
  },

  // ============================================
  // WEEK 6: SQL Fundamentals
  // ============================================

  {
    dayNumber: 21,
    week: 6,
    topic: "SQL Foundations and SELECT",
    subtitle: "The language of data - your most important skill",

    objectives: [
      "Understand relational database concepts",
      "Write basic SELECT queries",
      "Use WHERE for filtering",
      "Sort results with ORDER BY"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "AI is excellent at SQL. But you MUST understand what queries do. Ask AI to explain each part of generated queries.",
      warningWhenNotToUseAI: "Never run AI-generated SQL on production without understanding it completely."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL basics introduction", type: "video" },
      { time: "0:15-0:35", activity: "SELECT, FROM, WHERE fundamentals", type: "learn" },
      { time: "0:35-0:55", activity: "Filtering and sorting practice", type: "practice" },
      { time: "0:55-1:20", activity: "Query challenge exercises", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare your queries to AI solutions", type: "review" }
    ],

    resources: {
      required: [
        { title: "freeCodeCamp - SQL Full Course", url: "https://www.youtube.com/watch?v=HXV3zeQKqGY", type: "video", duration: "First 30 min" }
      ],
      optional: [
        { title: "SQLBolt Interactive Tutorial", url: "https://sqlbolt.com/", type: "interactive" }
      ]
    },

    exercises: [
      {
        title: "Basic Query Practice",
        description: "Write queries against a sample employee database",
        hints: [
          "SELECT specific columns, not SELECT *",
          "Practice various WHERE conditions",
          "Combine conditions with AND, OR",
          "Use ORDER BY for different sort orders"
        ],
        aiApproach: "Write queries yourself first. Then ask AI for the same query and compare approaches.",
        deliverable: "sql_basics.sql with 10+ queries"
      }
    ],

    successCriteria: [
      "Can write SELECT with specific columns",
      "Can filter with multiple WHERE conditions",
      "Understand NULL handling in comparisons"
    ],

    keyTerms: [
      { term: "Relational database", definition: "Database organizing data into tables with relationships" },
      { term: "Query", definition: "A request to retrieve or manipulate data" },
      { term: "NULL", definition: "Represents missing or unknown data" }
    ],

    commonMistakes: [
      { mistake: "Using = NULL instead of IS NULL", fix: "NULL comparisons require IS NULL or IS NOT NULL" },
      { mistake: "SELECT * in production queries", fix: "Always specify needed columns for performance" }
    ],

    futureProofNote: "SQL is THE most important data engineering skill. AI can write SQL, but understanding query logic deeply is irreplaceable. This is foundational."
  },

  {
    dayNumber: 22,
    week: 6,
    topic: "Aggregations and GROUP BY",
    subtitle: "Summarizing data - the heart of analytics",

    objectives: [
      "Use COUNT, SUM, AVG, MIN, MAX",
      "Group data with GROUP BY",
      "Filter groups with HAVING",
      "Understand aggregation logic"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'manual-practice',
      aiTip: "Aggregations are so fundamental you need to think in them. Practice manually first, then use AI to check your work.",
      warningWhenNotToUseAI: "Don't use AI for basic aggregation practice. You need these patterns internalized."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL aggregation functions", type: "video" },
      { time: "0:15-0:35", activity: "Aggregate functions deep dive", type: "learn" },
      { time: "0:35-0:55", activity: "GROUP BY patterns", type: "practice" },
      { time: "0:55-1:20", activity: "Analytics query challenges", type: "exercise" },
      { time: "1:20-1:30", activity: "HAVING vs WHERE comparison", type: "review" }
    ],

    resources: {
      required: [
        { title: "Socratica - SQL GROUP BY", url: "https://www.youtube.com/watch?v=rKzziNWCqYA", type: "video", duration: "8 min" }
      ],
      optional: [
        { title: "Mode Analytics - SQL Tutorial", url: "https://mode.com/sql-tutorial/", type: "interactive" }
      ]
    },

    exercises: [
      {
        title: "Sales Analytics Queries",
        description: "Answer business questions using aggregations",
        hints: [
          "Total sales by region",
          "Average order value by customer",
          "Count of orders by status",
          "Top 10 customers by revenue"
        ],
        aiApproach: "Write each query yourself, time yourself. Only use AI if stuck for more than 5 minutes.",
        deliverable: "aggregations.sql with business analytics queries"
      }
    ],

    successCriteria: [
      "Can write GROUP BY without errors",
      "Know difference between WHERE and HAVING",
      "Can combine aggregations in complex queries"
    ],

    keyTerms: [
      { term: "Aggregation", definition: "Combining multiple rows into summary statistics" },
      { term: "GROUP BY", definition: "Groups rows sharing values for aggregate calculations" },
      { term: "HAVING", definition: "Filters groups after aggregation (like WHERE for groups)" }
    ],

    commonMistakes: [
      { mistake: "Using WHERE to filter aggregated values", fix: "Use HAVING for post-aggregation filtering" },
      { mistake: "Forgetting GROUP BY columns in SELECT", fix: "All non-aggregate SELECT columns must be in GROUP BY" }
    ],

    futureProofNote: "Every data report, dashboard, and metric uses aggregations. This is the core of data analysis."
  },

  {
    dayNumber: 23,
    week: 6,
    topic: "JOINs Fundamentals",
    subtitle: "Connecting tables - the relational power",

    objectives: [
      "Understand table relationships",
      "Master INNER JOIN syntax",
      "Know LEFT, RIGHT, FULL OUTER JOINs",
      "Avoid common JOIN pitfalls"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to draw Venn diagrams explaining each JOIN type. Visual understanding is crucial.",
      warningWhenNotToUseAI: "Always trace through JOIN results manually for small datasets. Understand exactly which rows match."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL JOINs explained visually", type: "video" },
      { time: "0:15-0:35", activity: "INNER JOIN mechanics", type: "learn" },
      { time: "0:35-0:55", activity: "OUTER JOIN variations", type: "practice" },
      { time: "0:55-1:20", activity: "Multi-table JOIN challenges", type: "exercise" },
      { time: "1:20-1:30", activity: "Trace through JOIN results manually", type: "review" }
    ],

    resources: {
      required: [
        { title: "Socratica - SQL JOINs", url: "https://www.youtube.com/watch?v=9yeOJ0ZMUYw", type: "video", duration: "9 min" }
      ],
      optional: [
        { title: "Visual JOIN Representation", url: "https://joins.spathon.com/", type: "interactive" }
      ]
    },

    exercises: [
      {
        title: "JOIN Challenge Series",
        description: "Solve progressively complex JOIN scenarios",
        hints: [
          "Start with 2-table INNER JOINs",
          "Add LEFT JOIN for optional relationships",
          "Join 3+ tables in sequence",
          "Handle NULL in JOIN results"
        ],
        aiApproach: "Solve each problem yourself. Ask AI only after completing to compare approaches.",
        deliverable: "joins_practice.sql with annotated queries"
      }
    ],

    successCriteria: [
      "Can write multi-table JOINs correctly",
      "Know when to use each JOIN type",
      "Can predict JOIN output row counts"
    ],

    keyTerms: [
      { term: "INNER JOIN", definition: "Returns only rows with matches in both tables" },
      { term: "LEFT JOIN", definition: "Returns all left table rows, matched right rows or NULL" },
      { term: "Foreign key", definition: "Column that references primary key of another table" }
    ],

    commonMistakes: [
      { mistake: "Cartesian product from missing JOIN condition", fix: "Always specify ON clause with proper keys" },
      { mistake: "Losing rows unexpectedly with INNER JOIN", fix: "Use LEFT JOIN when you need all rows from one table" }
    ],

    futureProofNote: "JOINs are the heart of relational databases. Every complex query uses them. Master JOINs and you can query anything."
  },

  {
    dayNumber: 24,
    week: 6,
    topic: "Subqueries and CTEs",
    subtitle: "Breaking down complex problems into manageable pieces",

    objectives: [
      "Write subqueries in WHERE and FROM",
      "Master Common Table Expressions (CTEs)",
      "Know when CTEs beat subqueries",
      "Chain multiple CTEs for complex logic"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'ai-review',
      aiTip: "AI excels at converting nested subqueries to CTEs. Ask it to refactor messy queries for readability.",
      warningWhenNotToUseAI: "Understand WHY a CTE structure works before using AI-generated ones."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: CTEs explained", type: "video" },
      { time: "0:15-0:35", activity: "Subquery patterns", type: "learn" },
      { time: "0:35-0:55", activity: "CTE syntax and benefits", type: "practice" },
      { time: "0:55-1:20", activity: "Refactor complex queries", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare readability before/after", type: "review" }
    ],

    resources: {
      required: [
        { title: "Alex the Analyst - CTEs", url: "https://www.youtube.com/watch?v=K1WeoKxLZ5o", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Mode Analytics - SQL Subqueries", url: "https://mode.com/sql-tutorial/sql-sub-queries/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Query Refactoring Challenge",
        description: "Take messy nested queries and restructure with CTEs",
        hints: [
          "Identify logical components of complex query",
          "Extract each component as a CTE",
          "Name CTEs clearly for readability",
          "Compare performance of both versions"
        ],
        aiApproach: "Ask AI to refactor your subquery to CTEs. Compare its naming and structure to yours.",
        deliverable: "cte_refactoring.sql with before/after examples"
      }
    ],

    successCriteria: [
      "Can write readable CTEs for complex logic",
      "Know when subqueries are still appropriate",
      "Can chain CTEs effectively"
    ],

    weeklyCheckpoint: {
      title: "Week 6: SQL Fundamentals",
      description: "You should now write confident, correct SQL queries.",
      deliverables: [
        "sql_basics.sql with filtered queries",
        "aggregations.sql with GROUP BY analytics",
        "joins_practice.sql with multi-table queries",
        "cte_refactoring.sql with clean structure"
      ],
      selfAssessment: [
        "Can I write SELECT queries without syntax errors?",
        "Do I understand when to use each JOIN type?",
        "Can I break complex queries into CTEs?",
        "Can I predict query results before running?"
      ]
    },

    keyTerms: [
      { term: "Subquery", definition: "A query nested inside another query" },
      { term: "CTE", definition: "Common Table Expression - named temporary result set" },
      { term: "WITH clause", definition: "SQL syntax for defining CTEs" }
    ],

    commonMistakes: [
      { mistake: "Deeply nested subqueries", fix: "Refactor to CTEs for readability" },
      { mistake: "Using CTE when simple subquery suffices", fix: "Simple inline subqueries can be clearer for small cases" }
    ],

    futureProofNote: "CTEs are the standard for readable, maintainable SQL. They're essential for dbt and modern data transformation."
  },

  // ============================================
  // WEEK 7: SQL Intermediate
  // ============================================

  {
    dayNumber: 25,
    week: 7,
    topic: "Window Functions Introduction",
    subtitle: "Analytics superpowers - calculations across related rows",

    objectives: [
      "Understand window function concepts",
      "Use ROW_NUMBER, RANK, DENSE_RANK",
      "Calculate running totals with SUM OVER",
      "Understand PARTITION BY vs GROUP BY"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Window functions are complex. Ask ChatGPT to explain each part: the function, PARTITION BY, ORDER BY, and frame clause.",
      warningWhenNotToUseAI: "Don't just copy window function queries. Trace through results row by row to understand."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Video: Window functions explained", type: "video" },
      { time: "0:20-0:40", activity: "ROW_NUMBER and ranking functions", type: "learn" },
      { time: "0:40-1:00", activity: "Running totals and aggregates", type: "practice" },
      { time: "1:00-1:20", activity: "Analytics challenges", type: "exercise" },
      { time: "1:20-1:30", activity: "Compare to GROUP BY solutions", type: "review" }
    ],

    resources: {
      required: [
        { title: "Advanced SQL - Window Functions", url: "https://www.youtube.com/watch?v=H6OTMoXjNiM", type: "video", duration: "35 min" }
      ],
      optional: [
        { title: "Mode Analytics - Window Functions", url: "https://mode.com/sql-tutorial/sql-window-functions/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Window Function Analytics",
        description: "Solve business problems that require window functions",
        hints: [
          "Rank employees by salary within department",
          "Calculate running revenue total by date",
          "Find first and last order per customer",
          "Calculate month-over-month growth"
        ],
        aiApproach: "Try each problem yourself. Then ask AI for alternative approaches and compare.",
        deliverable: "window_functions.sql with annotated solutions"
      }
    ],

    successCriteria: [
      "Can write basic window functions correctly",
      "Understand PARTITION BY grouping",
      "Know when window functions are needed vs GROUP BY"
    ],

    keyTerms: [
      { term: "Window function", definition: "Calculation across rows related to current row" },
      { term: "PARTITION BY", definition: "Divides result set into partitions for window calculations" },
      { term: "Frame clause", definition: "Defines which rows the window function considers" }
    ],

    commonMistakes: [
      { mistake: "Confusing PARTITION BY with GROUP BY", fix: "PARTITION BY keeps all rows, GROUP BY aggregates them" },
      { mistake: "Forgetting ORDER BY in ranking functions", fix: "Ranking functions need ORDER BY to define the ranking order" }
    ],

    futureProofNote: "Window functions are advanced SQL that separates senior from junior engineers. They're essential for analytics and dbt transformations."
  },

  {
    dayNumber: 26,
    week: 7,
    topic: "Advanced Window Functions",
    subtitle: "LAG, LEAD, and complex analytical patterns",

    objectives: [
      "Use LAG and LEAD for row comparisons",
      "Calculate differences between periods",
      "Use FIRST_VALUE and LAST_VALUE",
      "Combine multiple window functions"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'prompt-engineering',
      aiTip: "Describe the business problem clearly: 'I need to compare each row to the previous row within each group.' Good prompts get better SQL.",
      warningWhenNotToUseAI: "Complex window functions are error-prone. Always verify results with small test datasets."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: LAG and LEAD functions", type: "video" },
      { time: "0:15-0:35", activity: "Row comparison patterns", type: "learn" },
      { time: "0:35-0:55", activity: "Period-over-period calculations", type: "practice" },
      { time: "0:55-1:20", activity: "Time series analytics", type: "exercise" },
      { time: "1:20-1:30", activity: "Validate results manually", type: "review" }
    ],

    resources: {
      required: [
        { title: "Bro Code - SQL Window Functions", url: "https://www.youtube.com/watch?v=Ww71knvhQ-s", type: "video", duration: "18 min" }
      ],
      optional: [
        { title: "Window Functions Cheat Sheet", url: "https://learnsql.com/blog/sql-window-functions-cheat-sheet/", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Time Series Analytics",
        description: "Build queries for time-based analysis patterns",
        hints: [
          "Calculate day-over-day change",
          "Calculate week-over-week percentage change",
          "Find gaps in sequential data",
          "Calculate moving averages"
        ],
        aiApproach: "Prompt AI with specific business scenarios. Refine prompts until you get correct SQL.",
        deliverable: "time_series_analysis.sql with business metrics"
      }
    ],

    successCriteria: [
      "Can use LAG/LEAD for comparisons",
      "Can calculate period-over-period metrics",
      "Can verify window function results manually"
    ],

    keyTerms: [
      { term: "LAG", definition: "Accesses data from previous row in the partition" },
      { term: "LEAD", definition: "Accesses data from next row in the partition" },
      { term: "Moving average", definition: "Average calculated over a sliding window of rows" }
    ],

    commonMistakes: [
      { mistake: "Wrong offset in LAG/LEAD", fix: "Verify offset matches your time period (1 for previous day, 7 for previous week)" },
      { mistake: "Forgetting NULL handling for first/last rows", fix: "Use COALESCE or default value parameter" }
    ],

    futureProofNote: "Time series analysis is core to data engineering. These patterns appear in almost every analytics project."
  },

  {
    dayNumber: 27,
    week: 7,
    topic: "String and Date Functions",
    subtitle: "Manipulating text and temporal data - daily necessities",

    objectives: [
      "Master common string functions",
      "Handle date extraction and formatting",
      "Calculate date differences",
      "Clean messy text data with SQL"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'debug-ai-code',
      aiTip: "Date functions vary between databases. Always ask AI which database syntax it's using (PostgreSQL, MySQL, etc.).",
      warningWhenNotToUseAI: "AI often generates database-specific syntax. Verify it works in your target database."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL string functions", type: "video" },
      { time: "0:15-0:35", activity: "String manipulation patterns", type: "learn" },
      { time: "0:35-0:55", activity: "Date/time functions", type: "practice" },
      { time: "0:55-1:20", activity: "Data cleaning challenges", type: "exercise" },
      { time: "1:20-1:30", activity: "Database syntax differences", type: "review" }
    ],

    resources: {
      required: [
        { title: "Alex the Analyst - String Functions", url: "https://www.youtube.com/watch?v=XbCF6MXmKW8", type: "video", duration: "12 min" }
      ],
      optional: [
        { title: "PostgreSQL Date Functions", url: "https://www.postgresql.org/docs/current/functions-datetime.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Data Cleaning with SQL",
        description: "Clean messy data using string and date functions",
        hints: [
          "Standardize name formats (UPPER, LOWER, INITCAP)",
          "Extract parts from messy strings",
          "Parse dates from various formats",
          "Handle timezone conversions"
        ],
        aiApproach: "Ask AI for the PostgreSQL syntax, then adapt for your database if different.",
        deliverable: "data_cleaning.sql with transformation examples"
      }
    ],

    successCriteria: [
      "Can use common string functions confidently",
      "Can extract and format dates",
      "Know which functions are database-specific"
    ],

    keyTerms: [
      { term: "SUBSTRING", definition: "Extracts part of a string" },
      { term: "DATE_TRUNC", definition: "Truncates timestamp to specified precision (PostgreSQL)" },
      { term: "COALESCE", definition: "Returns first non-NULL value in the list" }
    ],

    commonMistakes: [
      { mistake: "Using MySQL syntax in PostgreSQL or vice versa", fix: "Know your target database and verify syntax" },
      { mistake: "Not handling NULL in string concatenation", fix: "Use COALESCE to handle NULLs" }
    ],

    futureProofNote: "Data cleaning is 80% of data engineering work. These SQL patterns are used daily."
  },

  {
    dayNumber: 28,
    week: 7,
    topic: "CASE Statements and Conditional Logic",
    subtitle: "Business logic in SQL - categorizing and transforming data",

    objectives: [
      "Write CASE statements for categorization",
      "Use CASE in SELECT and WHERE",
      "Implement complex business logic",
      "Pivot data with conditional aggregation"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'ai-review',
      aiTip: "AI writes CASE statements well but may miss edge cases. Always list all possible values and verify each is handled.",
      warningWhenNotToUseAI: "Business logic must be correct. Review every CASE condition against requirements."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL CASE statements", type: "video" },
      { time: "0:15-0:35", activity: "CASE syntax and patterns", type: "learn" },
      { time: "0:35-0:55", activity: "Conditional aggregation", type: "practice" },
      { time: "0:55-1:20", activity: "Business rule implementation", type: "exercise" },
      { time: "1:20-1:30", activity: "Edge case review", type: "review" }
    ],

    resources: {
      required: [
        { title: "Socratica - SQL CASE", url: "https://www.youtube.com/watch?v=8j0a2t0gqV8", type: "video", duration: "6 min" }
      ],
      optional: [
        { title: "Mode Analytics - CASE", url: "https://mode.com/sql-tutorial/sql-case/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Business Logic Challenge",
        description: "Implement complex business rules in SQL",
        hints: [
          "Create customer tiers based on spending",
          "Calculate shipping rates by region and weight",
          "Generate status labels from multiple conditions",
          "Build a simple pivot table with CASE"
        ],
        aiApproach: "Describe business rules clearly. Have AI generate CASE logic, then verify every branch.",
        deliverable: "business_logic.sql with rule implementations"
      }
    ],

    successCriteria: [
      "Can write complex nested CASE statements",
      "Can pivot data with conditional aggregation",
      "Always include ELSE clause for safety"
    ],

    weeklyCheckpoint: {
      title: "Week 7: SQL Intermediate",
      description: "You should now handle complex analytical queries.",
      deliverables: [
        "window_functions.sql with analytics",
        "time_series_analysis.sql with LAG/LEAD",
        "data_cleaning.sql with transformations",
        "business_logic.sql with CASE patterns"
      ],
      selfAssessment: [
        "Can I write window functions without help?",
        "Do I know when to use LAG vs ROW_NUMBER?",
        "Can I clean data with SQL string functions?",
        "Can I implement complex business rules?"
      ]
    },

    keyTerms: [
      { term: "CASE", definition: "Conditional expression for if-then-else logic in SQL" },
      { term: "Conditional aggregation", definition: "Using CASE inside aggregate functions to pivot data" },
      { term: "ELSE clause", definition: "Default value when no CASE conditions match" }
    ],

    commonMistakes: [
      { mistake: "Forgetting ELSE clause", fix: "Always include ELSE to handle unexpected values" },
      { mistake: "Overlapping CASE conditions", fix: "Conditions are evaluated in order; first match wins" }
    ],

    futureProofNote: "Business logic in SQL is how you build data products. These skills transfer directly to dbt and analytics engineering."
  },

  // ============================================
  // WEEK 8: SQL Advanced & Performance
  // ============================================

  {
    dayNumber: 29,
    week: 8,
    topic: "Query Performance and EXPLAIN",
    subtitle: "Making queries fast - the difference between junior and senior",

    objectives: [
      "Understand query execution plans",
      "Use EXPLAIN to analyze queries",
      "Identify common performance issues",
      "Know basic indexing concepts"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'learn-with-ai',
      aiTip: "Paste EXPLAIN output to ChatGPT and ask it to interpret. Understanding execution plans is a senior skill.",
      warningWhenNotToUseAI: "AI can suggest optimizations, but you must understand WHY they help."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL query optimization", type: "video" },
      { time: "0:15-0:35", activity: "Reading EXPLAIN output", type: "learn" },
      { time: "0:35-0:55", activity: "Identifying slow patterns", type: "practice" },
      { time: "0:55-1:20", activity: "Optimize slow queries", type: "exercise" },
      { time: "1:20-1:30", activity: "Before/after comparison", type: "review" }
    ],

    resources: {
      required: [
        { title: "Hussein Nasser - SQL EXPLAIN", url: "https://www.youtube.com/watch?v=D-vZh8Mkef4", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Use The Index, Luke", url: "https://use-the-index-luke.com/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Query Optimization Lab",
        description: "Take slow queries and optimize them",
        hints: [
          "Run EXPLAIN on each query",
          "Identify table scans vs index usage",
          "Rewrite to use indexes effectively",
          "Measure before/after performance"
        ],
        aiApproach: "Share EXPLAIN output with AI and ask for optimization suggestions. Understand each suggestion before applying.",
        deliverable: "optimization_examples.sql with before/after"
      }
    ],

    successCriteria: [
      "Can read basic EXPLAIN output",
      "Know what table scans and index scans mean",
      "Can identify obvious performance issues"
    ],

    keyTerms: [
      { term: "EXPLAIN", definition: "Shows the query execution plan without running the query" },
      { term: "Seq Scan", definition: "Reading every row in a table (often slow)" },
      { term: "Index Scan", definition: "Using an index to find rows (usually fast)" }
    ],

    commonMistakes: [
      { mistake: "Optimizing before measuring", fix: "Always measure first with EXPLAIN" },
      { mistake: "Adding indexes without understanding", fix: "Indexes have write overhead; add strategically" }
    ],

    futureProofNote: "Query performance is what makes you valuable. Anyone can write slow queries. Making them fast is senior-level work."
  },

  {
    dayNumber: 30,
    week: 8,
    topic: "Set Operations and Advanced Joins",
    subtitle: "UNION, INTERSECT, EXCEPT, and self-joins",

    objectives: [
      "Use UNION and UNION ALL correctly",
      "Understand INTERSECT and EXCEPT",
      "Write self-joins for hierarchical data",
      "Combine set operations with other queries"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'manual-practice',
      aiTip: "These operations are fundamental. Practice manually to build intuition. Use AI only to verify your understanding.",
      warningWhenNotToUseAI: "Don't skip manual practice. Set operations are interview staples."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQL set operations", type: "video" },
      { time: "0:15-0:35", activity: "UNION, INTERSECT, EXCEPT", type: "learn" },
      { time: "0:35-0:55", activity: "Self-joins for hierarchies", type: "practice" },
      { time: "0:55-1:20", activity: "Complex query challenges", type: "exercise" },
      { time: "1:20-1:30", activity: "Draw Venn diagrams for each operation", type: "review" }
    ],

    resources: {
      required: [
        { title: "Socratica - UNION", url: "https://www.youtube.com/watch?v=T7lH-L8QrI4", type: "video", duration: "6 min" }
      ],
      optional: [
        { title: "Self-Joins Explained", url: "https://www.sqlshack.com/sql-self-join/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Set Operations Challenge",
        description: "Solve problems requiring set operations and self-joins",
        hints: [
          "Find customers in A but not B",
          "Combine results from different tables",
          "Build organizational hierarchy with self-join",
          "Find pairs of related records"
        ],
        aiApproach: "Write solutions yourself. Use AI to check and explain alternatives.",
        deliverable: "set_operations.sql with solutions"
      }
    ],

    successCriteria: [
      "Know when UNION vs UNION ALL",
      "Can write self-joins correctly",
      "Understand set operation semantics"
    ],

    keyTerms: [
      { term: "UNION", definition: "Combines results, removing duplicates" },
      { term: "UNION ALL", definition: "Combines results, keeping all rows" },
      { term: "Self-join", definition: "Joining a table to itself" }
    ],

    commonMistakes: [
      { mistake: "Using UNION when UNION ALL is correct", fix: "UNION removes duplicates (expensive); use UNION ALL if duplicates are OK" },
      { mistake: "Column type mismatches in UNION", fix: "All queries must have same number and types of columns" }
    ],

    futureProofNote: "Set operations and self-joins solve specific problems elegantly. They're interview favorites and production necessities."
  },

  {
    dayNumber: 31,
    week: 8,
    topic: "Data Integrity and Transactions",
    subtitle: "Keeping data correct - constraints, keys, and ACID",

    objectives: [
      "Understand primary and foreign keys",
      "Know constraint types and purposes",
      "Understand transaction basics (ACID)",
      "Know when transactions are needed"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to explain ACID with real-world analogies. Understanding transactions is crucial for data reliability.",
      warningWhenNotToUseAI: "Transactions are about correctness, not speed. Understand the concepts deeply."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Database constraints", type: "video" },
      { time: "0:15-0:35", activity: "Keys and constraints", type: "learn" },
      { time: "0:35-0:55", activity: "Transaction basics", type: "practice" },
      { time: "0:55-1:20", activity: "Design constrained tables", type: "exercise" },
      { time: "1:20-1:30", activity: "ACID property review", type: "review" }
    ],

    resources: {
      required: [
        { title: "Database Constraints Explained", url: "https://www.youtube.com/watch?v=6oZj7Y0gGt8", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "PostgreSQL Constraints", url: "https://www.postgresql.org/docs/current/ddl-constraints.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Constraint Design Exercise",
        description: "Design tables with proper constraints for data integrity",
        hints: [
          "Define primary keys for each table",
          "Add foreign keys for relationships",
          "Use CHECK constraints for valid values",
          "Consider NOT NULL and UNIQUE constraints"
        ],
        aiApproach: "Design first, then ask AI to review your constraints and suggest improvements.",
        deliverable: "constrained_schema.sql with DDL statements"
      }
    ],

    successCriteria: [
      "Know all common constraint types",
      "Can explain ACID properties",
      "Understand when to use transactions"
    ],

    keyTerms: [
      { term: "ACID", definition: "Atomicity, Consistency, Isolation, Durability - transaction guarantees" },
      { term: "Primary key", definition: "Unique identifier for each row in a table" },
      { term: "Foreign key", definition: "Reference to primary key in another table" }
    ],

    commonMistakes: [
      { mistake: "Skipping constraints to save time", fix: "Constraints prevent bad data; they save time long-term" },
      { mistake: "Not using transactions for multi-statement updates", fix: "Wrap related changes in a transaction" }
    ],

    futureProofNote: "Data integrity is non-negotiable in production. Understanding transactions is essential for reliable data systems."
  },

  {
    dayNumber: 32,
    week: 8,
    topic: "SQL Project: End-to-End Analytics",
    subtitle: "Putting it all together - a complete SQL project",

    objectives: [
      "Design a complete analytics query suite",
      "Combine all SQL concepts learned",
      "Write production-quality queries",
      "Document your SQL work professionally"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Use AI for code review. Ask it to critique your SQL for performance, readability, and correctness.",
      warningWhenNotToUseAI: "Write the queries yourself. Only use AI for review and improvement suggestions."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Review project requirements", type: "learn" },
      { time: "0:15-0:45", activity: "Write core analytics queries", type: "exercise" },
      { time: "0:45-1:10", activity: "Add documentation and comments", type: "exercise" },
      { time: "1:10-1:30", activity: "AI code review and refinement", type: "review" }
    ],

    resources: {
      required: [
        { title: "SQL Style Guide", url: "https://www.sqlstyle.guide/", type: "reference" }
      ],
      optional: [
        { title: "Mode Analytics Case Studies", url: "https://mode.com/sql-tutorial/sql-business-analytics-training/", type: "tutorial" }
      ]
    },

    exercises: [
      {
        title: "Complete Analytics Suite",
        description: "Build a set of production-quality analytics queries",
        hints: [
          "Customer segmentation query",
          "Revenue trends with window functions",
          "Cohort analysis query",
          "Executive summary dashboard query",
          "Document each query thoroughly"
        ],
        aiApproach: "Write all queries yourself. Use AI for final review and polish.",
        deliverable: "analytics_suite.sql with documented queries"
      }
    ],

    successCriteria: [
      "Queries are correct and performant",
      "Code is well-documented",
      "Uses appropriate SQL features"
    ],

    weeklyCheckpoint: {
      title: "Week 8: SQL Advanced & Performance",
      description: "You should now write senior-level SQL confidently.",
      deliverables: [
        "optimization_examples.sql with EXPLAIN analysis",
        "set_operations.sql with advanced queries",
        "constrained_schema.sql with DDL",
        "analytics_suite.sql project"
      ],
      selfAssessment: [
        "Can I read and understand EXPLAIN output?",
        "Do I know when to use each set operation?",
        "Can I design tables with proper constraints?",
        "Can I write production-quality analytics SQL?"
      ]
    },

    futureProofNote: "This project demonstrates your SQL skills. Keep it polished for your portfolio."
  },

  // ============================================
  // WEEK 9: SQL Data Modeling
  // ============================================

  {
    dayNumber: 33,
    week: 9,
    topic: "Dimensional Modeling Concepts",
    subtitle: "Star schemas and data warehouse design fundamentals",

    objectives: [
      "Understand dimensional modeling principles",
      "Know the difference between OLTP and OLAP",
      "Design star schemas with facts and dimensions",
      "Understand slowly changing dimensions basics"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to explain Kimball methodology with examples. Understanding data modeling philosophy is as important as syntax.",
      warningWhenNotToUseAI: "Data modeling is about understanding the business, not just technical patterns."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Video: Dimensional modeling intro", type: "video" },
      { time: "0:20-0:40", activity: "Star schema design principles", type: "learn" },
      { time: "0:40-1:00", activity: "Design a fact table", type: "practice" },
      { time: "1:00-1:20", activity: "Design dimension tables", type: "exercise" },
      { time: "1:20-1:30", activity: "Review OLTP vs OLAP trade-offs", type: "review" }
    ],

    resources: {
      required: [
        { title: "Data Warehouse Toolkit Concepts", url: "https://www.youtube.com/watch?v=lWPiSZf7-uQ", type: "video", duration: "25 min" }
      ],
      optional: [
        { title: "Kimball Group Design Tips", url: "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "E-commerce Star Schema",
        description: "Design a star schema for an e-commerce analytics use case",
        hints: [
          "Identify the fact table (sales_fact)",
          "Design dimension tables (date, product, customer, store)",
          "Define grain of the fact table",
          "Determine appropriate measures and attributes"
        ],
        aiApproach: "Design first, then ask AI to review your schema and suggest improvements.",
        deliverable: "ecommerce_star_schema.sql with DDL"
      }
    ],

    successCriteria: [
      "Can explain star schema components",
      "Know when to use dimensional modeling",
      "Can identify facts vs dimensions"
    ],

    keyTerms: [
      { term: "Fact table", definition: "Table containing measurable events/transactions" },
      { term: "Dimension table", definition: "Table containing descriptive attributes for analysis" },
      { term: "Grain", definition: "The level of detail in a fact table (e.g., one row per order line)" }
    ],

    commonMistakes: [
      { mistake: "Putting descriptive attributes in fact tables", fix: "Move attributes to dimension tables" },
      { mistake: "Using normalized designs for analytics", fix: "Denormalize for query performance in OLAP" }
    ],

    futureProofNote: "Dimensional modeling is the foundation of data warehouses. Understanding it is essential for dbt and analytics engineering."
  },

  {
    dayNumber: 34,
    week: 9,
    topic: "Normalization and Denormalization",
    subtitle: "When to normalize, when to denormalize, and why",

    objectives: [
      "Understand 1NF, 2NF, 3NF normalization",
      "Know when normalization helps/hurts",
      "Understand denormalization trade-offs",
      "Design for appropriate use cases"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often generates normalized schemas by default. Question whether denormalization is better for your analytics use case.",
      warningWhenNotToUseAI: "Schema design requires understanding usage patterns. AI doesn't know your query patterns."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Database normalization", type: "video" },
      { time: "0:15-0:35", activity: "1NF, 2NF, 3NF explained", type: "learn" },
      { time: "0:35-0:55", activity: "Normalization practice", type: "practice" },
      { time: "0:55-1:20", activity: "Denormalization decisions", type: "exercise" },
      { time: "1:20-1:30", activity: "Trade-offs summary", type: "review" }
    ],

    resources: {
      required: [
        { title: "Database Normalization Explained", url: "https://www.youtube.com/watch?v=GFQaEYEc8_8", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Normalization Deep Dive", url: "https://www.guru99.com/database-normalization.html", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Normalize and Denormalize",
        description: "Take a flat table and normalize it, then denormalize for analytics",
        hints: [
          "Start with a wide, repeated data table",
          "Normalize to 3NF step by step",
          "Then create denormalized analytics views",
          "Document trade-offs at each step"
        ],
        aiApproach: "Have AI explain each normalization step. Verify you understand the 'why' behind each change.",
        deliverable: "normalization_exercise.sql with steps documented"
      }
    ],

    successCriteria: [
      "Can identify normalization violations",
      "Know when denormalization is appropriate",
      "Can explain trade-offs clearly"
    ],

    keyTerms: [
      { term: "1NF", definition: "First Normal Form - atomic values, no repeating groups" },
      { term: "3NF", definition: "Third Normal Form - no transitive dependencies" },
      { term: "Denormalization", definition: "Intentionally adding redundancy for performance" }
    ],

    commonMistakes: [
      { mistake: "Over-normalizing analytics tables", fix: "Analytics queries need fewer JOINs" },
      { mistake: "Under-normalizing transactional tables", fix: "OLTP systems need normalization to prevent anomalies" }
    ],

    futureProofNote: "Knowing when to break the rules is what makes you senior. Normalization is a guideline, not a law."
  },

  {
    dayNumber: 35,
    week: 9,
    topic: "Slowly Changing Dimensions",
    subtitle: "Tracking history in dimension tables",

    objectives: [
      "Understand SCD Types 1, 2, and 3",
      "Implement SCD Type 2 with surrogate keys",
      "Know when each SCD type is appropriate",
      "Handle SCD in queries"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'copilot'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask ChatGPT to explain SCD Type 2 with a customer address change example. Visual examples make this clearer.",
      warningWhenNotToUseAI: "SCD implementation varies by tool. Understand the pattern before AI generates code."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Slowly Changing Dimensions", type: "video" },
      { time: "0:15-0:35", activity: "SCD types compared", type: "learn" },
      { time: "0:35-0:55", activity: "SCD Type 2 implementation", type: "practice" },
      { time: "0:55-1:20", activity: "Build SCD customer dimension", type: "exercise" },
      { time: "1:20-1:30", activity: "Query historical data", type: "review" }
    ],

    resources: {
      required: [
        { title: "SCD Types Explained", url: "https://www.youtube.com/watch?v=Qq-18qNIlec", type: "video", duration: "18 min" }
      ],
      optional: [
        { title: "Kimball SCD Techniques", url: "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-2/", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "SCD Type 2 Implementation",
        description: "Build a customer dimension with full history tracking",
        hints: [
          "Add surrogate key, natural key, start_date, end_date, is_current",
          "Write INSERT for new customers",
          "Write UPDATE logic for changes",
          "Query to get customer state at any point in time"
        ],
        aiApproach: "Design the schema yourself. Use AI to help with the merge/update logic.",
        deliverable: "scd_customer_dimension.sql with history tracking"
      }
    ],

    successCriteria: [
      "Can implement SCD Type 2",
      "Know when each SCD type fits",
      "Can query historical dimension state"
    ],

    keyTerms: [
      { term: "SCD Type 1", definition: "Overwrite old values - no history" },
      { term: "SCD Type 2", definition: "Add new row for each change - full history" },
      { term: "Surrogate key", definition: "System-generated unique identifier for each dimension row" }
    ],

    commonMistakes: [
      { mistake: "Using natural keys as fact table foreign keys", fix: "Use surrogate keys to reference correct dimension version" },
      { mistake: "Forgetting is_current flag", fix: "Always maintain a current record indicator" }
    ],

    futureProofNote: "SCD Type 2 is essential for any historical analysis. It's implemented in every major data warehouse."
  },

  {
    dayNumber: 36,
    week: 9,
    topic: "Data Modeling Project",
    subtitle: "Design a complete data model from requirements",

    objectives: [
      "Translate business requirements to data model",
      "Design a complete star schema",
      "Implement tables with proper DDL",
      "Document the model professionally"
    ],

    aiIntegration: {
      toolsUsed: ['claude', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Use AI to review your model and ask probing questions about edge cases you might have missed.",
      warningWhenNotToUseAI: "Design the model yourself first. AI review is for refinement, not creation."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Review project requirements", type: "learn" },
      { time: "0:15-0:45", activity: "Design conceptual model", type: "exercise" },
      { time: "0:45-1:10", activity: "Write DDL statements", type: "exercise" },
      { time: "1:10-1:30", activity: "AI review and documentation", type: "review" }
    ],

    resources: {
      required: [
        { title: "ERD Drawing Tools", url: "https://dbdiagram.io/", type: "tool" }
      ],
      optional: [
        { title: "Data Model Documentation Best Practices", url: "https://www.dataversity.net/data-modeling-101-documenting-your-data-model/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Complete Data Model",
        description: "Design a data model for a ride-sharing company",
        hints: [
          "Fact: rides (trip_id, timestamps, measures)",
          "Dimensions: driver, rider, vehicle, location, date",
          "Consider SCD for driver/rider changes",
          "Document grain, keys, and relationships"
        ],
        aiApproach: "Complete your design, then ask AI to find holes in your model.",
        deliverable: "rideshare_data_model.sql with documentation"
      }
    ],

    successCriteria: [
      "Model handles all requirements",
      "DDL is correct and complete",
      "Documentation is professional"
    ],

    weeklyCheckpoint: {
      title: "Week 9: SQL Data Modeling",
      description: "You should now design professional data models.",
      deliverables: [
        "ecommerce_star_schema.sql",
        "normalization_exercise.sql",
        "scd_customer_dimension.sql",
        "rideshare_data_model.sql project"
      ],
      selfAssessment: [
        "Can I design a star schema from requirements?",
        "Do I know when to normalize vs denormalize?",
        "Can I implement SCD Type 2?",
        "Can I document a data model professionally?"
      ]
    },

    futureProofNote: "Data modeling skills are highly valued. Good models make everything downstream easier - dbt, dashboards, ML features."
  },

  // ============================================
  // WEEK 10: Python-SQL Integration
  // ============================================

  {
    dayNumber: 37,
    week: 10,
    topic: "Database Connections with Python",
    subtitle: "Connecting Python to databases - the bridge to automation",

    objectives: [
      "Connect to databases using DB-API",
      "Execute queries and fetch results",
      "Handle connection errors properly",
      "Use context managers for connections"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask AI for connection patterns for your specific database (PostgreSQL, SQLite, etc.). Patterns vary by database.",
      warningWhenNotToUseAI: "Never let AI generate code with hardcoded credentials. Use environment variables."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python database connectivity", type: "video" },
      { time: "0:15-0:35", activity: "DB-API concepts", type: "learn" },
      { time: "0:35-0:55", activity: "Connection patterns", type: "practice" },
      { time: "0:55-1:20", activity: "Build a database utility module", type: "exercise" },
      { time: "1:20-1:30", activity: "Error handling review", type: "review" }
    ],

    resources: {
      required: [
        { title: "Python SQLite Tutorial", url: "https://www.youtube.com/watch?v=pd-0G0MigUA", type: "video", duration: "30 min" }
      ],
      optional: [
        { title: "Real Python - SQLite", url: "https://realpython.com/python-sqlite-sqlalchemy/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Database Utility Module",
        description: "Create a reusable module for database operations",
        hints: [
          "Create connection context manager",
          "Add execute_query() function",
          "Add fetch_all() and fetch_one() helpers",
          "Handle connection errors gracefully"
        ],
        aiApproach: "Ask AI for the pattern, but ensure credentials come from environment variables.",
        deliverable: "db_utils.py with connection utilities"
      }
    ],

    successCriteria: [
      "Can connect to SQLite and PostgreSQL",
      "Always use context managers for connections",
      "Never hardcode credentials"
    ],

    keyTerms: [
      { term: "DB-API 2.0", definition: "Python standard for database interfaces" },
      { term: "Cursor", definition: "Object that executes queries and fetches results" },
      { term: "Connection pool", definition: "Cache of database connections for reuse" }
    ],

    commonMistakes: [
      { mistake: "Hardcoding database credentials", fix: "Use environment variables or config files" },
      { mistake: "Not closing connections", fix: "Always use context managers (with statement)" }
    ],

    futureProofNote: "Database connectivity is how you build data pipelines. These patterns are used in every data engineering job."
  },

  {
    dayNumber: 38,
    week: 10,
    topic: "SQLAlchemy Introduction",
    subtitle: "The most important Python ORM for data engineering",

    objectives: [
      "Understand SQLAlchemy architecture",
      "Use SQLAlchemy Core for SQL execution",
      "Build queries programmatically",
      "Know when ORM vs Core is appropriate"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'learn-with-ai',
      aiTip: "SQLAlchemy is complex. Ask AI to explain Core vs ORM trade-offs. For data engineering, Core is often better.",
      warningWhenNotToUseAI: "AI often generates ORM patterns. For data pipelines, SQLAlchemy Core is usually more appropriate."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: SQLAlchemy introduction", type: "video" },
      { time: "0:15-0:35", activity: "SQLAlchemy Core concepts", type: "learn" },
      { time: "0:35-0:55", activity: "Programmatic query building", type: "practice" },
      { time: "0:55-1:20", activity: "Build a data extractor", type: "exercise" },
      { time: "1:20-1:30", activity: "Core vs ORM decision framework", type: "review" }
    ],

    resources: {
      required: [
        { title: "SQLAlchemy Tutorial", url: "https://www.youtube.com/watch?v=woKYyhLCcnU", type: "video", duration: "45 min" }
      ],
      optional: [
        { title: "SQLAlchemy Core Documentation", url: "https://docs.sqlalchemy.org/en/20/core/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "SQLAlchemy Data Extractor",
        description: "Build a flexible data extraction tool using SQLAlchemy Core",
        hints: [
          "Use create_engine() for connection",
          "Build queries using Table and select()",
          "Add dynamic filtering",
          "Return results as dictionaries"
        ],
        aiApproach: "Ask AI for SQLAlchemy Core patterns specifically, not ORM patterns.",
        deliverable: "sqlalchemy_extractor.py with extraction functions"
      }
    ],

    successCriteria: [
      "Can use SQLAlchemy Core for queries",
      "Can build dynamic queries programmatically",
      "Know when to use Core vs ORM"
    ],

    keyTerms: [
      { term: "Engine", definition: "SQLAlchemy's connection factory" },
      { term: "Core", definition: "SQLAlchemy's SQL expression language (SQL-focused)" },
      { term: "ORM", definition: "Object-Relational Mapper (object-focused)" }
    ],

    commonMistakes: [
      { mistake: "Using ORM for bulk data operations", fix: "Use Core for ETL - it's faster and more explicit" },
      { mistake: "Creating too many engines", fix: "Create one engine and share it" }
    ],

    futureProofNote: "SQLAlchemy is used in Airflow, most Python web frameworks, and countless data tools. Master it."
  },

  {
    dayNumber: 39,
    week: 10,
    topic: "Pandas and SQL Integration",
    subtitle: "The most powerful data manipulation combo",

    objectives: [
      "Read SQL results into DataFrames",
      "Write DataFrames to databases",
      "Use pandas for data transformations",
      "Know when pandas vs pure SQL is better"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'prompt-engineering',
      aiTip: "Describe your data transformation in plain English. AI is excellent at generating pandas code from natural language descriptions.",
      warningWhenNotToUseAI: "Always verify data types after reading SQL into pandas. AI assumes types are correct."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Pandas SQL integration", type: "video" },
      { time: "0:15-0:35", activity: "read_sql and to_sql", type: "learn" },
      { time: "0:35-0:55", activity: "DataFrame transformations", type: "practice" },
      { time: "0:55-1:20", activity: "Build ETL with pandas", type: "exercise" },
      { time: "1:20-1:30", activity: "Pandas vs SQL decision framework", type: "review" }
    ],

    resources: {
      required: [
        { title: "Pandas Read SQL Tutorial", url: "https://www.youtube.com/watch?v=M-4EpNdlSuY", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Pandas SQL Documentation", url: "https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Pandas ETL Pipeline",
        description: "Build a complete ETL pipeline using pandas and SQL",
        hints: [
          "Extract data from SQL into DataFrame",
          "Clean and transform with pandas",
          "Handle missing values appropriately",
          "Write results back to a new table"
        ],
        aiApproach: "Describe each transformation step in plain English, get pandas code, then verify results.",
        deliverable: "pandas_etl.py with complete pipeline"
      }
    ],

    successCriteria: [
      "Can move data between SQL and pandas fluently",
      "Can transform data efficiently in pandas",
      "Know when to use SQL vs pandas for transformations"
    ],

    keyTerms: [
      { term: "DataFrame", definition: "Pandas 2D labeled data structure (like a table)" },
      { term: "read_sql()", definition: "Reads SQL query results into a DataFrame" },
      { term: "to_sql()", definition: "Writes DataFrame to a SQL table" }
    ],

    commonMistakes: [
      { mistake: "Loading huge tables into memory", fix: "Use SQL WHERE clauses to filter first" },
      { mistake: "Not specifying dtypes", fix: "Check and convert data types after loading" }
    ],

    futureProofNote: "Pandas + SQL is the backbone of Python data engineering. This combo solves most data problems."
  },

  {
    dayNumber: 40,
    week: 10,
    topic: "Bulk Data Operations",
    subtitle: "Moving large datasets efficiently",

    objectives: [
      "Understand bulk insert strategies",
      "Use COPY command for PostgreSQL",
      "Handle large files efficiently",
      "Optimize for throughput"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Ask AI about bulk loading best practices for your specific database. Methods vary significantly.",
      warningWhenNotToUseAI: "Bulk operations can corrupt data if wrong. Test on small datasets first."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Bulk data loading", type: "video" },
      { time: "0:15-0:35", activity: "Bulk insert strategies", type: "learn" },
      { time: "0:35-0:55", activity: "COPY command for PostgreSQL", type: "practice" },
      { time: "0:55-1:20", activity: "Build bulk loader", type: "exercise" },
      { time: "1:20-1:30", activity: "Performance comparison", type: "review" }
    ],

    resources: {
      required: [
        { title: "PostgreSQL COPY Command", url: "https://www.postgresql.org/docs/current/sql-copy.html", type: "docs" }
      ],
      optional: [
        { title: "Bulk Loading Best Practices", url: "https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples", type: "article" }
      ]
    },

    exercises: [
      {
        title: "High-Performance Bulk Loader",
        description: "Build a bulk loader that handles millions of rows efficiently",
        hints: [
          "Compare row-by-row vs batch vs COPY",
          "Measure execution time for each approach",
          "Handle errors without losing good data",
          "Add progress reporting for long operations"
        ],
        aiApproach: "Ask AI for the fastest approach for your database. Verify with benchmarks.",
        deliverable: "bulk_loader.py with performance metrics"
      }
    ],

    successCriteria: [
      "Know multiple bulk loading strategies",
      "Can use database-specific optimizations",
      "Can benchmark and choose the fastest approach"
    ],

    weeklyCheckpoint: {
      title: "Week 10: Python-SQL Integration",
      description: "You should now build complete data pipelines with Python and SQL.",
      deliverables: [
        "db_utils.py connection utilities",
        "sqlalchemy_extractor.py",
        "pandas_etl.py pipeline",
        "bulk_loader.py with benchmarks"
      ],
      selfAssessment: [
        "Can I connect to databases securely?",
        "Do I know when to use SQLAlchemy Core vs ORM?",
        "Can I move data between SQL and pandas efficiently?",
        "Can I load large datasets performantly?"
      ]
    },

    keyTerms: [
      { term: "Bulk insert", definition: "Loading many rows at once instead of one at a time" },
      { term: "COPY", definition: "PostgreSQL command for high-speed bulk loading" },
      { term: "Batch size", definition: "Number of rows processed together in one operation" }
    ],

    commonMistakes: [
      { mistake: "Inserting rows one at a time", fix: "Batch inserts or use COPY" },
      { mistake: "No error handling in bulk operations", fix: "Use transactions and savepoints" }
    ],

    futureProofNote: "Performance matters in production. Knowing bulk loading techniques is essential for real data engineering work."
  },

  // ============================================
  // WEEK 11: APIs and Data Extraction
  // ============================================

  {
    dayNumber: 41,
    week: 11,
    topic: "REST API Fundamentals",
    subtitle: "Accessing web data - the modern data source",

    objectives: [
      "Understand REST API concepts",
      "Make HTTP requests with requests library",
      "Handle authentication methods",
      "Parse JSON API responses"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Paste API documentation to ChatGPT and ask it to write the Python code. This is a legitimate and efficient workflow.",
      warningWhenNotToUseAI: "Never share API keys or secrets with AI tools."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: REST API basics", type: "video" },
      { time: "0:15-0:35", activity: "HTTP methods and status codes", type: "learn" },
      { time: "0:35-0:55", activity: "requests library practice", type: "practice" },
      { time: "0:55-1:20", activity: "Access a public API", type: "exercise" },
      { time: "1:20-1:30", activity: "Authentication patterns", type: "review" }
    ],

    resources: {
      required: [
        { title: "Python Requests Tutorial", url: "https://www.youtube.com/watch?v=tb8gHvYlCFs", type: "video", duration: "22 min" }
      ],
      optional: [
        { title: "Real Python - API Tutorial", url: "https://realpython.com/api-integration-in-python/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "API Data Extractor",
        description: "Build a function to extract data from a public API",
        hints: [
          "Use a free public API (JSONPlaceholder, GitHub, etc.)",
          "Handle rate limiting with retries",
          "Parse nested JSON responses",
          "Store results in a structured format"
        ],
        aiApproach: "Share API docs with AI for code generation. Review auth handling carefully.",
        deliverable: "api_extractor.py with extraction functions"
      }
    ],

    successCriteria: [
      "Can make authenticated API requests",
      "Can handle errors and retries",
      "Can parse complex JSON responses"
    ],

    keyTerms: [
      { term: "REST", definition: "Representational State Transfer - API design pattern" },
      { term: "Endpoint", definition: "URL path for a specific API resource" },
      { term: "Rate limiting", definition: "Restriction on how many requests you can make" }
    ],

    commonMistakes: [
      { mistake: "Ignoring rate limits", fix: "Implement exponential backoff" },
      { mistake: "Hardcoding API keys", fix: "Use environment variables" }
    ],

    futureProofNote: "APIs are how modern systems share data. Knowing how to extract API data is essential for data engineering."
  },

  {
    dayNumber: 42,
    week: 11,
    topic: "Pagination and Rate Limiting",
    subtitle: "Handling real-world API challenges",

    objectives: [
      "Implement cursor-based pagination",
      "Handle offset-based pagination",
      "Implement rate limit handling",
      "Build robust API clients"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'debug-ai-code',
      aiTip: "AI often generates pagination code that works for simple cases but fails on edge cases. Test with multiple pages.",
      warningWhenNotToUseAI: "Pagination logic is tricky. Verify the stopping conditions work correctly."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: API pagination patterns", type: "video" },
      { time: "0:15-0:35", activity: "Pagination strategies", type: "learn" },
      { time: "0:35-0:55", activity: "Rate limit handling", type: "practice" },
      { time: "0:55-1:20", activity: "Build paginated extractor", type: "exercise" },
      { time: "1:20-1:30", activity: "Edge case testing", type: "review" }
    ],

    resources: {
      required: [
        { title: "API Pagination Best Practices", url: "https://nordicapis.com/everything-you-need-to-know-about-api-pagination/", type: "article" }
      ],
      optional: [
        { title: "Tenacity Library", url: "https://tenacity.readthedocs.io/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Full API Extraction",
        description: "Extract all data from a paginated API endpoint",
        hints: [
          "Detect pagination type (cursor, offset, or link-based)",
          "Implement extraction loop with proper stopping",
          "Add rate limit handling with tenacity",
          "Report progress during extraction"
        ],
        aiApproach: "Generate pagination code with AI, then test with different page sizes and data volumes.",
        deliverable: "paginated_extractor.py with full extraction"
      }
    ],

    successCriteria: [
      "Can handle any pagination pattern",
      "Implement proper rate limit backoff",
      "Test edge cases thoroughly"
    ],

    keyTerms: [
      { term: "Cursor pagination", definition: "Using a marker/token to request next page" },
      { term: "Offset pagination", definition: "Using skip/take parameters for pages" },
      { term: "Exponential backoff", definition: "Increasing wait time between retries" }
    ],

    commonMistakes: [
      { mistake: "Infinite loops from bad pagination logic", fix: "Always have a maximum iterations limit" },
      { mistake: "Not handling empty last page", fix: "Check for empty results as stop condition" }
    ],

    futureProofNote: "Real APIs require pagination and rate limit handling. These patterns are used in every production data pipeline."
  },

  {
    dayNumber: 43,
    week: 11,
    topic: "Web Scraping Basics",
    subtitle: "When there's no API - ethical data extraction",

    objectives: [
      "Understand web scraping ethics and legality",
      "Use BeautifulSoup for HTML parsing",
      "Handle dynamic content considerations",
      "Respect robots.txt and rate limits"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'learn-with-ai',
      aiTip: "Paste HTML snippets to AI and ask for parsing code. AI is excellent at generating BeautifulSoup selectors.",
      warningWhenNotToUseAI: "Always check if scraping is allowed. AI won't warn you about legal/ethical issues."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Web scraping intro", type: "video" },
      { time: "0:15-0:35", activity: "Ethics, legality, robots.txt", type: "learn" },
      { time: "0:35-0:55", activity: "BeautifulSoup basics", type: "practice" },
      { time: "0:55-1:20", activity: "Scrape a practice site", type: "exercise" },
      { time: "1:20-1:30", activity: "When not to scrape", type: "review" }
    ],

    resources: {
      required: [
        { title: "Web Scraping with Python", url: "https://www.youtube.com/watch?v=ng2o98k983k", type: "video", duration: "45 min" }
      ],
      optional: [
        { title: "Real Python - Web Scraping", url: "https://realpython.com/beautiful-soup-web-scraper-python/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Practice Site Scraper",
        description: "Scrape data from a site designed for scraping practice",
        hints: [
          "Use http://quotes.toscrape.com/ or similar practice site",
          "Parse structured data from HTML",
          "Navigate multiple pages",
          "Store results in clean format"
        ],
        aiApproach: "Paste HTML to AI for selector generation. Verify selectors work before running full scrape.",
        deliverable: "web_scraper.py with extracted data"
      }
    ],

    successCriteria: [
      "Know when scraping is appropriate",
      "Can parse HTML with BeautifulSoup",
      "Respect site policies and rate limits"
    ],

    keyTerms: [
      { term: "robots.txt", definition: "File that tells crawlers what's allowed to access" },
      { term: "BeautifulSoup", definition: "Python library for parsing HTML/XML" },
      { term: "Selector", definition: "CSS or XPath pattern to find HTML elements" }
    ],

    commonMistakes: [
      { mistake: "Scraping without checking terms of service", fix: "Always verify scraping is allowed" },
      { mistake: "Hammering sites with requests", fix: "Add delays between requests" }
    ],

    futureProofNote: "Scraping is useful but secondary to APIs. Prefer APIs when available. Know scraping for when there's no other option."
  },

  {
    dayNumber: 44,
    week: 11,
    topic: "Data Extraction Project",
    subtitle: "Build a complete data extraction pipeline",

    objectives: [
      "Design an extraction pipeline architecture",
      "Combine multiple data sources",
      "Handle errors and logging",
      "Store extracted data appropriately"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Use AI to review your pipeline design. Ask about edge cases, error handling, and production readiness.",
      warningWhenNotToUseAI: "Design the architecture yourself. Use AI for implementation details and code review."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Review project requirements", type: "learn" },
      { time: "0:15-0:45", activity: "Design and implement pipeline", type: "exercise" },
      { time: "0:45-1:10", activity: "Add logging and error handling", type: "exercise" },
      { time: "1:10-1:30", activity: "AI code review", type: "review" }
    ],

    resources: {
      required: [
        { title: "Python Logging Tutorial", url: "https://www.youtube.com/watch?v=jxmzY9soFXg", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Logging Best Practices", url: "https://docs.python.org/3/howto/logging.html", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Multi-Source Extraction Pipeline",
        description: "Build a pipeline that extracts data from API and transforms it",
        hints: [
          "Extract from at least one API",
          "Transform and validate the data",
          "Store results in SQLite database",
          "Add comprehensive logging"
        ],
        aiApproach: "Implement core logic yourself. Use AI to add polish - logging, error handling, type hints.",
        deliverable: "extraction_pipeline.py with complete pipeline"
      }
    ],

    successCriteria: [
      "Pipeline runs end-to-end",
      "Errors are handled gracefully",
      "Logging provides visibility into execution"
    ],

    weeklyCheckpoint: {
      title: "Week 11: APIs and Data Extraction",
      description: "You should now extract data from any web source.",
      deliverables: [
        "api_extractor.py",
        "paginated_extractor.py",
        "web_scraper.py",
        "extraction_pipeline.py project"
      ],
      selfAssessment: [
        "Can I work with any REST API?",
        "Can I handle pagination and rate limits?",
        "Do I know when scraping is appropriate?",
        "Can I build production-quality extraction pipelines?"
      ]
    },

    futureProofNote: "Data extraction is where data engineering starts. Every pipeline begins with getting the data. Master this."
  },

  // ============================================
  // WEEK 12: Integration and Testing
  // ============================================

  {
    dayNumber: 45,
    week: 12,
    topic: "Testing Data Pipelines",
    subtitle: "Quality assurance for data engineering",

    objectives: [
      "Understand testing strategies for data",
      "Write unit tests with pytest",
      "Test data transformations",
      "Use fixtures and mocking"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'prompt-engineering',
      aiTip: "Ask AI to generate test cases for your functions. AI is excellent at thinking of edge cases you might miss.",
      warningWhenNotToUseAI: "Verify AI-generated tests actually test what matters. Don't test trivial things."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python testing with pytest", type: "video" },
      { time: "0:15-0:35", activity: "Testing strategies for data", type: "learn" },
      { time: "0:35-0:55", activity: "Write tests for previous code", type: "practice" },
      { time: "0:55-1:20", activity: "Test your ETL functions", type: "exercise" },
      { time: "1:20-1:30", activity: "Fixtures and mocking", type: "review" }
    ],

    resources: {
      required: [
        { title: "Pytest Tutorial", url: "https://www.youtube.com/watch?v=cHYq1MRoyI0", type: "video", duration: "36 min" }
      ],
      optional: [
        { title: "Real Python - Pytest", url: "https://realpython.com/pytest-python-testing/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Test Your Pipeline",
        description: "Add comprehensive tests to your extraction pipeline",
        hints: [
          "Test each function individually",
          "Use fixtures for test data",
          "Mock API calls",
          "Test error handling paths"
        ],
        aiApproach: "Ask AI to generate test cases. Review for relevance and add edge cases it missed.",
        deliverable: "test_pipeline.py with comprehensive tests"
      }
    ],

    successCriteria: [
      "Can write pytest tests",
      "Know how to mock external dependencies",
      "Test coverage on critical functions"
    ],

    keyTerms: [
      { term: "Unit test", definition: "Test of a single function in isolation" },
      { term: "Fixture", definition: "Reusable test setup code" },
      { term: "Mock", definition: "Fake object that replaces real dependencies" }
    ],

    commonMistakes: [
      { mistake: "Testing trivial code", fix: "Focus tests on complex logic and edge cases" },
      { mistake: "Tests that depend on external services", fix: "Mock external dependencies" }
    ],

    futureProofNote: "Testing is what separates production code from scripts. Data quality issues cost real money. Test your pipelines."
  },

  {
    dayNumber: 46,
    week: 12,
    topic: "Data Validation Patterns",
    subtitle: "Catching bad data before it causes problems",

    objectives: [
      "Implement data validation checks",
      "Use Pydantic for data validation",
      "Design validation strategies",
      "Handle validation failures gracefully"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude'],
      focusArea: 'learn-with-ai',
      aiTip: "Ask Claude about Pydantic patterns. It's excellent for generating validation models from data examples.",
      warningWhenNotToUseAI: "Define validation rules based on business requirements, not just what AI suggests."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Pydantic introduction", type: "video" },
      { time: "0:15-0:35", activity: "Validation patterns", type: "learn" },
      { time: "0:35-0:55", activity: "Pydantic models", type: "practice" },
      { time: "0:55-1:20", activity: "Add validation to pipeline", type: "exercise" },
      { time: "1:20-1:30", activity: "Error handling strategies", type: "review" }
    ],

    resources: {
      required: [
        { title: "Pydantic Tutorial", url: "https://www.youtube.com/watch?v=502XOB0u8OY", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Pydantic Documentation", url: "https://docs.pydantic.dev/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Validated Data Pipeline",
        description: "Add Pydantic validation to your data pipeline",
        hints: [
          "Create Pydantic models for each data structure",
          "Validate at pipeline boundaries",
          "Handle validation errors appropriately",
          "Log validation failures for debugging"
        ],
        aiApproach: "Show AI your data structure and ask for Pydantic model. Review and adjust constraints.",
        deliverable: "validated_pipeline.py with Pydantic models"
      }
    ],

    successCriteria: [
      "Can create Pydantic models",
      "Validate data at pipeline boundaries",
      "Handle validation errors gracefully"
    ],

    keyTerms: [
      { term: "Pydantic", definition: "Python library for data validation using type hints" },
      { term: "Schema", definition: "Definition of expected data structure and types" },
      { term: "Validation boundary", definition: "Point where external data enters your system" }
    ],

    commonMistakes: [
      { mistake: "Validating too late in the pipeline", fix: "Validate as early as possible" },
      { mistake: "Silently dropping invalid records", fix: "Log and track validation failures" }
    ],

    futureProofNote: "Data validation is essential for data quality. Pydantic is increasingly used in modern Python data tools."
  },

  {
    dayNumber: 47,
    week: 12,
    topic: "Logging and Observability",
    subtitle: "Knowing what your pipelines are doing",

    objectives: [
      "Implement structured logging",
      "Design log levels and messages",
      "Add metrics and monitoring hooks",
      "Debug pipelines using logs"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Ask AI to add logging to existing code. It's great at placing log statements in the right locations.",
      warningWhenNotToUseAI: "Don't log sensitive data. Review AI-generated logging for privacy issues."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python logging deep dive", type: "video" },
      { time: "0:15-0:35", activity: "Logging best practices", type: "learn" },
      { time: "0:35-0:55", activity: "Add logging to code", type: "practice" },
      { time: "0:55-1:20", activity: "Observable pipeline project", type: "exercise" },
      { time: "1:20-1:30", activity: "Debugging with logs", type: "review" }
    ],

    resources: {
      required: [
        { title: "Python Logging Guide", url: "https://www.youtube.com/watch?v=9L77QExPmI0", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Structlog Library", url: "https://www.structlog.org/", type: "docs" }
      ]
    },

    exercises: [
      {
        title: "Observable Pipeline",
        description: "Add comprehensive logging and metrics to your pipeline",
        hints: [
          "Configure logging with appropriate levels",
          "Log at key pipeline stages",
          "Include useful context in log messages",
          "Add timing metrics for performance tracking"
        ],
        aiApproach: "Ask AI to add logging to your existing code. Review for completeness and privacy.",
        deliverable: "observable_pipeline.py with comprehensive logging"
      }
    ],

    successCriteria: [
      "Logging configured correctly",
      "Appropriate log levels used",
      "Can debug issues using logs"
    ],

    keyTerms: [
      { term: "Log level", definition: "Severity of log message (DEBUG, INFO, WARNING, ERROR)" },
      { term: "Structured logging", definition: "Logging with consistent, parseable format" },
      { term: "Observability", definition: "Ability to understand system state from outputs" }
    ],

    commonMistakes: [
      { mistake: "Logging too much at INFO level", fix: "Use DEBUG for verbose information" },
      { mistake: "Not including context in logs", fix: "Add identifiers like job_id, record_id" }
    ],

    futureProofNote: "Observability is essential for production systems. You can't fix what you can't see. Log thoughtfully."
  },

  {
    dayNumber: 48,
    week: 12,
    topic: "Code Quality and Documentation",
    subtitle: "Professional-grade code for your portfolio",

    objectives: [
      "Use linters and formatters (black, ruff)",
      "Write comprehensive docstrings",
      "Create README documentation",
      "Organize projects professionally"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'claude', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "AI is excellent at writing documentation. Generate docstrings and README content, then review for accuracy.",
      warningWhenNotToUseAI: "Verify AI-generated documentation matches what the code actually does."
    },

    sessionPlan: [
      { time: "0:00-0:15", activity: "Video: Python code quality tools", type: "video" },
      { time: "0:15-0:35", activity: "black, ruff, mypy setup", type: "learn" },
      { time: "0:35-0:55", activity: "Add docstrings to code", type: "practice" },
      { time: "0:55-1:20", activity: "Create project documentation", type: "exercise" },
      { time: "1:20-1:30", activity: "Portfolio preparation", type: "review" }
    ],

    resources: {
      required: [
        { title: "Python Code Formatting", url: "https://www.youtube.com/watch?v=SsoOG6ZeyUI", type: "video", duration: "15 min" }
      ],
      optional: [
        { title: "Google Python Style Guide", url: "https://google.github.io/styleguide/pyguide.html", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Portfolio-Ready Codebase",
        description: "Polish your Q1 code to portfolio quality",
        hints: [
          "Run black and ruff on all code",
          "Add type hints throughout",
          "Write docstrings for public functions",
          "Create README with setup instructions"
        ],
        aiApproach: "Use AI to generate documentation drafts. Review and edit for accuracy.",
        deliverable: "Polished codebase with documentation"
      }
    ],

    successCriteria: [
      "Code passes linting",
      "All public functions documented",
      "README explains how to use the code"
    ],

    weeklyCheckpoint: {
      title: "Week 12: Integration and Testing",
      description: "You should now write production-quality code.",
      deliverables: [
        "test_pipeline.py with tests",
        "validated_pipeline.py with Pydantic",
        "observable_pipeline.py with logging",
        "Polished, documented codebase"
      ],
      selfAssessment: [
        "Do I write tests for important code?",
        "Do I validate data at boundaries?",
        "Can I debug issues using logs?",
        "Is my code portfolio-ready?"
      ]
    },

    futureProofNote: "Code quality is what makes you hireable. Clean, tested, documented code is the mark of a professional."
  },

  // ============================================
  // WEEK 13: Q1 Capstone Project
  // ============================================

  {
    dayNumber: 49,
    week: 13,
    topic: "Q1 Capstone: Project Planning",
    subtitle: "Design a complete data pipeline from scratch",

    objectives: [
      "Define capstone project requirements",
      "Design system architecture",
      "Break project into tasks",
      "Set up project structure"
    ],

    aiIntegration: {
      toolsUsed: ['chatgpt', 'claude'],
      focusArea: 'prompt-engineering',
      aiTip: "Use AI as a thought partner for architecture design. Describe your idea and ask for feedback and suggestions.",
      warningWhenNotToUseAI: "The design decisions are yours. AI helps refine, but you own the architecture."
    },

    sessionPlan: [
      { time: "0:00-0:20", activity: "Define project scope", type: "learn" },
      { time: "0:20-0:45", activity: "Design architecture", type: "exercise" },
      { time: "0:45-1:10", activity: "Break into tasks", type: "exercise" },
      { time: "1:10-1:30", activity: "Set up project structure", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "Data Pipeline Architecture Patterns", url: "https://www.youtube.com/watch?v=VtzvF17ysbc", type: "video", duration: "20 min" }
      ],
      optional: [
        { title: "Project Planning Best Practices", url: "https://realpython.com/python-project-documentation/", type: "article" }
      ]
    },

    exercises: [
      {
        title: "Capstone Project Design",
        description: "Design a complete data pipeline that demonstrates Q1 skills",
        hints: [
          "Extract data from at least one API",
          "Transform and validate the data",
          "Store in a properly modeled database",
          "Include tests, logging, and documentation"
        ],
        aiApproach: "Discuss your design with AI. Ask for potential problems and improvements.",
        deliverable: "DESIGN.md with architecture and task breakdown"
      }
    ],

    successCriteria: [
      "Clear project requirements defined",
      "Architecture documented",
      "Tasks broken down and estimated"
    ],

    futureProofNote: "Planning is where senior engineers add value. Anyone can code a solution - designing the right solution is the skill."
  },

  {
    dayNumber: 50,
    week: 13,
    topic: "Q1 Capstone: Implementation Day 1",
    subtitle: "Build the extraction layer",

    objectives: [
      "Implement data extraction",
      "Handle errors and edge cases",
      "Add logging and monitoring",
      "Test extraction thoroughly"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'cursor'],
      focusArea: 'ai-review',
      aiTip: "Use Copilot for implementation speed. Have AI review your code for edge cases you might have missed.",
      warningWhenNotToUseAI: "You should be able to explain every line. Don't use code you don't understand."
    },

    sessionPlan: [
      { time: "0:00-0:45", activity: "Implement extraction", type: "exercise" },
      { time: "0:45-1:15", activity: "Add tests and error handling", type: "exercise" },
      { time: "1:15-1:30", activity: "AI code review", type: "review" }
    ],

    resources: {
      required: [
        { title: "Your previous extraction code", url: "", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Extraction Layer",
        description: "Build the extraction portion of your capstone",
        hints: [
          "Reuse patterns from Week 11",
          "Handle all error cases",
          "Add comprehensive logging",
          "Write tests for extraction"
        ],
        aiApproach: "Code with AI assistance. Review everything for understanding.",
        deliverable: "Working extraction layer with tests"
      }
    ],

    successCriteria: [
      "Extraction works reliably",
      "Errors handled gracefully",
      "Tests pass"
    ],

    futureProofNote: "Building from scratch with guidance is how you internalize skills. This project proves you can deliver."
  },

  {
    dayNumber: 51,
    week: 13,
    topic: "Q1 Capstone: Implementation Day 2",
    subtitle: "Build the transformation and loading layers",

    objectives: [
      "Implement data transformations",
      "Build the database schema",
      "Load data into the database",
      "Add validation throughout"
    ],

    aiIntegration: {
      toolsUsed: ['copilot', 'cursor'],
      focusArea: 'ai-review',
      aiTip: "Use AI to generate boilerplate, but design the transformations yourself based on your domain understanding.",
      warningWhenNotToUseAI: "Schema design and transformation logic should come from your understanding of the data."
    },

    sessionPlan: [
      { time: "0:00-0:30", activity: "Implement transformations", type: "exercise" },
      { time: "0:30-1:00", activity: "Build database and loading", type: "exercise" },
      { time: "1:00-1:30", activity: "Integration testing", type: "exercise" }
    ],

    resources: {
      required: [
        { title: "Your previous SQL and Python-SQL code", url: "", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Transformation and Loading",
        description: "Complete the transformation and loading layers",
        hints: [
          "Apply all relevant data transformations",
          "Validate data before loading",
          "Use appropriate bulk loading",
          "Test end-to-end pipeline"
        ],
        aiApproach: "Use AI for implementation, you design the logic.",
        deliverable: "Working transformation and loading with tests"
      }
    ],

    successCriteria: [
      "Transformations produce correct output",
      "Data loads successfully",
      "End-to-end pipeline works"
    ],

    futureProofNote: "A complete working pipeline is worth more than ten partially finished projects. Finish this one."
  },

  {
    dayNumber: 52,
    week: 13,
    topic: "Q1 Capstone: Polish and Review",
    subtitle: "Complete, document, and reflect on Q1 journey",

    objectives: [
      "Polish code to portfolio quality",
      "Write comprehensive documentation",
      "Reflect on Q1 learning",
      "Plan Q2 goals"
    ],

    aiIntegration: {
      toolsUsed: ['claude', 'chatgpt'],
      focusArea: 'ai-review',
      aiTip: "Use AI for documentation writing and code review. Get feedback on your project from multiple AI perspectives.",
      warningWhenNotToUseAI: "The reflection is yours. AI can help articulate, but the insights come from you."
    },

    sessionPlan: [
      { time: "0:00-0:30", activity: "Code polish and documentation", type: "exercise" },
      { time: "0:30-1:00", activity: "Final testing and fixes", type: "exercise" },
      { time: "1:00-1:30", activity: "Q1 reflection and Q2 planning", type: "review" }
    ],

    resources: {
      required: [
        { title: "Your complete Q1 work", url: "", type: "reference" }
      ]
    },

    exercises: [
      {
        title: "Q1 Capstone Completion",
        description: "Finish and polish your capstone project",
        hints: [
          "Run linters and formatters",
          "Complete README with setup and usage",
          "Record a demo or write a walkthrough",
          "Push to GitHub for your portfolio"
        ],
        aiApproach: "Use AI for documentation drafts. Make it your own voice.",
        deliverable: "Complete, polished capstone on GitHub"
      }
    ],

    successCriteria: [
      "Project is complete and polished",
      "Documentation is professional",
      "Code is on GitHub"
    ],

    weeklyCheckpoint: {
      title: "Q1 Complete: Python & SQL Mastery",
      description: "You've completed the foundation. You can now write production-quality Python and SQL.",
      deliverables: [
        "Complete Q1 capstone project",
        "All weekly exercises in workspace",
        "Portfolio-ready GitHub repository",
        "Q2 learning plan"
      ],
      selfAssessment: [
        "Can I build data pipelines from scratch?",
        "Is my Python code production-quality?",
        "Can I write complex analytical SQL?",
        "Am I using AI effectively without over-relying on it?"
      ]
    },

    futureProofNote: "Q1 gave you the foundation. Python and SQL skills are timeless - they'll serve you regardless of how AI tools evolve. You now understand what AI generates, not just how to use it."
  }
];

// ============================================
// END OF Q1 LESSONS
// ============================================
// Q2-Q8 lessons will be built following the same AI-enhanced pattern:
// - Q2 (Weeks 14-26): Cloud Fundamentals (AWS) & Infrastructure
// - Q3 (Weeks 27-39): Orchestration (Airflow/Dagster) & Workflow Automation
// - Q4 (Weeks 40-52): dbt & Modern Data Stack
// - Q5 (Weeks 53-65): System Design & Architecture
// - Q6 (Weeks 66-78): Data Quality & Governance
// - Q7 (Weeks 79-91): Advanced Topics & Specialization
// - Q8 (Weeks 92-104): Interview Prep & Career Launch

// Helper function to get lesson by day number
export function getLessonByDay(dayNumber: number): Lesson | undefined {
  return Q1_LESSONS.find(l => l.dayNumber === dayNumber);
}

// Get all lessons for a week
export function getLessonsByWeek(weekNumber: number): Lesson[] {
  return Q1_LESSONS.filter(l => l.week === weekNumber);
}

// Export the full curriculum
export const ALL_LESSONS: Lesson[] = [
  ...Q1_LESSONS,
];
