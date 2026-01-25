#!/usr/bin/env python3
"""
Day 23: Alpha Vantage API Integration
======================================
Duration: 2-2.5 hours

Build a robust stock data extractor using Alpha Vantage API.
Handle rate limits, errors, and data validation.

WHY THIS MATTERS:
- Real pipelines extract from APIs
- Rate limiting is a common challenge
- Error handling separates good from great
- This is core of Project 1

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import time
import json
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime
from dataclasses import dataclass

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Get Alpha Vantage API Key (10 min)
==============================================

1. Go to: https://www.alphavantage.co/support/#api-key
2. Enter your email
3. Copy your API key
4. Create .env file:
   ALPHA_VANTAGE_API_KEY=your_key_here
5. Add .env to .gitignore


EXERCISE 2: Build Stock Extractor Class (30 min)
================================================

Create a class that:
- Takes API key from environment
- Handles rate limiting (5 calls/min on free tier)
- Returns clean data
- Logs all operations

See StockExtractor class below.


EXERCISE 3: Add Retry Logic (20 min)
====================================

Implement exponential backoff:
- Retry on failures
- Increase wait time each retry
- Max 3 retries
- Log each attempt


EXERCISE 4: Data Validation (20 min)
====================================

Validate API responses:
- Check required fields exist
- Validate data types
- Handle missing data
- Return validation status


EXERCISE 5: Extract Multiple Symbols (20 min)
=============================================

Build batch extractor:
- Accept list of symbols
- Respect rate limits (wait between calls)
- Aggregate results
- Report success/failure for each


EXERCISE 6: Integration Test (30 min)
=====================================

Test your extractor:
- Extract 3 different stocks
- Save to JSON file
- Verify data quality
- Check for errors
"""

# =============================================================================
# IMPLEMENTATION
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class StockQuote:
    """Represents a stock price quote."""
    symbol: str
    price: float
    volume: int
    timestamp: datetime
    change_percent: float
    
    def to_dict(self) -> Dict:
        return {
            "symbol": self.symbol,
            "price": self.price,
            "volume": self.volume,
            "timestamp": self.timestamp.isoformat(),
            "change_percent": self.change_percent
        }


class RateLimiter:
    """Simple rate limiter for API calls."""
    
    def __init__(self, calls_per_minute: int = 5):
        self.calls_per_minute = calls_per_minute
        self.calls = []
    
    def wait_if_needed(self) -> None:
        """Wait if we've exceeded rate limit."""
        now = time.time()
        # Remove calls older than 1 minute
        self.calls = [t for t in self.calls if now - t < 60]
        
        if len(self.calls) >= self.calls_per_minute:
            wait_time = 60 - (now - self.calls[0])
            if wait_time > 0:
                logger.info(f"Rate limit reached. Waiting {wait_time:.1f}s")
                time.sleep(wait_time)
        
        self.calls.append(time.time())


class StockExtractor:
    """Extract stock data from Alpha Vantage API."""
    
    BASE_URL = "https://www.alphavantage.co/query"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ALPHA_VANTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("API key required. Set ALPHA_VANTAGE_API_KEY env var.")
        
        self.rate_limiter = RateLimiter(calls_per_minute=5)
        self._session = None
    
    @property
    def session(self):
        """Lazy load requests session."""
        if self._session is None:
            import requests
            self._session = requests.Session()
        return self._session
    
    def get_quote(self, symbol: str) -> Optional[StockQuote]:
        """
        Get current quote for a stock symbol.
        
        Args:
            symbol: Stock ticker (e.g., 'AAPL', 'MSFT')
        
        Returns:
            StockQuote or None if failed
        """
        self.rate_limiter.wait_if_needed()
        
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.api_key
        }
        
        try:
            logger.info(f"Fetching quote for {symbol}")
            response = self.session.get(self.BASE_URL, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Check for API errors
            if "Error Message" in data:
                logger.error(f"API error: {data['Error Message']}")
                return None
            
            if "Note" in data:
                logger.warning(f"API limit note: {data['Note']}")
                return None
            
            return self._parse_quote(symbol, data)
            
        except Exception as e:
            logger.error(f"Failed to fetch {symbol}: {e}")
            return None
    
    def _parse_quote(self, symbol: str, data: Dict) -> Optional[StockQuote]:
        """Parse API response into StockQuote."""
        quote_data = data.get("Global Quote", {})
        
        if not quote_data:
            logger.warning(f"No quote data for {symbol}")
            return None
        
        try:
            return StockQuote(
                symbol=symbol,
                price=float(quote_data.get("05. price", 0)),
                volume=int(quote_data.get("06. volume", 0)),
                timestamp=datetime.now(),
                change_percent=float(
                    quote_data.get("10. change percent", "0%").replace("%", "")
                )
            )
        except (ValueError, KeyError) as e:
            logger.error(f"Failed to parse quote for {symbol}: {e}")
            return None
    
    def get_quotes(self, symbols: List[str]) -> Dict[str, Optional[StockQuote]]:
        """
        Get quotes for multiple symbols.
        
        Args:
            symbols: List of stock tickers
        
        Returns:
            Dict mapping symbol to quote (or None if failed)
        """
        results = {}
        
        for symbol in symbols:
            results[symbol] = self.get_quote(symbol)
        
        success = sum(1 for q in results.values() if q is not None)
        logger.info(f"Fetched {success}/{len(symbols)} quotes successfully")
        
        return results


def demo_extractor():
    """Demonstrate the stock extractor."""
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    
    if not api_key:
        print("⚠️  Set ALPHA_VANTAGE_API_KEY environment variable")
        print("   Get a free key at: https://www.alphavantage.co/support/#api-key")
        return
    
    extractor = StockExtractor(api_key)
    
    # Test with a single symbol
    quote = extractor.get_quote("AAPL")
    
    if quote:
        print("\n✅ Successfully fetched quote:")
        print(json.dumps(quote.to_dict(), indent=2))
    else:
        print("\n❌ Failed to fetch quote")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "demo":
            demo_extractor()
        elif cmd == "test":
            # Quick API test
            api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
            if api_key:
                print(f"✅ API key found ({len(api_key)} chars)")
            else:
                print("❌ No API key set")
    else:
        print("Day 23: Alpha Vantage API Integration")
        print("=" * 42)
        print("\nBuild a robust stock data extractor.")
        print("\nCommands:")
        print("  python day23_api_integration.py demo - Demo the extractor")
        print("  python day23_api_integration.py test - Check API key")
