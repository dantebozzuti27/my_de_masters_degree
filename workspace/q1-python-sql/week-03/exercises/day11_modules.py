#!/usr/bin/env python3
"""
Day 11 Exercise: Python Module System
=====================================
Imports, packages, __init__.py - organizing code like a professional.
This is how real Python projects are structured.
"""

import sys
import os
from typing import List, Dict, Any, Optional
from importlib import import_module

# =============================================================================
# EXERCISE 1: Understanding Imports
# =============================================================================

# These exercises test your understanding of how imports work.
# Answer by implementing the functions.

def get_python_path() -> List[str]:
    """
    Return the list of directories Python searches for modules.
    
    Hint: It's stored in sys.path
    
    Example:
        >>> paths = get_python_path()
        >>> len(paths) > 0
        True
    """
    pass


def get_current_module_name() -> str:
    """
    Return the name of the current module.
    
    Hint: Use __name__
    
    Example:
        >>> get_current_module_name()  # When run as script
        '__main__'
    """
    pass


def get_module_file_path(module_name: str) -> Optional[str]:
    """
    Get the file path of an imported module.
    Return None if module not found.
    
    Example:
        >>> get_module_file_path('os')
        '/usr/lib/python3.11/os.py'  # varies by system
        >>> get_module_file_path('nonexistent')
        None
    """
    pass


# =============================================================================
# EXERCISE 2: Dynamic Imports
# =============================================================================

def safe_import(module_name: str) -> tuple:
    """
    Safely import a module, returning (module, None) on success
    or (None, error_message) on failure.
    
    Example:
        >>> module, error = safe_import('json')
        >>> module is not None
        True
        >>> _, error = safe_import('nonexistent_module')
        >>> 'No module named' in error
        True
    """
    pass


def import_function(module_name: str, function_name: str) -> Optional[callable]:
    """
    Dynamically import a function from a module.
    
    Example:
        >>> loads = import_function('json', 'loads')
        >>> loads('{"key": "value"}')
        {'key': 'value'}
    """
    pass


def list_module_contents(module_name: str) -> Dict[str, List[str]]:
    """
    List the contents of a module, categorized.
    
    Return a dict with:
    - 'functions': list of callable names
    - 'classes': list of class names
    - 'constants': list of UPPERCASE names (likely constants)
    - 'private': list of names starting with _
    
    Example:
        >>> contents = list_module_contents('os')
        >>> 'getcwd' in contents['functions']
        True
    """
    pass


# =============================================================================
# EXERCISE 3: Creating Module Structures
# =============================================================================

def create_package_structure(base_path: str, package_name: str, modules: List[str]) -> Dict[str, str]:
    """
    Create a package directory structure and return paths created.
    
    Creates:
    - base_path/package_name/
    - base_path/package_name/__init__.py
    - base_path/package_name/module1.py
    - base_path/package_name/module2.py
    - etc.
    
    Returns dict mapping module name to file path.
    
    Example:
        >>> paths = create_package_structure('/tmp', 'mypackage', ['utils', 'models'])
        >>> paths['__init__']
        '/tmp/mypackage/__init__.py'
        >>> paths['utils']
        '/tmp/mypackage/utils.py'
    """
    pass


def generate_init_file(modules: List[str], include_all: bool = True) -> str:
    """
    Generate __init__.py content that exports from submodules.
    
    Example:
        >>> print(generate_init_file(['utils', 'models']))
        \"\"\"Package docstring.\"\"\"
        
        from .utils import *
        from .models import *
        
        __all__ = ['utils', 'models']
    """
    pass


# =============================================================================
# EXERCISE 4: Module Patterns
# =============================================================================

def create_singleton_module_pattern() -> str:
    """
    Return Python code for a module that acts as a singleton.
    
    Pattern: Module-level variables with functions to access/modify them.
    This is how many configuration modules work.
    
    The returned code should define:
    - _config = {} (private dict)
    - get(key, default) function
    - set(key, value) function
    - reset() function
    """
    pass


def create_lazy_import_pattern(module_name: str) -> str:
    """
    Return Python code that lazily imports a module.
    
    Lazy imports delay the import until the module is actually used.
    This speeds up initial load time for large packages.
    
    Example:
        >>> print(create_lazy_import_pattern('pandas'))
        _pandas = None
        
        def get_pandas():
            global _pandas
            if _pandas is None:
                import pandas as _pandas
            return _pandas
    """
    pass


# =============================================================================
# EXERCISE 5: Relative vs Absolute Imports
# =============================================================================

def explain_import_difference() -> Dict[str, str]:
    """
    Return a dict explaining the difference between import types.
    
    Return dict with keys:
    - 'absolute': explanation of absolute imports
    - 'relative': explanation of relative imports
    - 'when_absolute': when to use absolute
    - 'when_relative': when to use relative
    - 'example_absolute': example of absolute import
    - 'example_relative': example of relative import
    """
    pass


# =============================================================================
# EXERCISE 6: Building a Mini Package
# =============================================================================

def generate_utils_module() -> str:
    """
    Generate content for a utils.py module with common utilities.
    
    Should include:
    - log(message) function
    - measure_time decorator
    - config dictionary
    """
    pass


def generate_models_module() -> str:
    """
    Generate content for a models.py module with data classes.
    
    Should include:
    - User dataclass with: id, name, email, created_at
    - Product dataclass with: id, name, price, stock
    """
    pass


def generate_main_module() -> str:
    """
    Generate content for a __main__.py module.
    
    Should:
    - Import from utils and models
    - Have a main() function
    - Use if __name__ == '__main__' pattern
    """
    pass


# =============================================================================
# EXERCISE 7: Module Best Practices
# =============================================================================

def analyze_module_quality(code: str) -> Dict[str, Any]:
    """
    Analyze Python module code for best practices.
    
    Check for:
    - has_docstring: bool - module has docstring
    - has_all: bool - defines __all__
    - import_at_top: bool - imports at top of file
    - no_star_imports: bool - no 'from x import *' (except in __init__)
    - has_main_guard: bool - has if __name__ == '__main__'
    
    Return dict with these keys and a 'score' (0-5).
    """
    pass


def fix_circular_import(module_a_imports_b: str, module_b_imports_a: str) -> Dict[str, str]:
    """
    Given two modules that have circular imports, return fixed versions.
    
    Common fixes:
    1. Move imports inside functions (lazy import)
    2. Restructure to remove the cycle
    3. Create a third module for shared code
    
    Return dict with 'module_a' and 'module_b' fixed code.
    """
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 11: Python Module System - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: get_python_path
    total += 1
    try:
        paths = get_python_path()
        if paths and isinstance(paths, list) and len(paths) > 0:
            print("✅ get_python_path()")
            passed += 1
        else:
            print("❌ get_python_path()")
    except:
        print("❌ get_python_path()")
    
    # Test 2: get_current_module_name
    total += 1
    try:
        name = get_current_module_name()
        if name == '__main__':
            print("✅ get_current_module_name()")
            passed += 1
        else:
            print("❌ get_current_module_name()")
    except:
        print("❌ get_current_module_name()")
    
    # Test 3: get_module_file_path
    total += 1
    try:
        path = get_module_file_path('os')
        missing = get_module_file_path('nonexistent_module_xyz')
        if path and 'os' in path and missing is None:
            print("✅ get_module_file_path()")
            passed += 1
        else:
            print("❌ get_module_file_path()")
    except:
        print("❌ get_module_file_path()")
    
    # Test 4: safe_import
    total += 1
    try:
        mod, err = safe_import('json')
        _, err2 = safe_import('nonexistent_module_xyz')
        if mod is not None and err is None and err2 is not None:
            print("✅ safe_import()")
            passed += 1
        else:
            print("❌ safe_import()")
    except:
        print("❌ safe_import()")
    
    # Test 5: import_function
    total += 1
    try:
        loads = import_function('json', 'loads')
        if loads and loads('{"key": "value"}') == {'key': 'value'}:
            print("✅ import_function()")
            passed += 1
        else:
            print("❌ import_function()")
    except:
        print("❌ import_function()")
    
    # Test 6: list_module_contents
    total += 1
    try:
        contents = list_module_contents('os')
        if contents and 'functions' in contents and 'getcwd' in contents.get('functions', []):
            print("✅ list_module_contents()")
            passed += 1
        else:
            print("❌ list_module_contents()")
    except:
        print("❌ list_module_contents()")
    
    # Test 7: generate_init_file
    total += 1
    try:
        init_content = generate_init_file(['utils', 'models'])
        if init_content and 'from .utils import' in init_content and '__all__' in init_content:
            print("✅ generate_init_file()")
            passed += 1
        else:
            print("❌ generate_init_file()")
    except:
        print("❌ generate_init_file()")
    
    # Test 8: create_singleton_module_pattern
    total += 1
    try:
        pattern = create_singleton_module_pattern()
        if pattern and '_config' in pattern and 'def get' in pattern and 'def set' in pattern:
            print("✅ create_singleton_module_pattern()")
            passed += 1
        else:
            print("❌ create_singleton_module_pattern()")
    except:
        print("❌ create_singleton_module_pattern()")
    
    # Test 9: create_lazy_import_pattern
    total += 1
    try:
        pattern = create_lazy_import_pattern('pandas')
        if pattern and '_pandas' in pattern and 'import pandas' in pattern:
            print("✅ create_lazy_import_pattern()")
            passed += 1
        else:
            print("❌ create_lazy_import_pattern()")
    except:
        print("❌ create_lazy_import_pattern()")
    
    # Test 10: explain_import_difference
    total += 1
    try:
        explanation = explain_import_difference()
        if explanation and 'absolute' in explanation and 'relative' in explanation:
            print("✅ explain_import_difference()")
            passed += 1
        else:
            print("❌ explain_import_difference()")
    except:
        print("❌ explain_import_difference()")
    
    # Test 11: generate_utils_module
    total += 1
    try:
        utils = generate_utils_module()
        if utils and 'def log' in utils and 'measure_time' in utils:
            print("✅ generate_utils_module()")
            passed += 1
        else:
            print("❌ generate_utils_module()")
    except:
        print("❌ generate_utils_module()")
    
    # Test 12: analyze_module_quality
    total += 1
    try:
        good_code = '''"""Module docstring."""

import os

__all__ = ['main']

def main():
    pass

if __name__ == '__main__':
    main()
'''
        analysis = analyze_module_quality(good_code)
        if analysis and analysis.get('has_docstring') and analysis.get('has_all') and analysis.get('score', 0) >= 4:
            print("✅ analyze_module_quality()")
            passed += 1
        else:
            print("❌ analyze_module_quality()")
    except:
        print("❌ analyze_module_quality()")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
