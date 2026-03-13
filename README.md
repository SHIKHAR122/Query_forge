# Query Forge 🔍
> Production-grade SQL Analytical Engine built with DuckDB, Python, and Streamlit.

![Intro Page](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/INTRO_PAGE.png)

---

## What is Query Forge?

Query Forge is an upgraded analytical system built on top of a previous SQL project that used SQLite and DB Browser.

The analytical logic was solid — but the tech stack wasn't production-ready. Query Forge rebuilds the same depth of analysis on a professional-grade stack that scales, performs, and demos like a real system.

---

## Why the Upgrade?

| Previous Version | Query Forge |
|---|---|
| SQLite | DuckDB (OLAP-optimized) |
| DB Browser | Python Query Interface Class |
| Manual query runs | Streamlit Live Multi-Page Dashboard |
| Small dataset | 9994 row Superstore dataset |
| No benchmarking | Query performance benchmarking across 29 functions |

---

## Tech Stack

- **DuckDB** — Columnar analytical database, built for fast aggregations at scale
- **Python** — Class-based Query Engine interface
- **Pandas** — Data loading and DataFrame handling
- **Matplotlib** — Chart visualizations
- **Streamlit** — Live interactive multi-page dashboard

---

## Project Structure

```
query_forge/
├── data/
│   └── superstore.csv          ← Raw dataset (9994 rows)
├── utils/
│   └── db.py                   ← QueryEngine class (DuckDB interface)
├── queries/
│   ├── sales_analysis.py       ← Module 2 — 11 analytical functions
│   ├── customer_analysis.py    ← Module 3 — 7 analytical functions
│   ├── product_analysis.py     ← Module 4 — 5 analytical functions
│   ├── time_series_analysis.py ← Module 5 — 6 analytical functions
│   └── benchmarking.py         ← Performance benchmarking module
├── pages/
│   ├── 1_Sales_Analysis.py
│   ├── 2_Customer_Intelligence.py
│   ├── 3_Product_Performance.py
│   ├── 4_Time_Series.py
│   └── 5_Benchmarking.py
└── app.py                      ← Home page
```

---

## Analytical Modules

### Module 1 — Sales Aggregation & Regional Performance
![Sales Analysis](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/MODULE%201%20example.png)

- Total Sales, Profit, Margin % and Revenue Contribution by Region
- Region Performance Rankings with Highest/Lowest Performer Detection
- Sales vs Profit Mismatch Analysis
- Category and Sub-Category Performance Breakdown
- Segment Analysis with Average Order Value
- Monthly Sales Trend with MoM Growth, Cumulative Sales, Rolling Average
- Year-over-Year Growth Analysis
- Seasonal Pattern Detection
- Pareto Analysis (80/20 Rule)

---

### Module 2 — Customer Intelligence & Behavioral Analytics
![Customer Intelligence](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/MODULE%202%20example.png)

- Customer Lifetime Value — Top 20 customers by revenue
- Repeat vs One-Time Customer Analysis
- RFM Segmentation — Recency, Frequency, Monetary scoring using NTILE(5)
- Customer Revenue Tiers — Platinum, Gold, Silver, Bronze
- Customer Distribution across Region, Segment, Category, Sub-Category

---

### Module 3 — Product Performance Intelligence
![Product Performance](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/MODULE%203%20example.png)

- Best Selling Products by Revenue
- Most Profitable Products by Profit Margin
- Negative Margin Product Detection — products actively losing money
- Product Profit Margin Analysis — Premium, Healthy, Low Margin, Loss Making
- Pareto Analysis at Product Level

---

### Module 4 — Time Series Trend Analysis
![Time Series](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/MODULE%204%20example.png)

- Monthly Revenue and Profit Trend
- Month-over-Month Growth for both Revenue and Profit
- Year-over-Year Pivot Comparison across 2014-2017
- Cumulative Revenue with percentage milestones
- Rolling 3-Month and 6-Month Average Trends
- Sales Volatility and Anomaly Detection using Z-Score

---

### Benchmarking Module
![Benchmarking](https://raw.githubusercontent.com/SHIKHAR122/Query_forge/master/Desktop/query_forge/assets/BENCHMARK.png)

- Execution time measurement for all 29 query functions
- Performance tagging — Fast, Moderate, Slow
- Bar chart visualization of query performance
- Built using Python's `time` module

---

## How to Run Locally

```bash
# Clone the repository
git clone https://github.com/SHIKHAR122/Query_forge.git

# Navigate to project folder
cd Query_forge

# Install dependencies
pip install duckdb pandas streamlit matplotlib

# Run the app
streamlit run app.py
```

---

## Key SQL Concepts Used

- Window Functions — RANK, NTILE, LAG, SUM OVER, AVG OVER
- PARTITION BY for group-level rankings
- CTEs for multi-step query logic
- CASE logic for business classification
- HAVING for post-aggregation filtering
- Rolling averages with ROWS BETWEEN frame clause
- Z-Score based anomaly detection
- Conditional aggregation for pivot tables

---

## Built By

**Shikhar** — Aspiring Data Engineer

Building toward a Data Engineering internship by March 2027.

> *"Most students stop at SQLite and DB Browser. Query Forge is what happens when you rebuild the right way."*
