#!/usr/bin/env python3
"""
Day 12 Exercise: Building Your First Utility Library
=====================================================
Create reusable code you'll use throughout the program.
This is your personal data engineering toolkit.
"""

from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
import json
import os

# =============================================================================
# EXERCISE 1: String Utilities
# =============================================================================

def snake_to_camel(s: str) -> str:
    """Convert snake_case to camelCase."""
    pass

def camel_to_snake(s: str) -> str:
    """Convert camelCase to snake_case."""
    pass

def truncate(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncate string to max_length, adding suffix if truncated."""
    pass

def slugify(s: str) -> str:
    """Convert string to URL-safe slug (lowercase, hyphens)."""
    pass

# =============================================================================
# EXERCISE 2: Collection Utilities
# =============================================================================

def chunk(items: List, size: int) -> List[List]:
    """Split list into chunks of given size."""
    pass

def flatten(nested: List) -> List:
    """Flatten arbitrarily nested lists."""
    pass

def unique_by(items: List[Dict], key: str) -> List[Dict]:
    """Remove duplicates based on a key field."""
    pass

def group_by(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """Group items by a key field."""
    pass

# =============================================================================
# EXERCISE 3: Dict Utilities
# =============================================================================

def deep_get(data: Dict, path: str, default: Any = None) -> Any:
    """Get nested value using dot notation: 'user.profile.name'"""
    pass

def deep_set(data: Dict, path: str, value: Any) -> Dict:
    """Set nested value using dot notation."""
    pass

def pick(d: Dict, keys: List[str]) -> Dict:
    """Return dict with only specified keys."""
    pass

def omit(d: Dict, keys: List[str]) -> Dict:
    """Return dict without specified keys."""
    pass

# =============================================================================
# EXERCISE 4: Date Utilities
# =============================================================================

def parse_date(s: str) -> Optional[datetime]:
    """Parse common date formats, return None if invalid."""
    pass

def format_date(dt: datetime, fmt: str = "iso") -> str:
    """Format datetime. Supports: 'iso', 'date', 'datetime', custom."""
    pass

def days_between(d1: datetime, d2: datetime) -> int:
    """Return absolute number of days between two dates."""
    pass

# =============================================================================
# EXERCISE 5: File Utilities
# =============================================================================

def ensure_dir(path: str) -> str:
    """Create directory if it doesn't exist. Return path."""
    pass

def read_json(path: str, default: Any = None) -> Any:
    """Read JSON file, return default if missing/invalid."""
    pass

def write_json(path: str, data: Any, pretty: bool = True) -> None:
    """Write data as JSON."""
    pass

# =============================================================================
# EXERCISE 6: Validation Utilities  
# =============================================================================

def is_email(s: str) -> bool:
    """Check if string is valid email format."""
    pass

def is_url(s: str) -> bool:
    """Check if string is valid URL format."""
    pass

def validate(data: Dict, schema: Dict) -> tuple:
    """Validate data against schema. Return (is_valid, errors)."""
    pass

# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 12: Utility Library - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # String utilities
    total += 1
    if snake_to_camel("hello_world") == "helloWorld":
        print("✅ snake_to_camel()"); passed += 1
    else: print("❌ snake_to_camel()")
    
    total += 1
    if camel_to_snake("helloWorld") == "hello_world":
        print("✅ camel_to_snake()"); passed += 1
    else: print("❌ camel_to_snake()")
    
    total += 1
    if truncate("Hello World", 8) == "Hello...":
        print("✅ truncate()"); passed += 1
    else: print("❌ truncate()")
    
    total += 1
    if slugify("Hello World!") == "hello-world":
        print("✅ slugify()"); passed += 1
    else: print("❌ slugify()")
    
    # Collection utilities
    total += 1
    if chunk([1,2,3,4,5], 2) == [[1,2], [3,4], [5]]:
        print("✅ chunk()"); passed += 1
    else: print("❌ chunk()")
    
    total += 1
    if flatten([[1,2], [3, [4,5]]]) == [1,2,3,4,5]:
        print("✅ flatten()"); passed += 1
    else: print("❌ flatten()")
    
    total += 1
    items = [{'id': 1, 'name': 'a'}, {'id': 1, 'name': 'b'}, {'id': 2, 'name': 'c'}]
    if len(unique_by(items, 'id')) == 2:
        print("✅ unique_by()"); passed += 1
    else: print("❌ unique_by()")
    
    total += 1
    items = [{'dept': 'eng', 'name': 'a'}, {'dept': 'eng', 'name': 'b'}, {'dept': 'sales', 'name': 'c'}]
    grouped = group_by(items, 'dept')
    if grouped and len(grouped.get('eng', [])) == 2:
        print("✅ group_by()"); passed += 1
    else: print("❌ group_by()")
    
    # Dict utilities
    total += 1
    data = {'user': {'profile': {'name': 'Alice'}}}
    if deep_get(data, 'user.profile.name') == 'Alice':
        print("✅ deep_get()"); passed += 1
    else: print("❌ deep_get()")
    
    total += 1
    if pick({'a': 1, 'b': 2, 'c': 3}, ['a', 'c']) == {'a': 1, 'c': 3}:
        print("✅ pick()"); passed += 1
    else: print("❌ pick()")
    
    total += 1
    if omit({'a': 1, 'b': 2, 'c': 3}, ['b']) == {'a': 1, 'c': 3}:
        print("✅ omit()"); passed += 1
    else: print("❌ omit()")
    
    # Validation
    total += 1
    if is_email("test@example.com") and not is_email("invalid"):
        print("✅ is_email()"); passed += 1
    else: print("❌ is_email()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
