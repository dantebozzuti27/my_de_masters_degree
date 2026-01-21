#!/usr/bin/env python3
"""
Day 9: Python Classes & OOP for Production
===========================================
Duration: 2 hours

Learn to design classes for data engineering. When to use OOP, when functions are better.
Master __init__, __str__, __repr__, properties, and class methods.

WHY THIS MATTERS:
- Pandas, SQLAlchemy, Airflow - all use OOP heavily
- Classes let you encapsulate state and behavior together
- Good class design = reusable, testable code
- Senior engineers understand OOP trade-offs
"""

from pyexpat import errors
from queue import Empty
from sys import api_version
from typing import Any, Dict, List, Optional
from datetime import datetime
import json

# =============================================================================
# EXERCISE 1: Basic Class Design (20 min)
# =============================================================================
# Purpose: Understand the fundamental structure of a Python class
# Key concepts: __init__, instance attributes, methods

class DataRecord:
    """
    A simple data record that stores key-value pairs with metadata.
    
    This is the pattern you'll use constantly - wrapping data with
    additional context like timestamps, sources, and validation status.
    
    Example:
        >>> record = DataRecord({"name": "Alice", "age": 30}, source="api")
        >>> record.data
        {'name': 'Alice', 'age': 30}
        >>> record.source
        'api'
        >>> record.created_at  # Should be a datetime
    """
    
    def __init__(self, data: Dict[str, Any], source: str = "unknown"):
        """
        Initialize the record with data and metadata.
        
        Args:
            data: The actual data payload
            source: Where this data came from
        
        TODO: Store data, source, and created_at (current datetime)
        """
        # YOUR CODE HERE
        self.data = data
        self.source = source
        self.created_at = datetime.now()
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a value from the data, with optional default.
        
        Example:
            >>> record = DataRecord({"name": "Alice"})
            >>> record.get("name")
            'Alice'
            >>> record.get("age", 0)
            0
        """
        # YOUR CODE HERE
        return self.data.get(key, default)
    
    def update(self, key: str, value: Any) -> None:
        """
        Update a value in the data.
        
        Example:
            >>> record = DataRecord({"count": 1})
            >>> record.update("count", 2)
            >>> record.data["count"]
            2
        """
        # YOUR CODE HERE
        self.data[key] = value


class User:
    """
    A user with validation built into the class.
    
    Example:
        >>> user = User("alice@example.com", "Alice Smith")
        >>> user.email
        'alice@example.com'
        >>> user.display_name
        'Alice Smith'
    """
    
    def __init__(self, email: str, display_name: str):
        """
        Initialize user with email validation.
        
        TODO:
        1. Validate email contains '@'
        2. Store email and display_name as instance attributes
        3. Raise ValueError if email is invalid
        """
        # YOUR CODE HERE
        if "@" not in email:
            raise ValueError("Invalid Email")
        self.email = email
        self.display_name = display_name
        


    def is_valid_email(self, email: str) -> bool:
        """Check if email contains @ symbol."""
        # YOUR CODE HERE
        if "@" not in email:
            return False
        else: return True


# =============================================================================
# EXERCISE 2: __str__ and __repr__ (15 min)
# =============================================================================
# Purpose: Control how your objects display
# Key insight: __repr__ for debugging, __str__ for users

class Pipeline:
    """
    A data pipeline with proper string representations.
    
    __repr__: Unambiguous, for debugging - should ideally be valid Python
    __str__: Readable, for end users
    
    Example:
        >>> p = Pipeline("etl_daily", ["extract", "transform", "load"])
        >>> repr(p)
        "Pipeline('etl_daily', steps=['extract', 'transform', 'load'])"
        >>> str(p)
        'Pipeline: etl_daily (3 steps)'
    """
    
    def __init__(self, name: str, steps: List[str]):
        """Store name and steps."""
        # YOUR CODE HERE
        self.name = name
        self.steps = steps
        
    
    def __repr__(self) -> str:
        """
        Return unambiguous string representation.
        Format: Pipeline('name', steps=['step1', 'step2'])
        """
        # YOUR CODE HERE
        return f"Pipeline('{self.name}' steps={self.steps})"
    
    def __str__(self) -> str:
        """
        Return readable string representation.
        Format: Pipeline: name (N steps)
        """
        # YOUR CODE HERE
        return f"Pipeline: {self.name} ({len(self.steps)} steps)"


class APIResponse:
    """
    Represents an API response with status and data.
    
    Example:
        >>> resp = APIResponse(200, {"users": []}, 0.5)
        >>> repr(resp)
        "APIResponse(status=200, data_size=1, latency=0.5)"
        >>> str(resp)
        '200 OK (0.5s)'
        >>> resp = APIResponse(404, {}, 0.1)
        >>> str(resp)
        '404 ERROR (0.1s)'
    """
    
    def __init__(self, status: int, data: Dict, latency: float):
        """Store status, data, and latency."""
        # YOUR CODE HERE
        self.status = status
        self.data = data
        self.latency = latency
    
    def __repr__(self) -> str:
        """Return: APIResponse(status=X, data_size=Y, latency=Z)"""
        # YOUR CODE HERE
        return f"APIResponse(status={self.status}, data_size={len(self.data)}, latency={self.latency})"
    
    def __str__(self) -> str:
        """Return: 'STATUS OK/ERROR (Xs)' based on status code"""
        # YOUR CODE HERE
        if self.status < 400:
            result = "OK"
        else:
            result = "ERROR"
        return f"{self.status} {result} ({self.latency}s)"


# =============================================================================
# EXERCISE 3: Properties (20 min)
# =============================================================================
# Purpose: Computed attributes that look like regular attributes
# Key insight: Properties let you add logic without changing the API

class DataBatch:
    """
    A batch of records with computed properties.
    
    Properties let you compute values on-demand while keeping a clean API.
    Users access batch.count like a regular attribute, but it's computed.
    
    Example:
        >>> batch = DataBatch([{"a": 1}, {"b": 2}, {"c": 3}])
        >>> batch.count
        3
        >>> batch.is_empty
        False
        >>> batch.first
        {'a': 1}
        >>> empty_batch = DataBatch([])
        >>> empty_batch.is_empty
        True
        >>> empty_batch.first is None
        True
    """
    
    def __init__(self, records: List[Dict]):
        """Store the records."""
        self._records = records  # Convention: _ prefix for "private"
    
    @property
    def records(self) -> List[Dict]:
        """Return the records (read-only access)."""
        return self._records
    
    @property
    def count(self) -> int:
        """Return number of records."""
        # YOUR CODE HERE
        return len(self.records)
    
    @property
    def is_empty(self) -> bool:
        """Return True if no records."""
        # YOUR CODE HERE
        return len(self._records) == 0
    
    @property
    def first(self) -> Optional[Dict]:
        """Return first record or None if empty."""
        # YOUR CODE HERE
        if self._records:
            return self._records[0]
        return None
    
    @property
    def last(self) -> Optional[Dict]:
        """Return last record or None if empty."""
        # YOUR CODE HERE
        if self._records:
            return self._records[-1]
        return None


class Connection:
    """
    Database connection with status tracking.
    
    Example:
        >>> conn = Connection("localhost", 5432)
        >>> conn.status
        'disconnected'
        >>> conn.connect()
        >>> conn.status
        'connected'
        >>> conn.connection_string
        'localhost:5432'
    """
    
    def __init__(self, host: str, port: int):
        """Store host, port, and initial connection state."""
        # YOUR CODE HERE - set host, port, _connected = False
        self.host = host
        self.port = port
        self._connected = False
    
    @property
    def status(self) -> str:
        """Return 'connected' or 'disconnected'."""
        # YOUR CODE HERE
        if self._connected is False:
            return "disconnected"
        else: return "connected"

    
    @property
    def connection_string(self) -> str:
        """Return 'host:port' format."""
        # YOUR CODE HERE
        return f"{self.host}:{self.port}"
    
    def connect(self) -> None:
        """Set connection state to True."""
        # YOUR CODE HERE
        self._connected = True
    
    def disconnect(self) -> None:
        """Set connection state to False."""
        # YOUR CODE HERE
        self._connected = False


# =============================================================================
# EXERCISE 4: Class Methods & Static Methods (20 min)
# =============================================================================
# Purpose: Factory methods and utility functions
# Key insight: @classmethod for alternative constructors, @staticmethod for utilities

class Config:
    """
    Configuration class with multiple ways to create instances.
    
    Class methods are perfect for factory patterns - creating instances
    from different sources (files, dicts, env vars).
    
    Example:
        >>> config = Config({"debug": True, "port": 8080})
        >>> config.get("port")
        8080
        >>> config = Config.from_json('{"debug": false}')
        >>> config.get("debug")
        False
        >>> config = Config.default()
        >>> config.get("debug")
        False
    """
    
    def __init__(self, settings: Dict[str, Any]):
        """Store settings dictionary."""
        # YOUR CODE HERE
        self.settings = settings
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        # YOUR CODE HERE
        return self.settings.get(key, default)
    
    @classmethod
    def from_json(cls, json_string: str) -> "Config":
        """
        Create Config from JSON string.
        
        This is a factory method - it's an alternative constructor.
        'cls' refers to the class itself (Config).
        """
        # YOUR CODE HERE
        # Hint: use json.loads() then create instance with cls(...)
        settings_dict = json.loads(json_string)
        return cls(settings_dict)

    
    @classmethod
    def default(cls) -> "Config":
        """Create Config with default settings."""
        defaults = {"debug": False, "port": 8080, "timeout": 30}
        # YOUR CODE HERE
        return cls(defaults)
    
    @staticmethod
    def validate_port(port: int) -> bool:
        """
        Static method - doesn't need instance or class.
        Just a utility function that logically belongs to Config.
        
        Returns True if port is valid (1-65535).
        """
        # YOUR CODE HERE
        if 1 <= port <= 65535:
            return True
        else: return False



class DataLoader:
    """
    Data loader with factory methods for different sources.
    
    Example:
        >>> loader = DataLoader.from_csv_path("/data/users.csv")
        >>> loader.source_type
        'csv'
        >>> loader = DataLoader.from_api_endpoint("https://api.example.com/users")
        >>> loader.source_type
        'api'
    """
    
    def __init__(self, source: str, source_type: str):
        """Store source and source_type."""
        # YOUR CODE HERE
        self.source = source
        self.source_type = source_type
    
    @classmethod
    def from_csv_path(cls, path: str) -> "DataLoader":
        """Create loader for CSV file."""
        # YOUR CODE HERE
        return cls(path, "csv")
    
    @classmethod
    def from_api_endpoint(cls, url: str) -> "DataLoader":
        """Create loader for API endpoint."""
        # YOUR CODE HERE
        return cls(url, "api")
    
    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Check if URL starts with http:// or https://"""
        # YOUR CODE HERE
        if url.startswith(("http://" , "https://")):
            return True
        else: return False



# =============================================================================
# EXERCISE 5: Data Engineering Class Pattern (25 min)
# =============================================================================
# Purpose: Build a production-ready data extractor class
# This is the pattern you'll use in real projects

class DataExtractor:
    """
    Production data extractor with proper structure.
    
    This pattern encapsulates:
    - Configuration (in __init__)
    - Core logic (extract method)
    - Validation (validate method)
    - State management (properties)
    
    Example:
        >>> extractor = DataExtractor("users_api", {"base_url": "https://api.example.com"})
        >>> extractor.name
        'users_api'
        >>> extractor.is_configured
        True
        >>> extractor.extract_count
        0
    """
    
    def __init__(self, name: str, config: Dict[str, Any]):
        """
        Initialize extractor with name and configuration.
        
        Store:
        - name
        - config
        - _extract_count (starts at 0)
        - _last_extract_time (starts as None)
        """
        # YOUR CODE HERE
        self.name = name
        self.config = config
        self._extract_count = 0
        self._last_extract_time = None
    
    @property
    def is_configured(self) -> bool:
        """Return True if config has 'base_url' key."""
        # YOUR CODE HERE
        return "base_url" in self.config
    
    @property
    def extract_count(self) -> int:
        """Return number of extracts performed."""
        # YOUR CODE HERE
        return self._extract_count
    
    @property
    def last_extract_time(self) -> Optional[datetime]:
        """Return time of last extract, or None if never extracted."""
        # YOUR CODE HERE
        return self._last_extract_time
    
    def extract(self, endpoint: str) -> Dict[str, Any]:
        """
        Simulate data extraction.
        
        1. Increment _extract_count
        2. Update _last_extract_time to now
        3. Return dict with endpoint, config, and timestamp
        
        Example:
            >>> extractor = DataExtractor("test", {"base_url": "http://test.com"})
            >>> result = extractor.extract("/users")
            >>> result["endpoint"]
            '/users'
            >>> extractor.extract_count
            1
        """
        # YOUR CODE HERE
        self._extract_count = self._extract_count + 1
        self._last_extract_time = datetime.now()
        return {"endpoint": endpoint, "config": self.config, "timestamp": self._last_extract_time}

    
    def validate(self, data: Dict) -> bool:
        """
        Validate extracted data.
        Return True if data is a non-empty dict.
        """
        # YOUR CODE HERE
        return len(data) > 0
    
    def __repr__(self) -> str:
        """Return: DataExtractor('name', extracts=N)"""
        # YOUR CODE HERE
        return f"DataExtractor('{self.name}', extracts={self._extract_count})"


class DataValidator:
    """
    Validates data against a schema.
    
    Example:
        >>> schema = {"name": str, "age": int}
        >>> validator = DataValidator(schema)
        >>> validator.validate({"name": "Alice", "age": 30})
        True
        >>> validator.validate({"name": "Bob", "age": "thirty"})
        False
        >>> validator.errors
        ["Field 'age' expected <class 'int'>, got <class 'str'>"]
    """
    
    def __init__(self, schema: Dict[str, type]):
        """
        Store schema and initialize errors list.
        Schema maps field names to expected types.
        """
        # YOUR CODE HERE
        self.schema = schema
        self._errors = []
    
    @property
    def errors(self) -> List[str]:
        """Return list of validation errors from last validate() call."""
        # YOUR CODE HERE
        return self._errors
    
    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validate data against schema.
        
        1. Clear previous errors
        2. Check each schema field exists and has correct type
        3. Add error message for each failure
        4. Return True if no errors
        """
        # YOUR CODE HERE
        self._errors = []
        for field_name, expected_type in self.schema.items():
            actual_value = data.get(field_name)
            if not isinstance(actual_value, expected_type):
                self._errors.append("error message here")
        return len(self._errors) == 0

    
    def validate_batch(self, records: List[Dict]) -> Dict[str, Any]:
        """
        Validate multiple records.
        
        Returns:
            {
                "valid_count": N,
                "invalid_count": M,
                "invalid_indices": [list of indices that failed]
            }
        """
        # YOUR CODE HERE
        valid_count = 0
        invalid_count = 0
        invalid_indices = []
        for index, record in enumerate(records):
            if self.validate(record):
                valid_count += 1
            else:
                invalid_count += 1
                invalid_indices.append(index)
        return {"valid_count": valid_count, "invalid_count": invalid_count, "invalid_indices": invalid_indices}
        


# =============================================================================
# EXERCISE 6: Composition Over Inheritance (20 min)
# =============================================================================
# Purpose: Understand that combining classes is often better than inheritance
# Key insight: Has-a vs Is-a relationships

class Logger:
    """Simple logger that stores messages."""
    
    def __init__(self, name: str):
        self.name = name
        self.messages: List[str] = []
    
    def log(self, level: str, message: str) -> None:
        """Add a log message."""
        self.messages.append(f"[{level}] {self.name}: {message}")
    
    def info(self, message: str) -> None:
        self.log("INFO", message)
    
    def error(self, message: str) -> None:
        self.log("ERROR", message)


class DataPipeline:
    """
    A pipeline that USES a logger (composition).
    
    This is better than inheriting from Logger because:
    - Pipeline HAS-A logger (not IS-A logger)
    - Can swap out logger implementations
    - Cleaner separation of concerns
    
    Example:
        >>> pipeline = DataPipeline("etl", ["extract", "transform", "load"])
        >>> pipeline.run()
        True
        >>> len(pipeline.logger.messages)
        4  # Started + 3 step messages
    """
    
    def __init__(self, name: str, steps: List[str]):
        """
        Initialize pipeline with name, steps, and a Logger instance.
        
        Create self.logger as Logger(name)
        """
        # YOUR CODE HERE
        self.name = name
        self.steps = steps
        self.logger = Logger(name)
    
    def run(self) -> bool:
        """
        Run all steps and log progress.
        
        1. Log "Pipeline started" as INFO
        2. For each step, log "Running step: {step}" as INFO
        3. Return True
        """
        # YOUR CODE HERE
        self.logger.info("Pipeline started")
        for step in self.steps:
            self.logger.info(f"Running step: {step}")
        return True
    
    def get_logs(self) -> List[str]:
        """Return all log messages."""
        # YOUR CODE HERE
        return self.logger.messages


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 9: Python Classes & OOP - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Exercise 1: DataRecord
    total += 1
    try:
        record = DataRecord({"name": "test"}, source="api")
        if record.data == {"name": "test"} and record.source == "api" and hasattr(record, 'created_at'):
            if record.get("name") == "test" and record.get("missing", "default") == "default":
                record.update("name", "updated")
                if record.data["name"] == "updated":
                    print("✅ DataRecord")
                    passed += 1
                else:
                    print("❌ DataRecord - update failed")
            else:
                print("❌ DataRecord - get failed")
        else:
            print("❌ DataRecord - init failed")
    except Exception as e:
        print(f"❌ DataRecord - {e}")
    
    # Exercise 1: User
    total += 1
    try:
        user = User("test@example.com", "Test User")
        if user.email == "test@example.com":
            try:
                User("invalid", "Bad User")
                print("❌ User - should reject invalid email")
            except ValueError:
                print("✅ User")
                passed += 1
        else:
            print("❌ User")
    except Exception as e:
        print(f"❌ User - {e}")
    
    # Exercise 2: Pipeline repr/str
    total += 1
    try:
        p = Pipeline("test", ["a", "b"])
        if "test" in repr(p) and "steps=" in repr(p):
            if "test" in str(p) and "2 steps" in str(p):
                print("✅ Pipeline __repr__ and __str__")
                passed += 1
            else:
                print("❌ Pipeline __str__")
        else:
            print("❌ Pipeline __repr__")
    except Exception as e:
        print(f"❌ Pipeline - {e}")
    
    # Exercise 2: APIResponse
    total += 1
    try:
        resp = APIResponse(200, {"data": 1}, 0.5)
        if "200" in repr(resp) and "0.5" in repr(resp):
            if "OK" in str(resp) and "0.5" in str(resp):
                resp404 = APIResponse(404, {}, 0.1)
                if "ERROR" in str(resp404):
                    print("✅ APIResponse")
                    passed += 1
                else:
                    print("❌ APIResponse - 404 should show ERROR")
            else:
                print("❌ APIResponse __str__")
        else:
            print("❌ APIResponse __repr__")
    except Exception as e:
        print(f"❌ APIResponse - {e}")
    
    # Exercise 3: DataBatch properties
    total += 1
    try:
        batch = DataBatch([{"a": 1}, {"b": 2}])
        empty = DataBatch([])
        if batch.count == 2 and not batch.is_empty:
            if batch.first == {"a": 1} and batch.last == {"b": 2}:
                if empty.is_empty and empty.first is None:
                    print("✅ DataBatch properties")
                    passed += 1
                else:
                    print("❌ DataBatch empty handling")
            else:
                print("❌ DataBatch first/last")
        else:
            print("❌ DataBatch count/is_empty")
    except Exception as e:
        print(f"❌ DataBatch - {e}")
    
    # Exercise 3: Connection
    total += 1
    try:
        conn = Connection("localhost", 5432)
        if conn.status == "disconnected" and conn.connection_string == "localhost:5432":
            conn.connect()
            if conn.status == "connected":
                print("✅ Connection")
                passed += 1
            else:
                print("❌ Connection - connect failed")
        else:
            print("❌ Connection - initial state wrong")
    except Exception as e:
        print(f"❌ Connection - {e}")
    
    # Exercise 4: Config
    total += 1
    try:
        config = Config({"test": True})
        if config.get("test") == True:
            json_config = Config.from_json('{"port": 9000}')
            if json_config.get("port") == 9000:
                default_config = Config.default()
                if default_config.get("debug") == False:
                    if Config.validate_port(8080) and not Config.validate_port(99999):
                        print("✅ Config")
                        passed += 1
                    else:
                        print("❌ Config validate_port")
                else:
                    print("❌ Config default")
            else:
                print("❌ Config from_json")
        else:
            print("❌ Config get")
    except Exception as e:
        print(f"❌ Config - {e}")
    
    # Exercise 4: DataLoader
    total += 1
    try:
        csv_loader = DataLoader.from_csv_path("/data/test.csv")
        api_loader = DataLoader.from_api_endpoint("https://api.test.com")
        if csv_loader.source_type == "csv" and api_loader.source_type == "api":
            if DataLoader.is_valid_url("https://test.com") and not DataLoader.is_valid_url("not-a-url"):
                print("✅ DataLoader")
                passed += 1
            else:
                print("❌ DataLoader is_valid_url")
        else:
            print("❌ DataLoader factory methods")
    except Exception as e:
        print(f"❌ DataLoader - {e}")
    
    # Exercise 5: DataExtractor
    total += 1
    try:
        extractor = DataExtractor("test", {"base_url": "http://test.com"})
        if extractor.is_configured and extractor.extract_count == 0:
            result = extractor.extract("/users")
            if extractor.extract_count == 1 and result.get("endpoint") == "/users":
                if extractor.last_extract_time is not None:
                    print("✅ DataExtractor")
                    passed += 1
                else:
                    print("❌ DataExtractor - last_extract_time not set")
            else:
                print("❌ DataExtractor - extract failed")
        else:
            print("❌ DataExtractor - init failed")
    except Exception as e:
        print(f"❌ DataExtractor - {e}")
    
    # Exercise 5: DataValidator
    total += 1
    try:
        validator = DataValidator({"name": str, "age": int})
        if validator.validate({"name": "Alice", "age": 30}):
            if not validator.validate({"name": "Bob", "age": "thirty"}):
                if len(validator.errors) > 0:
                    batch_result = validator.validate_batch([
                        {"name": "A", "age": 1},
                        {"name": "B", "age": "bad"},
                        {"name": "C", "age": 3}
                    ])
                    if batch_result["valid_count"] == 2 and batch_result["invalid_count"] == 1:
                        print("✅ DataValidator")
                        passed += 1
                    else:
                        print("❌ DataValidator - validate_batch")
                else:
                    print("❌ DataValidator - errors not populated")
            else:
                print("❌ DataValidator - should reject invalid type")
        else:
            print("❌ DataValidator - should accept valid data")
    except Exception as e:
        print(f"❌ DataValidator - {e}")
    
    # Exercise 6: DataPipeline with composition
    total += 1
    try:
        pipeline = DataPipeline("test", ["a", "b"])
        result = pipeline.run()
        if result and len(pipeline.logger.messages) >= 3:
            if any("started" in m.lower() for m in pipeline.logger.messages):
                print("✅ DataPipeline composition")
                passed += 1
            else:
                print("❌ DataPipeline - missing start log")
        else:
            print("❌ DataPipeline - run failed or not enough logs")
    except Exception as e:
        print(f"❌ DataPipeline - {e}")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
