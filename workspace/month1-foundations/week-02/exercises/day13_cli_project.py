#!/usr/bin/env python3
"""
Day 13: Week 2 Project - CLI Data Processing Tool
===================================================
Duration: 6 hours (Saturday Project Day)

BUILD A REAL TOOL that combines everything from Week 2:
- Python OOP (classes, methods, properties)
- Logging & Configuration
- Error Handling
- Git Workflow (branches, commits, PR)

PROJECT: Data File Processor CLI
================================
A command-line tool that:
1. Reads data files (CSV, JSON)
2. Validates data against a schema
3. Transforms data (filtering, mapping)
4. Outputs results with statistics
5. Logs everything properly

COMPLETION: Delete the marker below when project is complete.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN PROJECT COMPLETE

import argparse
import csv
import json
import logging
import os
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod

# =============================================================================
# PROJECT REQUIREMENTS
# =============================================================================
"""
GIT WORKFLOW (Do this FIRST before coding):
==========================================
1. Create a new repo or use your git-practice folder:
   cd ~/Desktop/git-practice  # or create new folder
   
2. Create a feature branch:
   git checkout -b feature/cli-data-tool
   
3. As you complete each part, make commits:
   git add .
   git commit -m "Add: <what you just built>"

4. When done, merge to main:
   git checkout main
   git merge feature/cli-data-tool
   
5. (Optional) Push to GitHub and create a PR


PROJECT STRUCTURE:
==================
Your final tool should be runnable like:

  python day13_cli_project.py --input data.csv --output results.json --log-level INFO

And produce:
  - Validated, transformed data
  - A log file with execution details
  - Statistics about the processing


SESSION PLAN (6 hours):
=======================
Hour 1: Build the core data models (DataRecord, DataBatch)
Hour 2: Build the file readers (CSVReader, JSONReader)  
Hour 3: Build the validators and transformers
Hour 4: Build the CLI interface with argparse
Hour 5: Add logging and configuration
Hour 6: Testing, polish, git workflow
"""

# =============================================================================
# PART 1: CONFIGURATION (30 min)
# =============================================================================
# Build a configuration class that can load from a JSON file or use defaults

class Config:
    """
    Configuration for the data processor.
    
    Supports:
    - Loading from JSON file
    - Environment variable overrides
    - Sensible defaults
    
    Example config.json:
    {
        "log_level": "INFO",
        "log_file": "processor.log",
        "output_format": "json",
        "validate": true,
        "max_errors": 10
    }
    """
    
    DEFAULTS = {
        "log_level": "INFO",
        "log_file": None,
        "output_format": "json",
        "validate": True,
        "max_errors": 10,
        "date_format": "%Y-%m-%d"
    }
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize config with defaults, then override from file if provided.
        
        TODO:
        1. Start with DEFAULTS.copy()
        2. If config_path provided and file exists, load and merge
        3. Check environment variables for overrides (e.g., PROCESSOR_LOG_LEVEL)
        """
        # YOUR CODE HERE
        pass
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a config value."""
        # YOUR CODE HERE
        pass
    
    def __repr__(self) -> str:
        """Show config for debugging."""
        # YOUR CODE HERE
        pass


# =============================================================================
# PART 2: LOGGING SETUP (20 min)
# =============================================================================
# Create a function that sets up logging based on config

def setup_logging(config: Config) -> logging.Logger:
    """
    Set up logging based on configuration.
    
    - Console output always
    - File output if log_file configured
    - Level from config
    - Format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    TODO:
    1. Create logger named "data_processor"
    2. Set level from config
    3. Add console handler
    4. Add file handler if log_file configured
    5. Return the logger
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PART 3: DATA MODELS (45 min)
# =============================================================================
# Build the core data structures

class DataRecord:
    """
    A single record of data with validation support.
    
    Example:
        >>> record = DataRecord({"name": "Alice", "age": 30})
        >>> record.get("name")
        'Alice'
        >>> record.validate({"name": str, "age": int})
        True
    """
    
    def __init__(self, data: Dict[str, Any], source: str = "unknown"):
        """
        Initialize a data record.
        
        TODO:
        1. Store the data dict
        2. Store the source (where this record came from)
        3. Initialize _errors as empty list
        4. Store created_at timestamp
        """
        # YOUR CODE HERE
        pass
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value from the record."""
        # YOUR CODE HERE
        pass
    
    def set(self, key: str, value: Any) -> None:
        """Set a value in the record."""
        # YOUR CODE HERE
        pass
    
    def validate(self, schema: Dict[str, type]) -> bool:
        """
        Validate record against a schema.
        
        Schema format: {"field_name": expected_type}
        Example: {"name": str, "age": int, "email": str}
        
        Returns True if valid, False if not.
        Populates self._errors with any issues.
        """
        # YOUR CODE HERE
        pass
    
    @property
    def errors(self) -> List[str]:
        """Get validation errors."""
        # YOUR CODE HERE
        pass
    
    @property
    def is_valid(self) -> bool:
        """Check if record has no errors."""
        # YOUR CODE HERE
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert record to dictionary."""
        # YOUR CODE HERE
        pass
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        # YOUR CODE HERE
        pass


class DataBatch:
    """
    A collection of DataRecords with batch operations.
    
    Example:
        >>> batch = DataBatch()
        >>> batch.add(DataRecord({"name": "Alice"}))
        >>> batch.add(DataRecord({"name": "Bob"}))
        >>> len(batch)
        2
        >>> batch.filter(lambda r: r.get("name") == "Alice")
        DataBatch with 1 records
    """
    
    def __init__(self, records: Optional[List[DataRecord]] = None):
        """Initialize with optional list of records."""
        # YOUR CODE HERE
        pass
    
    def add(self, record: DataRecord) -> None:
        """Add a record to the batch."""
        # YOUR CODE HERE
        pass
    
    def __len__(self) -> int:
        """Return number of records."""
        # YOUR CODE HERE
        pass
    
    def __iter__(self):
        """Iterate over records."""
        # YOUR CODE HERE
        pass
    
    def filter(self, predicate) -> "DataBatch":
        """
        Return new DataBatch with only records matching predicate.
        
        predicate is a function that takes a DataRecord and returns bool.
        """
        # YOUR CODE HERE
        pass
    
    def map(self, transform) -> "DataBatch":
        """
        Return new DataBatch with transform applied to each record.
        
        transform is a function that takes a DataRecord and returns a DataRecord.
        """
        # YOUR CODE HERE
        pass
    
    def validate_all(self, schema: Dict[str, type]) -> tuple:
        """
        Validate all records against schema.
        
        Returns (valid_batch, invalid_batch) tuple.
        """
        # YOUR CODE HERE
        pass
    
    def to_list(self) -> List[Dict[str, Any]]:
        """Convert all records to list of dicts."""
        # YOUR CODE HERE
        pass
    
    @property
    def statistics(self) -> Dict[str, Any]:
        """
        Return statistics about the batch.
        
        Include: total_records, valid_records, invalid_records, fields
        """
        # YOUR CODE HERE
        pass
    
    def __repr__(self) -> str:
        """String representation."""
        # YOUR CODE HERE
        pass


# =============================================================================
# PART 4: FILE READERS (45 min)
# =============================================================================
# Abstract base class and concrete implementations

class DataReader(ABC):
    """Abstract base class for data readers."""
    
    def __init__(self, filepath: str, logger: Optional[logging.Logger] = None):
        """Initialize with filepath and optional logger."""
        self.filepath = filepath
        self.logger = logger or logging.getLogger(__name__)
    
    @abstractmethod
    def read(self) -> DataBatch:
        """Read data and return a DataBatch."""
        pass
    
    def _log(self, level: str, message: str, **kwargs):
        """Helper to log with context."""
        getattr(self.logger, level.lower())(message, extra=kwargs)


class CSVReader(DataReader):
    """
    Read data from CSV files.
    
    Example:
        >>> reader = CSVReader("data.csv")
        >>> batch = reader.read()
        >>> len(batch)
        100
    """
    
    def read(self) -> DataBatch:
        """
        Read CSV file and return DataBatch.
        
        TODO:
        1. Log start of reading
        2. Open file and use csv.DictReader
        3. Create DataRecord for each row
        4. Log completion with count
        5. Handle errors gracefully
        """
        # YOUR CODE HERE
        pass


class JSONReader(DataReader):
    """
    Read data from JSON files.
    
    Supports:
    - Array of objects: [{"name": "Alice"}, {"name": "Bob"}]
    - Object with data key: {"data": [...], "metadata": {...}}
    """
    
    def __init__(self, filepath: str, data_key: Optional[str] = None, 
                 logger: Optional[logging.Logger] = None):
        """Initialize with optional data_key for nested data."""
        super().__init__(filepath, logger)
        self.data_key = data_key
    
    def read(self) -> DataBatch:
        """
        Read JSON file and return DataBatch.
        
        TODO:
        1. Log start
        2. Load JSON
        3. Extract data (handle array or nested object)
        4. Create DataRecords
        5. Log completion
        """
        # YOUR CODE HERE
        pass


def get_reader(filepath: str, logger: Optional[logging.Logger] = None) -> DataReader:
    """
    Factory function to get appropriate reader based on file extension.
    
    TODO:
    1. Get file extension
    2. Return CSVReader for .csv
    3. Return JSONReader for .json
    4. Raise ValueError for unknown types
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# PART 5: DATA TRANSFORMERS (30 min)
# =============================================================================

class Transformer(ABC):
    """Abstract base class for data transformers."""
    
    @abstractmethod
    def transform(self, record: DataRecord) -> DataRecord:
        """Transform a single record."""
        pass
    
    def transform_batch(self, batch: DataBatch) -> DataBatch:
        """Transform all records in a batch."""
        return batch.map(self.transform)


class FieldRenamer(Transformer):
    """
    Rename fields in records.
    
    Example:
        >>> renamer = FieldRenamer({"old_name": "new_name"})
        >>> renamer.transform(record)
    """
    
    def __init__(self, mapping: Dict[str, str]):
        """mapping: {old_field_name: new_field_name}"""
        self.mapping = mapping
    
    def transform(self, record: DataRecord) -> DataRecord:
        """Rename fields according to mapping."""
        # YOUR CODE HERE
        pass


class FieldFilter(Transformer):
    """
    Keep only specified fields.
    
    Example:
        >>> filter = FieldFilter(["name", "email"])
        >>> filter.transform(record)  # Only keeps name and email
    """
    
    def __init__(self, fields: List[str]):
        """fields: list of field names to keep"""
        self.fields = fields
    
    def transform(self, record: DataRecord) -> DataRecord:
        """Keep only specified fields."""
        # YOUR CODE HERE
        pass


class TypeConverter(Transformer):
    """
    Convert field types.
    
    Example:
        >>> converter = TypeConverter({"age": int, "salary": float})
        >>> converter.transform(record)
    """
    
    def __init__(self, conversions: Dict[str, type]):
        """conversions: {field_name: target_type}"""
        self.conversions = conversions
    
    def transform(self, record: DataRecord) -> DataRecord:
        """Convert field types."""
        # YOUR CODE HERE
        pass


class Pipeline:
    """
    Chain multiple transformers together.
    
    Example:
        >>> pipeline = Pipeline([
        ...     FieldRenamer({"old": "new"}),
        ...     TypeConverter({"age": int}),
        ...     FieldFilter(["name", "age"])
        ... ])
        >>> result = pipeline.run(batch)
    """
    
    def __init__(self, transformers: List[Transformer]):
        self.transformers = transformers
    
    def run(self, batch: DataBatch) -> DataBatch:
        """Run all transformers in sequence."""
        # YOUR CODE HERE
        pass


# =============================================================================
# PART 6: OUTPUT WRITERS (30 min)
# =============================================================================

class DataWriter(ABC):
    """Abstract base class for data writers."""
    
    def __init__(self, filepath: str, logger: Optional[logging.Logger] = None):
        self.filepath = filepath
        self.logger = logger or logging.getLogger(__name__)
    
    @abstractmethod
    def write(self, batch: DataBatch) -> int:
        """Write batch to file, return number of records written."""
        pass


class JSONWriter(DataWriter):
    """Write data to JSON file."""
    
    def __init__(self, filepath: str, pretty: bool = True,
                 logger: Optional[logging.Logger] = None):
        super().__init__(filepath, logger)
        self.pretty = pretty
    
    def write(self, batch: DataBatch) -> int:
        """
        Write batch to JSON file.
        
        TODO:
        1. Log start
        2. Convert batch to list
        3. Write with json.dump (indent=2 if pretty)
        4. Log completion
        5. Return count
        """
        # YOUR CODE HERE
        pass


class CSVWriter(DataWriter):
    """Write data to CSV file."""
    
    def write(self, batch: DataBatch) -> int:
        """
        Write batch to CSV file.
        
        TODO:
        1. Log start
        2. Get fieldnames from first record
        3. Use csv.DictWriter
        4. Write header and rows
        5. Log completion
        6. Return count
        """
        # YOUR CODE HERE
        pass


# =============================================================================
# PART 7: CLI INTERFACE (45 min)
# =============================================================================

class DataProcessor:
    """
    Main application class that ties everything together.
    
    Example:
        >>> processor = DataProcessor(config)
        >>> processor.run("input.csv", "output.json")
    """
    
    def __init__(self, config: Config):
        """Initialize with configuration."""
        self.config = config
        self.logger = setup_logging(config)
        self.stats = {
            "input_file": None,
            "output_file": None,
            "records_read": 0,
            "records_valid": 0,
            "records_invalid": 0,
            "records_written": 0,
            "start_time": None,
            "end_time": None,
            "errors": []
        }
    
    def run(self, input_path: str, output_path: str, 
            schema: Optional[Dict[str, type]] = None,
            transformers: Optional[List[Transformer]] = None) -> Dict[str, Any]:
        """
        Run the full processing pipeline.
        
        TODO:
        1. Log start, record start time
        2. Read input file
        3. Validate if schema provided
        4. Transform if transformers provided
        5. Write output
        6. Log completion, record end time
        7. Return stats
        """
        # YOUR CODE HERE
        pass
    
    def print_stats(self) -> None:
        """Print processing statistics to console."""
        # YOUR CODE HERE
        pass


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.
    
    Arguments to support:
    --input, -i: Input file path (required)
    --output, -o: Output file path (required)
    --config, -c: Config file path (optional)
    --log-level: Logging level (optional, default INFO)
    --validate: Enable validation (optional flag)
    --schema: Schema file for validation (optional)
    """
    parser = argparse.ArgumentParser(
        description="Process data files with validation and transformation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python day13_cli_project.py -i data.csv -o output.json
  python day13_cli_project.py -i data.json -o clean.csv --validate
  python day13_cli_project.py -i data.csv -o out.json -c config.json --log-level DEBUG
        """
    )
    
    # TODO: Add arguments using parser.add_argument()
    # YOUR CODE HERE
    
    return parser


def main():
    """
    Main entry point for the CLI.
    
    TODO:
    1. Parse arguments
    2. Load config
    3. Create DataProcessor
    4. Run processing
    5. Print stats
    6. Exit with appropriate code
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# SAMPLE DATA FOR TESTING
# =============================================================================

SAMPLE_CSV = """name,age,email,department
Alice,30,alice@example.com,Engineering
Bob,25,bob@example.com,Marketing
Charlie,invalid,charlie@example.com,Engineering
Diana,28,diana@example.com,Sales
"""

SAMPLE_JSON = """[
    {"name": "Alice", "age": 30, "email": "alice@example.com"},
    {"name": "Bob", "age": 25, "email": "bob@example.com"},
    {"name": "Charlie", "age": "invalid", "email": "charlie@example.com"}
]"""


def create_sample_files():
    """Create sample data files for testing."""
    with open("sample_data.csv", "w") as f:
        f.write(SAMPLE_CSV)
    
    with open("sample_data.json", "w") as f:
        f.write(SAMPLE_JSON)
    
    print("Created sample_data.csv and sample_data.json")


# =============================================================================
# TESTS
# =============================================================================

def run_tests():
    """Run basic tests to verify implementation."""
    print("=" * 60)
    print("DAY 13: CLI Data Tool - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: Config
    total += 1
    try:
        config = Config()
        if config.get("log_level") == "INFO":
            print("✅ Config with defaults")
            passed += 1
        else:
            print("❌ Config with defaults")
    except Exception as e:
        print(f"❌ Config - {e}")
    
    # Test 2: DataRecord
    total += 1
    try:
        record = DataRecord({"name": "Test", "age": 25}, source="test")
        if record.get("name") == "Test" and record.get("age") == 25:
            print("✅ DataRecord basic")
            passed += 1
        else:
            print("❌ DataRecord basic")
    except Exception as e:
        print(f"❌ DataRecord - {e}")
    
    # Test 3: DataRecord validation
    total += 1
    try:
        record = DataRecord({"name": "Test", "age": "not_a_number"})
        is_valid = record.validate({"name": str, "age": int})
        if not is_valid and len(record.errors) > 0:
            print("✅ DataRecord validation")
            passed += 1
        else:
            print("❌ DataRecord validation")
    except Exception as e:
        print(f"❌ DataRecord validation - {e}")
    
    # Test 4: DataBatch
    total += 1
    try:
        batch = DataBatch()
        batch.add(DataRecord({"name": "A"}))
        batch.add(DataRecord({"name": "B"}))
        if len(batch) == 2:
            print("✅ DataBatch")
            passed += 1
        else:
            print("❌ DataBatch")
    except Exception as e:
        print(f"❌ DataBatch - {e}")
    
    # Test 5: DataBatch filter
    total += 1
    try:
        batch = DataBatch([
            DataRecord({"name": "Alice", "age": 30}),
            DataRecord({"name": "Bob", "age": 25})
        ])
        filtered = batch.filter(lambda r: r.get("age") > 27)
        if len(filtered) == 1:
            print("✅ DataBatch.filter")
            passed += 1
        else:
            print("❌ DataBatch.filter")
    except Exception as e:
        print(f"❌ DataBatch.filter - {e}")
    
    # Test 6: CSVReader (requires sample file)
    total += 1
    try:
        create_sample_files()
        reader = CSVReader("sample_data.csv")
        batch = reader.read()
        if len(batch) == 4:
            print("✅ CSVReader")
            passed += 1
        else:
            print(f"❌ CSVReader - got {len(batch)} records")
    except Exception as e:
        print(f"❌ CSVReader - {e}")
    
    # Test 7: JSONReader
    total += 1
    try:
        reader = JSONReader("sample_data.json")
        batch = reader.read()
        if len(batch) == 3:
            print("✅ JSONReader")
            passed += 1
        else:
            print(f"❌ JSONReader - got {len(batch)} records")
    except Exception as e:
        print(f"❌ JSONReader - {e}")
    
    # Test 8: FieldRenamer
    total += 1
    try:
        record = DataRecord({"old_field": "value"})
        renamer = FieldRenamer({"old_field": "new_field"})
        transformed = renamer.transform(record)
        if transformed.get("new_field") == "value":
            print("✅ FieldRenamer")
            passed += 1
        else:
            print("❌ FieldRenamer")
    except Exception as e:
        print(f"❌ FieldRenamer - {e}")
    
    # Test 9: Pipeline
    total += 1
    try:
        batch = DataBatch([DataRecord({"name": "Test", "extra": "remove"})])
        pipeline = Pipeline([
            FieldFilter(["name"])
        ])
        result = pipeline.run(batch)
        record = list(result)[0]
        if record.get("name") == "Test" and record.get("extra") is None:
            print("✅ Pipeline")
            passed += 1
        else:
            print("❌ Pipeline")
    except Exception as e:
        print(f"❌ Pipeline - {e}")
    
    # Test 10: JSONWriter
    total += 1
    try:
        batch = DataBatch([DataRecord({"name": "Test"})])
        writer = JSONWriter("test_output.json")
        count = writer.write(batch)
        if count == 1 and os.path.exists("test_output.json"):
            print("✅ JSONWriter")
            passed += 1
            os.remove("test_output.json")
        else:
            print("❌ JSONWriter")
    except Exception as e:
        print(f"❌ JSONWriter - {e}")
    
    # Cleanup
    for f in ["sample_data.csv", "sample_data.json"]:
        if os.path.exists(f):
            os.remove(f)
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
        print("\nNow test the CLI:")
        print("  python day13_cli_project.py --help")
        print("  python day13_cli_project.py -i sample.csv -o output.json")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    # If no arguments, run tests
    if len(sys.argv) == 1:
        run_tests()
    else:
        main()
