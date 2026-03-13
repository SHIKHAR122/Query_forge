import streamlit as st

st.title("Query Forge 🔍")
st.markdown("---")

st.markdown("""
### What is Query Forge?
A production-grade SQL analytical engine built on **DuckDB**, **Python**, and **Streamlit**.

Query Forge takes raw Superstore sales data and runs advanced business intelligence 
queries through a Python-based Query Interface, displayed on a live interactive dashboard.

This project is an upgraded version of a previous SQL project that ran on SQLite and 
DB Browser. Same analytical depth — completely different engineering standard.
""")

st.markdown("---")

st.markdown("""
### Tech Stack
- **DuckDB** — Columnar analytical database, OLAP-optimized
- **Python** — Class-based Query Engine interface
- **Pandas** — Data loading and DataFrame handling  
- **Streamlit** — Live interactive multi-page dashboard
""")

st.markdown("---")

st.markdown("""
### Analytical Modules
Navigate using the sidebar to explore each module.

| Module | Focus |
|---|---|
| Sales Analysis | Regional, category, segment performance + trends |
| Customer Intelligence | CLV, RFM segmentation, retention, tiers |
| Product Performance | Best sellers, margins, Pareto analysis |
| Time Series | MoM/YoY growth, rolling averages, anomaly detection |
| Benchmarking | Query execution time across all 29 functions |
""")

st.markdown("---")

st.markdown("""
### Built By
**Shikhar Sharma** — Btech Somophore @ PSIT , KANPUR

> *"Most students stop at SQLite and DB Browser. 
Query Forge is what happens when you rebuild the right way."*
""")