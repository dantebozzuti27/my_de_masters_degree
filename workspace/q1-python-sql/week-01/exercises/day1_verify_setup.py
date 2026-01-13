#!/usr/bin/env python3
"""
Day 1 Exercise: Verify Development Environment Setup
=====================================================

Run this script to verify your Python environment is correctly configured.

Instructions:
1. Activate your virtual environment
2. Run: python day1_verify_setup.py
3. All checks should pass ✅

Your Task:
- Complete the TODO sections below
- Make all tests pass
- Commit this file to git
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Verify Python 3.11+ is installed."""
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 11:
        print("✅ Python version OK (3.11+)")
        return True
    else:
        print("❌ Python version should be 3.11+")
        return False


def check_virtual_env():
    """Verify running in a virtual environment."""
    venv = os.environ.get('VIRTUAL_ENV')
    
    if venv:
        print(f"Virtual Environment: {venv}")
        print("✅ Running in virtual environment")
        return True
    else:
        print("❌ Not running in a virtual environment!")
        print("   Activate with: source venv/bin/activate")
        return False


def check_working_directory():
    """Display current working directory."""
    cwd = Path.cwd()
    print(f"Working Directory: {cwd}")
    print("✅ Working directory OK")
    return True


# =============================================================================
# TODO: Complete the exercises below
# =============================================================================

def my_first_function():
    """
    TODO: Write a function that returns your name as a string.
    
    Example:
        >>> my_first_function()
        'Dante Bozzuti'
    """
    # YOUR CODE HERE
    name = "Dante Bozzuti"  # Replace with your name
    return name


def add_numbers(a: int, b: int) -> int:
    """
    TODO: Write a function that adds two numbers and returns the result.
    
    Example:
        >>> add_numbers(5, 3)
        8
    """
    # YOUR CODE HERE
    return a + b  # Replace with your implementation


def is_even(number: int) -> bool:
    """
    TODO: Write a function that returns True if number is even, False otherwise.
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
    """
    # YOUR CODE HERE
    return number % 2 == 0  # Replace with your implementation


# =============================================================================
# Tests - Don't modify below this line
# =============================================================================

def run_tests():
    """Run all verification tests."""
    print("\n" + "=" * 60)
    print("ENVIRONMENT CHECKS")
    print("=" * 60 + "\n")
    
    checks = [
        check_python_version(),
        check_virtual_env(),
        check_working_directory(),
    ]
    
    print("\n" + "=" * 60)
    print("EXERCISE TESTS")
    print("=" * 60 + "\n")
    
    # Test my_first_function
    name = my_first_function()
    if name and len(name) > 0:
        print(f"✅ my_first_function() returned: '{name}'")
        checks.append(True)
    else:
        print("❌ my_first_function() should return your name")
        checks.append(False)
    
    # Test add_numbers
    result = add_numbers(5, 3)
    if result == 8:
        print(f"✅ add_numbers(5, 3) = {result}")
        checks.append(True)
    else:
        print(f"❌ add_numbers(5, 3) should be 8, got {result}")
        checks.append(False)
    
    # Test is_even
    if is_even(4) == True and is_even(7) == False:
        print("✅ is_even() works correctly")
        checks.append(True)
    else:
        print("❌ is_even() not working correctly")
        checks.append(False)
    
    # Summary
    print("\n" + "=" * 60)
    passed = sum(checks)
    total = len(checks)
    
    if passed == total:
        print(f"🎉 ALL CHECKS PASSED! ({passed}/{total})")
        print("You're ready to move forward!")
    else:
        print(f"⚠️  {passed}/{total} checks passed")
        print("Complete the TODOs and run again.")
    
    print("=" * 60 + "\n")
    return passed == total


if __name__ == "__main__":
    run_tests()
