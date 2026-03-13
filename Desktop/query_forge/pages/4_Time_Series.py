import streamlit as st
import matplotlib.pyplot as plt
from queries.time_series_analysis import (
    monthly_revenue_trend, mom_growth,
    yoy_comparison, cumulative_revenue,
    rolling_revenue_trend, sales_volatility
)

st.title("Module 4 - Time Series Analysis")

st.subheader("Monthly Revenue Trend")
df1 = monthly_revenue_trend()
st.dataframe(df1)
fig1, ax1 = plt.subplots(figsize=(12, 4))
ax1.plot(df1["Month"], df1["Total_Revenue"], marker="o", color="#4C72B0", linewidth=2)
ax1.plot(df1["Month"], df1["Total_Profit"], marker="o", color="#55A868", linewidth=2)
ax1.set_title("Monthly Revenue vs Profit Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Amount")
ax1.legend(["Revenue", "Profit"])
plt.xticks(rotation=90)
st.pyplot(fig1)

st.subheader("Month Over Month Growth")
df2 = mom_growth()
st.dataframe(df2)
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.bar(df2["Month"], df2["MoM_Revenue_Growth"], color=[
    "#55A868" if x >= 0 else "#C44E52" for x in df2["MoM_Revenue_Growth"]
])
ax2.axhline(y=0, color="black", linewidth=0.8)
ax2.set_title("Month Over Month Revenue Growth %")
ax2.set_xlabel("Month")
ax2.set_ylabel("Growth %")
plt.xticks(rotation=90)
st.pyplot(fig2)

st.subheader("Year Over Year Comparison")
df3 = yoy_comparison()
st.dataframe(df3)
fig3, ax3 = plt.subplots(figsize=(12, 4))
for col in ["Revenue_2014", "Revenue_2015", "Revenue_2016", "Revenue_2017"]:
    ax3.plot(df3["Month_Num"], df3[col], marker="o", linewidth=2, label=col)
ax3.set_title("Year Over Year Revenue Comparison")
ax3.set_xlabel("Month")
ax3.set_ylabel("Revenue")
ax3.legend()
st.pyplot(fig3)

st.subheader("Cumulative Revenue Generation")
df4 = cumulative_revenue()
st.dataframe(df4)
fig4, ax4 = plt.subplots(figsize=(12, 4))
ax4.fill_between(df4["Month"], df4["Cumulative_Revenue"], alpha=0.4, color="#4C72B0")
ax4.plot(df4["Month"], df4["Cumulative_Revenue"], color="#4C72B0", linewidth=2)
ax4.set_title("Cumulative Revenue Over Time")
ax4.set_xlabel("Month")
ax4.set_ylabel("Cumulative Revenue")
plt.xticks(rotation=90)
st.pyplot(fig4)

st.subheader("Rolling Average Trend")
df5 = rolling_revenue_trend()
st.dataframe(df5)
fig5, ax5 = plt.subplots(figsize=(12, 4))
ax5.plot(df5["Month"], df5["Total_Revenue"], color="#DD8452", linewidth=1, label="Actual")
ax5.plot(df5["Month"], df5["Rolling_3Month_Avg"], color="#4C72B0", linewidth=2, label="3M Avg")
ax5.plot(df5["Month"], df5["Rolling_6Month_Avg"], color="#55A868", linewidth=2, label="6M Avg")
ax5.set_title("Rolling Revenue Trend")
ax5.set_xlabel("Month")
ax5.set_ylabel("Revenue")
ax5.legend()
plt.xticks(rotation=90)
st.pyplot(fig5)

st.subheader("Sales Volatility Trend")
df6 = sales_volatility()
st.dataframe(df6)
fig6, ax6 = plt.subplots(figsize=(12, 4))
colors = df6["Volatility_Tag"].map({
    "Anomaly": "#C44E52",
    "Unusual": "#DD8452",
    "Normal": "#4C72B0"
})
ax6.bar(df6["Month"], df6["Total_Revenue"], color=colors)
ax6.set_title("Sales Volatility — Anomaly Detection")
ax6.set_xlabel("Month")
ax6.set_ylabel("Revenue")
plt.xticks(rotation=90)
st.pyplot(fig6)