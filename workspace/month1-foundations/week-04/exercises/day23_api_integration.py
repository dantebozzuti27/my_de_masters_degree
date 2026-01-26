#!/usr/bin/env python3
"""
Day 23: API Integration Patterns - Production Data Extraction
==============================================================
Duration: 3-4 hours total

Today you'll master API integration for data engineering:
- Rate limiting and throttling
- Pagination handling
- Authentication (API keys, OAuth)
- Robust error handling
- Incremental extraction

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: Python requests basics, error handling

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHY API INTEGRATION MATTERS
===========================

Most data comes from APIs:
- Internal microservices
- Third-party SaaS (Salesforce, HubSpot, Stripe)
- Public data (government, social media)
- Partner systems

Data engineers must handle:
- Rate limits (don't get blocked!)
- Authentication (API keys, OAuth, tokens)
- Pagination (large datasets)
- Errors (network, API errors, retries)
- Data quality (validation, cleaning)


KEY CONCEPTS:
=============

1. RATE LIMITING
   APIs limit how many requests you can make
   - Per second: 10 requests/second
   - Per minute: 100 requests/minute
   - Per day: 10,000 requests/day
   
   Strategies:
   - Sleep between requests
   - Exponential backoff on 429 errors
   - Request queue with rate limiter

2. PAGINATION
   Large datasets are split into pages
   
   Types:
   - Offset: ?page=2&limit=100
   - Cursor: ?cursor=abc123
   - Link header: Next page URL in response header
   
3. AUTHENTICATION
   Types:
   - API Key: X-API-Key header or query param
   - Bearer Token: Authorization: Bearer <token>
   - OAuth 2.0: Token refresh flow
   - Basic Auth: Base64 encoded username:password

4. ERROR HANDLING
   HTTP Status Codes:
   - 200: Success
   - 400: Bad request (your fault)
   - 401: Unauthorized (bad credentials)
   - 403: Forbidden (no permission)
   - 404: Not found
   - 429: Rate limited (slow down!)
   - 500: Server error (their fault, retry)

5. IDEMPOTENCY
   Same request = same result
   Important for:
   - Retries
   - Crash recovery
   - Duplicate prevention


LEARNING RESOURCES:
==================

VIDEO:
- "REST API Tutorial" - Programming with Mosh (1 hour)
  https://www.youtube.com/watch?v=SLwpqD8n3d0
  
- "Python Requests Library" - Corey Schafer (30 min)
  https://www.youtube.com/watch?v=tb8gHvYlCFs

READING:
- requests library documentation
  https://docs.python-requests.org/en/latest/

- "Fundamentals of Data Engineering" - Chapter on Ingestion
  Focus on: API extraction patterns
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

import requests
import time
import logging
from typing import Dict, List, Optional, Any, Generator
from dataclasses import dataclass
from datetime import datetime, timezone
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
EXERCISE 1: BASIC API CLIENT (20 min)
=====================================

Let's build a proper API client from scratch.
"""

class APIClient:
    """
    Production-ready API client with error handling.
    
    Usage:
        client = APIClient("https://api.example.com")
        data = client.get("/users")
    """
    
    def __init__(
        self,
        base_url: str,
        timeout: int = 30,
        headers: Optional[Dict[str, str]] = None
    ):
        """
        Initialize API client.
        
        Args:
            base_url: Base URL (e.g., "https://api.example.com")
            timeout: Request timeout in seconds
            headers: Default headers for all requests
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        
        # Set default headers
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            **(headers or {})
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Any]:
        """
        Make a GET request.
        
        Args:
            endpoint: API endpoint (e.g., "/users")
            params: Query parameters
            
        Returns:
            JSON response data, or None on error
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.get(
                url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
            
        except requests.HTTPError as e:
            logger.error(f"HTTP error {response.status_code}: {e}")
            return None
            
        except requests.Timeout:
            logger.error(f"Request timed out: {url}")
            return None
            
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            return None


"""
EXERCISE 2: RATE LIMITER (25 min)
=================================

A rate limiter prevents API blocking.
"""

class RateLimiter:
    """
    Simple rate limiter using sleep.
    
    Usage:
        limiter = RateLimiter(requests_per_second=10)
        for item in items:
            limiter.wait()
            make_request()
    """
    
    def __init__(self, requests_per_second: float = 10):
        """
        Initialize rate limiter.
        
        Args:
            requests_per_second: Maximum requests per second
        """
        self.min_interval = 1.0 / requests_per_second
        self.last_request_time = 0.0
    
    def wait(self):
        """Wait if needed to respect rate limit."""
        current_time = time.time()
        elapsed = current_time - self.last_request_time
        
        if elapsed < self.min_interval:
            sleep_time = self.min_interval - elapsed
            logger.debug(f"Rate limiting: sleeping {sleep_time:.3f}s")
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()


"""
EXERCISE 3: RETRY LOGIC (25 min)
================================

Proper retry logic with exponential backoff.
"""

def retry_with_backoff(
    func,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    retryable_status_codes: tuple = (429, 500, 502, 503, 504)
):
    """
    Retry a function with exponential backoff.
    
    Args:
        func: Function to retry (should raise requests.HTTPError on failure)
        max_retries: Maximum number of retry attempts
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
        exponential_base: Base for exponential calculation
        retryable_status_codes: HTTP status codes that trigger retry
        
    Returns:
        Function result
        
    Raises:
        Last exception if all retries fail
    """
    last_exception = None
    
    for attempt in range(max_retries + 1):
        try:
            return func()
            
        except requests.HTTPError as e:
            last_exception = e
            status_code = e.response.status_code if e.response else None
            
            # Don't retry client errors (except rate limiting)
            if status_code and status_code not in retryable_status_codes:
                raise
            
            if attempt < max_retries:
                delay = min(base_delay * (exponential_base ** attempt), max_delay)
                
                # Add jitter to prevent thundering herd
                jitter = delay * 0.1 * (2 * (0.5 - time.time() % 1))
                delay += jitter
                
                logger.warning(
                    f"Retry {attempt + 1}/{max_retries} after {delay:.2f}s "
                    f"(status: {status_code})"
                )
                time.sleep(delay)
            
        except (requests.Timeout, requests.ConnectionError) as e:
            last_exception = e
            
            if attempt < max_retries:
                delay = min(base_delay * (exponential_base ** attempt), max_delay)
                logger.warning(f"Retry {attempt + 1}/{max_retries} after {delay:.2f}s")
                time.sleep(delay)
    
    raise last_exception


"""
EXERCISE 4: PAGINATION HANDLER (30 min)
=======================================

Handle different pagination styles.
"""

class PaginatedAPIClient(APIClient):
    """
    API client with pagination support.
    """
    
    def __init__(self, *args, rate_limit: float = 10, **kwargs):
        super().__init__(*args, **kwargs)
        self.rate_limiter = RateLimiter(rate_limit)
    
    def fetch_all_offset(
        self,
        endpoint: str,
        page_size: int = 100,
        max_pages: Optional[int] = None
    ) -> Generator[Dict, None, None]:
        """
        Fetch all data using offset pagination.
        
        Example API: /users?page=1&per_page=100
        
        Yields:
            Individual records from all pages
        """
        page = 1
        
        while True:
            self.rate_limiter.wait()
            
            logger.info(f"Fetching page {page} from {endpoint}")
            
            data = self.get(
                endpoint,
                params={"page": page, "per_page": page_size}
            )
            
            if not data:
                break
            
            # Handle both list and dict responses
            records = data if isinstance(data, list) else data.get("data", [])
            
            if not records:
                break
            
            for record in records:
                yield record
            
            # Check if we've reached max pages
            if max_pages and page >= max_pages:
                logger.info(f"Reached max pages ({max_pages})")
                break
            
            # If we got less than page_size, we're on the last page
            if len(records) < page_size:
                break
            
            page += 1
        
        logger.info(f"Finished fetching {endpoint}")
    
    def fetch_all_cursor(
        self,
        endpoint: str,
        cursor_param: str = "cursor",
        cursor_field: str = "next_cursor",
        data_field: str = "data"
    ) -> Generator[Dict, None, None]:
        """
        Fetch all data using cursor pagination.
        
        Example API: /users?cursor=abc123
        Response: {"data": [...], "next_cursor": "xyz789"}
        
        Yields:
            Individual records from all pages
        """
        cursor = None
        
        while True:
            self.rate_limiter.wait()
            
            params = {cursor_param: cursor} if cursor else {}
            
            logger.info(f"Fetching {endpoint} with cursor: {cursor}")
            
            response = self.get(endpoint, params=params)
            
            if not response:
                break
            
            records = response.get(data_field, [])
            
            for record in records:
                yield record
            
            # Get next cursor
            cursor = response.get(cursor_field)
            
            if not cursor:
                break
        
        logger.info(f"Finished fetching {endpoint}")


"""
EXERCISE 5: AUTHENTICATED CLIENT (25 min)
=========================================

Handle different authentication methods.
"""

class AuthenticatedAPIClient(PaginatedAPIClient):
    """
    API client with authentication support.
    """
    
    def set_api_key(self, api_key: str, header_name: str = "X-API-Key"):
        """
        Set API key authentication.
        
        Usage:
            client.set_api_key("my-secret-key")
            # Adds header: X-API-Key: my-secret-key
        """
        self.session.headers[header_name] = api_key
    
    def set_bearer_token(self, token: str):
        """
        Set Bearer token authentication.
        
        Usage:
            client.set_bearer_token("eyJhbGciOiJI...")
            # Adds header: Authorization: Bearer eyJhbGciOiJI...
        """
        self.session.headers["Authorization"] = f"Bearer {token}"
    
    def set_basic_auth(self, username: str, password: str):
        """
        Set Basic authentication.
        
        Usage:
            client.set_basic_auth("user", "pass")
        """
        from requests.auth import HTTPBasicAuth
        self.session.auth = HTTPBasicAuth(username, password)


"""
EXERCISE 6: FULL EXTRACTION PIPELINE (30 min)
=============================================

Let's put it all together with a real extraction.
"""

@dataclass
class ExtractionResult:
    """Result of an extraction run."""
    endpoint: str
    records_extracted: int
    start_time: datetime
    end_time: datetime
    errors: List[str]
    
    @property
    def duration_seconds(self) -> float:
        return (self.end_time - self.start_time).total_seconds()
    
    @property
    def success(self) -> bool:
        return len(self.errors) == 0


class DataExtractor:
    """
    Production data extractor with all best practices.
    """
    
    def __init__(
        self,
        base_url: str,
        rate_limit: float = 10,
        max_retries: int = 3
    ):
        self.client = AuthenticatedAPIClient(
            base_url=base_url,
            rate_limit=rate_limit
        )
        self.max_retries = max_retries
    
    def extract_endpoint(
        self,
        endpoint: str,
        page_size: int = 100,
        enrich: bool = True
    ) -> ExtractionResult:
        """
        Extract all data from an endpoint.
        
        Args:
            endpoint: API endpoint
            page_size: Records per page
            enrich: Add metadata to records
            
        Returns:
            ExtractionResult with all records
        """
        start_time = datetime.now(timezone.utc)
        records = []
        errors = []
        
        try:
            for record in self.client.fetch_all_offset(endpoint, page_size):
                if enrich:
                    record = self._enrich_record(record, endpoint)
                records.append(record)
                
        except Exception as e:
            errors.append(str(e))
            logger.error(f"Extraction failed: {e}")
        
        end_time = datetime.now(timezone.utc)
        
        result = ExtractionResult(
            endpoint=endpoint,
            records_extracted=len(records),
            start_time=start_time,
            end_time=end_time,
            errors=errors
        )
        
        logger.info(
            f"Extracted {result.records_extracted} records from {endpoint} "
            f"in {result.duration_seconds:.2f}s"
        )
        
        return result
    
    def _enrich_record(self, record: Dict, source: str) -> Dict:
        """Add metadata to a record."""
        record["_metadata"] = {
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "source_endpoint": source,
            "extractor_version": "1.0"
        }
        return record


"""
EXERCISE 7: TEST WITH REAL API (20 min)
=======================================

Let's test our client with JSONPlaceholder.

Run this code:
"""

def test_api_client():
    """Test the API client with JSONPlaceholder."""
    
    print("=" * 60)
    print("API CLIENT TEST")
    print("=" * 60)
    
    # Create client
    client = PaginatedAPIClient(
        base_url="https://jsonplaceholder.typicode.com",
        rate_limit=5  # 5 requests per second
    )
    
    # Test simple GET
    print("\n1. Simple GET request:")
    users = client.get("/users")
    print(f"   Fetched {len(users)} users")
    
    # Test paginated fetch
    print("\n2. Paginated fetch (simulated):")
    posts = list(client.fetch_all_offset("/posts", page_size=10, max_pages=3))
    print(f"   Fetched {len(posts)} posts")
    
    # Test full extraction
    print("\n3. Full extraction with metadata:")
    extractor = DataExtractor(
        base_url="https://jsonplaceholder.typicode.com",
        rate_limit=5
    )
    
    result = extractor.extract_endpoint("/comments", page_size=50)
    
    print(f"   Endpoint: {result.endpoint}")
    print(f"   Records: {result.records_extracted}")
    print(f"   Duration: {result.duration_seconds:.2f}s")
    print(f"   Success: {result.success}")
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


"""
EXERCISE 8: INCREMENTAL EXTRACTION (25 min)
===========================================

For large datasets, extract only new/changed data.
"""

class IncrementalExtractor(DataExtractor):
    """
    Extractor that supports incremental loads.
    """
    
    def __init__(self, *args, state_file: str = "extraction_state.json", **kwargs):
        super().__init__(*args, **kwargs)
        self.state_file = state_file
        self.state = self._load_state()
    
    def _load_state(self) -> Dict:
        """Load extraction state from file."""
        try:
            with open(self.state_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def _save_state(self):
        """Save extraction state to file."""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2, default=str)
    
    def get_last_extraction(self, endpoint: str) -> Optional[datetime]:
        """Get the last extraction time for an endpoint."""
        last = self.state.get(endpoint, {}).get("last_extraction")
        if last:
            return datetime.fromisoformat(last)
        return None
    
    def update_extraction_state(self, endpoint: str, result: ExtractionResult):
        """Update state after successful extraction."""
        self.state[endpoint] = {
            "last_extraction": result.end_time.isoformat(),
            "records_extracted": result.records_extracted
        }
        self._save_state()
    
    def extract_incremental(
        self,
        endpoint: str,
        modified_since_param: str = "modified_since"
    ) -> ExtractionResult:
        """
        Extract only records modified since last run.
        
        Args:
            endpoint: API endpoint
            modified_since_param: Query parameter name for date filter
            
        Returns:
            ExtractionResult with new/modified records
        """
        last_extraction = self.get_last_extraction(endpoint)
        
        if last_extraction:
            logger.info(f"Incremental extraction since {last_extraction}")
            # Note: JSONPlaceholder doesn't support this, but real APIs do
            # params = {modified_since_param: last_extraction.isoformat()}
        else:
            logger.info("Full extraction (no previous state)")
        
        result = self.extract_endpoint(endpoint)
        
        if result.success:
            self.update_extraction_state(endpoint, result)
        
        return result


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Concepts:
[ ] Rate limiting - why and how
[ ] Pagination types (offset, cursor)
[ ] Authentication methods (API key, Bearer, OAuth)
[ ] Retry with exponential backoff
[ ] HTTP status codes and their meaning
[ ] Incremental vs full extraction

Code patterns:
[ ] requests.Session for connection reuse
[ ] Custom exception handling
[ ] Generator functions for pagination
[ ] State management for incremental loads

Best practices:
[ ] Always use timeouts
[ ] Implement rate limiting before API blocks you
[ ] Log all requests for debugging
[ ] Handle partial failures gracefully


KNOWLEDGE CHECK:
================

1. You get a 429 status code. What does it mean and what should you do?

2. An API returns 10,000 records. How would you fetch all of them
   without running out of memory?

3. Your extraction script crashes halfway through. How do you resume
   without re-fetching already-extracted data?

4. What's the difference between offset and cursor pagination?
   When would you prefer one over the other?


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 23: API Integration Patterns"
    git push


WHAT'S NEXT:
============
Day 24: AWS Lambda Basics
- What is serverless?
- Creating Lambda functions
- Event triggers
- Lambda + S3 integration
"""


if __name__ == "__main__":
    test_api_client()
