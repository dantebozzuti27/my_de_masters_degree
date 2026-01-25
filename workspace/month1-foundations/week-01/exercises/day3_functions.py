#!/usr/bin/env python3
"""
Day 3 Exercise: Control Flow & Functions (AI-Enhanced)
=======================================================

AI-ENHANCED LEARNING APPROACH:
- FizzBuzz: Try it WITHOUT AI first - this is the classic interview warm-up
- Other exercises: Use AI to help, but ALWAYS trace through the logic
- AI often has bugs in loops (off-by-one errors) - find them!

CRITICAL SKILL: Debug AI-Generated Code
Loops are where AI makes the most mistakes. Your job is to:
1. Let AI generate the loop
2. Trace through with sample input (manually step through)
3. Find and fix any edge case bugs
4. Add test cases that break the AI's version

AI TIP: After AI generates a function, ask ChatGPT:
"What edge cases might break this function?"
Then test those edge cases.
"""

# =============================================================================
# EXERCISE 1: FizzBuzz (The Classic!)
# =============================================================================

def fizzbuzz(n: int) -> list:
    """
    TODO: Implement FizzBuzz for numbers 1 to n.
    
    Rules:
    - If divisible by 3: "Fizz"
    - If divisible by 5: "Buzz"  
    - If divisible by both: "FizzBuzz"
    - Otherwise: the number as a string
    
    Return a list of results.
    
    Example:
        >>> fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        
        >>> fizzbuzz(15)[-1]
        'FizzBuzz'
    """
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    return result


# =============================================================================
# EXERCISE 2: Factorial
# =============================================================================

def factorial_iterative(n: int) -> int:
    """
    TODO: Calculate factorial using a loop (iterative approach).
    
    n! = n × (n-1) × (n-2) × ... × 1
    
    Edge case: 0! = 1
    
    Example:
        >>> factorial_iterative(5)
        120
        >>> factorial_iterative(0)
        1
    """
    result = 1
    
    for i in range(1, n + 1):
        result = result * i
    
    return result


def factorial_recursive(n: int) -> int:
    """
    TODO: Calculate factorial using recursion.
    
    Hint: n! = n × (n-1)!
    Base case: 0! = 1
    
    Example:
        >>> factorial_recursive(5)
        120
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# =============================================================================
# EXERCISE 3: Prime Number Checker
# =============================================================================

def is_prime(n: int) -> bool:
    """
    TODO: Check if n is a prime number.
    
    A prime number is only divisible by 1 and itself.
    
    Optimization: Only check divisors up to sqrt(n)
    
    Example:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(17)
        True
        >>> is_prime(1)
        False
    """
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def primes_up_to(n: int) -> list:
    """
    TODO: Return a list of all prime numbers up to n.
    
    Example:
        >>> primes_up_to(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result


# =============================================================================
# EXERCISE 4: Temperature Converter
# =============================================================================

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    TODO: Convert Celsius to Fahrenheit.
    
    Formula: F = C × 9/5 + 32
    
    Example:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    TODO: Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) × 5/9
    
    Example:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
    """
    return (fahrenheit - 32) * 5/9


# =============================================================================
# EXERCISE 5: Palindrome Checker
# =============================================================================

def is_palindrome(text: str) -> bool:
    """
    TODO: Check if text is a palindrome (reads same forwards and backwards).
    
    Ignore spaces and case.
    
    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


# =============================================================================
# EXERCISE 6: Fibonacci Sequence
# =============================================================================

def fibonacci(n: int) -> list:
    """
    TODO: Return the first n numbers in the Fibonacci sequence.
    
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the two before it.
    
    Example:
        >>> fibonacci(8)
        [0, 1, 1, 2, 3, 5, 8, 13]
    """
    if n <= 0:
        return list()  # Empty list for invalid input
    if n == 1:
        return [0]
    
    result = [0, 1]
    while len(result) < n:
        result.append(result[-1] + result[-2])
    return result


# =============================================================================
# BONUS: Number Guessing Game
# =============================================================================

def guessing_game():
    """
    BONUS: Interactive number guessing game.
    
    - Computer picks random number 1-100
    - Player guesses until correct
    - Give "Higher!" or "Lower!" hints
    - Count and report number of guesses
    
    This is interactive - uncomment the call at the bottom to play!
    """
    import random
    
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


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 3: Control Flow & Functions - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test FizzBuzz
    total += 1
    result = fizzbuzz(15)
    if result and result[-1] == 'FizzBuzz' and result[2] == 'Fizz':
        print("✅ fizzbuzz() works correctly")
        passed += 1
    else:
        print(f"❌ fizzbuzz(15) should end with 'FizzBuzz'. Got: {result}")
    
    # Test Factorial (iterative)
    total += 1
    if factorial_iterative(5) == 120 and factorial_iterative(0) == 1:
        print("✅ factorial_iterative() works correctly")
        passed += 1
    else:
        print("❌ factorial_iterative() needs work")
    
    # Test Factorial (recursive)
    total += 1
    if factorial_recursive(5) == 120 and factorial_recursive(0) == 1:
        print("✅ factorial_recursive() works correctly")
        passed += 1
    else:
        print("❌ factorial_recursive() needs work")
    
    # Test is_prime
    total += 1
    if is_prime(2) and is_prime(17) and not is_prime(4) and not is_prime(1):
        print("✅ is_prime() works correctly")
        passed += 1
    else:
        print("❌ is_prime() needs work")
    
    # Test primes_up_to
    total += 1
    primes = primes_up_to(20)
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    if primes == expected:
        print("✅ primes_up_to() works correctly")
        passed += 1
    else:
        print(f"❌ primes_up_to(20) should be {expected}. Got: {primes}")
    
    # Test Temperature conversions
    total += 1
    if celsius_to_fahrenheit(0) == 32 and fahrenheit_to_celsius(32) == 0:
        print("✅ Temperature conversions work correctly")
        passed += 1
    else:
        print("❌ Temperature conversions need work")
    
    # Test Palindrome
    total += 1
    if (is_palindrome("racecar") and 
        is_palindrome("A man a plan a canal Panama") and 
        not is_palindrome("hello")):
        print("✅ is_palindrome() works correctly")
        passed += 1
    else:
        print("❌ is_palindrome() needs work")
    
    # Test Fibonacci
    total += 1
    fib = fibonacci(8)
    expected = [0, 1, 1, 2, 3, 5, 8, 13]
    if fib == expected:
        print("✅ fibonacci() works correctly")
        passed += 1
    else:
        print(f"❌ fibonacci(8) should be {expected}. Got: {fib}")
    
    # Summary
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
        print("You're ready for Day 4!")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print("Keep working on the remaining exercises!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
    
    # Uncomment to play the guessing game:
    # guessing_game()
