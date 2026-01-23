#!/usr/bin/env python3
"""
Day 11: Git Fundamentals
========================
Duration: 2 hours

This is a PRACTICE-FOCUSED day. Most exercises are done in the terminal.
This file contains helper functions to verify your Git work.

WHY THIS MATTERS:
- Every professional project uses Git
- Branching/merging is daily work
- Clean commit history = professional code
- Interviewers check your GitHub for commit quality

COMPLETION: Exercises completed!
"""

import subprocess
import os
from typing import List, Dict, Optional, Tuple

# =============================================================================
# GIT PRACTICE EXERCISES (Do these in terminal)
# =============================================================================

"""
EXERCISE 1: Repository Setup (10 min)
=====================================

In your terminal, create a practice repository:

1. Create a new directory:
   mkdir git-practice && cd git-practice

2. Initialize Git:
   git init

3. Create initial files:
   echo "# Git Practice" > README.md
   echo "*.pyc" > .gitignore
   
4. Make first commit:
   git add .
   git commit -m "Initial commit: add README and gitignore"

5. Check your work:
   git log --oneline

Expected: You should see one commit with your message.


EXERCISE 2: Branching Practice (20 min)
=======================================

1. Create and switch to a feature branch:
   git checkout -b feature/add-calculator
   
   # Or in newer Git:
   git switch -c feature/add-calculator

2. Create a calculator.py file:
   # calculator.py
   def add(a, b):
       return a + b
   
   def subtract(a, b):
       return a - b

3. Commit your changes:
   git add calculator.py
   git commit -m "Add: basic calculator with add/subtract functions"

4. Create another branch from main:
   git checkout main
   git checkout -b feature/add-tests

5. Create tests:
   # test_calculator.py
   from calculator import add, subtract
   
   def test_add():
       assert add(1, 2) == 3

6. Commit:
   git add test_calculator.py
   git commit -m "Add: test for add function"

7. View all branches:
   git branch -a

Expected: Three branches - main, feature/add-calculator, feature/add-tests


EXERCISE 3: Merging Practice (20 min)
=====================================

1. Go back to main:
   git checkout main

2. Merge the calculator feature:
   git merge feature/add-calculator

3. Check the log:
   git log --oneline --graph

4. Merge the tests feature:
   git merge feature/add-tests

5. You might see a merge conflict! If so:
   - Open the conflicted file
   - Edit to resolve (keep both changes if both are good)
   - git add <file>
   - git commit  (no -m, will open editor)

6. Clean up branches:
   git branch -d feature/add-calculator
   git branch -d feature/add-tests


EXERCISE 4: Commit Message Practice (20 min)
============================================

Good commit messages follow this pattern:

<type>: <short description>

<optional body explaining why>

Types:
- Add: New feature
- Fix: Bug fix  
- Update: Enhancement to existing feature
- Refactor: Code change that doesn't add features
- Docs: Documentation only
- Test: Adding or updating tests

Practice:
1. Make a small change
2. Commit with a good message:
   git commit -m "Add: multiply function to calculator

   Supports integer and float multiplication.
   Returns product of two numbers."


EXERCISE 5: Viewing History (15 min)
====================================

Try these commands:

1. See commit history:
   git log

2. Compact view:
   git log --oneline

3. See graph:
   git log --oneline --graph --all

4. See changes in a commit:
   git show <commit-hash>

5. See what changed between commits:
   git diff <hash1>..<hash2>

6. See who changed what:
   git blame <filename>


EXERCISE 6: Undoing Changes (15 min)
====================================

Practice safely undoing:

1. Unstage a file:
   git reset HEAD <file>

2. Discard changes in working directory:
   git checkout -- <file>
   
   # Or newer Git:
   git restore <file>

3. Amend last commit (only if not pushed!):
   git commit --amend -m "New message"

4. See what would be in next commit:
   git diff --staged


EXERCISE 7: Stashing (10 min)
=============================

Stash is for temporarily saving work:

1. Make some changes but don't commit

2. Stash them:
   git stash save "Work in progress on feature X"

3. Your working directory is now clean

4. See stashes:
   git stash list

5. Apply the stash:
   git stash pop

6. Or apply without removing from stash:
   git stash apply
"""

# =============================================================================
# VERIFICATION HELPERS
# =============================================================================
# Use these functions to check your Git work

def run_git_command(command: str, cwd: Optional[str] = None) -> Tuple[bool, str]:
    """
    Run a git command and return (success, output).
    
    Example:
        >>> success, output = run_git_command("git status")
    """
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


def check_git_repo(path: str = ".") -> Dict[str, any]:
    """
    Check if path is a valid Git repository.
    
    Returns info about the repo.
    """
    result = {
        "is_git_repo": False,
        "branch": None,
        "commits": 0,
        "branches": [],
        "has_remote": False,
        "clean": False
    }
    
    # Check if it's a git repo
    success, _ = run_git_command("git status", path)
    if not success:
        return result
    
    result["is_git_repo"] = True
    
    # Get current branch
    success, output = run_git_command("git branch --show-current", path)
    if success:
        result["branch"] = output.strip()
    
    # Count commits
    success, output = run_git_command("git rev-list --count HEAD", path)
    if success:
        result["commits"] = int(output.strip())
    
    # List branches
    success, output = run_git_command("git branch", path)
    if success:
        result["branches"] = [b.strip().replace("* ", "") for b in output.strip().split("\n") if b.strip()]
    
    # Check for remote
    success, output = run_git_command("git remote", path)
    if success and output.strip():
        result["has_remote"] = True
    
    # Check if clean
    success, output = run_git_command("git status --porcelain", path)
    if success and not output.strip():
        result["clean"] = True
    
    return result


def analyze_commit_messages(path: str = ".", count: int = 10) -> List[Dict]:
    """
    Analyze recent commit messages for quality.
    
    Returns list of commits with quality assessment.
    """
    success, output = run_git_command(f"git log --oneline -n {count}", path)
    if not success:
        return []
    
    commits = []
    good_prefixes = ["Add:", "Fix:", "Update:", "Refactor:", "Docs:", "Test:", "feat:", "fix:", "chore:"]
    
    for line in output.strip().split("\n"):
        if not line:
            continue
        parts = line.split(" ", 1)
        hash_val = parts[0]
        message = parts[1] if len(parts) > 1 else ""
        
        quality = "good" if any(message.startswith(p) for p in good_prefixes) else "needs_improvement"
        has_body = len(message.split("\n")) > 1 or len(message) > 50
        
        commits.append({
            "hash": hash_val,
            "message": message,
            "quality": quality,
            "descriptive": has_body or len(message) > 20
        })
    
    return commits


def get_branch_info(path: str = ".") -> Dict[str, List[str]]:
    """
    Get information about branches.
    
    Returns dict with local and remote branches.
    """
    result = {"local": [], "remote": [], "merged": []}
    
    # Local branches
    success, output = run_git_command("git branch", path)
    if success:
        result["local"] = [b.strip().replace("* ", "") for b in output.strip().split("\n") if b.strip()]
    
    # Remote branches
    success, output = run_git_command("git branch -r", path)
    if success:
        result["remote"] = [b.strip() for b in output.strip().split("\n") if b.strip()]
    
    # Merged branches
    success, output = run_git_command("git branch --merged", path)
    if success:
        result["merged"] = [b.strip().replace("* ", "") for b in output.strip().split("\n") if b.strip()]
    
    return result


# =============================================================================
# QUIZ: Git Concepts
# =============================================================================

def git_quiz() -> None:
    """
    Test your Git knowledge.
    Run this and answer the questions.
    """
    questions = [
        {
            "q": "What command creates a new branch AND switches to it?",
            "options": ["git branch new", "git checkout -b new", "git switch new", "git new branch"],
            "answer": 1,
            "explanation": "git checkout -b creates and switches. git switch -c does the same in newer Git."
        },
        {
            "q": "What's the difference between 'git reset' and 'git revert'?",
            "options": [
                "No difference",
                "reset rewrites history, revert creates a new commit",
                "revert rewrites history, reset creates a new commit",
                "reset is for files, revert is for commits"
            ],
            "answer": 1,
            "explanation": "reset rewrites history (dangerous for shared branches), revert safely creates a new commit that undoes changes."
        },
        {
            "q": "What does 'git stash' do?",
            "options": [
                "Deletes uncommitted changes",
                "Creates a commit",
                "Temporarily saves changes without committing",
                "Pushes to remote"
            ],
            "answer": 2,
            "explanation": "Stash saves your work-in-progress so you can switch branches cleanly, then restore it later."
        },
        {
            "q": "What should you do BEFORE merging a feature branch into main?",
            "options": [
                "Delete the feature branch",
                "Pull latest main and resolve conflicts",
                "Push directly to main",
                "Reset main"
            ],
            "answer": 1,
            "explanation": "Always pull latest main first, merge main into your feature branch, resolve conflicts there, then merge to main."
        },
        {
            "q": "What's a good commit message for adding a new login feature?",
            "options": [
                "updated stuff",
                "Add: user login with email/password authentication",
                "login",
                "WIP"
            ],
            "answer": 1,
            "explanation": "Good commits: start with type (Add/Fix/etc), describe WHAT and optionally WHY."
        }
    ]
    
    print("=" * 60)
    print("GIT KNOWLEDGE QUIZ")
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
        print("🎉 Perfect! You know your Git!")
    elif score >= 3:
        print("👍 Good job! Review the ones you missed.")
    else:
        print("📚 Keep practicing! Git mastery takes time.")
    print("=" * 60)


# =============================================================================
# Verification
# =============================================================================

def verify_exercises(repo_path: str = ".") -> None:
    """
    Verify that Git exercises were completed.
    Run this in your git-practice directory.
    """
    print("=" * 60)
    print("GIT EXERCISE VERIFICATION")
    print("=" * 60 + "\n")
    
    info = check_git_repo(repo_path)
    
    if not info["is_git_repo"]:
        print("❌ Not a Git repository. Run 'git init' first.")
        return
    
    print(f"✅ Valid Git repository")
    print(f"   Current branch: {info['branch']}")
    print(f"   Total commits: {info['commits']}")
    print(f"   Branches: {', '.join(info['branches'])}")
    print(f"   Has remote: {'Yes' if info['has_remote'] else 'No'}")
    print(f"   Working tree clean: {'Yes' if info['clean'] else 'No'}")
    print()
    
    # Check commits
    if info["commits"] >= 3:
        print("✅ Multiple commits made")
    else:
        print("⚠️  Make more commits to practice")
    
    # Check branches
    if len(info["branches"]) >= 1:
        print("✅ At least one branch exists")
    
    # Analyze commit messages
    commits = analyze_commit_messages(repo_path)
    good_commits = sum(1 for c in commits if c["quality"] == "good")
    print(f"\nCommit message quality: {good_commits}/{len(commits)} follow conventions")
    
    if commits:
        print("\nRecent commits:")
        for c in commits[:5]:
            emoji = "✅" if c["quality"] == "good" else "⚠️"
            print(f"   {emoji} {c['hash']} {c['message'][:50]}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "quiz":
        git_quiz()
    elif len(sys.argv) > 1 and sys.argv[1] == "verify":
        path = sys.argv[2] if len(sys.argv) > 2 else "."
        verify_exercises(path)
    else:
        print("Day 11: Git Fundamentals")
        print("=" * 40)
        print("\nThis is a practice-focused day.")
        print("Open this file and follow the exercises in the terminal.")
        print("\nCommands:")
        print("  python day11_git_fundamentals.py quiz    - Take the Git quiz")
        print("  python day11_git_fundamentals.py verify  - Verify your work")
