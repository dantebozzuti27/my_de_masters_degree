#!/usr/bin/env python3
"""
Day 9 Exercise: Advanced Function Patterns
==========================================
Default arguments, *args, **kwargs - the building blocks of flexible APIs.
Master these and you'll understand how libraries like pandas work under the hood.
"""

from typing import Any, Dict, List, Callable, Optional
from functools import wraps

# =============================================================================
# EXERCISE 1: Default Arguments
# =============================================================================

def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    """
    Create a greeting string with customizable parts.
    
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
        >>> greet("Bob", greeting="Hi")
        'Hi, Bob!'
        >>> greet("Charlie", punctuation="...")
        'Hello, Charlie...'
    """
    pass


def create_user(
    name: str,
    email: str,
    age: Optional[int] = None,
    role: str = "user",
    active: bool = True
) -> Dict[str, Any]:
    """
    Create a user dictionary with sensible defaults.
    
    Example:
        >>> create_user("Alice", "alice@example.com")
        {'name': 'Alice', 'email': 'alice@example.com', 'age': None, 'role': 'user', 'active': True}
        >>> create_user("Bob", "bob@example.com", age=30, role="admin")
        {'name': 'Bob', 'email': 'bob@example.com', 'age': 30, 'role': 'admin', 'active': True}
    """
    pass


# COMMON MISTAKE: Mutable default arguments!
# DON'T do this: def append_item(item, lst=[]):
# DO this instead:

def append_item(item: Any, lst: Optional[List] = None) -> List:
    """
    Append an item to a list, creating a new list if none provided.
    
    Example:
        >>> append_item(1)
        [1]
        >>> append_item(2, [1])
        [1, 2]
    """
    pass


# =============================================================================
# EXERCISE 2: *args - Variable Positional Arguments
# =============================================================================

def sum_all(*numbers) -> float:
    """
    Sum any number of arguments.
    
    Example:
        >>> sum_all(1, 2, 3)
        6
        >>> sum_all(1, 2, 3, 4, 5)
        15
        >>> sum_all()
        0
    """
    pass


def join_strings(separator: str, *strings) -> str:
    """
    Join any number of strings with a separator.
    
    Example:
        >>> join_strings(", ", "a", "b", "c")
        'a, b, c'
        >>> join_strings("-", "2024", "01", "15")
        '2024-01-15'
    """
    pass


def make_pipeline(*functions) -> Callable:
    """
    Create a pipeline that applies functions in sequence.
    
    Example:
        >>> double = lambda x: x * 2
        >>> add_one = lambda x: x + 1
        >>> pipeline = make_pipeline(double, add_one)
        >>> pipeline(5)
        11  # (5 * 2) + 1
    """
    pass


# =============================================================================
# EXERCISE 3: **kwargs - Variable Keyword Arguments
# =============================================================================

def build_query(table: str, **conditions) -> str:
    """
    Build a simple SQL WHERE query from keyword arguments.
    
    Example:
        >>> build_query("users", name="Alice", age=30)
        "SELECT * FROM users WHERE name = 'Alice' AND age = 30"
        >>> build_query("products")
        "SELECT * FROM products"
    """
    pass


def create_html_tag(tag: str, content: str = "", **attributes) -> str:
    """
    Create an HTML tag with attributes.
    
    Example:
        >>> create_html_tag("div", "Hello", class_="container", id="main")
        '<div class="container" id="main">Hello</div>'
        >>> create_html_tag("input", type="text", name="username")
        '<input type="text" name="username" />'
    
    Note: class_ is used because 'class' is a Python keyword
    """
    pass


def merge_configs(*configs, **overrides) -> Dict:
    """
    Merge multiple config dictionaries, with explicit overrides taking precedence.
    
    Example:
        >>> base = {'debug': False, 'port': 8080}
        >>> prod = {'debug': False, 'host': 'prod.example.com'}
        >>> merge_configs(base, prod, port=9000)
        {'debug': False, 'port': 9000, 'host': 'prod.example.com'}
    """
    pass


# =============================================================================
# EXERCISE 4: Combining *args and **kwargs
# =============================================================================

def flexible_print(*args, sep: str = " ", end: str = "\n", prefix: str = "") -> str:
    """
    A more flexible print function that returns the string instead of printing.
    
    Example:
        >>> flexible_print("Hello", "World")
        'Hello World\\n'
        >>> flexible_print("a", "b", "c", sep="-", end="!")
        'a-b-c!'
        >>> flexible_print("message", prefix="[INFO] ")
        '[INFO] message\\n'
    """
    pass


def call_with_logging(func: Callable, *args, **kwargs) -> Any:
    """
    Call a function and return a dict with:
    - 'result': the function's return value
    - 'args': the positional arguments passed
    - 'kwargs': the keyword arguments passed
    
    Example:
        >>> def add(a, b): return a + b
        >>> call_with_logging(add, 1, 2)
        {'result': 3, 'args': (1, 2), 'kwargs': {}}
        >>> call_with_logging(add, a=1, b=2)
        {'result': 3, 'args': (), 'kwargs': {'a': 1, 'b': 2}}
    """
    pass


# =============================================================================
# EXERCISE 5: Function Decorators (Intro)
# =============================================================================

def log_calls(func: Callable) -> Callable:
    """
    Decorator that logs function calls.
    Returns a list of call records as func.call_log
    
    Example:
        >>> @log_calls
        ... def add(a, b):
        ...     return a + b
        >>> add(1, 2)
        3
        >>> add.call_log
        [{'args': (1, 2), 'kwargs': {}, 'result': 3}]
    """
    pass


def validate_types(*type_args, **type_kwargs):
    """
    Decorator factory that validates argument types.
    
    Example:
        >>> @validate_types(int, int)
        ... def add(a, b):
        ...     return a + b
        >>> add(1, 2)
        3
        >>> add("1", "2")  # Raises TypeError
    """
    pass


def retry(max_attempts: int = 3, exceptions: tuple = (Exception,)):
    """
    Decorator factory that retries a function on failure.
    
    Example:
        >>> attempts = [0]
        >>> @retry(max_attempts=3)
        ... def flaky():
        ...     attempts[0] += 1
        ...     if attempts[0] < 3:
        ...         raise ValueError()
        ...     return "success"
        >>> flaky()
        'success'
    """
    pass


# =============================================================================
# EXERCISE 6: Practical Patterns
# =============================================================================

def partial_apply(func: Callable, *fixed_args, **fixed_kwargs) -> Callable:
    """
    Create a new function with some arguments pre-applied.
    
    Example:
        >>> def greet(greeting, name):
        ...     return f"{greeting}, {name}!"
        >>> say_hello = partial_apply(greet, "Hello")
        >>> say_hello("Alice")
        'Hello, Alice!'
        >>> say_hi_to_bob = partial_apply(greet, "Hi", "Bob")
        >>> say_hi_to_bob()
        'Hi, Bob!'
    """
    pass


def compose(*functions) -> Callable:
    """
    Compose functions right-to-left (mathematical composition).
    
    Example:
        >>> double = lambda x: x * 2
        >>> add_one = lambda x: x + 1
        >>> f = compose(add_one, double)  # add_one(double(x))
        >>> f(5)
        11  # (5 * 2) + 1
    """
    pass


def memoize(func: Callable) -> Callable:
    """
    Decorator that caches function results.
    
    Example:
        >>> @memoize
        ... def expensive(n):
        ...     print(f"Computing {n}")
        ...     return n * 2
        >>> expensive(5)
        Computing 5
        10
        >>> expensive(5)  # No print, uses cache
        10
    """
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 9: Advanced Function Patterns - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: greet
    total += 1
    if greet("Alice") == "Hello, Alice!" and \
       greet("Bob", greeting="Hi") == "Hi, Bob!" and \
       greet("Charlie", punctuation="...") == "Hello, Charlie...":
        print("✅ greet()")
        passed += 1
    else:
        print("❌ greet()")
    
    # Test 2: create_user
    total += 1
    user1 = create_user("Alice", "alice@example.com")
    user2 = create_user("Bob", "bob@example.com", age=30, role="admin")
    if user1 == {'name': 'Alice', 'email': 'alice@example.com', 'age': None, 'role': 'user', 'active': True} and \
       user2.get('age') == 30 and user2.get('role') == 'admin':
        print("✅ create_user()")
        passed += 1
    else:
        print("❌ create_user()")
    
    # Test 3: append_item (mutable default test)
    total += 1
    result1 = append_item(1)
    result2 = append_item(2)
    if result1 == [1] and result2 == [2]:  # Should NOT be [1, 2]!
        print("✅ append_item()")
        passed += 1
    else:
        print("❌ append_item()")
    
    # Test 4: sum_all
    total += 1
    if sum_all(1, 2, 3) == 6 and sum_all(1, 2, 3, 4, 5) == 15 and sum_all() == 0:
        print("✅ sum_all()")
        passed += 1
    else:
        print("❌ sum_all()")
    
    # Test 5: join_strings
    total += 1
    if join_strings(", ", "a", "b", "c") == "a, b, c" and \
       join_strings("-", "2024", "01", "15") == "2024-01-15":
        print("✅ join_strings()")
        passed += 1
    else:
        print("❌ join_strings()")
    
    # Test 6: make_pipeline
    total += 1
    try:
        double = lambda x: x * 2
        add_one = lambda x: x + 1
        pipeline = make_pipeline(double, add_one)
        if pipeline(5) == 11:
            print("✅ make_pipeline()")
            passed += 1
        else:
            print("❌ make_pipeline()")
    except:
        print("❌ make_pipeline()")
    
    # Test 7: build_query
    total += 1
    q1 = build_query("users", name="Alice", age=30)
    q2 = build_query("products")
    if "SELECT * FROM users WHERE" in q1 and "name" in q1 and q2 == "SELECT * FROM products":
        print("✅ build_query()")
        passed += 1
    else:
        print("❌ build_query()")
    
    # Test 8: create_html_tag
    total += 1
    tag1 = create_html_tag("div", "Hello", class_="container")
    tag2 = create_html_tag("input", type="text")
    if 'class="container"' in tag1 and "Hello" in tag1 and 'type="text"' in tag2:
        print("✅ create_html_tag()")
        passed += 1
    else:
        print("❌ create_html_tag()")
    
    # Test 9: merge_configs
    total += 1
    base = {'debug': False, 'port': 8080}
    prod = {'debug': False, 'host': 'prod.example.com'}
    merged = merge_configs(base, prod, port=9000)
    if merged.get('port') == 9000 and merged.get('host') == 'prod.example.com':
        print("✅ merge_configs()")
        passed += 1
    else:
        print("❌ merge_configs()")
    
    # Test 10: flexible_print
    total += 1
    if flexible_print("Hello", "World") == "Hello World\n" and \
       flexible_print("a", "b", "c", sep="-", end="!") == "a-b-c!":
        print("✅ flexible_print()")
        passed += 1
    else:
        print("❌ flexible_print()")
    
    # Test 11: call_with_logging
    total += 1
    def add(a, b): return a + b
    result = call_with_logging(add, 1, 2)
    if result and result.get('result') == 3 and result.get('args') == (1, 2):
        print("✅ call_with_logging()")
        passed += 1
    else:
        print("❌ call_with_logging()")
    
    # Test 12: partial_apply
    total += 1
    try:
        def greet_fn(greeting, name):
            return f"{greeting}, {name}!"
        say_hello = partial_apply(greet_fn, "Hello")
        if say_hello("Alice") == "Hello, Alice!":
            print("✅ partial_apply()")
            passed += 1
        else:
            print("❌ partial_apply()")
    except:
        print("❌ partial_apply()")
    
    # Test 13: compose
    total += 1
    try:
        double = lambda x: x * 2
        add_one = lambda x: x + 1
        f = compose(add_one, double)
        if f(5) == 11:
            print("✅ compose()")
            passed += 1
        else:
            print("❌ compose()")
    except:
        print("❌ compose()")
    
    # Test 14: memoize
    total += 1
    try:
        call_count = [0]
        @memoize
        def expensive(n):
            call_count[0] += 1
            return n * 2
        expensive(5)
        expensive(5)
        if call_count[0] == 1 and expensive(5) == 10:
            print("✅ memoize()")
            passed += 1
        else:
            print("❌ memoize()")
    except:
        print("❌ memoize()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
