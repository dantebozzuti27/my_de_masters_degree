#!/usr/bin/env python3
"""
Day 6 Exercise: Dictionaries & JSON
====================================
JSON is THE data format for APIs and data engineering.
Master it, and you master data interchange.
"""

import json
from typing import Dict, List, Any, Optional

# =============================================================================
# EXERCISE 1: Dictionary Basics
# =============================================================================

def create_user(name: str, email: str, age: int) -> Dict[str, Any]:
    """
    Create a user dictionary with the given fields.
    
    Example:
        >>> create_user("Alice", "alice@example.com", 30)
        {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}
    """
    return {'name': name, 'email': email, 'age': age}


def get_nested_value(data: Dict, *keys) -> Any:
    """
    Safely get a nested value from a dictionary.
    Return None if any key is missing.
    
    Example:
        >>> data = {'user': {'profile': {'name': 'Alice'}}}
        >>> get_nested_value(data, 'user', 'profile', 'name')
        'Alice'
        >>> get_nested_value(data, 'user', 'missing', 'name')
        None
    """
    result = data
    for key in keys:
        if result is None:
            return None
        result = result.get(key)
    return result


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """
    Merge two dictionaries. Values from dict2 override dict1.
    
    Example:
        >>> merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        {'a': 1, 'b': 3, 'c': 4}
    """
    return {**dict1, **dict2}


# =============================================================================
# EXERCISE 2: Dictionary Transformations
# =============================================================================

def invert_dict(d: Dict[str, int]) -> Dict[int, str]:
    """
    Swap keys and values in a dictionary.
    
    Example:
        >>> invert_dict({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    return {value: key for key, value in d.items()}


def filter_dict(d: Dict[str, int], min_value: int) -> Dict[str, int]:
    """
    Keep only entries where value >= min_value.
    
    Example:
        >>> filter_dict({'a': 1, 'b': 5, 'c': 3}, 3)
        {'b': 5, 'c': 3}
    """
    return {key: value for key, value in d.items() if value >= min_value}


def transform_keys(d: Dict[str, Any], transform_fn) -> Dict[str, Any]:
    """
    Apply a function to all keys in a dictionary.
    
    Example:
        >>> transform_keys({'Name': 'Alice', 'Age': 30}, str.lower)
        {'name': 'Alice', 'age': 30}
    """
    return {transform_fn(key): value for key, value in d.items()}


# =============================================================================
# EXERCISE 3: JSON Parsing (Critical for Data Engineering!)
# =============================================================================

# Sample API response (this is what you'll get from real APIs)
SAMPLE_API_RESPONSE = '''
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "department": "Engineering"},
            {"id": 2, "name": "Bob", "department": "Sales"},
            {"id": 3, "name": "Charlie", "department": "Engineering"}
        ],
        "total_count": 3
    },
    "metadata": {
        "request_id": "abc123",
        "timestamp": "2026-01-15T10:30:00Z"
    }
}
'''

def parse_api_response(json_string: str) -> Dict:
    """
    Parse a JSON string into a Python dictionary.
    
    Example:
        >>> result = parse_api_response('{"name": "test"}')
        >>> result['name']
        'test'
    """
    return json.loads(json_string)


def extract_users(api_response: Dict) -> List[Dict]:
    """
    Extract the list of users from the parsed API response.
    
    Example:
        >>> response = json.loads(SAMPLE_API_RESPONSE)
        >>> users = extract_users(response)
        >>> len(users)
        3
        >>> users[0]['name']
        'Alice'
    """
    return api_response['data']['users']


def get_users_by_department(api_response: Dict, department: str) -> List[str]:
    """
    Get names of all users in a specific department.
    
    Example:
        >>> response = json.loads(SAMPLE_API_RESPONSE)
        >>> get_users_by_department(response, 'Engineering')
        ['Alice', 'Charlie']
    """
    return [user['name'] for user in api_response['data']['users'] if user['department'] == department]


# =============================================================================
# EXERCISE 4: JSON Generation
# =============================================================================

def dict_to_json(d: Dict, pretty: bool = False) -> str:
    """
    Convert a dictionary to a JSON string.
    If pretty=True, format with indentation.
    
    Example:
        >>> dict_to_json({'name': 'test'})
        '{"name": "test"}'
    """
    return json.dumps(d)


def create_api_response(data: Any, success: bool = True) -> str:
    """
    Create a standardized API response JSON string.
    
    Example:
        >>> create_api_response({'id': 1}, success=True)
        '{"status": "success", "data": {"id": 1}}'
        >>> create_api_response("Not found", success=False)
        '{"status": "error", "message": "Not found"}'
    """
    if success:
        result = {"status": "success", "data": data}
    else:
        result = {"status": "error", "message": data}
    return json.dumps(result)


# =============================================================================
# EXERCISE 5: Real-World Data Transformations
# =============================================================================

# Sample data from a database (rows as dicts)
DATABASE_ROWS = [
    {'id': 1, 'first_name': 'Alice', 'last_name': 'Smith', 'salary': 75000},
    {'id': 2, 'first_name': 'Bob', 'last_name': 'Jones', 'salary': 65000},
    {'id': 3, 'first_name': 'Charlie', 'last_name': 'Brown', 'salary': 85000},
]

def rows_to_lookup(rows: List[Dict], key_field: str) -> Dict[Any, Dict]:
    """
    Convert a list of rows to a lookup dictionary by a key field.
    This is a common pattern for fast lookups!
    
    Example:
        >>> lookup = rows_to_lookup(DATABASE_ROWS, 'id')
        >>> lookup[2]['first_name']
        'Bob'
    """
    return {row[key_field]: row for row in rows}


def pluck(rows: List[Dict], field: str) -> List[Any]:
    """
    Extract a single field from each row.
    
    Example:
        >>> pluck(DATABASE_ROWS, 'first_name')
        ['Alice', 'Bob', 'Charlie']
    """
    return [row[field] for row in rows]


def rename_keys(row: Dict, mapping: Dict[str, str]) -> Dict:
    """
    Rename keys in a dictionary based on a mapping.
    Keys not in the mapping stay unchanged.
    
    Example:
        >>> rename_keys({'first_name': 'Alice'}, {'first_name': 'firstName'})
        {'firstName': 'Alice'}
    """
    return {mapping.get(key, key): value for key, value in row.items()}


def flatten_nested(data: Dict, separator: str = '.') -> Dict[str, Any]:
    """
    Flatten a nested dictionary.
    
    Example:
        >>> flatten_nested({'user': {'name': 'Alice', 'age': 30}})
        {'user.name': 'Alice', 'user.age': 30}
    """
    result = {}
    for key, value in data.items():
        if isinstance(value, dict):
            for nested_key, nested_value in flatten_nested(value, separator).items():
                result[key + separator + nested_key] = nested_value
        else:
            result[key] = value
    return result


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 6: Dictionaries & JSON - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Exercise 1
    total += 1
    result = create_user("Alice", "alice@example.com", 30)
    if result == {'name': 'Alice', 'email': 'alice@example.com', 'age': 30}:
        print("✅ create_user()")
        passed += 1
    else:
        print("❌ create_user()")
    
    total += 1
    data = {'user': {'profile': {'name': 'Alice'}}}
    if get_nested_value(data, 'user', 'profile', 'name') == 'Alice' and \
       get_nested_value(data, 'user', 'missing', 'name') is None:
        print("✅ get_nested_value()")
        passed += 1
    else:
        print("❌ get_nested_value()")
    
    total += 1
    if merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 3, 'c': 4}:
        print("✅ merge_dicts()")
        passed += 1
    else:
        print("❌ merge_dicts()")
    
    # Exercise 2
    total += 1
    if invert_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}:
        print("✅ invert_dict()")
        passed += 1
    else:
        print("❌ invert_dict()")
    
    total += 1
    if filter_dict({'a': 1, 'b': 5, 'c': 3}, 3) == {'b': 5, 'c': 3}:
        print("✅ filter_dict()")
        passed += 1
    else:
        print("❌ filter_dict()")
    
    total += 1
    if transform_keys({'Name': 'Alice', 'Age': 30}, str.lower) == {'name': 'Alice', 'age': 30}:
        print("✅ transform_keys()")
        passed += 1
    else:
        print("❌ transform_keys()")
    
    # Exercise 3
    total += 1
    if parse_api_response('{"name": "test"}') == {'name': 'test'}:
        print("✅ parse_api_response()")
        passed += 1
    else:
        print("❌ parse_api_response()")
    
    total += 1
    response = json.loads(SAMPLE_API_RESPONSE)
    users = extract_users(response)
    if users and len(users) == 3 and users[0]['name'] == 'Alice':
        print("✅ extract_users()")
        passed += 1
    else:
        print("❌ extract_users()")
    
    total += 1
    if get_users_by_department(response, 'Engineering') == ['Alice', 'Charlie']:
        print("✅ get_users_by_department()")
        passed += 1
    else:
        print("❌ get_users_by_department()")
    
    # Exercise 4
    total += 1
    if dict_to_json({'name': 'test'}) == '{"name": "test"}':
        print("✅ dict_to_json()")
        passed += 1
    else:
        print("❌ dict_to_json()")
    
    total += 1
    try:
        success_resp = json.loads(create_api_response({'id': 1}, success=True) or '{}')
        error_resp = json.loads(create_api_response("Not found", success=False) or '{}')
        if success_resp.get('status') == 'success' and error_resp.get('status') == 'error':
            print("✅ create_api_response()")
            passed += 1
        else:
            print("❌ create_api_response()")
    except:
        print("❌ create_api_response()")
    
    # Exercise 5
    total += 1
    lookup = rows_to_lookup(DATABASE_ROWS, 'id')
    if lookup and lookup.get(2, {}).get('first_name') == 'Bob':
        print("✅ rows_to_lookup()")
        passed += 1
    else:
        print("❌ rows_to_lookup()")
    
    total += 1
    if pluck(DATABASE_ROWS, 'first_name') == ['Alice', 'Bob', 'Charlie']:
        print("✅ pluck()")
        passed += 1
    else:
        print("❌ pluck()")
    
    total += 1
    if rename_keys({'first_name': 'Alice', 'age': 30}, {'first_name': 'firstName'}) == {'firstName': 'Alice', 'age': 30}:
        print("✅ rename_keys()")
        passed += 1
    else:
        print("❌ rename_keys()")
    
    total += 1
    flattened = flatten_nested({'user': {'name': 'Alice', 'age': 30}})
    if flattened == {'user.name': 'Alice', 'user.age': 30}:
        print("✅ flatten_nested()")
        passed += 1
    else:
        print("❌ flatten_nested()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
