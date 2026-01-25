#!/usr/bin/env python3
"""
Day 14: Week 2 Review & Week 3 Prep
====================================
Duration: 3-4 hours (Sunday)

REVIEW what you learned, CATCH UP on anything incomplete, and PREVIEW Week 3.

COMPLETION: Delete the marker below when review is complete.
"""

def week2_complete():
    """Marker function indicating Week 2 review is complete."""
    return True  # Week 2 review completed

# =============================================================================
# WEEK 2 REVIEW CHECKLIST
# =============================================================================
"""
Check off each item you're confident with:

ERROR HANDLING (Day 8):
[x] try/except/finally blocks
[x] Raising exceptions with raise
[x] Custom exception classes
[x] Exception chaining (from e)
[x] Defensive coding patterns
[x] Input validation

PYTHON OOP (Day 9):
[x] Classes with __init__, __str__, __repr__
[x] Properties with @property decorator
[x] Class methods with @classmethod (alternative constructors)
[x] Static methods with @staticmethod (utility functions)
[x] Composition over inheritance ("has-a" relationships)
[x] Data validation patterns

LOGGING & CONFIGURATION (Day 10):
[x] Python logging module (Logger, Handler, Formatter)
[x] Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
[x] Structured logging (JSON format)
[x] Environment variable configuration
[x] Config file loading and merging
[x] Configurable pipeline pattern

GIT FUNDAMENTALS (Day 11):
[x] git init, add, commit
[x] Branching (checkout -b, branch, switch)
[x] Merging branches
[x] Commit message best practices (Add:, Fix:, Update:)
[x] Viewing history (log, show, blame)
[x] Undoing changes (restore, reset, amend)
[x] Stashing work

GITHUB PRs (Day 12):
[x] Creating pull requests
[x] Code review process
[x] GitHub Issues
[x] Branch protection (concept)

CLI PROJECT (Day 13):
[x] Combined OOP, logging, config, git workflow
[x] argparse for CLI interfaces
[x] File readers/writers
[x] Data validation and transformation
"""

# =============================================================================
# QUICK SELF-TEST
# =============================================================================

def week2_quiz():
    """
    Quick quiz to test your understanding.
    Run this and answer in your head before checking.
    """
    questions = [
        {
            "q": "What's the difference between @property and @classmethod?",
            "a": "@property creates a computed attribute accessed like obj.prop. "
                 "@classmethod receives the class (cls) and can create instances."
        },
        {
            "q": "When would you use DEBUG vs INFO log level?",
            "a": "DEBUG for detailed diagnostic info during development. "
                 "INFO for normal operation milestones in production."
        },
        {
            "q": "What does 'git stash' do?",
            "a": "Temporarily saves uncommitted changes so you can switch branches, "
                 "then 'git stash pop' restores them."
        },
        {
            "q": "Why use environment variables for configuration?",
            "a": "Secrets shouldn't be in code/git. Different environments (dev/prod) "
                 "need different values. 12-factor app principle."
        },
        {
            "q": "What's composition over inheritance?",
            "a": "Instead of class A extending class B, class A 'has-a' instance of B. "
                 "More flexible and easier to change."
        },
        {
            "q": "What makes a good commit message?",
            "a": "Type prefix (Add:, Fix:), short description of WHAT, "
                 "optional body explaining WHY."
        },
        {
            "q": "When should you NOT use git commit --amend?",
            "a": "Never amend commits that have already been pushed to a shared branch. "
                 "It rewrites history and causes conflicts for others."
        },
        {
            "q": "What's the purpose of a Pull Request?",
            "a": "Code review before merging. Catches bugs, shares knowledge, "
                 "maintains code quality. Required at most companies."
        }
    ]
    
    print("=" * 60)
    print("WEEK 2 QUICK QUIZ")
    print("=" * 60)
    print("\nAnswer each question in your head, then press Enter to see the answer.\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        input("\n[Press Enter for answer...]")
        print(f"A: {q['a']}\n")
        print("-" * 40 + "\n")
    
    print("Quiz complete! Review any topics you weren't sure about.\n")


# =============================================================================
# CATCH-UP TASKS
# =============================================================================
"""
If you didn't complete any of these, do them now:

1. Day 9: Run tests in day9_classes_oop.py - all should pass
2. Day 10: Run tests in day10_logging_config.py - all should pass
3. Day 11: Complete all git exercises in a practice repo
4. Day 12: Create at least one PR on GitHub
5. Day 13: Get the CLI tool working with at least 5 tests passing
"""


# =============================================================================
# WEEK 3 PREVIEW
# =============================================================================
"""
WEEK 3: Advanced Git + AWS + Docker

Day 15 (Mon): Advanced Git - rebasing, cherry-pick, bisect
Day 16 (Tue): AWS Account Setup - IAM, CLI, security
Day 17 (Wed): S3 Fundamentals - buckets, storage classes, lifecycle
Day 18 (Thu): Docker Fundamentals - images, containers, Dockerfile
Day 19 (Fri): Docker for Data Engineering - compose, volumes, networking
Day 20 (Sat): Project - Containerized data pipeline
Day 21 (Sun): Review + Week 4 planning

PREPARATION:
- Make sure you have an AWS account (free tier is fine)
- Install Docker Desktop: https://www.docker.com/products/docker-desktop/
- Install AWS CLI: https://aws.amazon.com/cli/
"""


# =============================================================================
# REFLECTION
# =============================================================================

def week2_reflection():
    """
    Guided reflection on your Week 2 learning.
    """
    print("=" * 60)
    print("WEEK 2 REFLECTION")
    print("=" * 60)
    
    prompts = [
        "What was the most challenging concept this week?",
        "What concept 'clicked' for you this week?",
        "How confident are you with Git workflow (1-10)?",
        "What would you do differently next week?",
        "What are you most excited to learn in Week 3?"
    ]
    
    print("\nTake a moment to reflect on each prompt:\n")
    for i, prompt in enumerate(prompts, 1):
        print(f"{i}. {prompt}")
        input("   [Your answer, then press Enter] ")
        print()
    
    print("Reflection complete! You've finished Week 2. 🎉\n")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║           DAY 14: WEEK 2 REVIEW                          ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║  Options:                                                ║
    ║  1. Take the quick quiz                                  ║
    ║  2. Week 2 reflection                                    ║
    ║  3. Both                                                 ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)
    
    choice = input("Enter choice (1/2/3): ").strip()
    
    if choice == "1":
        week2_quiz()
    elif choice == "2":
        week2_reflection()
    elif choice == "3":
        week2_quiz()
        week2_reflection()
    else:
        print("Invalid choice. Run again with 1, 2, or 3.")


if __name__ == "__main__":
    main()
