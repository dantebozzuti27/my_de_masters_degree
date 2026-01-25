#!/usr/bin/env python3
"""
Day 29: Data Transformation Pipeline
======================================
Duration: 2-2.5 hours

Build clean transformation logic for your stock data.
Add data quality checks and output to processed layer.

WHY THIS MATTERS:
- Raw data is never clean enough
- Transformation is where value is added
- This is what dbt automates (Month 2)
- Data quality prevents disasters

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Transformation Patterns (20 min)
============================================

Common transformations:
- Type casting (string → number)
- Date parsing (string → datetime)
- Null handling (defaults, filters)
- Normalization (uppercase, trim)
- Derivation (calculated fields)
- Aggregation (daily summary)


EXERCISE 2: Build Stock Transformer (40 min)
============================================

Create a transformer that:
1. Validates incoming data
2. Cleans and normalizes
3. Adds derived fields
4. Outputs clean records

See StockTransformer class below.


EXERCISE 3: Data Quality Checks (30 min)
========================================

Add quality checks:
- Required fields present
- Values in valid ranges
- No duplicates
- Timestamps valid

See DataQualityChecker class.


EXERCISE 4: Aggregation (30 min)
================================

Create daily summary aggregation:
- Daily high/low/avg price per symbol
- Total volume
- Number of observations


EXERCISE 5: Output to Processed Layer (20 min)
==============================================

Write transformed data to processed/ in S3:
- Parquet format (optional)
- JSON with clean schema
- Proper partitioning
"""

# =============================================================================
# IMPLEMENTATION
# =============================================================================

@dataclass
class QualityResult:
    """Result of a data quality check."""
    passed: bool
    check_name: str
    message: str
    failed_records: List[Dict] = field(default_factory=list)


class DataQualityChecker:
    """Run data quality checks on records."""
    
    def __init__(self):
        self.results: List[QualityResult] = []
    
    def check_required_fields(
        self, 
        records: List[Dict], 
        required: List[str]
    ) -> QualityResult:
        """Check that required fields are present."""
        failed = []
        for record in records:
            missing = [f for f in required if f not in record or record[f] is None]
            if missing:
                failed.append({"record": record, "missing": missing})
        
        result = QualityResult(
            passed=len(failed) == 0,
            check_name="required_fields",
            message=f"{len(failed)} records missing required fields",
            failed_records=failed
        )
        self.results.append(result)
        return result
    
    def check_value_range(
        self,
        records: List[Dict],
        field: str,
        min_val: float,
        max_val: float
    ) -> QualityResult:
        """Check that values are in valid range."""
        failed = []
        for record in records:
            value = record.get(field)
            if value is not None and (value < min_val or value > max_val):
                failed.append({"record": record, "value": value})
        
        result = QualityResult(
            passed=len(failed) == 0,
            check_name=f"range_{field}",
            message=f"{len(failed)} records with {field} out of range [{min_val}, {max_val}]",
            failed_records=failed
        )
        self.results.append(result)
        return result
    
    def check_no_duplicates(
        self,
        records: List[Dict],
        key_fields: List[str]
    ) -> QualityResult:
        """Check for duplicate records."""
        seen = set()
        duplicates = []
        
        for record in records:
            key = tuple(record.get(f) for f in key_fields)
            if key in seen:
                duplicates.append(record)
            seen.add(key)
        
        result = QualityResult(
            passed=len(duplicates) == 0,
            check_name="no_duplicates",
            message=f"{len(duplicates)} duplicate records found",
            failed_records=duplicates
        )
        self.results.append(result)
        return result
    
    def get_summary(self) -> Dict:
        """Get summary of all checks."""
        return {
            "total_checks": len(self.results),
            "passed": sum(1 for r in self.results if r.passed),
            "failed": sum(1 for r in self.results if not r.passed),
            "details": [
                {"check": r.check_name, "passed": r.passed, "message": r.message}
                for r in self.results
            ]
        }


class StockTransformer:
    """Transform raw stock data into clean format."""
    
    REQUIRED_FIELDS = ["symbol", "price"]
    
    def __init__(self):
        self.quality_checker = DataQualityChecker()
    
    def transform(self, raw_records: List[Dict]) -> List[Dict]:
        """
        Transform raw records into clean format.
        
        Args:
            raw_records: Raw data from extraction
            
        Returns:
            Cleaned and enriched records
        """
        # Run quality checks
        self.quality_checker.check_required_fields(raw_records, self.REQUIRED_FIELDS)
        self.quality_checker.check_value_range(raw_records, "price", 0, 100000)
        
        # Transform each record
        transformed = []
        for record in raw_records:
            clean = self._transform_record(record)
            if clean:
                transformed.append(clean)
        
        logger.info(f"Transformed {len(transformed)}/{len(raw_records)} records")
        return transformed
    
    def _transform_record(self, record: Dict) -> Optional[Dict]:
        """Transform a single record."""
        try:
            # Parse timestamp
            timestamp = record.get("timestamp")
            if isinstance(timestamp, str):
                timestamp = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
            elif timestamp is None:
                timestamp = datetime.utcnow()
            
            # Clean and normalize
            return {
                "symbol": record.get("symbol", "").upper().strip(),
                "price": float(record.get("price", 0)),
                "volume": int(record.get("volume", 0)),
                "change_percent": self._parse_percent(record.get("change_percent")),
                "timestamp": timestamp.isoformat(),
                "date": timestamp.date().isoformat(),
                "hour": timestamp.hour,
                # Derived fields
                "is_positive": float(record.get("price", 0)) > 0,
                "transformed_at": datetime.utcnow().isoformat()
            }
        except Exception as e:
            logger.warning(f"Failed to transform record: {e}")
            return None
    
    def _parse_percent(self, value: Any) -> float:
        """Parse percentage value."""
        if value is None:
            return 0.0
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            return float(value.replace("%", "").strip())
        return 0.0
    
    def aggregate_daily(self, records: List[Dict]) -> List[Dict]:
        """Aggregate records to daily summary."""
        from collections import defaultdict
        
        daily = defaultdict(lambda: {
            "prices": [],
            "volumes": [],
            "count": 0
        })
        
        for record in records:
            key = (record["symbol"], record["date"])
            daily[key]["prices"].append(record["price"])
            daily[key]["volumes"].append(record["volume"])
            daily[key]["count"] += 1
        
        summaries = []
        for (symbol, date), data in daily.items():
            summaries.append({
                "symbol": symbol,
                "date": date,
                "price_high": max(data["prices"]),
                "price_low": min(data["prices"]),
                "price_avg": sum(data["prices"]) / len(data["prices"]),
                "volume_total": sum(data["volumes"]),
                "observation_count": data["count"],
                "aggregated_at": datetime.utcnow().isoformat()
            })
        
        return summaries


def demo_transformation():
    """Demo the transformation pipeline."""
    # Sample raw data
    raw_data = [
        {"symbol": "aapl", "price": "175.50", "volume": 1000000, "change_percent": "1.5%"},
        {"symbol": "MSFT", "price": 380.25, "volume": 800000, "change_percent": 0.8},
        {"symbol": "GOOGL", "price": None, "volume": 500000},  # Missing price
        {"symbol": "TSLA", "price": 250.00, "volume": 1200000, "change_percent": "-2.1%"},
    ]
    
    transformer = StockTransformer()
    
    print("Raw Data:")
    print(json.dumps(raw_data, indent=2))
    
    print("\n" + "=" * 40)
    
    transformed = transformer.transform(raw_data)
    
    print("\nTransformed Data:")
    print(json.dumps(transformed, indent=2))
    
    print("\n" + "=" * 40)
    
    print("\nQuality Check Summary:")
    print(json.dumps(transformer.quality_checker.get_summary(), indent=2))


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_transformation()
    else:
        print("Day 29: Data Transformation Pipeline")
        print("=" * 40)
        print("\nBuild clean transformation logic.")
        print("\nCommands:")
        print("  python day29_data_transformation.py demo - Run demo")
