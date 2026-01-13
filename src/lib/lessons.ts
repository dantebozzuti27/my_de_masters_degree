// Complete Lesson Plans for 2-Year Senior Data Engineer Program
// Structured like a graduate-level curriculum with full daily lesson plans

export interface Lesson {
  dayNumber: number;
  week: number;
  topic: string;
  subtitle: string;
  
  // Learning objectives - specific, measurable outcomes
  objectives: string[];
  
  // Session structure (90 minutes total)
  sessionPlan: {
    warmup: {
      duration: number; // minutes
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
  
  // Resources
  resources: LessonResource[];
  
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
  
  // Common mistakes to avoid
  commonMistakes?: string[];
  
  // Additional notes
  instructorNotes?: string;
}

export interface LessonResource {
  title: string;
  url: string;
  type: 'video' | 'article' | 'documentation' | 'tutorial' | 'practice' | 'book' | 'course';
  duration?: string; // e.g., "15 min read", "45 min video"
  priority: 'required' | 'recommended' | 'optional';
  notes?: string;
}

export interface Exercise {
  title: string;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  estimatedTime: number; // minutes
  instructions: string[];
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

// ============================================================================
// QUARTER 1: PYTHON & SQL FOUNDATIONS (Weeks 1-13)
// ============================================================================

export const Q1_LESSONS: Lesson[] = [
  // ============================================================================
  // WEEK 1: Development Environment & Python Basics
  // ============================================================================
  {
    dayNumber: 1,
    week: 1,
    topic: "Development Environment Setup",
    subtitle: "Building Your Data Engineering Workstation",
    
    objectives: [
      "Install and configure Python 3.11+ with proper PATH settings",
      "Set up VS Code with essential Python extensions",
      "Create and activate virtual environments using venv",
      "Understand package management with pip",
      "Initialize a Git repository and make your first commit"
    ],
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Review your current development setup. What tools do you already have? What's missing?"
      },
      theory: {
        duration: 25,
        content: [
          "Why environment setup matters for data engineering",
          "Python version management and why 3.11+ is recommended",
          "Virtual environments: isolation and reproducibility",
          "Git fundamentals for version control"
        ],
        keyConceptes: [
          "PATH environment variable",
          "Virtual environment isolation",
          "pip and package dependencies",
          "Git staging and commits"
        ]
      },
      practice: {
        duration: 50,
        exercises: [
          {
            title: "Complete Python Installation",
            difficulty: "beginner",
            estimatedTime: 15,
            instructions: [
              "Download Python 3.11+ from python.org",
              "Run installer - CHECK 'Add Python to PATH'",
              "Open terminal and verify: python --version",
              "Verify pip: pip --version"
            ],
            deliverable: "Screenshot of terminal showing Python 3.11+ version"
          },
          {
            title: "VS Code Setup",
            difficulty: "beginner",
            estimatedTime: 15,
            instructions: [
              "Install VS Code from code.visualstudio.com",
              "Install extensions: Python, Pylance, GitLens",
              "Configure Python interpreter in VS Code",
              "Create a test.py file and run it"
            ],
            deliverable: "VS Code running a simple Python script"
          },
          {
            title: "Virtual Environment Creation",
            difficulty: "beginner",
            estimatedTime: 10,
            instructions: [
              "Create project folder: mkdir sde-learning && cd sde-learning",
              "Create venv: python -m venv venv",
              "Activate: source venv/bin/activate (Mac/Linux) or venv\\Scripts\\activate (Windows)",
              "Verify: which python (should point to venv)"
            ],
            deliverable: "Active virtual environment"
          },
          {
            title: "Git Repository Initialization",
            difficulty: "beginner",
            estimatedTime: 10,
            instructions: [
              "Install Git from git-scm.com if needed",
              "Configure: git config --global user.name 'Your Name'",
              "Configure: git config --global user.email 'you@example.com'",
              "In project folder: git init",
              "Create .gitignore with: venv/, __pycache__/, *.pyc",
              "git add . && git commit -m 'Initial commit'"
            ],
            deliverable: "Git repository with first commit"
          }
        ]
      },
      review: {
        duration: 10,
        activities: [
          "Verify all installations work correctly",
          "Document any issues encountered and solutions",
          "Create a README.md with your setup notes"
        ]
      }
    },
    
    resources: [
      {
        title: "Real Python: Setting Up Python",
        url: "https://realpython.com/installing-python/",
        type: "article",
        duration: "20 min read",
        priority: "required",
        notes: "Follow the section for your operating system"
      },
      {
        title: "VS Code Python Tutorial",
        url: "https://code.visualstudio.com/docs/python/python-tutorial",
        type: "documentation",
        duration: "30 min",
        priority: "required"
      },
      {
        title: "Real Python: Virtual Environments Primer",
        url: "https://realpython.com/python-virtual-environments-a-primer/",
        type: "article",
        duration: "25 min read",
        priority: "required"
      },
      {
        title: "Git Handbook",
        url: "https://guides.github.com/introduction/git-handbook/",
        type: "article",
        duration: "10 min read",
        priority: "recommended"
      }
    ],
    
    exercises: [
      {
        title: "Environment Verification Script",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Create a file called verify_setup.py",
          "Write code to print Python version, pip version, and current working directory",
          "Run the script and save the output"
        ],
        solution: `import sys
import subprocess
import os

print(f"Python Version: {sys.version}")
print(f"Python Executable: {sys.executable}")
print(f"Current Directory: {os.getcwd()}")
print(f"Virtual Env: {os.environ.get('VIRTUAL_ENV', 'Not in venv')}")

# Check pip
result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
print(f"Pip: {result.stdout.strip()}")`,
        deliverable: "verify_setup.py committed to your repository"
      }
    ],
    
    successCriteria: [
      "Python 3.11+ runs from terminal with 'python --version'",
      "VS Code opens Python files with syntax highlighting",
      "Virtual environment activates without errors",
      "Git repository created with .gitignore and initial commit",
      "verify_setup.py runs successfully"
    ],
    
    workApplication: "Document your current work database connection patterns. How do you connect to databases? What tools do you use? This will be valuable context as we build data pipelines.",
    
    keyTerms: [
      { term: "PATH", definition: "Environment variable that tells your OS where to find executable programs" },
      { term: "Virtual Environment", definition: "Isolated Python installation with its own packages, separate from system Python" },
      { term: "pip", definition: "Python's package installer - used to install libraries from PyPI" },
      { term: "Git", definition: "Distributed version control system for tracking code changes" }
    ],
    
    commonMistakes: [
      "Forgetting to check 'Add Python to PATH' during installation",
      "Not activating virtual environment before installing packages",
      "Installing packages globally instead of in venv",
      "Committing venv folder to git (should be in .gitignore)"
    ]
  },
  
  // Day 2
  {
    dayNumber: 2,
    week: 1,
    topic: "Python Syntax Fundamentals",
    subtitle: "Variables, Data Types, and Basic Operations",
    
    objectives: [
      "Declare and use variables with proper naming conventions",
      "Work with Python's core data types: int, float, str, bool",
      "Perform arithmetic and comparison operations",
      "Use print() for output and input() for user input",
      "Write and run Python scripts from the command line"
    ],
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Open VS Code, activate your virtual environment, create a new file called day2_basics.py"
      },
      theory: {
        duration: 20,
        content: [
          "Python as a dynamically typed language",
          "Variable naming conventions (snake_case)",
          "Immutable vs mutable types preview",
          "Type inference and type checking"
        ],
        keyConceptes: [
          "Dynamic typing",
          "Variable assignment",
          "Type conversion (casting)",
          "String formatting"
        ]
      },
      practice: {
        duration: 55,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review code written today",
          "Commit changes to git",
          "Note any concepts that need more practice"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Official Tutorial: Chapters 1-3",
        url: "https://docs.python.org/3/tutorial/introduction.html",
        type: "documentation",
        duration: "30 min read",
        priority: "required",
        notes: "This is THE authoritative source - bookmark it"
      },
      {
        title: "Corey Schafer: Python Basics Playlist",
        url: "https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU",
        type: "video",
        duration: "Watch videos 1-5 (~45 min)",
        priority: "required",
        notes: "Excellent visual explanations, watch at 1.25x speed"
      },
      {
        title: "Real Python: Variables",
        url: "https://realpython.com/python-variables/",
        type: "article",
        duration: "15 min read",
        priority: "recommended"
      }
    ],
    
    exercises: [
      {
        title: "Variable Declaration Practice",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Create variables for: your name, age, height (as float), is_student (boolean)",
          "Print each variable with a descriptive label",
          "Use type() to check the type of each variable"
        ],
        solution: `# Variable declarations
name = "Dante"
age = 28
height = 5.9
is_student = True

# Print with labels
print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Student: {is_student} (type: {type(is_student).__name__})")`,
        deliverable: "variables.py with all variable types demonstrated"
      },
      {
        title: "Arithmetic Operations",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Create two number variables",
          "Perform and print: addition, subtraction, multiplication, division",
          "Demonstrate integer division (//) and modulo (%)",
          "Show exponentiation (**)"
        ],
        solution: `a = 17
b = 5

print(f"{a} + {b} = {a + b}")      # Addition: 22
print(f"{a} - {b} = {a - b}")      # Subtraction: 12
print(f"{a} * {b} = {a * b}")      # Multiplication: 85
print(f"{a} / {b} = {a / b}")      # Division: 3.4
print(f"{a} // {b} = {a // b}")    # Integer Division: 3
print(f"{a} % {b} = {a % b}")      # Modulo: 2
print(f"{a} ** {b} = {a ** b}")    # Exponentiation: 1419857`
      },
      {
        title: "String Operations",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Create a string with your full name",
          "Print it in uppercase, lowercase, and title case",
          "Extract your first name using slicing",
          "Concatenate strings using + and f-strings",
          "Find the length of your name"
        ],
        solution: `full_name = "dante bozzuti"

# Case methods
print(full_name.upper())      # DANTE BOZZUTI
print(full_name.lower())      # dante bozzuti
print(full_name.title())      # Dante Bozzuti

# Slicing (get first name - up to space)
space_index = full_name.index(" ")
first_name = full_name[:space_index]
print(f"First name: {first_name}")

# Concatenation
greeting = "Hello, " + first_name + "!"
print(greeting)

# f-string (preferred method)
print(f"Welcome, {first_name.title()}! Your name has {len(full_name)} characters.")`
      },
      {
        title: "User Input Calculator",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Prompt user for two numbers using input()",
          "Convert inputs to floats",
          "Calculate and display sum, difference, product, quotient",
          "Handle the case where user might divide by zero"
        ],
        solution: `# Simple calculator with user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\\n{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Cannot divide by zero!")`,
        hints: [
          "input() always returns a string - you need to convert it",
          "Use float() for decimal numbers, int() for whole numbers"
        ]
      },
      {
        title: "Exercism: 10 Basic Exercises",
        difficulty: "beginner",
        estimatedTime: 30,
        instructions: [
          "Go to https://exercism.org/tracks/python",
          "Create a free account if you don't have one",
          "Complete these exercises: Hello World, Lasagna, Guido's Gorgeous Lasagna",
          "Read the instructions carefully and submit solutions"
        ],
        deliverable: "Complete at least 3 Exercism exercises"
      }
    ],
    
    successCriteria: [
      "Can declare variables of all basic types without errors",
      "Understands the difference between = (assignment) and == (comparison)",
      "Can use f-strings for formatted output",
      "Can convert between types using int(), float(), str()",
      "Completed at least 3 Exercism exercises"
    ],
    
    keyTerms: [
      { term: "Variable", definition: "A named reference to a value stored in memory" },
      { term: "Data Type", definition: "Classification of data that tells Python what operations can be performed" },
      { term: "String", definition: "A sequence of characters, created with quotes (single, double, or triple)" },
      { term: "f-string", definition: "Formatted string literal (f'...') that allows embedding expressions inside strings" },
      { term: "Type Casting", definition: "Converting a value from one type to another (e.g., int('5') → 5)" }
    ],
    
    commonMistakes: [
      "Using reserved keywords as variable names (e.g., print, list, type)",
      "Forgetting that input() returns a string, not a number",
      "Using single = when you mean == for comparison",
      "Not closing string quotes properly"
    ]
  },
  
  // Day 3
  {
    dayNumber: 3,
    week: 1,
    topic: "Control Flow & Functions",
    subtitle: "Making Decisions and Creating Reusable Code",
    
    objectives: [
      "Write conditional statements using if, elif, and else",
      "Create loops using for and while",
      "Define functions with parameters and return values",
      "Understand variable scope (local vs global)",
      "Use the range() function effectively"
    ],
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Write a simple program that checks if a number is positive, negative, or zero - use what you remember before looking anything up"
      },
      theory: {
        duration: 25,
        content: [
          "Boolean logic and comparison operators",
          "Truthy and falsy values in Python",
          "Loop control: break, continue, pass",
          "Function design principles"
        ],
        keyConceptes: [
          "Conditional execution",
          "Iteration",
          "Function abstraction",
          "DRY principle (Don't Repeat Yourself)"
        ]
      },
      practice: {
        duration: 50,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Review all functions written today",
          "Add docstrings to your functions",
          "Commit to git with message 'Add control flow and functions'"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Tutorial: Control Flow",
        url: "https://docs.python.org/3/tutorial/controlflow.html",
        type: "documentation",
        duration: "25 min read",
        priority: "required"
      },
      {
        title: "Corey Schafer: Functions",
        url: "https://www.youtube.com/watch?v=9Os0o3wzS_I",
        type: "video",
        duration: "21 min",
        priority: "required"
      },
      {
        title: "Corey Schafer: Loops",
        url: "https://www.youtube.com/watch?v=6iF8Xb7Z3wQ",
        type: "video",
        duration: "11 min",
        priority: "required"
      },
      {
        title: "Real Python: Defining Functions",
        url: "https://realpython.com/defining-your-own-python-functions/",
        type: "article",
        duration: "30 min read",
        priority: "recommended"
      }
    ],
    
    exercises: [
      {
        title: "FizzBuzz",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Write a function fizzbuzz(n) that prints numbers 1 to n",
          "For multiples of 3, print 'Fizz' instead of the number",
          "For multiples of 5, print 'Buzz'",
          "For multiples of both 3 and 5, print 'FizzBuzz'",
          "This is THE classic programming interview warm-up!"
        ],
        solution: `def fizzbuzz(n):
    """Print FizzBuzz sequence from 1 to n."""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Test it
fizzbuzz(15)`,
        hints: [
          "Check for divisibility by both 3 AND 5 first",
          "Use the modulo operator % to check divisibility"
        ]
      },
      {
        title: "Factorial Function",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Write a function factorial(n) that returns n!",
          "factorial(5) should return 120 (5 * 4 * 3 * 2 * 1)",
          "Handle edge case: factorial(0) = 1",
          "Try both iterative and recursive approaches"
        ],
        solution: `# Iterative approach
def factorial_iterative(n):
    """Calculate factorial using a loop."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Test both
print(factorial_iterative(5))  # 120
print(factorial_recursive(5))  # 120`
      },
      {
        title: "Prime Number Checker",
        difficulty: "intermediate",
        estimatedTime: 15,
        instructions: [
          "Write a function is_prime(n) that returns True if n is prime",
          "A prime number is only divisible by 1 and itself",
          "Optimize: only check up to square root of n"
        ],
        solution: `def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd numbers up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
for num in range(20):
    if is_prime(num):
        print(f"{num} is prime")`
      },
      {
        title: "Number Guessing Game",
        difficulty: "beginner",
        estimatedTime: 20,
        instructions: [
          "Create a game where the computer picks a random number 1-100",
          "Player guesses until they get it right",
          "Provide 'higher' or 'lower' hints",
          "Track and display number of guesses at the end"
        ],
        solution: `import random

def guessing_game():
    """Play a number guessing game."""
    secret = random.randint(1, 100)
    guesses = 0
    
    print("I'm thinking of a number between 1 and 100...")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            guesses += 1
            
            if guess < secret:
                print("Higher!")
            elif guess > secret:
                print("Lower!")
            else:
                print(f"Correct! You got it in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

# guessing_game()  # Uncomment to play`
      },
      {
        title: "Temperature Converter Functions",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Write celsius_to_fahrenheit(c) and fahrenheit_to_celsius(f)",
          "F = C * 9/5 + 32",
          "C = (F - 32) * 5/9",
          "Create a main function that demonstrates both"
        ],
        solution: `def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    # Test conversions
    temps_c = [0, 20, 37, 100]
    for c in temps_c:
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.1f}°F")
    
    print()
    
    temps_f = [32, 68, 98.6, 212]
    for f in temps_f:
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.1f}°C")

if __name__ == "__main__":
    main()`
      }
    ],
    
    successCriteria: [
      "Can write if/elif/else statements without syntax errors",
      "Understands the difference between for and while loops",
      "Can define functions with parameters and return values",
      "FizzBuzz works correctly for any input",
      "All functions have docstrings"
    ],
    
    keyTerms: [
      { term: "Conditional", definition: "Code that executes only when a condition is True" },
      { term: "Iteration", definition: "Repeating a block of code multiple times" },
      { term: "Function", definition: "A reusable block of code that performs a specific task" },
      { term: "Parameter", definition: "A variable in a function definition that receives a value when called" },
      { term: "Return Value", definition: "The value a function sends back to the caller" },
      { term: "Scope", definition: "The region of code where a variable is accessible" }
    ],
    
    commonMistakes: [
      "Forgetting the colon : after if, elif, else, for, while, def",
      "Incorrect indentation (Python requires consistent indentation)",
      "Infinite loops - forgetting to update the loop variable",
      "Returning inside a loop when you meant to just break"
    ]
  },
  
  // Day 4
  {
    dayNumber: 4,
    week: 1,
    topic: "Data Types Deep Dive",
    subtitle: "Lists, Tuples, Dictionaries, and Sets",
    
    objectives: [
      "Create and manipulate lists with indexing and slicing",
      "Understand tuple immutability and use cases",
      "Build dictionaries for key-value data storage",
      "Use sets for unique collections and set operations",
      "Choose the right data structure for different problems"
    ],
    
    sessionPlan: {
      warmup: {
        duration: 5,
        activity: "Think of a real-world example for each: when would you use a list vs a dictionary? Write down your thoughts."
      },
      theory: {
        duration: 25,
        content: [
          "Mutable vs Immutable data structures",
          "Time complexity of common operations",
          "When to use each data structure",
          "Nested data structures"
        ],
        keyConceptes: [
          "Mutability",
          "Indexing (0-based)",
          "Slicing syntax [start:end:step]",
          "Hashing and hashability"
        ]
      },
      practice: {
        duration: 50,
        exercises: []
      },
      review: {
        duration: 10,
        activities: [
          "Create a cheat sheet for data structure methods",
          "Commit all code to git",
          "Review Week 1 concepts"
        ]
      }
    },
    
    resources: [
      {
        title: "Python Tutorial: Data Structures",
        url: "https://docs.python.org/3/tutorial/datastructures.html",
        type: "documentation",
        duration: "30 min read",
        priority: "required"
      },
      {
        title: "Corey Schafer: Lists, Tuples, Sets",
        url: "https://www.youtube.com/watch?v=W8KRzm-HUcc",
        type: "video",
        duration: "29 min",
        priority: "required"
      },
      {
        title: "Corey Schafer: Dictionaries",
        url: "https://www.youtube.com/watch?v=daefaLgNkw0",
        type: "video",
        duration: "15 min",
        priority: "required"
      },
      {
        title: "Real Python: Lists and Tuples",
        url: "https://realpython.com/python-lists-tuples/",
        type: "article",
        duration: "25 min read",
        priority: "recommended"
      }
    ],
    
    exercises: [
      {
        title: "List Operations Practice",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Create a list of 10 numbers",
          "Print: first element, last element, middle 3 elements",
          "Add a number to the end, insert one at position 3",
          "Remove an element by value, remove by index",
          "Sort the list in ascending and descending order",
          "Create a copy and reverse it"
        ],
        solution: `numbers = [5, 2, 8, 1, 9, 4, 7, 3, 6, 0]

# Accessing elements
print(f"First: {numbers[0]}")           # 5
print(f"Last: {numbers[-1]}")           # 0
print(f"Middle 3: {numbers[3:6]}")      # [1, 9, 4]

# Adding elements
numbers.append(10)                       # Add to end
numbers.insert(3, 99)                    # Insert at index 3
print(f"After adding: {numbers}")

# Removing elements
numbers.remove(99)                       # Remove by value
popped = numbers.pop(0)                  # Remove by index
print(f"Popped: {popped}, List: {numbers}")

# Sorting
numbers.sort()
print(f"Ascending: {numbers}")
numbers.sort(reverse=True)
print(f"Descending: {numbers}")

# Copying and reversing
numbers_copy = numbers.copy()
numbers_copy.reverse()
print(f"Original: {numbers}")
print(f"Reversed copy: {numbers_copy}")`
      },
      {
        title: "Dictionary for Data Storage",
        difficulty: "beginner",
        estimatedTime: 15,
        instructions: [
          "Create a dictionary representing a database record (user profile)",
          "Include: name, email, age, skills (as a list), active (boolean)",
          "Access and modify values",
          "Add a new key-value pair",
          "Iterate over keys, values, and items",
          "Check if a key exists before accessing"
        ],
        solution: `# User profile as a dictionary
user = {
    "name": "Dante Bozzuti",
    "email": "dante@example.com",
    "age": 28,
    "skills": ["SQL", "Excel", "Tableau"],
    "active": True
}

# Accessing values
print(f"Name: {user['name']}")
print(f"Skills: {', '.join(user['skills'])}")

# Modifying values
user["age"] = 29
user["skills"].append("Python")

# Adding new key
user["title"] = "Data Engineer"

# Safe access with .get()
phone = user.get("phone", "Not provided")
print(f"Phone: {phone}")

# Iterating
print("\\nAll user data:")
for key, value in user.items():
    print(f"  {key}: {value}")

# Check key exists
if "email" in user:
    print(f"\\nEmail is: {user['email']}")`
      },
      {
        title: "Set Operations",
        difficulty: "beginner",
        estimatedTime: 10,
        instructions: [
          "Create two sets of programming languages you know and want to learn",
          "Find: union, intersection, difference",
          "Check if one is a subset/superset of another",
          "Use sets to remove duplicates from a list"
        ],
        solution: `# Programming language sets
known = {"Python", "SQL", "JavaScript"}
want_to_learn = {"Python", "Go", "Rust", "SQL"}

# Set operations
print(f"All languages: {known | want_to_learn}")           # Union
print(f"Already know: {known & want_to_learn}")            # Intersection
print(f"Still need to learn: {want_to_learn - known}")     # Difference
print(f"Unique to me: {known ^ want_to_learn}")            # Symmetric diff

# Remove duplicates from list
data_with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_data = list(set(data_with_dupes))
print(f"Original: {data_with_dupes}")
print(f"Unique: {unique_data}")`
      },
      {
        title: "Nested Data Structure",
        difficulty: "intermediate",
        estimatedTime: 20,
        instructions: [
          "Create a list of dictionaries representing database tables",
          "Each dict has: table_name, columns (list), row_count, last_updated",
          "Write functions to: find table by name, get total rows, list all table names",
          "This pattern is common in data engineering!"
        ],
        solution: `# Database schema as nested data structure
database = [
    {
        "table_name": "users",
        "columns": ["id", "name", "email", "created_at"],
        "row_count": 150000,
        "last_updated": "2026-01-12"
    },
    {
        "table_name": "orders",
        "columns": ["id", "user_id", "total", "status", "created_at"],
        "row_count": 500000,
        "last_updated": "2026-01-12"
    },
    {
        "table_name": "products",
        "columns": ["id", "name", "price", "category"],
        "row_count": 5000,
        "last_updated": "2026-01-10"
    }
]

def find_table(db, name):
    """Find table by name, return None if not found."""
    for table in db:
        if table["table_name"] == name:
            return table
    return None

def get_total_rows(db):
    """Calculate total rows across all tables."""
    return sum(table["row_count"] for table in db)

def list_table_names(db):
    """Return list of all table names."""
    return [table["table_name"] for table in db]

# Usage
print(f"Tables: {list_table_names(database)}")
print(f"Total rows: {get_total_rows(database):,}")

users_table = find_table(database, "users")
if users_table:
    print(f"Users columns: {users_table['columns']}")`
      }
    ],
    
    successCriteria: [
      "Can create and manipulate all 4 data structures",
      "Understands when to use list vs tuple vs dict vs set",
      "Can work with nested data structures",
      "Code is committed to git with good commit message"
    ],
    
    weeklyCheckpoint: {
      title: "Week 1 Checkpoint: GitHub Repository",
      description: "Your learning journey should be tracked in version control from day one.",
      deliverables: [
        "GitHub account created",
        "sde-learning repository initialized locally",
        "At least 4 commits (one per day)",
        "README.md with your learning goals",
        ".gitignore properly configured",
        "All exercises from Week 1 in organized folders"
      ],
      selfAssessment: [
        "Can I explain what a virtual environment is and why we use it?",
        "Can I write a function from scratch without looking at examples?",
        "Do I know when to use a list vs a dictionary?",
        "Have I completed at least 5 Exercism exercises?"
      ]
    },
    
    keyTerms: [
      { term: "List", definition: "Ordered, mutable collection - use for sequences of similar items" },
      { term: "Tuple", definition: "Ordered, immutable collection - use for fixed data like coordinates" },
      { term: "Dictionary", definition: "Unordered key-value pairs - use for named/labeled data" },
      { term: "Set", definition: "Unordered unique elements - use for membership testing and deduplication" },
      { term: "Mutable", definition: "Can be changed after creation (lists, dicts, sets)" },
      { term: "Immutable", definition: "Cannot be changed after creation (strings, tuples, numbers)" }
    ],
    
    commonMistakes: [
      "Modifying a list while iterating over it",
      "Using a list when a set would be more efficient for lookups",
      "Forgetting that dict keys must be immutable (can't use lists as keys)",
      "Confusing list.append() (one item) with list.extend() (multiple items)"
    ]
  }
];

// Continue with more lessons...
// This structure continues for all 416 days

// Helper function to get lesson by day number
export function getLessonByDay(dayNumber: number): Lesson | undefined {
  // For now, return from Q1 lessons
  return Q1_LESSONS.find(l => l.dayNumber === dayNumber);
}

// Get all lessons for a week
export function getLessonsByWeek(weekNumber: number): Lesson[] {
  return Q1_LESSONS.filter(l => l.week === weekNumber);
}

// Export the full curriculum (will be expanded)
export const ALL_LESSONS: Lesson[] = [
  ...Q1_LESSONS,
  // Q2_LESSONS will be added
  // Q3_LESSONS will be added
  // etc.
];
