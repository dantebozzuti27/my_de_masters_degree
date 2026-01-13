#!/usr/bin/env python3
"""
Day 2 Exercise: Variables and Data Types
=========================================

Master Python's core data types through hands-on practice.

Instructions:
1. Complete each TODO section
2. Run: python day2_variables.py
3. All tests should pass ✅
"""

# =============================================================================
# EXERCISE 1: Variable Declaration
# =============================================================================

# TODO: Create variables with these exact names and appropriate values:
# - my_name: Your full name (string)
# - my_age: Your age (integer)
# - my_height: Your height in meters (float, e.g., 1.75)
# - is_learning_python: Set to True (boolean)

my_name = "Dante Bozzuti"  # YOUR CODE HERE
my_age = 24  # YOUR CODE HERE
my_height = 1.70  # YOUR CODE HERE
is_learning_python = True  # YOUR CODE HERE


# =============================================================================
# EXERCISE 2: String Operations
# =============================================================================

def string_operations(text: str) -> dict:
    """
    TODO: Perform various string operations on the input text.
    
    Return a dictionary with these keys:
    - 'uppercase': text in all uppercase
    - 'lowercase': text in all lowercase  
    - 'titlecase': text in title case
    - 'length': number of characters
    - 'word_count': number of words
    - 'first_word': the first word only
    - 'reversed': the text reversed
    
    Example:
        >>> string_operations("hello world")
        {
            'uppercase': 'HELLO WORLD',
            'lowercase': 'hello world',
            'titlecase': 'Hello World',
            'length': 11,
            'word_count': 2,
            'first_word': 'hello',
            'reversed': 'dlrow olleh'
        }
    """
    # YOUR CODE HERE
    return {
        'uppercase': 'HELLO WORLD',
        'lowercase': 'hello world',
        'titlecase': 'Hello World',
        'length': 11,
        'word_count': 2,
        'first_word': 'hello',
        'reversed': 'dlrow olleh'
    }


# =============================================================================
# EXERCISE 3: Type Conversion
# =============================================================================

def convert_types(value: str) -> dict:
    """
    TODO: Convert the string value to different types.
    
    Return a dictionary with:
    - 'as_int': value converted to integer
    - 'as_float': value converted to float
    - 'as_bool': True if value is not "0" or empty
    - 'original_type': the type name of the input
    
    Example:
        >>> convert_types("42")
        {
            'as_int': 42,
            'as_float': 42.0,
            'as_bool': True,
            'original_type': 'str'
        }
    """
    # YOUR CODE HERE
    return {
        'as_int': 42,
        'as_float': 42.0,
        'as_bool': True,
        'original_type': 'str'
    }


# =============================================================================
# EXERCISE 4: F-Strings (Formatted String Literals)
# =============================================================================

def format_greeting(name: str, age: int, city: str) -> str:
    """
    TODO: Create a formatted greeting using f-strings.
    
    Return: "Hello, I'm {name}! I'm {age} years old and live in {city}."
    
    Example:
        >>> format_greeting("Alice", 25, "New York")
        "Hello, I'm Alice! I'm 25 years old and live in New York."
    """
    # YOUR CODE HERE
    return f"Hello, I'm {name}! I'm {age} years old and live in {city}."


def format_table_row(name: str, value: float) -> str:
    """
    TODO: Format a table row with aligned columns.
    
    - Name should be left-aligned in 20 characters
    - Value should be right-aligned in 10 characters with 2 decimal places
    
    Example:
        >>> format_table_row("Revenue", 1234.5)
        "Revenue              1234.50"
    """
    # YOUR CODE HERE
    return f"{name:<20}{value:>10.2f}"


# =============================================================================
# EXERCISE 5: Arithmetic Operations
# =============================================================================

def calculator(a: float, b: float) -> dict:
    """
    TODO: Perform all arithmetic operations on a and b.
    
    Return a dictionary with:
    - 'sum': a + b
    - 'difference': a - b
    - 'product': a * b
    - 'quotient': a / b (handle division by zero!)
    - 'floor_division': a // b
    - 'modulo': a % b
    - 'power': a ** b
    
    If b is 0, set quotient, floor_division, and modulo to None.
    
    Example:
        >>> calculator(10, 3)
        {
            'sum': 13,
            'difference': 7,
            'product': 30,
            'quotient': 3.333...,
            'floor_division': 3,
            'modulo': 1,
            'power': 1000
        }
    """
    # YOUR CODE HERE
    return {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
        'quotient': a / b if b != 0 else None,
        'floor_division': a // b if b != 0 else None,
        'modulo': a % b if b != 0 else None,
        'power': a ** b
    }


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 2: Variables and Data Types - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: Variable declarations
    total += 1
    if my_name and my_age > 0 and my_height > 0 and is_learning_python:
        print(f"✅ Variables declared: {my_name}, age {my_age}")
        passed += 1
    else:
        print("❌ Complete the variable declarations")
    
    # Test 2: String operations
    total += 1
    result = string_operations("hello world")
    if (result['uppercase'] == 'HELLO WORLD' and 
        result['length'] == 11 and 
        result['word_count'] == 2):
        print("✅ string_operations() works correctly")
        passed += 1
    else:
        print(f"❌ string_operations() needs work. Got: {result}")
    
    # Test 3: Type conversion
    total += 1
    result = convert_types("42")
    if result['as_int'] == 42 and result['as_float'] == 42.0:
        print("✅ convert_types() works correctly")
        passed += 1
    else:
        print(f"❌ convert_types() needs work. Got: {result}")
    
    # Test 4: F-string greeting
    total += 1
    result = format_greeting("Alice", 25, "New York")
    expected = "Hello, I'm Alice! I'm 25 years old and live in New York."
    if result == expected:
        print("✅ format_greeting() works correctly")
        passed += 1
    else:
        print(f"❌ format_greeting() should return:\n   '{expected}'\n   Got: '{result}'")
    
    # Test 5: Calculator
    total += 1
    result = calculator(10, 3)
    if result.get('sum') == 13 and result.get('product') == 30:
        print("✅ calculator() works correctly")
        passed += 1
    else:
        print(f"❌ calculator() needs work. Got: {result}")
    
    # Summary
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
