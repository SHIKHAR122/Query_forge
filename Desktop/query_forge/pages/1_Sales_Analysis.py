import streamlit as st
import matplotlib.pyplot as plt
from queries.sales_analysis import (
    total_sales_by_region,
    sales_rank_by_region,
    sales_vs_profit_by_region,
    sales_by_category,
    subcategory_performance,
    sales_by_segment,
    monthly_sales_trend,
    yoy_growth,
    highest_lowest_sales_month,
    seasonal_patterns,
    pareto_analysis
)

st.title("Module 1 — Sales Aggregation")

st.subheader("Total Sales by Region")
df = total_sales_by_region()
st.dataframe(df)
fig, ax = plt.subplots()
ax.bar(df["Region"], df["Total_Sales"], color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
ax.set_title("Total Sales by Region")
ax.set_xlabel("Region")
ax.set_ylabel("Total Sales")
st.pyplot(fig)

st.subheader("Region Performance Rankings")
df2 = sales_rank_by_region()
st.dataframe(df2)

st.subheader("Sales vs Profit By Region")
df3 = sales_vs_profit_by_region()
st.dataframe(df3)
fig2, ax2 = plt.subplots()
x = range(len(df3["Region"]))
ax2.bar([i - 0.2 for i in x], df3["Total_Sales"], width=0.4, label="Sales", color="#4C72B0")
ax2.bar([i + 0.2 for i in x], df3["Total_Profit"], width=0.4, label="Profit", color="#55A868")
ax2.set_xticks(list(x))
ax2.set_xticklabels(df3["Region"])
ax2.set_title("Sales vs Profit by Region")
ax2.legend()
st.pyplot(fig2)

st.subheader("Sales by Category")
df4 = sales_by_category()
st.dataframe(df4)
fig3, ax3 = plt.subplots()
ax3.bar(df4["Category"], df4["Total_Sales"], color=["#4C72B0", "#DD8452", "#55A868"])
ax3.set_title("Sales by Category")
ax3.set_xlabel("Category")
ax3.set_ylabel("Total Sales")
st.pyplot(fig3)

st.subheader("Subcategory Performance")
df5 = subcategory_performance()
st.dataframe(df5)

st.subheader("Sales By Segment")
df6 = sales_by_segment()
st.dataframe(df6)
fig4, ax4 = plt.subplots()
ax4.bar(df6["Segment"], df6["Total_Sales"], color=["#4C72B0", "#DD8452", "#55A868"])
ax4.set_title("Sales by Segment")
ax4.set_xlabel("Segment")
ax4.set_ylabel("Total Sales")
st.pyplot(fig4)

st.subheader("Monthly Sales Trend")
df7 = monthly_sales_trend()
st.dataframe(df7)
fig5, ax5 = plt.subplots(figsize=(12, 4))
ax5.plot(df7["Month"], df7["Total_Sales"], marker="o", color="#4C72B0", linewidth=2)
ax5.set_title("Monthly Sales Trend")
ax5.set_xlabel("Month")
ax5.set_ylabel("Total Sales")
plt.xticks(rotation=90)
st.pyplot(fig5)

st.subheader("Year-Over-Year Growth")
df8 = yoy_growth()
st.dataframe(df8)

st.subheader("Highest & Lowest Sales Month")
df9 = highest_lowest_sales_month()
st.dataframe(df9)

st.subheader("Seasonal Patterns")
df10 = seasonal_patterns()
st.dataframe(df10)
fig6, ax6 = plt.subplots()
colors = df10["Season_Tag"].map({"Peak Season": "#55A868", "Low Season": "#C44E52", "Normal": "#4C72B0"})
ax6.bar(df10["Month_Name"], df10["Avg_Monthly_Sales"], color=colors)
ax6.set_title("Seasonal Patterns")
ax6.set_xlabel("Month")
ax6.set_ylabel("Avg Monthly Sales")
plt.xticks(rotation=45)
st.pyplot(fig6)

st.subheader("Pareto Analysis")
df11 = pareto_analysis()
st.dataframe(df11)