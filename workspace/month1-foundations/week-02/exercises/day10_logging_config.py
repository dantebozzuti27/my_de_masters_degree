#!/usr/bin/env python3
"""
Day 10: Logging & Configuration Management
==========================================
Duration: 2 hours

Production-ready logging and configuration patterns.
Learn to build observable, debuggable, configurable code.

WHY THIS MATTERS:
- You can't debug production without logs
- Configuration management enables different environments
- Senior engineers always add proper logging
- This separates junior from senior code
"""

import logging
import json
from operator import truediv
import os
from typing import Any, Dict, Optional, List
from datetime import datetime

# =============================================================================
# EXERCISE 1: Basic Logging Setup (20 min)
# =============================================================================
# Purpose: Understand Python's logging module fundamentals
# Key concepts: Loggers, handlers, formatters, log levels

def setup_basic_logger(name: str, level: str = "INFO") -> logging.Logger:
    """
    Create a basic logger with console output.
    
    Log Levels (from least to most severe):
    - DEBUG: Detailed info for debugging
    - INFO: General operational info
    - WARNING: Something unexpected but not critical
    - ERROR: Something failed
    - CRITICAL: System is failing
    
    Example:
        >>> logger = setup_basic_logger("my_app")
        >>> logger.info("Application started")
        >>> logger.error("Something went wrong")
    
    TODO:
    1. Create logger with given name
    2. Set log level (use getattr(logging, level.upper()))
    3. Create StreamHandler for console output
    4. Create formatter: '[%(levelname)s] %(name)s: %(message)s'
    5. Add formatter to handler, handler to logger
    6. Return logger
    """
    # YOUR CODE HERE
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(name)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def setup_file_logger(name: str, filepath: str, level: str = "DEBUG") -> logging.Logger:
    """
    Create a logger that writes to a file.
    
    Example:
        >>> logger = setup_file_logger("app", "app.log")
        >>> logger.info("This goes to file")
    
    TODO:
    1. Create logger with given name
    2. Set level
    3. Create FileHandler with filepath
    4. Create formatter: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    5. Add formatter to handler, handler to logger
    6. Return logger
    """
    # YOUR CODE HERE
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))
    handler = logging.FileHandler(filepath)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


# =============================================================================
# EXERCISE 2: Structured Logging (25 min)
# =============================================================================
# Purpose: Create logs that can be parsed and analyzed
# Key insight: JSON logs are searchable in production systems

class StructuredLogger:
    """
    A logger that outputs JSON-formatted log entries.
    
    In production, JSON logs can be:
    - Parsed by log aggregators (Datadog, Splunk)
    - Filtered by fields
    - Analyzed for patterns
    
    Example:
        >>> logger = StructuredLogger("my_app")
        >>> logger.info("User logged in", user_id=123, ip="192.168.1.1")
        # Outputs: {"timestamp": "...", "level": "INFO", "logger": "my_app", 
        #           "message": "User logged in", "user_id": 123, "ip": "192.168.1.1"}
    """
    
    def __init__(self, name: str, min_level: str = "DEBUG"):
        """
        Initialize structured logger.
        
        Store name and min_level (as uppercase string).
        Initialize self.entries as empty list to capture logs.
        """
        # YOUR CODE HERE
        self.name = name
        self.min_level = min_level.upper()
        self.entries = []

    
    def _should_log(self, level: str) -> bool:
        """
        Check if we should log at this level.
        
        Level hierarchy: DEBUG < INFO < WARNING < ERROR < CRITICAL
        If min_level is WARNING, only log WARNING, ERROR, CRITICAL
        """
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        # YOUR CODE HERE
        levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        incoming_index = levels.index(level)
        minimum_index = levels.index(self.min_level)
        return incoming_index >= minimum_index
    
    def _create_entry(self, level: str, message: str, **kwargs) -> Dict:
        """
        Create a log entry dict.
        
        Must include:
        - timestamp (ISO format)
        - level
        - logger (self.name)
        - message
        - Any additional kwargs
        """
        # YOUR CODE HERE
        entry = {
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "logger": self.name,
            "message": message,
        }
        entry.update(kwargs)
        return entry
    
    def log(self, level: str, message: str, **kwargs) -> Optional[Dict]:
        """
        Log a message at the specified level.
        
        1. Check if we should log at this level
        2. Create entry
        3. Append to self.entries
        4. Return the entry (or None if not logged)
        """
        # YOUR CODE HERE
        if not self._should_log(level):
            return None
        entry = self._create_entry(level, message, **kwargs)
        self.entries.append(entry)
        return entry


    
    def debug(self, message: str, **kwargs) -> Optional[Dict]:
        """Log at DEBUG level."""
        return self.log("DEBUG", message, **kwargs)
    
    def info(self, message: str, **kwargs) -> Optional[Dict]:
        """Log at INFO level."""
        return self.log("INFO", message, **kwargs)
    
    def warning(self, message: str, **kwargs) -> Optional[Dict]:
        """Log at WARNING level."""
        return self.log("WARNING", message, **kwargs)
    
    def error(self, message: str, **kwargs) -> Optional[Dict]:
        """Log at ERROR level."""
        return self.log("ERROR", message, **kwargs)
    
    def get_entries(self, level: Optional[str] = None) -> List[Dict]:
        """
        Get all log entries, optionally filtered by level.
        
        Example:
            >>> logger.get_entries("ERROR")  # Only ERROR entries
            >>> logger.get_entries()  # All entries
        """
        # YOUR CODE HERE
        if level is None:
            return self.entries
        else:
            result = []
            for entry in self.entries:
                if entry["level"] == level:
                    result.append(entry)
            return result


# =============================================================================
# EXERCISE 3: Configuration from Environment (25 min)
# =============================================================================
# Purpose: Load configuration from environment variables
# Key insight: Never hardcode secrets or environment-specific values

class EnvConfig:
    """
    Load configuration from environment variables with defaults.
    
    This is the standard pattern for 12-factor apps.
    Different environments (dev, staging, prod) just set different env vars.
    
    Example:
        >>> os.environ["APP_DEBUG"] = "true"
        >>> config = EnvConfig(prefix="APP")
        >>> config.get_bool("DEBUG")
        True
        >>> config.get_int("PORT", 8080)  # Uses default
        8080
    """
    
    def __init__(self, prefix: str = ""):
        """
        Store prefix for environment variable names.
        If prefix is "APP", we look for "APP_DEBUG", "APP_PORT", etc.
        """
        # YOUR CODE HERE
        self.prefix = prefix
    
    def _get_key(self, name: str) -> str:
        """
        Build full environment variable name.
        If prefix is "APP" and name is "DEBUG", return "APP_DEBUG".
        If prefix is empty, just return name.
        """
        # YOUR CODE HERE
        if self.prefix:
            return f"{self.prefix}_{name}"
        return name
    
    def get(self, name: str, default: Optional[str] = None) -> Optional[str]:
        """
        Get string value from environment.
        
        Example:
            >>> os.environ["APP_HOST"] = "localhost"
            >>> config.get("HOST")
            'localhost'
        """
        # YOUR CODE HERE
        key = self._get_key(name)
        return os.environ.get(key, default)
    
    def get_bool(self, name: str, default: bool = False) -> bool:
        """
        Get boolean value from environment.
        
        True values: "true", "1", "yes" (case insensitive)
        Everything else is False.
        """
        # YOUR CODE HERE
        value = self.get(name)
        if value is None:
            return default
        return value.lower() in ("true", "1", "yes")
    
    def get_int(self, name: str, default: int = 0) -> int:
        """
        Get integer value from environment.
        
        Returns default if not set or not a valid integer.
        """
        # YOUR CODE HERE
        value = self.get(name)
        if value is None:
            return default
        try:
            return int(value)
        except ValueError:
            return default
    
    def get_list(self, name: str, separator: str = ",", default: Optional[List[str]] = None) -> List[str]:
        """
        Get list value from environment (comma-separated by default).
        
        Example:
            >>> os.environ["APP_HOSTS"] = "host1,host2,host3"
            >>> config.get_list("HOSTS")
            ['host1', 'host2', 'host3']
        """
        # YOUR CODE HERE
        value = self.get(name)
        if value is None:
            return default if default is not None else []
        return value.split(separator)
        
    
    def require(self, name: str) -> str:
        """
        Get required value - raises error if not set.
        
        Use for critical config like database URLs.
        """
        # YOUR CODE HERE
        value = self.get(name)
        if value is None:
            key = self._get_key(name)
            raise ValueError(f"Required env variable {key} is not set")
        return value


# =============================================================================
# EXERCISE 4: Configuration File Loading (20 min)
# =============================================================================
# Purpose: Load configuration from JSON/dict with validation

class FileConfig:
    """
    Configuration from files/dicts with validation and defaults.
    
    Example:
        >>> config = FileConfig({"debug": True, "port": 8080})
        >>> config.get("port")
        8080
        >>> config.get("missing", "default")
        'default'
    """
    
    def __init__(self, settings: Dict[str, Any]):
        """Store settings dictionary."""
        # YOUR CODE HERE
        self.settings = settings
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a value with optional default."""
        # YOUR CODE HERE
        return self.settings.get(key, default)
    
    def get_nested(self, path: str, default: Any = None) -> Any:
        """
        Get nested value using dot notation.
        
        Example:
            >>> config = FileConfig({"database": {"host": "localhost"}})
            >>> config.get_nested("database.host")
            'localhost'
            >>> config.get_nested("database.port", 5432)
            5432
        """
        # YOUR CODE HERE
        keys = path.split(".")
        value = self.settings
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value    

    @classmethod
    def from_json_file(cls, filepath: str) -> "FileConfig":
        """
        Load config from JSON file.
        
        If file doesn't exist, return empty config.
        """
        # YOUR CODE HERE
        if not os.path.exists(filepath):
            return cls({})
        with open(filepath, 'r') as f:
            settings = json.load(f)
        return cls(settings)
    
    def merge(self, other: "FileConfig") -> "FileConfig":
        """
        Merge another config into this one.
        Other values override self values.
        Returns a new FileConfig.
        """
        # YOUR CODE HERE
        merged = {**self.settings, **other.settings}
        return FileConfig(merged)
    
    def validate_required(self, keys: List[str]) -> List[str]:
        """
        Check that required keys exist.
        Returns list of missing keys.
        """
        # YOUR CODE HERE
        missing = []
        for key in keys:
            if key not in self.settings:
                missing.append(key)
        return missing



# =============================================================================
# EXERCISE 5: Complete Configurable Pipeline (30 min)
# =============================================================================
# Purpose: Put it all together - a pipeline with logging and configuration

class ConfigurablePipeline:
    """
    A data pipeline with proper logging and configuration.
    
    This is the pattern for production code:
    - Configurable behavior
    - Comprehensive logging
    - Observable execution
    
    Example:
        >>> config = {"name": "etl", "debug": True, "steps": ["extract", "transform"]}
        >>> pipeline = ConfigurablePipeline(config)
        >>> pipeline.run()
        >>> len(pipeline.get_logs()) > 0
        True
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize pipeline with configuration.
        
        Required config:
        - name: Pipeline name
        - steps: List of step names
        
        Optional config:
        - debug: Enable debug logging (default False)
        - dry_run: Don't actually execute (default False)
        """
        self.config = config
        self.name = config.get("name", "unnamed_pipeline")
        self.steps = config.get("steps", [])
        self.debug = config.get("debug", False)
        self.dry_run = config.get("dry_run", False)
        
        # Create structured logger
        min_level = "DEBUG" if self.debug else "INFO"
        self.logger = StructuredLogger(self.name, min_level)
        
        # Track execution state
        self.executed_steps: List[str] = []
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None
    
    def run(self) -> Dict[str, Any]:
        """
        Run the pipeline.
        
        1. Log pipeline start (INFO)
        2. Log configuration if debug mode (DEBUG)
        3. For each step:
           - Log step start (INFO)
           - Execute step (or simulate if dry_run)
           - Log step complete (INFO)
        4. Log pipeline complete with duration (INFO)
        5. Return result dict with steps executed and duration
        
        TODO: Implement this method
        """
        # YOUR CODE HERE
        self.start_time = datetime.now()
        self.logger.info("Pipeline started", steps=len(self.steps))
        if self.debug:
            self.logger.debug("Configuration", config=self.config)
        for step in self.steps:
            self.logger.info(f"starting step: {step}")
            self._execute_step(step)
            self.logger.info(f"completed step: {step}")
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).total_seconds()
        self.logger.info("pipeline complete", duration_seconds=duration)
        return {
            "steps_executed": len(self.executed_steps),
            "duration_seconds": duration
        }
    
    def _execute_step(self, step: str) -> bool:
        """
        Execute a single step.
        
        For now, just simulate by adding to executed_steps.
        In real code, this would call actual step functions.
        """
        # YOUR CODE HERE
        self.executed_steps.append(step)
        return True
    
    def get_logs(self) -> List[Dict]:
        """Return all log entries."""
        # YOUR CODE HERE
        return self.logger.get_entries()
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Return execution statistics.
        
        Include:
        - name
        - steps_total
        - steps_executed
        - duration_seconds (if run completed)
        - status: "not_started", "completed", or "dry_run"
        """
        # YOUR CODE HERE
        if self.start_time is None:
            status = "not_started"
        elif self.dry_run:
            status = "dry_run"
        else:
            status = "completed"
        duration = None
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds()
        return {
            "name": self.name,
            "steps_total": len(self.steps),
            "steps_executed": len(self.executed_steps),
            "duration_seconds": duration,
            "status": status
        }


# =============================================================================
# Tests
# =============================================================================

def run_tests():
    print("=" * 60)
    print("DAY 10: Logging & Configuration - Tests")
    print("=" * 60 + "\n")
    
    passed = 0
    total = 0
    
    # Test 1: Basic Logger
    total += 1
    try:
        logger = setup_basic_logger("test_app", "INFO")
        if logger and logger.name == "test_app":
            print("✅ setup_basic_logger")
            passed += 1
        else:
            print("❌ setup_basic_logger")
    except Exception as e:
        print(f"❌ setup_basic_logger - {e}")
    
    # Test 2: StructuredLogger
    total += 1
    try:
        slog = StructuredLogger("app", "INFO")
        entry = slog.info("Test message", user_id=123)
        if entry and entry.get("message") == "Test message" and entry.get("user_id") == 123:
            if entry.get("level") == "INFO" and "timestamp" in entry:
                # Test level filtering
                debug_entry = slog.debug("Debug message")
                if debug_entry is None:  # Should be filtered
                    print("✅ StructuredLogger")
                    passed += 1
                else:
                    print("❌ StructuredLogger - DEBUG should be filtered")
            else:
                print("❌ StructuredLogger - missing fields")
        else:
            print("❌ StructuredLogger - entry format wrong")
    except Exception as e:
        print(f"❌ StructuredLogger - {e}")
    
    # Test 3: StructuredLogger.get_entries
    total += 1
    try:
        slog = StructuredLogger("test", "DEBUG")
        slog.info("Info 1")
        slog.error("Error 1")
        slog.info("Info 2")
        all_entries = slog.get_entries()
        error_entries = slog.get_entries("ERROR")
        if len(all_entries) == 3 and len(error_entries) == 1:
            print("✅ StructuredLogger.get_entries")
            passed += 1
        else:
            print(f"❌ StructuredLogger.get_entries - got {len(all_entries)} all, {len(error_entries)} errors")
    except Exception as e:
        print(f"❌ StructuredLogger.get_entries - {e}")
    
    # Test 4: EnvConfig
    total += 1
    try:
        os.environ["TEST_DEBUG"] = "true"
        os.environ["TEST_PORT"] = "9000"
        os.environ["TEST_HOSTS"] = "a,b,c"
        
        config = EnvConfig("TEST")
        if config.get_bool("DEBUG") == True:
            if config.get_int("PORT") == 9000:
                if config.get_list("HOSTS") == ["a", "b", "c"]:
                    print("✅ EnvConfig")
                    passed += 1
                else:
                    print("❌ EnvConfig - get_list")
            else:
                print("❌ EnvConfig - get_int")
        else:
            print("❌ EnvConfig - get_bool")
    except Exception as e:
        print(f"❌ EnvConfig - {e}")
    finally:
        os.environ.pop("TEST_DEBUG", None)
        os.environ.pop("TEST_PORT", None)
        os.environ.pop("TEST_HOSTS", None)
    
    # Test 5: EnvConfig.require
    total += 1
    try:
        config = EnvConfig("MISSING")
        try:
            config.require("NONEXISTENT")
            print("❌ EnvConfig.require - should raise error")
        except (ValueError, KeyError):
            print("✅ EnvConfig.require")
            passed += 1
    except Exception as e:
        print(f"❌ EnvConfig.require - {e}")
    
    # Test 6: FileConfig
    total += 1
    try:
        config = FileConfig({"name": "test", "port": 8080})
        if config.get("name") == "test" and config.get("missing", "default") == "default":
            print("✅ FileConfig.get")
            passed += 1
        else:
            print("❌ FileConfig.get")
    except Exception as e:
        print(f"❌ FileConfig.get - {e}")
    
    # Test 7: FileConfig.get_nested
    total += 1
    try:
        config = FileConfig({"db": {"host": "localhost", "port": 5432}})
        if config.get_nested("db.host") == "localhost":
            if config.get_nested("db.port") == 5432:
                if config.get_nested("db.missing", "default") == "default":
                    print("✅ FileConfig.get_nested")
                    passed += 1
                else:
                    print("❌ FileConfig.get_nested - default not working")
            else:
                print("❌ FileConfig.get_nested - port")
        else:
            print("❌ FileConfig.get_nested - host")
    except Exception as e:
        print(f"❌ FileConfig.get_nested - {e}")
    
    # Test 8: FileConfig.merge
    total += 1
    try:
        base = FileConfig({"a": 1, "b": 2})
        override = FileConfig({"b": 3, "c": 4})
        merged = base.merge(override)
        if merged.get("a") == 1 and merged.get("b") == 3 and merged.get("c") == 4:
            print("✅ FileConfig.merge")
            passed += 1
        else:
            print("❌ FileConfig.merge")
    except Exception as e:
        print(f"❌ FileConfig.merge - {e}")
    
    # Test 9: ConfigurablePipeline
    total += 1
    try:
        config = {"name": "test_pipeline", "steps": ["a", "b", "c"], "debug": True}
        pipeline = ConfigurablePipeline(config)
        result = pipeline.run()
        if result and len(pipeline.executed_steps) == 3:
            if len(pipeline.get_logs()) > 0:
                stats = pipeline.get_stats()
                if stats.get("steps_executed") == 3:
                    print("✅ ConfigurablePipeline")
                    passed += 1
                else:
                    print("❌ ConfigurablePipeline - stats wrong")
            else:
                print("❌ ConfigurablePipeline - no logs")
        else:
            print("❌ ConfigurablePipeline - run failed")
    except Exception as e:
        print(f"❌ ConfigurablePipeline - {e}")
    
    # Test 10: ConfigurablePipeline dry_run
    total += 1
    try:
        config = {"name": "dry", "steps": ["x"], "dry_run": True}
        pipeline = ConfigurablePipeline(config)
        result = pipeline.run()
        stats = pipeline.get_stats()
        if stats.get("status") == "dry_run":
            print("✅ ConfigurablePipeline dry_run")
            passed += 1
        else:
            print("❌ ConfigurablePipeline dry_run")
    except Exception as e:
        print(f"❌ ConfigurablePipeline dry_run - {e}")
    
    print("\n" + "=" * 60)
    if passed == total:
        print(f"🎉 ALL TESTS PASSED! ({passed}/{total})")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
