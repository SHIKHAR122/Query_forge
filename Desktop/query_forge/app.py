import streamlit as st
from queries.sales_analysis import total_sales_by_region, sales_rank_by_region , sales_vs_profit_by_region , sales_by_category , subcategory_performance,sales_by_segment,monthly_sales_trend,yoy_growth,highest_lowest_sales_month,seasonal_patterns,pareto_analysis

st.title("Query Forge")

st.header("Module 2 — Sales Aggregation")

st.subheader("Total Sales by Region")
df = total_sales_by_region()
st.dataframe(df)

st.subheader("Region Performance Rankings")
df2 = sales_rank_by_region()
st.dataframe(df2)


st.subheader("Sales vs Profit By Region ")
df3=sales_vs_profit_by_region()
st.dataframe(df3)



st.subheader("Sales by Category")
df4=sales_by_category()
st.dataframe(df4)

st.subheader("Subcategory Performance")
df5=subcategory_performance()
st.dataframe(df5)



st.subheader("Sales By Segment")
df6=sales_by_segment()
st.dataframe(df6)



st.subheader("Monthly Sales Trend")
df7=monthly_sales_trend()
st.dataframe(df7)



st.subheader("Year-Over-Year Growth")
df8=yoy_growth()
st.dataframe(df8)



st.subheader("Highest & Lowest Sales Month")
df9=highest_lowest_sales_month()
st.dataframe(df9)


st.subheader("Seasonal Patterns")
df10=seasonal_patterns()
st.dataframe(df10)


st.subheader("Pareto Analysis")
df11=pareto_analysis()
st.dataframe(df11)