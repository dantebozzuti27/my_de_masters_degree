#!/usr/bin/env python3
"""
Day 15: Advanced Git + Code Review Practice
============================================
Duration: 2-2.5 hours

Deep dive into Git workflows, history rewriting, and code review skills.
This builds on Days 11-12 to make you truly proficient.

WHY THIS MATTERS:
- Senior engineers rewrite history confidently
- Good code review skills are highly valued
- Git mastery = faster, cleaner workflows
- This is what separates juniors from seniors

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import subprocess
import os
from typing import List, Dict, Optional, Tuple

# =============================================================================
# GIT ADVANCED EXERCISES (Do these in terminal)
# =============================================================================

"""
EXERCISE 1: Interactive Rebase (20 min)
=======================================

Interactive rebase lets you rewrite commit history:
- Reorder commits
- Squash multiple commits into one
- Edit commit messages
- Drop commits entirely

Setup (create commits to practice with):
  mkdir rebase-practice && cd rebase-practice
  git init
  
  echo "v1" > file.txt && git add . && git commit -m "Add file"
  echo "v2" > file.txt && git add . && git commit -m "typo in message"
  echo "v3" > file.txt && git add . && git commit -m "Fix the typo"
  echo "v4" > file.txt && git add . && git commit -m "Add feature X"
  echo "v5" > file.txt && git add . && git commit -m "WIP"
  echo "v6" > file.txt && git add . && git commit -m "Finish feature X"

Now practice:
  git log --oneline  # See your commits

Interactive rebase the last 5 commits:
  git rebase -i HEAD~5

In the editor:
  pick abc1234 typo in message    → reword abc1234 typo in message
  pick def5678 Fix the typo       → fixup def5678 Fix the typo  
  pick ghi9012 Add feature X      → pick ghi9012 Add feature X
  pick jkl3456 WIP                → squash jkl3456 WIP
  pick mno7890 Finish feature X   → squash mno7890 Finish feature X

Commands:
  pick   = use commit as-is
  reword = use commit but edit message
  squash = meld into previous commit (keep message)
  fixup  = meld into previous but discard message
  drop   = remove commit entirely

After saving:
  git log --oneline  # Should be cleaner!

WARNING: NEVER rebase commits that have been pushed to a shared branch!


EXERCISE 2: Git Bisect (20 min)
===============================

Git bisect uses binary search to find which commit introduced a bug.

Setup (create a repo with a "bug"):
  mkdir bisect-practice && cd bisect-practice
  git init
  
  for i in {1..20}; do
    if [ $i -eq 12 ]; then
      echo "BUG" > code.txt  # The bug!
    else
      echo "GOOD version $i" > code.txt
    fi
    git add . && git commit -m "Commit $i"
  done

Now find the bug:
  git bisect start
  git bisect bad           # Current commit is bad
  git bisect good HEAD~15  # 15 commits ago was good

Git will checkout a commit. Test it:
  cat code.txt
  # If it says "BUG": git bisect bad
  # If it says "GOOD": git bisect good

Repeat until git tells you the first bad commit!

When done:
  git bisect reset


EXERCISE 3: Cherry-pick & Revert (20 min)
==========================================

Cherry-pick applies a specific commit to your current branch.
Revert creates a new commit that undoes a previous commit.

Setup:
  mkdir cherrypick-practice && cd cherrypick-practice
  git init
  
  echo "v1" > main.txt && git add . && git commit -m "Initial"
  
  # Create a feature branch
  git checkout -b feature
  echo "feature work" > feature.txt && git add . && git commit -m "Add feature"
  echo "more feature" >> feature.txt && git add . && git commit -m "Extend feature"
  
  # Go back to main
  git checkout main
  echo "v2" > main.txt && git add . && git commit -m "Update main"

Cherry-pick just the first feature commit:
  git log feature --oneline  # Find the commit hash
  git cherry-pick <hash>     # Apply just that commit to main
  git log --oneline          # See it's now on main

Revert a commit (safely undo):
  git revert HEAD            # Creates a new commit undoing the last one
  git log --oneline          # See the revert commit


EXERCISE 4: Pre-commit Hooks (20 min)
=====================================

Pre-commit hooks run checks before each commit.

1. Install pre-commit:
   pip install pre-commit

2. Create .pre-commit-config.yaml:
   repos:
     - repo: https://github.com/psf/black
       rev: 23.12.1
       hooks:
         - id: black
     
     - repo: https://github.com/pycqa/flake8
       rev: 6.1.0
       hooks:
         - id: flake8
     
     - repo: https://github.com/pre-commit/pre-commit-hooks
       rev: v4.5.0
       hooks:
         - id: trailing-whitespace
         - id: end-of-file-fixer
         - id: check-yaml
         - id: check-added-large-files

3. Install the hooks:
   pre-commit install

4. Test it:
   # Create a file with formatting issues
   echo "x=1" > bad.py
   git add bad.py
   git commit -m "Test"
   # Pre-commit will reformat and block the commit!
   
   # Check the reformatted file
   cat bad.py  # Now properly formatted
   git add bad.py
   git commit -m "Test"  # Now it passes!


EXERCISE 5: Code Review Practice (20 min)
==========================================

Go to GitHub and find an open source project to practice reviewing.

Good repos for practice:
- https://github.com/psf/black/pulls
- https://github.com/apache/airflow/pulls
- https://github.com/dbt-labs/dbt-core/pulls

For each PR:
1. Read the description - does it explain WHY?
2. Look at the files changed
3. Think: "What questions would I ask?"
4. Think: "What could go wrong?"
5. Think: "Is there a simpler way?"

Write out (don't post!) 3 review comments:
- One question asking for clarification
- One suggestion for improvement
- One piece of positive feedback

Review Comment Templates:

QUESTION:
"Could you help me understand why [X]? I'm wondering if [Y] 
would also work, or if there's a reason this approach is better."

SUGGESTION:
"Consider using [X] here instead of [Y] - it would [benefit].
Not blocking, just a thought!"

POSITIVE:
"Nice! I like how you [specific thing]. This is much cleaner than
the previous approach."


EXERCISE 6: Self-Review (30 min)
=================================

Review your own code from this week's work.

1. Open your Git history:
   git log --oneline -10

2. Pick a commit and review it:
   git show <hash>

3. Ask yourself:
   - Is this commit focused on one thing?
   - Is the message clear?
   - Would I understand this in 6 months?
   - Are there any bugs I missed?
   - Is there duplicate code?
   - Are variable names clear?

4. Create a new branch and fix any issues:
   git checkout -b refactor/week2-cleanup
   # Make improvements
   git add . && git commit -m "Refactor: clean up week 2 code
   
   - Improved variable names
   - Added docstrings
   - Removed duplicate code"
   
5. Merge it back:
   git checkout main
   git merge refactor/week2-cleanup
"""

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def run_git(command: str, cwd: Optional[str] = None) -> Tuple[bool, str]:
    """Run a git command and return (success, output)."""
    try:
        result = subprocess.run(
            command.split(),
            capture_output=True,
            text=True,
            cwd=cwd
        )
        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)


def check_rebase_skills(repo_path: str = ".") -> Dict:
    """Check if user has done interactive rebase practice."""
    result = {
        "has_squashed_commits": False,
        "has_rebased": False,
        "commit_messages_clean": False
    }
    
    # Check reflog for rebase evidence
    success, output = run_git("git reflog", repo_path)
    if success:
        result["has_rebased"] = "rebase" in output.lower()
    
    # Check for clean commit messages (no WIP, fixup, etc.)
    success, output = run_git("git log --oneline -20", repo_path)
    if success:
        bad_patterns = ["wip", "fixup", "squash", "temp", "xxx"]
        lines = output.lower().split("\n")
        bad_count = sum(1 for line in lines if any(p in line for p in bad_patterns))
        result["commit_messages_clean"] = bad_count == 0
    
    return result


def check_precommit_setup(repo_path: str = ".") -> bool:
    """Check if pre-commit is set up."""
    config_path = os.path.join(repo_path, ".pre-commit-config.yaml")
    return os.path.exists(config_path)


# =============================================================================
# CODE REVIEW CHECKLIST
# =============================================================================

CODE_REVIEW_CHECKLIST = """
╔══════════════════════════════════════════════════════════════╗
║                    CODE REVIEW CHECKLIST                      ║
╠══════════════════════════════════════════════════════════════╣
║ FUNCTIONALITY                                                 ║
║ [ ] Does the code do what it's supposed to do?               ║
║ [ ] Are edge cases handled?                                   ║
║ [ ] Is error handling appropriate?                            ║
║                                                               ║
║ READABILITY                                                   ║
║ [ ] Are variable/function names clear?                        ║
║ [ ] Is the code self-documenting?                             ║
║ [ ] Are comments useful (explain WHY, not WHAT)?              ║
║                                                               ║
║ DESIGN                                                        ║
║ [ ] Is the code DRY (Don't Repeat Yourself)?                  ║
║ [ ] Are functions small and focused?                          ║
║ [ ] Is the abstraction level consistent?                      ║
║                                                               ║
║ TESTING                                                       ║
║ [ ] Are there tests for new functionality?                    ║
║ [ ] Do tests cover edge cases?                                ║
║ [ ] Are tests readable and maintainable?                      ║
║                                                               ║
║ SECURITY                                                      ║
║ [ ] No hardcoded secrets?                                     ║
║ [ ] No sensitive data in logs?                                ║
║ [ ] Input validated where needed?                             ║
╚══════════════════════════════════════════════════════════════╝
"""

# =============================================================================
# QUIZ
# =============================================================================

def advanced_git_quiz() -> None:
    """Test your advanced Git knowledge."""
    questions = [
        {
            "q": "When should you NEVER use git rebase?",
            "options": [
                "On your local feature branch",
                "On commits that have been pushed to a shared branch",
                "When you have merge conflicts",
                "Before opening a PR"
            ],
            "answer": 1,
            "explanation": "Never rebase commits others may have based work on. It rewrites history and causes problems for collaborators."
        },
        {
            "q": "What does 'git bisect' help you do?",
            "options": [
                "Split a commit in two",
                "Find which commit introduced a bug",
                "Merge two branches",
                "Delete old commits"
            ],
            "answer": 1,
            "explanation": "Bisect uses binary search to efficiently find the commit that introduced a bug."
        },
        {
            "q": "What's the difference between 'squash' and 'fixup' in interactive rebase?",
            "options": [
                "No difference",
                "Squash keeps both messages, fixup discards the message",
                "Fixup keeps both messages, squash discards",
                "Squash is faster"
            ],
            "answer": 1,
            "explanation": "Squash combines commits and lets you edit the combined message. Fixup combines but discards the fixup commit's message."
        },
        {
            "q": "What happens when you 'git cherry-pick' a commit?",
            "options": [
                "Moves the commit to current branch",
                "Copies the commit to current branch",
                "Deletes the commit",
                "Reverts the commit"
            ],
            "answer": 1,
            "explanation": "Cherry-pick creates a new commit with the same changes on your current branch. The original stays where it was."
        },
        {
            "q": "What does pre-commit do?",
            "options": [
                "Commits code automatically",
                "Runs checks before allowing a commit",
                "Pushes code to remote",
                "Creates branches"
            ],
            "answer": 1,
            "explanation": "Pre-commit runs configured hooks (linting, formatting, etc.) before each commit, catching issues early."
        }
    ]
    
    print("=" * 60)
    print("ADVANCED GIT QUIZ")
    print("=" * 60 + "\n")
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j+1}. {opt}")
        
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. {q['explanation']}\n")
        except:
            print(f"Invalid input. {q['explanation']}\n")
    
    print("=" * 60)
    print(f"Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Perfect! You're ready for advanced Git workflows!")
    elif score >= 3:
        print("👍 Good job! Review the ones you missed.")
    else:
        print("📚 Review the advanced Git concepts before moving on.")
    print("=" * 60)


# =============================================================================
# Verification
# =============================================================================

def verify_exercises(repo_path: str = ".") -> None:
    """Verify advanced Git exercises completion."""
    print("=" * 60)
    print("ADVANCED GIT EXERCISES VERIFICATION")
    print("=" * 60 + "\n")
    
    # Check for pre-commit
    if check_precommit_setup(repo_path):
        print("✅ Pre-commit config found")
    else:
        print("⚠️  No .pre-commit-config.yaml found")
    
    # Check git skills
    skills = check_rebase_skills(repo_path)
    
    if skills["has_rebased"]:
        print("✅ Evidence of rebase in reflog")
    else:
        print("⚠️  No rebase history found - try Exercise 1")
    
    if skills["commit_messages_clean"]:
        print("✅ Commit messages look clean")
    else:
        print("⚠️  Some commits have WIP/temp messages")
    
    print("\n" + CODE_REVIEW_CHECKLIST)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "quiz":
            advanced_git_quiz()
        elif cmd == "verify":
            path = sys.argv[2] if len(sys.argv) > 2 else "."
            verify_exercises(path)
        elif cmd == "checklist":
            print(CODE_REVIEW_CHECKLIST)
    else:
        print("Day 15: Advanced Git + Code Review Practice")
        print("=" * 45)
        print("\nThis is a practice-focused day.")
        print("Open this file and follow the exercises in terminal.")
        print("\nCommands:")
        print("  python day13_advanced_git.py quiz      - Take the quiz")
        print("  python day13_advanced_git.py verify    - Verify your work")
        print("  python day13_advanced_git.py checklist - Show review checklist")
