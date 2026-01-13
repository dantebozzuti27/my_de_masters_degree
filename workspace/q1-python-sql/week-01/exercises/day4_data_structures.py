#!/usr/bin/env python3
"""
Day 4 Exercise: Data Types Deep Dive
=====================================

Master lists, tuples, dictionaries, and sets.

Instructions:
1. Complete each TODO section
2. Run: python day4_data_structures.py
3. All tests should pass ✅
"""

from typing import List, Dict, Set, Tuple, Any, Optional

# =============================================================================
# EXERCISE 1: List Operations
# =============================================================================

def list_statistics(numbers: List[int]) -> Dict[str, Any]:
    """
    TODO: Calculate statistics for a list of numbers.
    
    Return a dictionary with:
    - 'count': number of elements
    - 'sum': sum of all elements
    - 'min': minimum value
    - 'max': maximum value
    - 'average': average value (float)
    - 'sorted_asc': list sorted ascending
    - 'sorted_desc': list sorted descending
    - 'unique': list with duplicates removed (preserving order)
    
    Example:
        >>> list_statistics([5, 2, 8, 2, 9, 1, 5])
        {
            'count': 7,
            'sum': 32,
            'min': 1,
            'max': 9,
            'average': 4.571...,
            'sorted_asc': [1, 2, 2, 5, 5, 8, 9],
            'sorted_desc': [9, 8, 5, 5, 2, 2, 1],
            'unique': [5, 2, 8, 9, 1]
        }
    """
    # YOUR CODE HERE
    return {}


# =============================================================================
# EXERCISE 2: List Comprehensions
# =============================================================================

def transform_data(data: List[str]) -> Dict[str, List]:
    """
    TODO: Transform a list of strings using list comprehensions.
    
    Return a dictionary with:
    - 'uppercase': all strings in uppercase
    - 'lengths': length of each string
    - 'first_chars': first character of each string
    - 'long_words': only strings with 5+ characters
    - 'cleaned': stripped and lowercased, excluding empty strings
    
    Example:
        >>> transform_data(['  Hello ', 'WORLD', '', '  Python  ', 'Go'])
        {
            'uppercase': ['  HELLO ', 'WORLD', '', '  PYTHON  ', 'GO'],
            'lengths': [8, 5, 0, 10, 2],
            'first_chars': [' ', 'W', '', ' ', 'G'],
            'long_words': ['  Hello ', 'WORLD', '  Python  '],
            'cleaned': ['hello', 'world', 'python', 'go']
        }
    """
    # YOUR CODE HERE - use list comprehensions!
    return {}


# =============================================================================
# EXERCISE 3: Dictionary Operations
# =============================================================================

def analyze_user(user: Dict[str, Any]) -> Dict[str, Any]:
    """
    TODO: Analyze a user profile dictionary.
    
    Input user dict has: name, email, age, skills (list), active (bool)
    
    Return a dictionary with:
    - 'name_length': length of the name
    - 'email_domain': domain part of email (after @)
    - 'is_adult': True if age >= 18
    - 'skill_count': number of skills
    - 'first_skill': first skill or None if no skills
    - 'status': 'active' or 'inactive' based on active field
    
    Example:
        >>> user = {
        ...     'name': 'Dante',
        ...     'email': 'dante@example.com',
        ...     'age': 28,
        ...     'skills': ['Python', 'SQL', 'AWS'],
        ...     'active': True
        ... }
        >>> analyze_user(user)
        {
            'name_length': 5,
            'email_domain': 'example.com',
            'is_adult': True,
            'skill_count': 3,
            'first_skill': 'Python',
            'status': 'active'
        }
    """
    # YOUR CODE HERE
    return {}


def merge_user_data(user1: Dict, user2: Dict) -> Dict:
    """
    TODO: Merge two user dictionaries.
    
    - user2 values override user1 values for same keys
    - 'skills' lists should be combined (no duplicates)
    - Return the merged dictionary
    
    Example:
        >>> user1 = {'name': 'Alice', 'age': 25, 'skills': ['Python']}
        >>> user2 = {'age': 26, 'skills': ['SQL', 'Python'], 'city': 'NYC'}
        >>> merge_user_data(user1, user2)
        {'name': 'Alice', 'age': 26, 'skills': ['Python', 'SQL'], 'city': 'NYC'}
    """
    # YOUR CODE HERE
    return {}


# =============================================================================
# EXERCISE 4: Set Operations
# =============================================================================

def analyze_teams(team_a: Set[str], team_b: Set[str]) -> Dict[str, Set[str]]:
    """
    TODO: Analyze two teams using set operations.
    
    Return a dictionary with:
    - 'all_members': everyone in either team
    - 'in_both': people in both teams
    - 'only_a': people only in team A
    - 'only_b': people only in team B
    - 'not_in_both': people in one team but not the other
    
    Example:
        >>> team_a = {'Alice', 'Bob', 'Charlie'}
        >>> team_b = {'Bob', 'Diana', 'Eve'}
        >>> analyze_teams(team_a, team_b)
        {
            'all_members': {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'},
            'in_both': {'Bob'},
            'only_a': {'Alice', 'Charlie'},
            'only_b': {'Diana', 'Eve'},
            'not_in_both': {'Alice', 'Charlie', 'Diana', 'Eve'}
        }
    """
    # YOUR CODE HERE
    return {}


# =============================================================================
# EXERCISE 5: Nested Data Structures (Data Engineering Pattern!)
# =============================================================================

# This is a common pattern in data engineering - representing database schemas

DATABASE_SCHEMA = [
    {
        "table_name": "users",
        "columns": ["id", "name", "email", "created_at"],
        "row_count": 150000,
        "primary_key": "id",
        "foreign_keys": []
    },
    {
        "table_name": "orders",
        "columns": ["id", "user_id", "total", "status", "created_at"],
        "row_count": 500000,
        "primary_key": "id",
        "foreign_keys": [{"column": "user_id", "references": "users.id"}]
    },
    {
        "table_name": "products",
        "columns": ["id", "name", "price", "category_id"],
        "row_count": 5000,
        "primary_key": "id",
        "foreign_keys": [{"column": "category_id", "references": "categories.id"}]
    },
    {
        "table_name": "order_items",
        "columns": ["id", "order_id", "product_id", "quantity", "price"],
        "row_count": 1500000,
        "primary_key": "id",
        "foreign_keys": [
            {"column": "order_id", "references": "orders.id"},
            {"column": "product_id", "references": "products.id"}
        ]
    }
]


def find_table(schema: List[Dict], table_name: str) -> Optional[Dict]:
    """
    TODO: Find a table by name in the schema.
    
    Return the table dict if found, None otherwise.
    """
    # YOUR CODE HERE
    pass


def get_total_rows(schema: List[Dict]) -> int:
    """
    TODO: Calculate total rows across all tables.
    """
    # YOUR CODE HERE
    pass


def list_table_names(schema: List[Dict]) -> List[str]:
    """
    TODO: Return a list of all table names.
    """
    # YOUR CODE HERE
    pass


def get_tables_with_foreign_keys(schema: List[Dict]) -> List[str]:
    """
    TODO: Return names of tables that have foreign keys.
    """
    # YOUR CODE HERE
    pass


def find_tables_referencing(schema: List[Dict], table_name: str) -> List[str]:
    """
    TODO: Find all tables that have a foreign key referencing the given table.
    
    Example:
        >>> find_tables_referencing(DATABASE_SCHEMA, 'users')
        ['orders']
    """
    # YOUR CODE HERE
    pass


def schema_summary(schema: List[Dict]) -> Dict:
    """
    TODO: Create a summary of the database schema.
    
    Return:
    {
        'total_tables': number of tables,
        'total_rows': total rows across all tables,
        'total_columns': total columns across all tables,
        'largest_table': name of table with most rows,
        'tables_with_fks': list of tables with foreign keys
    }
    """
    # YOUR CODE HERE
    return {}


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 4: Data Structures - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test list_statistics
    total += 1
    result = list_statistics([5, 2, 8, 2, 9, 1, 5])
    if result.get('count') == 7 and result.get('sum') == 32:
        print("✅ list_statistics() works correctly")
        passed += 1
    else:
        print(f"❌ list_statistics() needs work. Got: {result}")
    
    # Test transform_data
    total += 1
    result = transform_data(['Hello', 'WORLD', 'Python'])
    if result.get('uppercase') == ['HELLO', 'WORLD', 'PYTHON']:
        print("✅ transform_data() works correctly")
        passed += 1
    else:
        print(f"❌ transform_data() needs work. Got: {result}")
    
    # Test analyze_user
    total += 1
    user = {'name': 'Dante', 'email': 'dante@example.com', 'age': 28, 
            'skills': ['Python', 'SQL'], 'active': True}
    result = analyze_user(user)
    if result.get('email_domain') == 'example.com' and result.get('skill_count') == 2:
        print("✅ analyze_user() works correctly")
        passed += 1
    else:
        print(f"❌ analyze_user() needs work. Got: {result}")
    
    # Test analyze_teams
    total += 1
    team_a = {'Alice', 'Bob', 'Charlie'}
    team_b = {'Bob', 'Diana'}
    result = analyze_teams(team_a, team_b)
    if result.get('in_both') == {'Bob'} and result.get('only_a') == {'Alice', 'Charlie'}:
        print("✅ analyze_teams() works correctly")
        passed += 1
    else:
        print(f"❌ analyze_teams() needs work. Got: {result}")
    
    # Test schema functions
    total += 1
    if (find_table(DATABASE_SCHEMA, 'users') is not None and
        get_total_rows(DATABASE_SCHEMA) == 2155000 and
        len(list_table_names(DATABASE_SCHEMA)) == 4):
        print("✅ Schema functions work correctly")
        passed += 1
    else:
        print("❌ Schema functions need work")
    
    # Test schema_summary
    total += 1
    summary = schema_summary(DATABASE_SCHEMA)
    if (summary.get('total_tables') == 4 and 
        summary.get('largest_table') == 'order_items'):
        print("✅ schema_summary() works correctly")
        passed += 1
    else:
        print(f"❌ schema_summary() needs work. Got: {summary}")
    
    # Summary
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
        print("Week 1 Complete! Commit your code and move to Week 2!")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
