#!/usr/bin/env python3
"""
Day 7 Exercise: File I/O & Context Managers
============================================
Data Engineering is ALL about files: CSVs, JSON, logs, configs.
Master file handling and you're ready for real ETL work.
"""

import os
import json
import csv
from typing import List, Dict, Any, Optional
from pathlib import Path

# =============================================================================
# EXERCISE 1: Basic File Reading
# =============================================================================

def read_entire_file(filepath: str) -> str:
    """
    Read and return the entire contents of a text file.
    
    Example:
        >>> content = read_entire_file('sample.txt')
        >>> print(content)
        'Hello, World!'
    """
    pass


def read_file_lines(filepath: str) -> List[str]:
    """
    Read a file and return a list of lines (without newline characters).
    
    Example:
        >>> lines = read_file_lines('sample.txt')
        >>> lines
        ['line 1', 'line 2', 'line 3']
    """
    pass


def count_lines(filepath: str) -> int:
    """
    Count the number of lines in a file.
    
    Example:
        >>> count_lines('sample.txt')
        100
    """
    pass


# =============================================================================
# EXERCISE 2: File Writing
# =============================================================================

def write_text_file(filepath: str, content: str) -> None:
    """
    Write content to a text file (overwriting if exists).
    
    Example:
        >>> write_text_file('output.txt', 'Hello, World!')
        # Creates file with 'Hello, World!'
    """
    pass


def append_to_file(filepath: str, content: str) -> None:
    """
    Append content to a file (create if doesn't exist).
    
    Example:
        >>> append_to_file('log.txt', 'New log entry\\n')
        # Adds to end of file
    """
    pass


def write_lines(filepath: str, lines: List[str]) -> None:
    """
    Write a list of lines to a file (adding newlines).
    
    Example:
        >>> write_lines('output.txt', ['line 1', 'line 2'])
        # Creates file with:
        # line 1
        # line 2
    """
    pass


# =============================================================================
# EXERCISE 3: Context Managers (The 'with' Statement)
# =============================================================================

def safe_read_file(filepath: str) -> Optional[str]:
    """
    Safely read a file using context manager.
    Return None if file doesn't exist.
    
    Why context managers? They automatically:
    - Close the file when done (even if error occurs)
    - Free up system resources
    - Prevent file corruption
    
    Example:
        >>> safe_read_file('exists.txt')
        'file content'
        >>> safe_read_file('missing.txt')
        None
    """
    pass


def process_large_file(filepath: str) -> Dict[str, int]:
    """
    Process a large file line by line (memory efficient).
    Return a dict with:
    - 'lines': total line count
    - 'chars': total character count
    - 'words': total word count
    
    IMPORTANT: For huge files (GB+), you can't load it all into memory.
    Use iteration instead of .read()!
    
    Example:
        >>> process_large_file('big.txt')
        {'lines': 1000, 'chars': 50000, 'words': 8500}
    """
    pass


# =============================================================================
# EXERCISE 4: CSV Files (The Data Engineer's Bread and Butter)
# =============================================================================

# Sample data for testing
SAMPLE_USERS = [
    {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'department': 'Engineering'},
    {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'department': 'Sales'},
    {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'department': 'Engineering'},
]

def read_csv_as_dicts(filepath: str) -> List[Dict[str, str]]:
    """
    Read a CSV file and return a list of dictionaries.
    Each row becomes a dict with column headers as keys.
    
    Example:
        # If users.csv contains:
        # id,name,email
        # 1,Alice,alice@example.com
        
        >>> read_csv_as_dicts('users.csv')
        [{'id': '1', 'name': 'Alice', 'email': 'alice@example.com'}]
    
    Hint: Use csv.DictReader
    """
    pass


def write_dicts_to_csv(filepath: str, data: List[Dict], fieldnames: List[str]) -> None:
    """
    Write a list of dictionaries to a CSV file.
    
    Example:
        >>> data = [{'name': 'Alice', 'age': 30}]
        >>> write_dicts_to_csv('output.csv', data, ['name', 'age'])
        # Creates CSV with header row and data
    
    Hint: Use csv.DictWriter
    """
    pass


def filter_csv(input_path: str, output_path: str, column: str, value: str) -> int:
    """
    Read a CSV, filter rows where column equals value, write to new CSV.
    Return the number of rows written.
    
    Example:
        >>> filter_csv('users.csv', 'engineers.csv', 'department', 'Engineering')
        25  # 25 engineers found and written
    """
    pass


# =============================================================================
# EXERCISE 5: JSON Files
# =============================================================================

def read_json_file(filepath: str) -> Any:
    """
    Read and parse a JSON file.
    
    Example:
        >>> read_json_file('config.json')
        {'database': 'postgres', 'port': 5432}
    """
    pass


def write_json_file(filepath: str, data: Any, pretty: bool = True) -> None:
    """
    Write data to a JSON file.
    If pretty=True, format with indentation.
    
    Example:
        >>> write_json_file('output.json', {'key': 'value'}, pretty=True)
        # Creates formatted JSON file
    """
    pass


def merge_json_files(filepaths: List[str], output_path: str) -> Dict:
    """
    Merge multiple JSON files (each containing a dict) into one.
    Later files override earlier ones for duplicate keys.
    
    Example:
        >>> merge_json_files(['base.json', 'override.json'], 'merged.json')
        {'combined': 'config'}
    """
    pass


# =============================================================================
# EXERCISE 6: Real-World File Operations
# =============================================================================

def find_files_by_extension(directory: str, extension: str) -> List[str]:
    """
    Find all files with a given extension in a directory.
    
    Example:
        >>> find_files_by_extension('/data', '.csv')
        ['/data/users.csv', '/data/orders.csv']
    
    Hint: Use pathlib.Path or os.walk
    """
    pass


def get_file_stats(filepath: str) -> Dict[str, Any]:
    """
    Get statistics about a file.
    
    Return dict with:
    - 'size_bytes': file size in bytes
    - 'size_mb': file size in megabytes (2 decimal places)
    - 'exists': boolean
    - 'extension': file extension
    
    Example:
        >>> get_file_stats('data.csv')
        {'size_bytes': 1024000, 'size_mb': 0.98, 'exists': True, 'extension': '.csv'}
    """
    pass


def backup_file(filepath: str) -> str:
    """
    Create a backup of a file by copying it with '.bak' extension.
    Return the backup file path.
    
    Example:
        >>> backup_file('config.json')
        'config.json.bak'
    """
    pass


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    import tempfile
    import shutil
    
    print("=" * 60)
    print("DAY 7: File I/O & Context Managers - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Create temp directory for tests
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Test 1: write_text_file and read_entire_file
        total += 1
        test_file = os.path.join(temp_dir, 'test.txt')
        try:
            write_text_file(test_file, 'Hello, World!')
            content = read_entire_file(test_file)
            if content == 'Hello, World!':
                print("✅ write_text_file() and read_entire_file()")
                passed += 1
            else:
                print("❌ write_text_file() and read_entire_file()")
        except:
            print("❌ write_text_file() and read_entire_file()")
        
        # Test 2: write_lines and read_file_lines
        total += 1
        lines_file = os.path.join(temp_dir, 'lines.txt')
        try:
            write_lines(lines_file, ['line 1', 'line 2', 'line 3'])
            lines = read_file_lines(lines_file)
            if lines == ['line 1', 'line 2', 'line 3']:
                print("✅ write_lines() and read_file_lines()")
                passed += 1
            else:
                print("❌ write_lines() and read_file_lines()")
        except:
            print("❌ write_lines() and read_file_lines()")
        
        # Test 3: count_lines
        total += 1
        try:
            count = count_lines(lines_file)
            if count == 3:
                print("✅ count_lines()")
                passed += 1
            else:
                print("❌ count_lines()")
        except:
            print("❌ count_lines()")
        
        # Test 4: append_to_file
        total += 1
        append_file = os.path.join(temp_dir, 'append.txt')
        try:
            append_to_file(append_file, 'first\n')
            append_to_file(append_file, 'second\n')
            content = read_entire_file(append_file)
            if content == 'first\nsecond\n':
                print("✅ append_to_file()")
                passed += 1
            else:
                print("❌ append_to_file()")
        except:
            print("❌ append_to_file()")
        
        # Test 5: safe_read_file
        total += 1
        try:
            content = safe_read_file(test_file)
            missing = safe_read_file(os.path.join(temp_dir, 'nonexistent.txt'))
            if content == 'Hello, World!' and missing is None:
                print("✅ safe_read_file()")
                passed += 1
            else:
                print("❌ safe_read_file()")
        except:
            print("❌ safe_read_file()")
        
        # Test 6: process_large_file
        total += 1
        large_file = os.path.join(temp_dir, 'large.txt')
        try:
            write_lines(large_file, ['hello world', 'foo bar', 'test line'])
            stats = process_large_file(large_file)
            if stats and stats.get('lines') == 3 and stats.get('words') == 6:
                print("✅ process_large_file()")
                passed += 1
            else:
                print("❌ process_large_file()")
        except:
            print("❌ process_large_file()")
        
        # Test 7: CSV operations
        total += 1
        csv_file = os.path.join(temp_dir, 'users.csv')
        try:
            write_dicts_to_csv(csv_file, SAMPLE_USERS, ['id', 'name', 'email', 'department'])
            rows = read_csv_as_dicts(csv_file)
            if rows and len(rows) == 3 and rows[0]['name'] == 'Alice':
                print("✅ write_dicts_to_csv() and read_csv_as_dicts()")
                passed += 1
            else:
                print("❌ write_dicts_to_csv() and read_csv_as_dicts()")
        except:
            print("❌ write_dicts_to_csv() and read_csv_as_dicts()")
        
        # Test 8: filter_csv
        total += 1
        filtered_file = os.path.join(temp_dir, 'engineers.csv')
        try:
            count = filter_csv(csv_file, filtered_file, 'department', 'Engineering')
            if count == 2:
                print("✅ filter_csv()")
                passed += 1
            else:
                print("❌ filter_csv()")
        except:
            print("❌ filter_csv()")
        
        # Test 9: JSON operations
        total += 1
        json_file = os.path.join(temp_dir, 'config.json')
        try:
            write_json_file(json_file, {'database': 'postgres', 'port': 5432})
            data = read_json_file(json_file)
            if data == {'database': 'postgres', 'port': 5432}:
                print("✅ write_json_file() and read_json_file()")
                passed += 1
            else:
                print("❌ write_json_file() and read_json_file()")
        except:
            print("❌ write_json_file() and read_json_file()")
        
        # Test 10: merge_json_files
        total += 1
        json1 = os.path.join(temp_dir, 'base.json')
        json2 = os.path.join(temp_dir, 'override.json')
        merged = os.path.join(temp_dir, 'merged.json')
        try:
            write_json_file(json1, {'a': 1, 'b': 2})
            write_json_file(json2, {'b': 3, 'c': 4})
            result = merge_json_files([json1, json2], merged)
            if result == {'a': 1, 'b': 3, 'c': 4}:
                print("✅ merge_json_files()")
                passed += 1
            else:
                print("❌ merge_json_files()")
        except:
            print("❌ merge_json_files()")
        
        # Test 11: find_files_by_extension
        total += 1
        try:
            files = find_files_by_extension(temp_dir, '.csv')
            if len(files) >= 2:  # users.csv and engineers.csv
                print("✅ find_files_by_extension()")
                passed += 1
            else:
                print("❌ find_files_by_extension()")
        except:
            print("❌ find_files_by_extension()")
        
        # Test 12: get_file_stats
        total += 1
        try:
            stats = get_file_stats(test_file)
            if stats and stats.get('exists') == True and stats.get('extension') == '.txt':
                print("✅ get_file_stats()")
                passed += 1
            else:
                print("❌ get_file_stats()")
        except:
            print("❌ get_file_stats()")
        
        # Test 13: backup_file
        total += 1
        try:
            backup_path = backup_file(test_file)
            if backup_path and os.path.exists(backup_path):
                print("✅ backup_file()")
                passed += 1
            else:
                print("❌ backup_file()")
        except:
            print("❌ backup_file()")
        
    finally:
        # Cleanup temp directory
        shutil.rmtree(temp_dir)
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
