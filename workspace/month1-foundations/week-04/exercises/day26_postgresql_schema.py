#!/usr/bin/env python3
"""
Day 26: PostgreSQL Setup + Schema Design
==========================================
Duration: 2-2.5 hours

Design a proper database schema for your stock data.
Learn dimensional modeling basics for analytics.

WHY THIS MATTERS:
- Good schema = good analytics
- Dimensional modeling is the standard
- This is what you'll do at every data job
- Foundation for dbt work later

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
from typing import Dict, List, Optional, Any
from datetime import datetime

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Understand Dimensional Modeling (20 min)
====================================================

Two types of tables:

FACT TABLES:
- Store measurements/events
- Numeric values you aggregate
- Examples: sales, transactions, prices
- Usually have foreign keys to dimensions

DIMENSION TABLES:
- Store descriptive attributes
- Context for facts
- Examples: customers, products, time
- Usually have a primary key

Star Schema:
           [dim_date]
               |
[dim_symbol]--[fact_stock_prices]--[dim_exchange]


EXERCISE 2: Design Stock Data Schema (30 min)
=============================================

Create these tables:

1. dim_symbol - Stock symbols
2. dim_date - Date dimension
3. fact_stock_prices - Price observations

See SCHEMA_SQL below for the complete schema.


EXERCISE 3: Create Tables in PostgreSQL (20 min)
================================================

Using your Docker PostgreSQL:

1. Connect:
   docker exec -it postgres psql -U pipeline -d stockdata

2. Run the schema SQL:
   \\i /path/to/schema.sql

3. Verify:
   \\dt  -- list tables
   \\d fact_stock_prices  -- describe table


EXERCISE 4: Write Python Loader (30 min)
========================================

Create a loader that:
- Upserts to dimension tables
- Inserts to fact table
- Handles duplicates
- Uses transactions

See StockDataLoader class below.


EXERCISE 5: Load Sample Data (20 min)
=====================================

1. Use your API extractor from Day 23
2. Load data through the loader
3. Verify in database:
   SELECT * FROM fact_stock_prices LIMIT 10;


EXERCISE 6: Add Indexes (20 min)
================================

Add indexes for common queries:

CREATE INDEX idx_fact_symbol_date 
    ON fact_stock_prices(symbol_id, price_date);

CREATE INDEX idx_fact_date 
    ON fact_stock_prices(price_date);

Analyze query performance:
EXPLAIN ANALYZE SELECT * FROM fact_stock_prices 
WHERE price_date >= '2024-01-01';
"""

# =============================================================================
# SCHEMA SQL
# =============================================================================

SCHEMA_SQL = '''
-- Dimension: Symbols
CREATE TABLE IF NOT EXISTS dim_symbol (
    symbol_id SERIAL PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL UNIQUE,
    company_name VARCHAR(255),
    sector VARCHAR(100),
    industry VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Dimension: Date (pre-populated)
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INTEGER PRIMARY KEY,  -- YYYYMMDD format
    full_date DATE NOT NULL UNIQUE,
    year INTEGER NOT NULL,
    quarter INTEGER NOT NULL,
    month INTEGER NOT NULL,
    month_name VARCHAR(20) NOT NULL,
    day INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL,
    day_name VARCHAR(20) NOT NULL,
    week_of_year INTEGER NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    is_trading_day BOOLEAN DEFAULT TRUE
);

-- Fact: Stock Prices
CREATE TABLE IF NOT EXISTS fact_stock_prices (
    price_id SERIAL PRIMARY KEY,
    symbol_id INTEGER NOT NULL REFERENCES dim_symbol(symbol_id),
    date_id INTEGER NOT NULL REFERENCES dim_date(date_id),
    price_date DATE NOT NULL,
    open_price DECIMAL(12, 4),
    high_price DECIMAL(12, 4),
    low_price DECIMAL(12, 4),
    close_price DECIMAL(12, 4),
    adjusted_close DECIMAL(12, 4),
    volume BIGINT,
    change_percent DECIMAL(8, 4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Prevent duplicates
    UNIQUE(symbol_id, price_date)
);

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_fact_symbol_date 
    ON fact_stock_prices(symbol_id, price_date);

CREATE INDEX IF NOT EXISTS idx_fact_date 
    ON fact_stock_prices(date_id);

CREATE INDEX IF NOT EXISTS idx_symbol_symbol 
    ON dim_symbol(symbol);

-- Function to populate date dimension
CREATE OR REPLACE FUNCTION populate_dim_date(start_date DATE, end_date DATE)
RETURNS VOID AS $$
DECLARE
    current_date DATE := start_date;
BEGIN
    WHILE current_date <= end_date LOOP
        INSERT INTO dim_date (
            date_id, full_date, year, quarter, month, month_name,
            day, day_of_week, day_name, week_of_year, is_weekend
        ) VALUES (
            TO_CHAR(current_date, 'YYYYMMDD')::INTEGER,
            current_date,
            EXTRACT(YEAR FROM current_date),
            EXTRACT(QUARTER FROM current_date),
            EXTRACT(MONTH FROM current_date),
            TO_CHAR(current_date, 'Month'),
            EXTRACT(DAY FROM current_date),
            EXTRACT(DOW FROM current_date),
            TO_CHAR(current_date, 'Day'),
            EXTRACT(WEEK FROM current_date),
            EXTRACT(DOW FROM current_date) IN (0, 6)
        )
        ON CONFLICT (date_id) DO NOTHING;
        
        current_date := current_date + INTERVAL '1 day';
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Populate dates for 2024-2026
SELECT populate_dim_date('2024-01-01', '2026-12-31');
'''


# =============================================================================
# PYTHON LOADER
# =============================================================================

class StockDataLoader:
    """Load stock data into PostgreSQL."""
    
    def __init__(self, connection_string: str):
        """
        Initialize loader with database connection.
        
        Args:
            connection_string: PostgreSQL connection string
                Example: postgresql://user:pass@localhost:5432/stockdata
        """
        try:
            import psycopg2
            self.conn = psycopg2.connect(connection_string)
            self.conn.autocommit = False
        except ImportError:
            print("Install psycopg2: pip install psycopg2-binary")
            raise
    
    def get_or_create_symbol(self, symbol: str) -> int:
        """Get symbol_id, creating if necessary."""
        with self.conn.cursor() as cur:
            # Try to get existing
            cur.execute(
                "SELECT symbol_id FROM dim_symbol WHERE symbol = %s",
                (symbol,)
            )
            row = cur.fetchone()
            
            if row:
                return row[0]
            
            # Create new
            cur.execute(
                "INSERT INTO dim_symbol (symbol) VALUES (%s) RETURNING symbol_id",
                (symbol,)
            )
            self.conn.commit()
            return cur.fetchone()[0]
    
    def get_date_id(self, date: datetime) -> int:
        """Get date_id for a date."""
        return int(date.strftime('%Y%m%d'))
    
    def load_price(self, data: Dict[str, Any]) -> bool:
        """
        Load a single price observation.
        
        Args:
            data: Dict with symbol, price, volume, timestamp, etc.
        
        Returns:
            True if successful
        """
        try:
            symbol_id = self.get_or_create_symbol(data['symbol'])
            
            price_date = data.get('timestamp')
            if isinstance(price_date, str):
                price_date = datetime.fromisoformat(price_date.replace('Z', '+00:00'))
            elif price_date is None:
                price_date = datetime.now()
            
            date_id = self.get_date_id(price_date)
            
            with self.conn.cursor() as cur:
                cur.execute('''
                    INSERT INTO fact_stock_prices 
                    (symbol_id, date_id, price_date, close_price, volume, change_percent)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (symbol_id, price_date) 
                    DO UPDATE SET 
                        close_price = EXCLUDED.close_price,
                        volume = EXCLUDED.volume,
                        change_percent = EXCLUDED.change_percent
                ''', (
                    symbol_id,
                    date_id,
                    price_date.date(),
                    data.get('price', 0),
                    data.get('volume', 0),
                    data.get('change_percent', 0)
                ))
            
            self.conn.commit()
            return True
            
        except Exception as e:
            self.conn.rollback()
            print(f"Error loading price: {e}")
            return False
    
    def load_prices(self, data_list: List[Dict]) -> Dict[str, int]:
        """Load multiple prices."""
        results = {"success": 0, "failed": 0}
        
        for data in data_list:
            if self.load_price(data):
                results["success"] += 1
            else:
                results["failed"] += 1
        
        return results
    
    def close(self):
        """Close database connection."""
        self.conn.close()


def print_schema():
    """Print the database schema."""
    print("=" * 60)
    print("STOCK DATA SCHEMA")
    print("=" * 60)
    print(SCHEMA_SQL)


def verify_connection():
    """Verify database connection."""
    conn_string = os.environ.get(
        "DATABASE_URL",
        "postgresql://pipeline:pipeline123@localhost:5432/stockdata"
    )
    
    try:
        import psycopg2
        conn = psycopg2.connect(conn_string)
        
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            print(f"✅ Connected to PostgreSQL")
            print(f"   {version[:50]}...")
            
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            tables = [row[0] for row in cur.fetchall()]
            print(f"\nTables: {', '.join(tables) if tables else 'None'}")
        
        conn.close()
    except Exception as e:
        print(f"❌ Connection failed: {e}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "schema":
            print_schema()
        elif cmd == "verify":
            verify_connection()
    else:
        print("Day 26: PostgreSQL Setup + Schema Design")
        print("=" * 45)
        print("\nDesign a proper schema for analytics.")
        print("\nCommands:")
        print("  python day26_postgresql_schema.py schema - Show schema SQL")
        print("  python day26_postgresql_schema.py verify - Test connection")
