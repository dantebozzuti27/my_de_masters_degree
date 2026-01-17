#!/usr/bin/env python3
"""
Day 10 Exercise: Lambda Functions & Functional Programming
==========================================================
Anonymous functions, map, filter, reduce - when (and when not) to use them.
These patterns power data transformation in pandas, PySpark, and more.
"""

from typing import Any, List, Dict, Callable, Optional, Iterable
from functools import reduce

# =============================================================================
# EXERCISE 1: Lambda Basics
# =============================================================================

# Convert these regular functions to lambda expressions stored in variables

def double_regular(x):
    return x * 2

# Your lambda version:
double = None  # Replace with lambda


def add_regular(a, b):
    return a + b

add = None  # Replace with lambda


def is_even_regular(n):
    return n % 2 == 0

is_even = None  # Replace with lambda


def get_name_regular(user):
    return user.get('name', 'Unknown')

get_name = None  # Replace with lambda


# =============================================================================
# EXERCISE 2: Map - Transform Every Element
# =============================================================================

def square_all(numbers: List[int]) -> List[int]:
    """
    Square each number using map().
    
    Example:
        >>> square_all([1, 2, 3, 4])
        [1, 4, 9, 16]
    """
    pass


def extract_emails(users: List[Dict]) -> List[str]:
    """
    Extract email from each user dict using map().
    
    Example:
        >>> users = [{'name': 'Alice', 'email': 'a@test.com'}, {'name': 'Bob', 'email': 'b@test.com'}]
        >>> extract_emails(users)
        ['a@test.com', 'b@test.com']
    """
    pass


def normalize_strings(strings: List[str]) -> List[str]:
    """
    Convert each string to lowercase and strip whitespace using map().
    
    Example:
        >>> normalize_strings(['  Hello  ', 'WORLD', '  Python  '])
        ['hello', 'world', 'python']
    """
    pass


def apply_discount(prices: List[float], discount: float) -> List[float]:
    """
    Apply a percentage discount to each price.
    
    Example:
        >>> apply_discount([100.0, 50.0, 200.0], 0.1)  # 10% discount
        [90.0, 45.0, 180.0]
    """
    pass


# =============================================================================
# EXERCISE 3: Filter - Select Elements
# =============================================================================

def filter_positive(numbers: List[int]) -> List[int]:
    """
    Keep only positive numbers using filter().
    
    Example:
        >>> filter_positive([-2, -1, 0, 1, 2])
        [1, 2]
    """
    pass


def filter_by_age(users: List[Dict], min_age: int) -> List[Dict]:
    """
    Keep only users with age >= min_age using filter().
    
    Example:
        >>> users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 17}]
        >>> filter_by_age(users, 18)
        [{'name': 'Alice', 'age': 25}]
    """
    pass


def filter_none_values(items: List[Any]) -> List[Any]:
    """
    Remove None values from a list using filter().
    
    Example:
        >>> filter_none_values([1, None, 2, None, 3])
        [1, 2, 3]
    """
    pass


def filter_long_words(words: List[str], min_length: int) -> List[str]:
    """
    Keep only words with length >= min_length.
    
    Example:
        >>> filter_long_words(['a', 'ab', 'abc', 'abcd'], 3)
        ['abc', 'abcd']
    """
    pass


# =============================================================================
# EXERCISE 4: Reduce - Combine Elements
# =============================================================================

def product_of_all(numbers: List[int]) -> int:
    """
    Calculate the product of all numbers using reduce().
    
    Example:
        >>> product_of_all([1, 2, 3, 4])
        24
    """
    pass


def find_max(numbers: List[int]) -> int:
    """
    Find the maximum value using reduce() (don't use max()).
    
    Example:
        >>> find_max([3, 1, 4, 1, 5, 9, 2, 6])
        9
    """
    pass


def flatten_lists(nested: List[List]) -> List:
    """
    Flatten a list of lists using reduce().
    
    Example:
        >>> flatten_lists([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
    """
    pass


def merge_dicts(dicts: List[Dict]) -> Dict:
    """
    Merge a list of dicts into one using reduce().
    Later dicts override earlier ones.
    
    Example:
        >>> merge_dicts([{'a': 1}, {'b': 2}, {'a': 3}])
        {'a': 3, 'b': 2}
    """
    pass


# =============================================================================
# EXERCISE 5: Combining Map, Filter, Reduce
# =============================================================================

def sum_of_squares_of_evens(numbers: List[int]) -> int:
    """
    Filter to even numbers, square them, then sum.
    
    Example:
        >>> sum_of_squares_of_evens([1, 2, 3, 4, 5, 6])
        56  # 2² + 4² + 6² = 4 + 16 + 36
    """
    pass


def get_active_user_names(users: List[Dict]) -> List[str]:
    """
    Filter to active users, then extract their names (uppercase).
    
    Example:
        >>> users = [
        ...     {'name': 'Alice', 'active': True},
        ...     {'name': 'Bob', 'active': False},
        ...     {'name': 'Charlie', 'active': True}
        ... ]
        >>> get_active_user_names(users)
        ['ALICE', 'CHARLIE']
    """
    pass


def calculate_total_revenue(orders: List[Dict]) -> float:
    """
    Filter to completed orders, extract amounts, sum them.
    
    Example:
        >>> orders = [
        ...     {'id': 1, 'amount': 100.0, 'status': 'completed'},
        ...     {'id': 2, 'amount': 50.0, 'status': 'pending'},
        ...     {'id': 3, 'amount': 75.0, 'status': 'completed'}
        ... ]
        >>> calculate_total_revenue(orders)
        175.0
    """
    pass


# =============================================================================
# EXERCISE 6: Sorting with Lambda
# =============================================================================

def sort_by_length(strings: List[str]) -> List[str]:
    """
    Sort strings by their length.
    
    Example:
        >>> sort_by_length(['python', 'go', 'java', 'c'])
        ['c', 'go', 'java', 'python']
    """
    pass


def sort_by_field(records: List[Dict], field: str, reverse: bool = False) -> List[Dict]:
    """
    Sort records by a specific field.
    
    Example:
        >>> users = [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25}]
        >>> sort_by_field(users, 'name')
        [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
        >>> sort_by_field(users, 'age', reverse=True)
        [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25}]
    """
    pass


def sort_by_multiple(records: List[Dict], *fields) -> List[Dict]:
    """
    Sort records by multiple fields (priority left to right).
    
    Example:
        >>> data = [
        ...     {'dept': 'Sales', 'name': 'Bob'},
        ...     {'dept': 'Engineering', 'name': 'Alice'},
        ...     {'dept': 'Sales', 'name': 'Alice'}
        ... ]
        >>> sort_by_multiple(data, 'dept', 'name')
        [{'dept': 'Engineering', 'name': 'Alice'}, {'dept': 'Sales', 'name': 'Alice'}, {'dept': 'Sales', 'name': 'Bob'}]
    """
    pass


# =============================================================================
# EXERCISE 7: When NOT to Use Lambda
# =============================================================================

# Sometimes a named function is clearer than a lambda.
# Implement these as regular functions:

def calculate_tax(price: float, rate: float = 0.1) -> float:
    """
    Calculate tax amount (use named function, not lambda).
    
    Example:
        >>> calculate_tax(100.0)
        10.0
        >>> calculate_tax(100.0, 0.2)
        20.0
    """
    pass


def is_valid_email(email: str) -> bool:
    """
    Check if email is valid (basic check - has @ and . after @).
    Use named function for readability.
    
    Example:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("invalid")
        False
    """
    pass


def format_currency(amount: float, currency: str = "USD", decimals: int = 2) -> str:
    """
    Format a number as currency.
    Complex formatting = use named function.
    
    Example:
        >>> format_currency(1234.5)
        'USD 1,234.50'
        >>> format_currency(1234.5, currency="EUR")
        'EUR 1,234.50'
    """
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 10: Lambda & Functional Programming - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: Lambda basics
    total += 1
    try:
        if double and double(5) == 10 and add and add(2, 3) == 5 and \
           is_even and is_even(4) == True and get_name and get_name({'name': 'Alice'}) == 'Alice':
            print("✅ Lambda basics")
            passed += 1
        else:
            print("❌ Lambda basics")
    except:
        print("❌ Lambda basics")
    
    # Test 2: square_all
    total += 1
    if square_all([1, 2, 3, 4]) == [1, 4, 9, 16]:
        print("✅ square_all()")
        passed += 1
    else:
        print("❌ square_all()")
    
    # Test 3: extract_emails
    total += 1
    users = [{'name': 'Alice', 'email': 'a@test.com'}, {'name': 'Bob', 'email': 'b@test.com'}]
    if extract_emails(users) == ['a@test.com', 'b@test.com']:
        print("✅ extract_emails()")
        passed += 1
    else:
        print("❌ extract_emails()")
    
    # Test 4: normalize_strings
    total += 1
    if normalize_strings(['  Hello  ', 'WORLD', '  Python  ']) == ['hello', 'world', 'python']:
        print("✅ normalize_strings()")
        passed += 1
    else:
        print("❌ normalize_strings()")
    
    # Test 5: filter_positive
    total += 1
    if filter_positive([-2, -1, 0, 1, 2]) == [1, 2]:
        print("✅ filter_positive()")
        passed += 1
    else:
        print("❌ filter_positive()")
    
    # Test 6: filter_by_age
    total += 1
    users = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 17}]
    if filter_by_age(users, 18) == [{'name': 'Alice', 'age': 25}]:
        print("✅ filter_by_age()")
        passed += 1
    else:
        print("❌ filter_by_age()")
    
    # Test 7: product_of_all
    total += 1
    if product_of_all([1, 2, 3, 4]) == 24:
        print("✅ product_of_all()")
        passed += 1
    else:
        print("❌ product_of_all()")
    
    # Test 8: flatten_lists
    total += 1
    if flatten_lists([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]:
        print("✅ flatten_lists()")
        passed += 1
    else:
        print("❌ flatten_lists()")
    
    # Test 9: sum_of_squares_of_evens
    total += 1
    if sum_of_squares_of_evens([1, 2, 3, 4, 5, 6]) == 56:
        print("✅ sum_of_squares_of_evens()")
        passed += 1
    else:
        print("❌ sum_of_squares_of_evens()")
    
    # Test 10: get_active_user_names
    total += 1
    users = [
        {'name': 'Alice', 'active': True},
        {'name': 'Bob', 'active': False},
        {'name': 'Charlie', 'active': True}
    ]
    if get_active_user_names(users) == ['ALICE', 'CHARLIE']:
        print("✅ get_active_user_names()")
        passed += 1
    else:
        print("❌ get_active_user_names()")
    
    # Test 11: sort_by_length
    total += 1
    if sort_by_length(['python', 'go', 'java', 'c']) == ['c', 'go', 'java', 'python']:
        print("✅ sort_by_length()")
        passed += 1
    else:
        print("❌ sort_by_length()")
    
    # Test 12: sort_by_field
    total += 1
    users = [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 25}]
    if sort_by_field(users, 'name') == [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]:
        print("✅ sort_by_field()")
        passed += 1
    else:
        print("❌ sort_by_field()")
    
    # Test 13: calculate_tax
    total += 1
    if calculate_tax(100.0) == 10.0 and calculate_tax(100.0, 0.2) == 20.0:
        print("✅ calculate_tax()")
        passed += 1
    else:
        print("❌ calculate_tax()")
    
    # Test 14: is_valid_email
    total += 1
    if is_valid_email("user@example.com") == True and is_valid_email("invalid") == False:
        print("✅ is_valid_email()")
        passed += 1
    else:
        print("❌ is_valid_email()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
