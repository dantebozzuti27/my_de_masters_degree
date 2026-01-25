#!/usr/bin/env python3
"""
Day 32: Streamlit Dashboard Basics
===================================
Duration: 2-2.5 hours

Build a data dashboard with Streamlit.
Connect to your PostgreSQL database and visualize stock data.

WHY THIS MATTERS:
- Stakeholders need to see data
- Streamlit = fastest way to build data apps
- No frontend knowledge required
- Portfolio-ready visualizations

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# EXERCISES
# =============================================================================

"""
EXERCISE 1: Install and Run Streamlit (15 min)
==============================================

1. Install:
   pip install streamlit

2. Create app.py with basic content:
   import streamlit as st
   st.title("Stock Dashboard")
   st.write("Hello, World!")

3. Run:
   streamlit run app.py

4. Open http://localhost:8501


EXERCISE 2: Basic Streamlit Components (30 min)
===============================================

Key components:
- st.title() / st.header() / st.subheader()
- st.write() / st.markdown()
- st.dataframe() / st.table()
- st.line_chart() / st.bar_chart()
- st.metric()
- st.sidebar


EXERCISE 3: Connect to Database (30 min)
========================================

Use @st.cache_data to cache database queries:

import streamlit as st
import psycopg2
import pandas as pd

@st.cache_data(ttl=60)  # Cache for 60 seconds
def get_stock_data():
    conn = psycopg2.connect(
        host="localhost",
        database="stockdata",
        user="pipeline",
        password="pipeline123"
    )
    query = "SELECT * FROM fact_stock_prices LIMIT 100"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = get_stock_data()
st.dataframe(df)


EXERCISE 4: Build Stock Dashboard (40 min)
==========================================

Create a dashboard with:
- Stock price chart
- Daily metrics (high, low, volume)
- Symbol selector
- Date range filter

See STREAMLIT_APP below for full example.


EXERCISE 5: Add Interactivity (20 min)
======================================

Interactive widgets:
- st.selectbox() - Dropdown
- st.multiselect() - Multi-select
- st.date_input() - Date picker
- st.slider() - Numeric slider
- st.button() - Action button


EXERCISE 6: Deploy to Streamlit Cloud (25 min)
==============================================

1. Push code to GitHub
2. Go to share.streamlit.io
3. Connect GitHub account
4. Select repository
5. Deploy!

Or use Docker:
  docker build -t stock-dashboard .
  docker run -p 8501:8501 stock-dashboard
"""

# =============================================================================
# STREAMLIT APP EXAMPLE
# =============================================================================

STREAMLIT_APP = '''
"""
Stock Dashboard - Streamlit App

Run with: streamlit run dashboard.py
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    page_title="Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

# Title
st.title("📈 Stock Market Dashboard")
st.markdown("Real-time stock data from your pipeline")


# Sidebar filters
st.sidebar.header("Filters")

symbols = st.sidebar.multiselect(
    "Select Stocks",
    options=["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"],
    default=["AAPL", "MSFT"]
)

date_range = st.sidebar.date_input(
    "Date Range",
    value=(datetime.now() - timedelta(days=30), datetime.now()),
    max_value=datetime.now()
)


# Cache database connection
@st.cache_resource
def get_connection():
    import psycopg2
    return psycopg2.connect(
        host="localhost",
        database="stockdata", 
        user="pipeline",
        password="pipeline123"
    )


# Cache data queries
@st.cache_data(ttl=60)
def get_stock_data(symbols: list, start_date, end_date):
    """Fetch stock data from database."""
    # In production, use actual database
    # For demo, create sample data
    import numpy as np
    
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    data = []
    
    for symbol in symbols:
        base_price = {"AAPL": 175, "MSFT": 380, "GOOGL": 140, "TSLA": 250, "AMZN": 175}.get(symbol, 100)
        
        for date in dates:
            price = base_price + np.random.randn() * 5
            data.append({
                "symbol": symbol,
                "date": date,
                "price": round(price, 2),
                "volume": int(np.random.uniform(500000, 2000000)),
                "change": round(np.random.randn() * 2, 2)
            })
    
    return pd.DataFrame(data)


# Get data
df = get_stock_data(symbols, date_range[0], date_range[1])


# Metrics row
st.subheader("Key Metrics")
cols = st.columns(len(symbols))

for i, symbol in enumerate(symbols):
    symbol_data = df[df["symbol"] == symbol]
    if not symbol_data.empty:
        latest = symbol_data.iloc[-1]
        prev = symbol_data.iloc[-2] if len(symbol_data) > 1 else latest
        
        cols[i].metric(
            label=symbol,
            value=f"${latest['price']:.2f}",
            delta=f"{latest['change']:.2f}%"
        )


# Price chart
st.subheader("Price History")

fig = px.line(
    df, 
    x="date", 
    y="price", 
    color="symbol",
    title="Stock Prices Over Time"
)
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Price ($)",
    legend_title="Symbol"
)
st.plotly_chart(fig, use_container_width=True)


# Volume chart
st.subheader("Trading Volume")

fig_vol = px.bar(
    df.groupby(["date", "symbol"])["volume"].sum().reset_index(),
    x="date",
    y="volume",
    color="symbol",
    barmode="group"
)
st.plotly_chart(fig_vol, use_container_width=True)


# Data table
st.subheader("Raw Data")
st.dataframe(
    df.sort_values("date", ascending=False),
    use_container_width=True,
    hide_index=True
)


# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data from Stock Pipeline")
'''


REQUIREMENTS = '''
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.18.0
psycopg2-binary>=2.9.0
'''


def print_app():
    """Print the Streamlit app code."""
    print(STREAMLIT_APP)


def print_requirements():
    """Print requirements."""
    print("requirements.txt:")
    print(REQUIREMENTS)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "app":
            print_app()
        elif cmd == "requirements":
            print_requirements()
    else:
        print("Day 32: Streamlit Dashboard Basics")
        print("=" * 38)
        print("\nBuild a data dashboard with Streamlit.")
        print("\nCommands:")
        print("  python day32_streamlit_basics.py app          - Show app code")
        print("  python day32_streamlit_basics.py requirements - Show requirements")
