#!/usr/bin/env python3
"""
Day 8 Exercise: Error Handling & Defensive Code
================================================
In production, things WILL go wrong. APIs fail, files disappear, 
data is malformed. This is how you build code that handles it gracefully.
"""

import json
from typing import Any, Dict, List, Optional, Tuple, Union
from datetime import datetime

# =============================================================================
# EXERCISE 1: Basic Exception Handling
# =============================================================================

def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Divide a by b, returning None if division by zero.
    
    Example:
        >>> safe_divide(10, 2)
        5.0
        >>> safe_divide(10, 0)
        None
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def safe_int_convert(value: str) -> Optional[int]:
    """
    Convert a string to integer, returning None if conversion fails.
    
    Example:
        >>> safe_int_convert("42")
        42
        >>> safe_int_convert("not a number")
        None
    """
    try:
        return int(value)
    except ValueError:
        return None


def safe_json_parse(json_string: str) -> Tuple[Optional[Dict], Optional[str]]:
    """
    Parse JSON string, returning (data, None) on success 
    or (None, error_message) on failure.
    
    This pattern is common in production code!
    
    Example:
        >>> safe_json_parse('{"name": "Alice"}')
        ({'name': 'Alice'}, None)
        >>> safe_json_parse('invalid json')
        (None, 'JSONDecodeError: ...')
    """
    try:
        return (json.loads(json_string), None)
    except json.JSONDecodeError as e:
        return (None, str(e))


# =============================================================================
# EXERCISE 2: Handling Multiple Exception Types
# =============================================================================

def get_value_safely(data: Dict, key: str, default: Any = None) -> Any:
    """
    Get a value from a dict with a default if key missing or data is None.
    
    Example:
        >>> get_value_safely({'a': 1}, 'a')
        1
        >>> get_value_safely({'a': 1}, 'b', 'default')
        'default'
        >>> get_value_safely(None, 'a', 'default')
        'default'
    """
    if data is None:
        return default
    return data.get(key, default)

def safe_list_access(lst: List, index: int, default: Any = None) -> Any:
    """
    Safely access a list index with a default value.
    
    Example:
        >>> safe_list_access([1, 2, 3], 1)
        2
        >>> safe_list_access([1, 2, 3], 10, 'not found')
        'not found'
    """
    try:
        return lst[index]
    except (IndexError, TypeError):
        return default


def process_api_response(response: Dict) -> Dict[str, Any]:
    """
    Process an API response that might be malformed.
    
    Expected structure:
    {'status': 'success', 'data': {'users': [...], 'count': N}}
    
    Return:
    {'success': bool, 'users': list, 'count': int, 'error': str or None}
    
    Handle cases where:
    - response is None
    - 'data' key is missing
    - 'users' is not a list
    - 'count' is not an integer
    
    Example:
        >>> process_api_response({'status': 'success', 'data': {'users': [{'id': 1}], 'count': 1}})
        {'success': True, 'users': [{'id': 1}], 'count': 1, 'error': None}
        
        >>> process_api_response(None)
        {'success': False, 'users': [], 'count': 0, 'error': 'Response is None'}
    """
    if response is None:
        return{'success': False, 'users': [], 'count': 0, 'error': 'Response is None'}
    try:
        data = response.get('data', {})
        users = data.get('users', [])
        count = data.get('count', 0)
        
        if not isinstance(users, list):
            users = []
        if not isinstance(count, int):
            count = len(users)
        success = response.get('status') == 'success'
        return {
            'success': success,
            'users': users,
            'count': count,
            'error': None if success else 'Request Failed'
        }
    except Exception as e:
        return {'success': False, 'users': [], 'count': 0, 'error': str(e)}


# =============================================================================
# EXERCISE 3: Raising Exceptions
# =============================================================================

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class DataProcessingError(Exception):
    """Custom exception for data processing errors."""
    pass


def validate_email(email: str) -> str:
    """
    Validate an email address. Return the email if valid,
    raise ValidationError if invalid.
    
    Basic validation:
    - Must contain exactly one @
    - Must have something before and after @
    - Part after @ must contain at least one .
    
    Example:
        >>> validate_email("user@example.com")
        'user@example.com'
        >>> validate_email("invalid")
        ValidationError: Invalid email format: invalid
    """
    if '@' not in email:
        raise ValidationError(f"Invalid email format: {email}")
    parts = email.split('@')
    if len(parts) != 2:
        raise ValidationError(f"Invalid email format: {email}")
    local, domain = parts
    if not local or '.' not in domain:
        raise ValidationError(f"Invalid email format: {email}")
    return email


def validate_age(age: Any) -> int:
    """
    Validate an age value. Return the age as int if valid,
    raise ValidationError if invalid.
    
    Validation rules:
    - Must be convertible to integer
    - Must be between 0 and 150
    
    Example:
        >>> validate_age(25)
        25
        >>> validate_age("30")
        30
        >>> validate_age(-5)
        ValidationError: Age must be between 0 and 150
    """
    try:
        age_int = int(age)
    except (ValueError, TypeError):
        raise ValidationError(f"Age must be a valid number: {age}")
    if age_int < 0 or age_int > 150:
        raise ValidationError ("Age must be between 0 and 150")
    return age_int


def validate_user_data(user: Dict) -> Dict:
    """
    Validate a user dictionary.
    
    Required fields: 'name', 'email', 'age'
    
    If valid, return the user dict with validated values.
    If invalid, raise ValidationError with a helpful message.
    
    Example:
        >>> validate_user_data({'name': 'Alice', 'email': 'alice@test.com', 'age': 30})
        {'name': 'Alice', 'email': 'alice@test.com', 'age': 30}
        
        >>> validate_user_data({'name': 'Bob'})
        ValidationError: Missing required field: email
    """
    for field in {'name', 'email', 'age'}:
        if field not in user:
            raise ValidationError(f"Missing required field: {field}")
    validate_email(user['email'])
    validate_age(user['age'])
    return user


# =============================================================================
# EXERCISE 4: Context Managers for Error Handling
# =============================================================================

def safe_file_read(filepath: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Safely read a file, returning (content, None) on success
    or (None, error_message) on failure.
    
    Handle:
    - FileNotFoundError
    - PermissionError
    - Other IOErrors
    
    Example:
        >>> safe_file_read('exists.txt')
        ('file content', None)
        >>> safe_file_read('missing.txt')
        (None, 'File not found: missing.txt')
    """
    try:
        with open(filepath, 'r') as f:
            return (f.read(), None)
    except FileNotFoundError:
        return (None, f'File not found: {filepath}')
    except PermissionError:
        return (None, f'Permission denied: {filepath}')
    except Exception as e:
        return (None, str(e))


def parse_config_file(filepath: str) -> Dict[str, Any]:
    """
    Parse a JSON config file with comprehensive error handling.
    
    Return a dict with:
    - 'success': bool
    - 'config': the parsed config or empty dict
    - 'error': error message or None
    - 'error_type': 'file_not_found' | 'permission_denied' | 'invalid_json' | None
    
    Example:
        >>> parse_config_file('valid_config.json')
        {'success': True, 'config': {...}, 'error': None, 'error_type': None}
        
        >>> parse_config_file('missing.json')
        {'success': False, 'config': {}, 'error': '...', 'error_type': 'file_not_found'}
    """
    try:
        with open(filepath, 'r') as f:
            config = json.load(f)
        return {
            'success': True,
            'config': config,
            'error': None,
            'error_type': None
        }
    except FileNotFoundError:
        return {
            'success': False,
            'config': {},
            'error': f'File not found: {filepath}',
            'error_type': 'file_not_found'
        }
    except PermissionError:
        return {
            'success': False,
            'config': {},
            'error': f'Permission denied: {filepath}',
            'error_type': 'permission_denied'
    }
    except json.JSONDecodeError as e:
        return {
            'success': False,
            'config': {},
            'error': str(e),
            'error_type': 'invalid_json'
        }


# =============================================================================
# EXERCISE 5: Retry Logic
# =============================================================================

def retry_operation(operation, max_attempts: int = 3, default: Any = None) -> Any:
    """
    Retry an operation up to max_attempts times.
    Return the result on success, or default after all attempts fail.
    
    This is a simplified version of what you'd use for flaky API calls.
    
    Example:
        >>> counter = [0]
        >>> def flaky():
        ...     counter[0] += 1
        ...     if counter[0] < 3:
        ...         raise ValueError("Not yet")
        ...     return "success"
        >>> retry_operation(flaky, max_attempts=3)
        'success'
    """
    for attempt in range(max_attempts):
        try:
            return operation()
        except Exception:
            continue
    return default


def fetch_with_retry(fetch_func, url: str, max_retries: int = 3) -> Dict[str, Any]:
    """
    Fetch data from a URL with retry logic.
    
    Return a dict with:
    - 'success': bool
    - 'data': the fetched data or None
    - 'attempts': number of attempts made
    - 'error': last error message or None
    
    Note: fetch_func is a mock function that takes a URL and returns data or raises an exception.
    
    Example:
        >>> def mock_fetch(url):
        ...     return {'users': []}
        >>> fetch_with_retry(mock_fetch, 'http://api.example.com/users')
        {'success': True, 'data': {'users': []}, 'attempts': 1, 'error': None}
    """
    for attempt in range(1, max_retries + 1):
        try:
            data = fetch_func(url)
            return {'success': True, 'data': data, 'attempts': attempt, 'error': None}
        except Exception as e:
            last_error = str(e)
    return {'success': False, 'data': None, 'attempts': max_retries, 'error': last_error}


# =============================================================================
# EXERCISE 6: Defensive Programming Patterns
# =============================================================================

def process_records(records: Any) -> List[Dict]:
    """
    Process a list of records defensively.
    
    - If records is None, return empty list
    - If records is not a list, wrap it in a list
    - Filter out None values
    - Filter out non-dict values
    
    Example:
        >>> process_records([{'id': 1}, None, {'id': 2}])
        [{'id': 1}, {'id': 2}]
        >>> process_records({'id': 1})
        [{'id': 1}]
        >>> process_records(None)
        []
    """
    if records is None:
        return []
    if not isinstance(records, list):
        records = [records]
    return [r for r in records if isinstance(r, dict)]



def safe_chain_get(data: Dict, *keys, default: Any = None) -> Any:
    """
    Safely get a nested value from a dict without raising KeyError.
    
    Example:
        >>> data = {'user': {'profile': {'name': 'Alice'}}}
        >>> safe_chain_get(data, 'user', 'profile', 'name')
        'Alice'
        >>> safe_chain_get(data, 'user', 'missing', 'key', default='N/A')
        'N/A'
    """
    current = data
    for key in keys:
        try:
            current = current[key]
        except (KeyError, TypeError, IndexError):
            return default
    return current


def coalesce(*values) -> Any:
    """
    Return the first non-None value, or None if all are None.
    
    This is like SQL's COALESCE function.
    
    Example:
        >>> coalesce(None, None, 'default')
        'default'
        >>> coalesce('first', 'second')
        'first'
        >>> coalesce(None, None)
        None
    """
    for value in values:
        if value is not None:
            return value
    return None


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 8: Error Handling & Defensive Code - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: safe_divide
    total += 1
    if safe_divide(10, 2) == 5.0 and safe_divide(10, 0) is None:
        print("✅ safe_divide()")
        passed += 1
    else:
        print("❌ safe_divide()")
    
    # Test 2: safe_int_convert
    total += 1
    if safe_int_convert("42") == 42 and safe_int_convert("not a number") is None:
        print("✅ safe_int_convert()")
        passed += 1
    else:
        print("❌ safe_int_convert()")
    
    # Test 3: safe_json_parse
    total += 1
    data, err = safe_json_parse('{"name": "Alice"}') if safe_json_parse('{"name": "Alice"}') else (None, None)
    data2, err2 = safe_json_parse('invalid') if safe_json_parse('invalid') else (None, None)
    if data == {'name': 'Alice'} and err is None and data2 is None and err2 is not None:
        print("✅ safe_json_parse()")
        passed += 1
    else:
        print("❌ safe_json_parse()")
    
    # Test 4: get_value_safely
    total += 1
    if get_value_safely({'a': 1}, 'a') == 1 and \
       get_value_safely({'a': 1}, 'b', 'default') == 'default' and \
       get_value_safely(None, 'a', 'default') == 'default':
        print("✅ get_value_safely()")
        passed += 1
    else:
        print("❌ get_value_safely()")
    
    # Test 5: safe_list_access
    total += 1
    if safe_list_access([1, 2, 3], 1) == 2 and safe_list_access([1, 2, 3], 10, 'not found') == 'not found':
        print("✅ safe_list_access()")
        passed += 1
    else:
        print("❌ safe_list_access()")
    
    # Test 6: process_api_response
    total += 1
    result = process_api_response({'status': 'success', 'data': {'users': [{'id': 1}], 'count': 1}})
    if result and result.get('success') == True and result.get('count') == 1:
        print("✅ process_api_response()")
        passed += 1
    else:
        print("❌ process_api_response()")
    
    # Test 7: validate_email
    total += 1
    try:
        valid = validate_email("user@example.com")
        try:
            validate_email("invalid")
            print("❌ validate_email()")
        except ValidationError:
            if valid == "user@example.com":
                print("✅ validate_email()")
                passed += 1
            else:
                print("❌ validate_email()")
    except:
        print("❌ validate_email()")
    
    # Test 8: validate_age
    total += 1
    try:
        age1 = validate_age(25)
        age2 = validate_age("30")
        try:
            validate_age(-5)
            print("❌ validate_age()")
        except ValidationError:
            if age1 == 25 and age2 == 30:
                print("✅ validate_age()")
                passed += 1
            else:
                print("❌ validate_age()")
    except:
        print("❌ validate_age()")
    
    # Test 9: validate_user_data
    total += 1
    try:
        valid_user = validate_user_data({'name': 'Alice', 'email': 'alice@test.com', 'age': 30})
        try:
            validate_user_data({'name': 'Bob'})
            print("❌ validate_user_data()")
        except ValidationError:
            if valid_user.get('name') == 'Alice':
                print("✅ validate_user_data()")
                passed += 1
            else:
                print("❌ validate_user_data()")
    except:
        print("❌ validate_user_data()")
    
    # Test 10: retry_operation
    total += 1
    counter = [0]
    def flaky():
        counter[0] += 1
        if counter[0] < 3:
            raise ValueError("Not yet")
        return "success"
    if retry_operation(flaky, max_attempts=3) == "success":
        print("✅ retry_operation()")
        passed += 1
    else:
        print("❌ retry_operation()")
    
    # Test 11: process_records
    total += 1
    if process_records([{'id': 1}, None, {'id': 2}]) == [{'id': 1}, {'id': 2}] and \
       process_records(None) == [] and \
       process_records({'id': 1}) == [{'id': 1}]:
        print("✅ process_records()")
        passed += 1
    else:
        print("❌ process_records()")
    
    # Test 12: safe_chain_get
    total += 1
    data = {'user': {'profile': {'name': 'Alice'}}}
    if safe_chain_get(data, 'user', 'profile', 'name') == 'Alice' and \
       safe_chain_get(data, 'user', 'missing', 'key', default='N/A') == 'N/A':
        print("✅ safe_chain_get()")
        passed += 1
    else:
        print("❌ safe_chain_get()")
    
    # Test 13: coalesce
    total += 1
    if coalesce(None, None, 'default') == 'default' and \
       coalesce('first', 'second') == 'first' and \
       coalesce(None, None) is None:
        print("✅ coalesce()")
        passed += 1
    else:
        print("❌ coalesce()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
