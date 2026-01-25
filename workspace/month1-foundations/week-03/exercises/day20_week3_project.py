#!/usr/bin/env python3
"""
Day 20: Week 3 Project - Containerized Data Pipeline
=====================================================
Duration: 6-7 hours (Saturday project day)

Build a complete containerized data extraction pipeline.
This combines everything from Week 3: Git, AWS, S3, Docker.

WHY THIS MATTERS:
- Real data engineering = containerized pipelines
- This is what your portfolio projects look like
- Deployable, reproducible, professional
- Interview-ready demonstration

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Any

# =============================================================================
# WEEK 3 PROJECT: CONTAINERIZED DATA PIPELINE
# =============================================================================

"""
PROJECT OVERVIEW
================

Build a containerized pipeline that:
1. Extracts data from a free public API
2. Transforms the data (cleaning, validation)
3. Loads to S3 (or local file system for testing)
4. Has proper logging, error handling, configuration
5. Runs in Docker

This is a mini version of Project 1 (Stock Pipeline).


PART 1: PROJECT SETUP (30 min)
==============================

Create this structure:
    
week3-project/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extractor.py
│   ├── transformer.py
│   ├── loader.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py
└── data/
    └── .gitkeep

Commands:
    mkdir -p week3-project/{src,tests,data}
    cd week3-project
    touch docker-compose.yml Dockerfile requirements.txt .env.example .gitignore README.md
    touch src/__init__.py src/config.py src/extractor.py src/transformer.py src/loader.py src/main.py
    touch tests/__init__.py tests/test_pipeline.py
    touch data/.gitkeep


PART 2: CONFIGURATION (45 min)
==============================

Create src/config.py - Configuration management
"""

# =============================================================================
# EXAMPLE: config.py
# =============================================================================

CONFIG_TEMPLATE = '''
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    """Pipeline configuration from environment variables."""
    
    # API Settings
    api_base_url: str = "https://api.coindesk.com/v1"
    api_timeout: int = 30
    
    # Storage Settings
    output_path: str = "./data"
    use_s3: bool = False
    s3_bucket: Optional[str] = None
    
    # Logging
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        return cls(
            api_base_url=os.getenv("API_BASE_URL", cls.api_base_url),
            api_timeout=int(os.getenv("API_TIMEOUT", cls.api_timeout)),
            output_path=os.getenv("OUTPUT_PATH", cls.output_path),
            use_s3=os.getenv("USE_S3", "false").lower() == "true",
            s3_bucket=os.getenv("S3_BUCKET"),
            log_level=os.getenv("LOG_LEVEL", cls.log_level),
            log_file=os.getenv("LOG_FILE")
        )
'''


# =============================================================================
# EXAMPLE: extractor.py
# =============================================================================

EXTRACTOR_TEMPLATE = '''
import requests
import logging
from typing import Dict, Any, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class APIExtractor:
    """Extract data from public API."""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def extract(self, endpoint: str) -> Optional[Dict[str, Any]]:
        """
        Extract data from API endpoint.
        
        Args:
            endpoint: API endpoint path
            
        Returns:
            JSON response data or None if failed
        """
        url = f"{self.base_url}/{endpoint}"
        
        try:
            logger.info(f"Extracting from {url}")
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"Successfully extracted data")
            return data
            
        except requests.exceptions.Timeout:
            logger.error(f"Request timed out: {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None
        except ValueError as e:
            logger.error(f"Invalid JSON response: {e}")
            return None
    
    def extract_with_metadata(self, endpoint: str) -> Dict[str, Any]:
        """Extract data with extraction metadata."""
        data = self.extract(endpoint)
        
        return {
            "extracted_at": datetime.utcnow().isoformat(),
            "source": f"{self.base_url}/{endpoint}",
            "success": data is not None,
            "data": data
        }
'''


# =============================================================================
# EXAMPLE: transformer.py  
# =============================================================================

TRANSFORMER_TEMPLATE = '''
import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class DataTransformer:
    """Transform extracted data."""
    
    def transform(self, raw_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Transform raw API data into clean format.
        
        Args:
            raw_data: Raw extraction result
            
        Returns:
            Transformed data or None if validation fails
        """
        if not raw_data.get("success"):
            logger.warning("Skipping transform - extraction failed")
            return None
        
        data = raw_data.get("data", {})
        
        # Validate required fields
        if not self._validate(data):
            return None
        
        # Transform to clean schema
        transformed = {
            "extracted_at": raw_data["extracted_at"],
            "transformed_at": datetime.utcnow().isoformat(),
            "source": raw_data["source"],
            "records": self._clean_records(data)
        }
        
        logger.info(f"Transformed {len(transformed['records'])} records")
        return transformed
    
    def _validate(self, data: Dict) -> bool:
        """Validate data structure."""
        # Add your validation logic here
        if not data:
            logger.error("Empty data received")
            return False
        return True
    
    def _clean_records(self, data: Dict) -> List[Dict]:
        """Clean and normalize records."""
        # This depends on your API structure
        # Example for Bitcoin price API:
        records = []
        
        if "bpi" in data:  # Bitcoin Price Index
            for currency, info in data["bpi"].items():
                records.append({
                    "currency": currency,
                    "rate": info.get("rate_float"),
                    "description": info.get("description")
                })
        
        return records
'''


# =============================================================================
# EXAMPLE: loader.py
# =============================================================================

LOADER_TEMPLATE = '''
import os
import json
import logging
from datetime import datetime
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class FileLoader:
    """Load data to local file system."""
    
    def __init__(self, output_path: str):
        self.output_path = output_path
        os.makedirs(output_path, exist_ok=True)
    
    def load(self, data: Dict[str, Any], prefix: str = "data") -> Optional[str]:
        """
        Save data to JSON file.
        
        Args:
            data: Data to save
            prefix: Filename prefix
            
        Returns:
            Output file path or None if failed
        """
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{prefix}_{timestamp}.json"
        filepath = os.path.join(self.output_path, filename)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2, default=str)
            
            logger.info(f"Saved data to {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Failed to save data: {e}")
            return None


class S3Loader:
    """Load data to S3."""
    
    def __init__(self, bucket: str):
        import boto3
        self.bucket = bucket
        self.s3 = boto3.client('s3')
    
    def load(self, data: Dict[str, Any], prefix: str = "data") -> Optional[str]:
        """Save data to S3."""
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        key = f"raw/{prefix}/{prefix}_{timestamp}.json"
        
        try:
            self.s3.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=json.dumps(data, indent=2, default=str),
                ContentType='application/json'
            )
            
            logger.info(f"Saved data to s3://{self.bucket}/{key}")
            return f"s3://{self.bucket}/{key}"
            
        except Exception as e:
            logger.error(f"Failed to save to S3: {e}")
            return None
'''


# =============================================================================
# EXAMPLE: main.py
# =============================================================================

MAIN_TEMPLATE = '''
import logging
import sys
from config import Config
from extractor import APIExtractor
from transformer import DataTransformer
from loader import FileLoader, S3Loader


def setup_logging(config: Config) -> None:
    """Configure logging."""
    handlers = [logging.StreamHandler(sys.stdout)]
    
    if config.log_file:
        handlers.append(logging.FileHandler(config.log_file))
    
    logging.basicConfig(
        level=getattr(logging, config.log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )


def run_pipeline(config: Config) -> bool:
    """
    Run the complete ETL pipeline.
    
    Returns:
        True if successful, False otherwise
    """
    logger = logging.getLogger(__name__)
    logger.info("Starting pipeline")
    
    # Extract
    extractor = APIExtractor(config.api_base_url, config.api_timeout)
    raw_data = extractor.extract_with_metadata("bpi/currentprice.json")
    
    if not raw_data["success"]:
        logger.error("Extraction failed")
        return False
    
    # Transform
    transformer = DataTransformer()
    transformed = transformer.transform(raw_data)
    
    if not transformed:
        logger.error("Transformation failed")
        return False
    
    # Load
    if config.use_s3 and config.s3_bucket:
        loader = S3Loader(config.s3_bucket)
    else:
        loader = FileLoader(config.output_path)
    
    output_path = loader.load(transformed, "bitcoin_price")
    
    if not output_path:
        logger.error("Loading failed")
        return False
    
    logger.info(f"Pipeline complete: {output_path}")
    return True


if __name__ == "__main__":
    config = Config.from_env()
    setup_logging(config)
    
    success = run_pipeline(config)
    sys.exit(0 if success else 1)
'''


# =============================================================================
# EXAMPLE: Dockerfile
# =============================================================================

DOCKERFILE_TEMPLATE = '''
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/

# Set Python path
ENV PYTHONPATH=/app/src

# Run pipeline
CMD ["python", "src/main.py"]
'''


# =============================================================================
# EXAMPLE: docker-compose.yml
# =============================================================================

DOCKER_COMPOSE_TEMPLATE = '''
version: '3.8'

services:
  pipeline:
    build: .
    environment:
      - API_BASE_URL=https://api.coindesk.com/v1
      - OUTPUT_PATH=/app/data
      - LOG_LEVEL=INFO
      # Uncomment for S3:
      # - USE_S3=true
      # - S3_BUCKET=your-bucket
      # - AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
      # - AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
    volumes:
      - ./data:/app/data
'''


# =============================================================================
# PROJECT VERIFICATION
# =============================================================================

def verify_project_structure() -> Dict[str, bool]:
    """Check if project structure is complete."""
    required_files = [
        "Dockerfile",
        "docker-compose.yml",
        "requirements.txt",
        "src/__init__.py",
        "src/config.py",
        "src/extractor.py",
        "src/transformer.py",
        "src/loader.py",
        "src/main.py"
    ]
    
    results = {}
    for file in required_files:
        results[file] = os.path.exists(file)
    
    return results


def print_templates() -> None:
    """Print all code templates."""
    templates = {
        "src/config.py": CONFIG_TEMPLATE,
        "src/extractor.py": EXTRACTOR_TEMPLATE,
        "src/transformer.py": TRANSFORMER_TEMPLATE,
        "src/loader.py": LOADER_TEMPLATE,
        "src/main.py": MAIN_TEMPLATE,
        "Dockerfile": DOCKERFILE_TEMPLATE,
        "docker-compose.yml": DOCKER_COMPOSE_TEMPLATE
    }
    
    for name, template in templates.items():
        print(f"\n{'='*60}")
        print(f"FILE: {name}")
        print('='*60)
        print(template)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "templates":
            print_templates()
        elif cmd == "verify":
            results = verify_project_structure()
            print("Project Structure Check:")
            for file, exists in results.items():
                status = "✅" if exists else "❌"
                print(f"  {status} {file}")
    else:
        print("Day 20: Week 3 Project - Containerized Data Pipeline")
        print("=" * 55)
        print("\nThis is a PROJECT day (6-7 hours).")
        print("Build a complete containerized ETL pipeline.")
        print("\nCommands:")
        print("  python day20_week3_project.py templates - Show all code templates")
        print("  python day20_week3_project.py verify    - Check project structure")
        print("\nDeliverables:")
        print("  1. Working Docker container")
        print("  2. Pipeline that extracts real data")
        print("  3. Clean code with logging")
        print("  4. README with instructions")
