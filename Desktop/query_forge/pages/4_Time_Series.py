import streamlit as st
from queries.time_series_analysis import monthly_revenue_trend , mom_growth ,  yoy_comparison , cumulative_revenue , rolling_revenue_trend , sales_volatility


st.title("Module 4 - Time Series Analysis ")
st.subheader("Monthly Revenue Trend ")
df1=monthly_revenue_trend()
st.dataframe(df1)


st.subheader("Month Over Month Growth ")
df2=mom_growth()
st.dataframe(df2)


st.subheader("Year Over Year Growth")
df3= yoy_comparison()
st.dataframe(df3)


st.subheader("Cumulative Revenue Generation")
df4=cumulative_revenue()
st.dataframe(df4)

st.subheader("Rolling Average Trend ")
df5=rolling_revenue_trend()
st.dataframe(df5)


st.subheader("Sales Volatility Trend")
df6=sales_volatility()
st.dataframe(df6)