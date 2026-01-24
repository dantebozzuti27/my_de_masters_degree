#!/usr/bin/env python3
"""
Day 12: GitHub PRs & Professional Workflows
============================================
Duration: 2 hours

Learn GitHub-specific features: Pull Requests, Code Review, Issues.
This is how professional teams collaborate.

WHY THIS MATTERS:
- All professional teams use PRs for code changes
- Code review skills are highly valued
- Good PRs get merged faster
- This is how you'll work every day as a data engineer

COMPLETION: Exercises completed!
"""

import subprocess
import os
from typing import List, Dict, Optional

# =============================================================================
# GITHUB EXERCISES (Do these on github.com and in terminal)
# =============================================================================

"""
EXERCISE 1: Create a GitHub Repository (15 min)
================================================

1. Go to github.com and sign in

2. Click "New repository" (+ icon in top right)

3. Fill in:
   - Repository name: data-engineering-practice
   - Description: Practice repository for DE skills
   - Public (for portfolio) or Private
   - Initialize with README: Yes
   - Add .gitignore: Python
   - License: MIT

4. Clone to your machine:
   git clone https://github.com/YOUR_USERNAME/data-engineering-practice.git
   cd data-engineering-practice


EXERCISE 2: Feature Branch Workflow (20 min)
=============================================

The professional workflow:
1. Create branch for your feature
2. Make changes and commit
3. Push branch to GitHub
4. Create Pull Request
5. Get review
6. Merge

Practice:

1. Create a feature branch:
   git checkout -b feature/add-data-loader

2. Create a file (data_loader.py):
   # data_loader.py
   def load_csv(filepath: str) -> list:
       '''Load data from CSV file.'''
       with open(filepath, 'r') as f:
           return f.readlines()

3. Commit:
   git add data_loader.py
   git commit -m "Add: data_loader module with CSV support"

4. Push the branch:
   git push -u origin feature/add-data-loader

5. Go to GitHub - you'll see "Compare & pull request" button


EXERCISE 3: Creating a Pull Request (20 min)
=============================================

On GitHub:

1. Click "Compare & pull request" (or go to Pull requests tab → New)

2. Fill in the PR template:

Title: Add data loader module

Description:
## Summary
Adds a data loading module that supports CSV file reading.

## Changes
- Added `data_loader.py` with `load_csv()` function
- Handles basic file reading

## Testing
- Tested with sample CSV files locally

## Checklist
- [x] Code follows project style
- [x] Tests pass locally
- [ ] Documentation updated

3. Add reviewers (if you have collaborators)

4. Click "Create pull request"


EXERCISE 4: Code Review Practice (25 min)
==========================================

Good code reviews:
- Are constructive and kind
- Focus on the code, not the person
- Ask questions instead of demanding changes
- Acknowledge good work

Practice reviewing your own PR:

1. Go to the "Files changed" tab

2. Click the + on any line to add a comment

3. Types of review comments:

   GOOD:
   "Nice clean implementation! Consider adding error handling 
    for when the file doesn't exist."
   
   "Could we add a docstring example here? It would help 
    future readers understand the expected input format."
   
   BAD:
   "This is wrong."
   "Why would you do it this way?"

4. Submit your review:
   - Comment: Just leave feedback
   - Approve: Code looks good to merge
   - Request changes: Must fix issues before merge


EXERCISE 5: Handling Review Feedback (20 min)
==============================================

When you receive feedback:

1. Update your local branch:
   git checkout feature/add-data-loader

2. Make the requested changes:
   (Edit files based on feedback)

3. Commit the fixes:
   git add .
   git commit -m "Fix: address review feedback

   - Added error handling for missing files
   - Added docstring examples"

4. Push updates (PR updates automatically):
   git push

5. Reply to review comments explaining what you did

6. Request re-review if needed


EXERCISE 6: Merging Strategies (15 min)
=======================================

GitHub offers three merge strategies:

1. MERGE COMMIT (default)
   - Creates a merge commit
   - Preserves full history
   - Shows the PR clearly in history
   
   Best for: Feature branches

2. SQUASH AND MERGE
   - Combines all commits into one
   - Cleaner main branch history
   - Loses individual commit detail
   
   Best for: Messy feature branches

3. REBASE AND MERGE
   - Replays commits on top of main
   - Linear history
   - Can cause issues with shared branches
   
   Best for: Clean, small feature branches

Practice:
1. Go to your PR
2. Click the dropdown on "Merge pull request"
3. See the options
4. Choose "Squash and merge" for cleaner history
5. Edit the commit message if needed
6. Click "Confirm squash and merge"


EXERCISE 7: Issue Tracking (15 min)
===================================

Issues are for tracking work:

1. Go to the Issues tab

2. Create a new issue:
   Title: Add support for JSON files
   
   Body:
   ## Description
   The data loader should support JSON files in addition to CSV.
   
   ## Requirements
   - [ ] Add `load_json()` function
   - [ ] Support nested JSON structures
   - [ ] Add error handling
   
   ## Additional context
   This is needed for the API data project.

3. Add labels: enhancement, good first issue

4. Reference issues in commits:
   git commit -m "Add: JSON loader support

   Closes #1"  # This auto-closes issue #1 when merged


EXERCISE 8: GitHub Actions (Bonus - 10 min)
===========================================

GitHub Actions automate tests and deployment.

1. Create .github/workflows/test.yml:

name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Run tests
        run: python -m pytest tests/

2. Commit and push - watch the Actions tab!
"""

# =============================================================================
# PR HELPERS & TEMPLATES
# =============================================================================

PR_TEMPLATE = '''## Summary
<!-- What does this PR do? Keep it brief. -->


## Changes
<!-- List the main changes -->
-
-

## Testing
<!-- How was this tested? -->
-

## Checklist
- [ ] Code follows project style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated if needed
- [ ] No sensitive data/secrets committed

## Related Issues
<!-- Link any related issues: Closes #123 -->
'''

ISSUE_TEMPLATE = '''## Description
<!-- Clear description of the problem or feature -->


## Expected Behavior
<!-- What should happen? -->


## Current Behavior  
<!-- What currently happens? -->


## Steps to Reproduce (for bugs)
1.
2.
3.

## Possible Solution
<!-- Optional: suggest how to fix/implement -->


## Additional Context
<!-- Any other relevant information -->
'''

def create_pr_template(repo_path: str = ".") -> None:
    """Create a PR template file for your repository."""
    template_dir = os.path.join(repo_path, ".github")
    os.makedirs(template_dir, exist_ok=True)
    
    template_path = os.path.join(template_dir, "pull_request_template.md")
    with open(template_path, "w") as f:
        f.write(PR_TEMPLATE)
    
    print(f"✅ Created PR template at {template_path}")
    print("   Commit and push to activate.")


def create_issue_template(repo_path: str = ".") -> None:
    """Create an issue template for your repository."""
    template_dir = os.path.join(repo_path, ".github", "ISSUE_TEMPLATE")
    os.makedirs(template_dir, exist_ok=True)
    
    # Bug report template
    bug_path = os.path.join(template_dir, "bug_report.md")
    with open(bug_path, "w") as f:
        f.write("---\nname: Bug report\nabout: Report a bug\n---\n\n")
        f.write(ISSUE_TEMPLATE)
    
    print(f"✅ Created issue template at {template_dir}")


# =============================================================================
# REVIEW CHECKLIST
# =============================================================================

REVIEW_CHECKLIST = {
    "code_quality": [
        "Are variable names descriptive?",
        "Is the code DRY (Don't Repeat Yourself)?",
        "Are functions small and focused?",
        "Is error handling appropriate?",
        "Are edge cases handled?"
    ],
    "documentation": [
        "Are functions documented with docstrings?",
        "Are complex sections commented?",
        "Is the README updated if needed?",
        "Are type hints used?"
    ],
    "testing": [
        "Are there tests for new functionality?",
        "Do tests cover edge cases?",
        "Do all tests pass?"
    ],
    "security": [
        "No hardcoded secrets/passwords?",
        "No sensitive data in logs?",
        "Input validation where needed?"
    ],
    "style": [
        "Consistent formatting?",
        "Follows project conventions?",
        "Imports organized?"
    ]
}

def print_review_checklist() -> None:
    """Print the code review checklist."""
    print("=" * 60)
    print("CODE REVIEW CHECKLIST")
    print("=" * 60 + "\n")
    
    for category, items in REVIEW_CHECKLIST.items():
        print(f"📋 {category.upper().replace('_', ' ')}")
        for item in items:
            print(f"   [ ] {item}")
        print()


# =============================================================================
# COMMIT MESSAGE ANALYZER
# =============================================================================

def analyze_pr_readiness(repo_path: str = ".") -> Dict:
    """
    Analyze if a branch is ready for PR.
    """
    result = {
        "has_changes": False,
        "commit_count": 0,
        "commit_quality": [],
        "branch_name_ok": False,
        "ready": False
    }
    
    # Check for uncommitted changes
    try:
        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=repo_path
        )
        result["has_changes"] = bool(status.stdout.strip())
    except:
        pass
    
    # Get branch name
    try:
        branch = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True, text=True, cwd=repo_path
        )
        branch_name = branch.stdout.strip()
        
        # Good branch names: feature/, fix/, docs/, etc.
        good_prefixes = ["feature/", "fix/", "docs/", "test/", "refactor/"]
        result["branch_name_ok"] = any(branch_name.startswith(p) for p in good_prefixes)
    except:
        pass
    
    # Count commits ahead of main
    try:
        count = subprocess.run(
            ["git", "rev-list", "--count", "main..HEAD"],
            capture_output=True, text=True, cwd=repo_path
        )
        result["commit_count"] = int(count.stdout.strip())
    except:
        pass
    
    # Check overall readiness
    result["ready"] = (
        not result["has_changes"] and  # No uncommitted changes
        result["commit_count"] > 0 and  # Has commits
        result["branch_name_ok"]        # Good branch name
    )
    
    return result


# =============================================================================
# Verification
# =============================================================================

def verify_github_exercises(repo_path: str = ".") -> None:
    """Verify GitHub workflow exercises."""
    print("=" * 60)
    print("GITHUB EXERCISES VERIFICATION")
    print("=" * 60 + "\n")
    
    # Check if it's a git repo
    try:
        subprocess.run(["git", "status"], capture_output=True, cwd=repo_path, check=True)
    except:
        print("❌ Not a Git repository")
        return
    
    print("✅ Valid Git repository\n")
    
    # Check for remote
    try:
        remote = subprocess.run(
            ["git", "remote", "-v"],
            capture_output=True, text=True, cwd=repo_path
        )
        if "github.com" in remote.stdout:
            print("✅ GitHub remote configured")
        else:
            print("⚠️  No GitHub remote found. Run: git remote add origin <url>")
    except:
        pass
    
    # Check for PR template
    template_path = os.path.join(repo_path, ".github", "pull_request_template.md")
    if os.path.exists(template_path):
        print("✅ PR template exists")
    else:
        print("⚠️  No PR template. Run: create_pr_template()")
    
    # Check branch naming
    try:
        branches = subprocess.run(
            ["git", "branch"],
            capture_output=True, text=True, cwd=repo_path
        )
        branch_list = branches.stdout.strip().split("\n")
        good_branches = [b for b in branch_list if any(
            p in b for p in ["feature/", "fix/", "docs/"]
        )]
        print(f"   Feature branches found: {len(good_branches)}")
    except:
        pass
    
    print("\n" + "-" * 40)
    print("Next steps:")
    print("1. Create a feature branch: git checkout -b feature/your-feature")
    print("2. Make changes and commit")
    print("3. Push to GitHub: git push -u origin feature/your-feature")
    print("4. Create a Pull Request on github.com")
    print("-" * 40)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "checklist":
            print_review_checklist()
        elif cmd == "template":
            create_pr_template()
        elif cmd == "verify":
            verify_github_exercises()
        elif cmd == "pr-ready":
            result = analyze_pr_readiness()
            print(f"PR Ready: {'Yes' if result['ready'] else 'No'}")
            print(f"Details: {result}")
    else:
        print("Day 12: GitHub PRs & Professional Workflows")
        print("=" * 45)
        print("\nThis is a GitHub-focused day.")
        print("Follow the exercises on github.com and in terminal.")
        print("\nCommands:")
        print("  python day12_github_prs.py checklist  - Show review checklist")
        print("  python day12_github_prs.py template   - Create PR template")
        print("  python day12_github_prs.py verify     - Verify your setup")
        print("  python day12_github_prs.py pr-ready   - Check if ready for PR")
