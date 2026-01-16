#!/usr/bin/env python3
"""
Day 5 Exercise: List Comprehensions & AI Patterns
==================================================
"""

from typing import List, Dict, Any, Tuple, Optional

# =============================================================================
# EXERCISE 1: Basic List Comprehensions
# =============================================================================

def squares(n: int) -> List[int]:
    return [i ** 2 for i in range(1, n + 1)]


def evens_only(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]


def words_longer_than(words: List[str], min_length: int) -> List[str]:
    return [word for word in words if len(word) > min_length]


# =============================================================================
# EXERCISE 2: Transformations with Comprehensions
# =============================================================================

def extract_emails(users: List[Dict[str, str]]) -> List[str]:
    return [user['email'] for user in users]


def normalize_names(names: List[str]) -> List[str]:
    return [name.strip().capitalize() for name in names]


def prices_with_tax(prices: List[float], tax_rate: float) -> List[float]:
    return [round(price * (1 + tax_rate), 2) for price in prices]


# =============================================================================
# EXERCISE 3: Dictionary Comprehensions
# =============================================================================

def word_lengths(words: List[str]) -> Dict[str, int]:
    return {word: len(word) for word in words}


def invert_dict(d: Dict[str, int]) -> Dict[int, str]:
    return {value: key for key, value in d.items()}


def filter_dict_by_value(d: Dict[str, int], min_value: int) -> Dict[str, int]:
    return {key: value for key, value in d.items() if value >= min_value}


# =============================================================================
# EXERCISE 4: Set Comprehensions
# =============================================================================

def unique_first_letters(words: List[str]) -> set:
    return {word[0].lower() for word in words}


def common_elements(list1: List[int], list2: List[int]) -> set:
    return set(list1) & set(list2)


# =============================================================================
# EXERCISE 5: Nested Comprehensions (Data Engineering!)
# =============================================================================

def flatten_matrix(matrix: List[List[int]]) -> List[int]:
    """
    Flatten a 2D matrix into a 1D list.
    
    Example:
        >>> flatten_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return [item for row in matrix for item in row]


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose a matrix (swap rows and columns).
    
    Example:
        >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    return [ list(row)  for row in zip(*matrix) ]    

def extract_column(table: List[Dict[str, Any]], column: str) -> List[Any]:
    """
    Extract a single column from a table (list of dicts).
    
    Example:
        >>> extract_column([{'name': 'Alice'}, {'name': 'Bob'}], 'name')
        ['Alice', 'Bob']
    """
    return [row[column] for row in table]


def group_by(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """
    Group items by a key (like SQL GROUP BY).
    
    Example:
        >>> group_by([{'dept': 'Eng'}, {'dept': 'Sales'}, {'dept': 'Eng'}], 'dept')
        {'Eng': [..., ...], 'Sales': [...]}
    """
    result = {}
    for item in items:
        group_value = item[key]
        if group_value not in result:
            result[group_value] = []
        result[group_value].append(item)
    return result

# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 5: List Comprehensions - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    total += 1
    if squares(5) == [1, 4, 9, 16, 25]:
        print("✅ squares()")
        passed += 1
    else:
        print("❌ squares()")
    
    total += 1
    if evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]:
        print("✅ evens_only()")
        passed += 1
    else:
        print("❌ evens_only()")
    
    total += 1
    if words_longer_than(['cat', 'elephant', 'dog'], 4) == ['elephant']:
        print("✅ words_longer_than()")
        passed += 1
    else:
        print("❌ words_longer_than()")
    
    total += 1
    if extract_emails([{'name': 'Alice', 'email': 'a@b.com'}]) == ['a@b.com']:
        print("✅ extract_emails()")
        passed += 1
    else:
        print("❌ extract_emails()")
    
    total += 1
    if normalize_names(['  alice  ', 'BOB']) == ['Alice', 'Bob']:
        print("✅ normalize_names()")
        passed += 1
    else:
        print("❌ normalize_names()")
    
    total += 1
    if prices_with_tax([10.00], 0.08) == [10.8]:
        print("✅ prices_with_tax()")
        passed += 1
    else:
        print("❌ prices_with_tax()")
    
    total += 1
    if word_lengths(['cat', 'dog']) == {'cat': 3, 'dog': 3}:
        print("✅ word_lengths()")
        passed += 1
    else:
        print("❌ word_lengths()")
    
    total += 1
    if invert_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}:
        print("✅ invert_dict()")
        passed += 1
    else:
        print("❌ invert_dict()")
    
    total += 1
    if filter_dict_by_value({'a': 1, 'b': 5}, 4) == {'b': 5}:
        print("✅ filter_dict_by_value()")
        passed += 1
    else:
        print("❌ filter_dict_by_value()")
    
    total += 1
    if unique_first_letters(['Apple', 'apricot']) == {'a'}:
        print("✅ unique_first_letters()")
        passed += 1
    else:
        print("❌ unique_first_letters()")
    
    total += 1
    if common_elements([1, 2, 3], [2, 3, 4]) == {2, 3}:
        print("✅ common_elements()")
        passed += 1
    else:
        print("❌ common_elements()")
    
    total += 1
    if flatten_matrix([[1, 2], [3, 4]]) == [1, 2, 3, 4]:
        print("✅ flatten_matrix()")
        passed += 1
    else:
        print("❌ flatten_matrix()")
    
    total += 1
    if transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]:
        print("✅ transpose_matrix()")
        passed += 1
    else:
        print("❌ transpose_matrix()")
    
    total += 1
    if extract_column([{'name': 'A'}, {'name': 'B'}], 'name') == ['A', 'B']:
        print("✅ extract_column()")
        passed += 1
    else:
        print("❌ extract_column()")
    
    total += 1
    items = [{'g': 'a'}, {'g': 'a'}, {'g': 'b'}]
    grouped = group_by(items, 'g')
    if grouped and len(grouped.get('a', [])) == 2 and len(grouped.get('b', [])) == 1:
        print("✅ group_by()")
        passed += 1
    else:
        print("❌ group_by()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
