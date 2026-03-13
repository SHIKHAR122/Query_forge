import streamlit as st
import matplotlib.pyplot as plt
from queries.product_analysis import (
    best_selling_products, most_profitable_products,
    negative_margin_products, product_profit_margin_analysis,
    product_pareto_analysis
)

st.title("Module 3 — Product Performance Intelligence")

st.subheader("Best Selling Products")
df1 = best_selling_products()
st.dataframe(df1)
fig1, ax1 = plt.subplots(figsize=(12, 4))
ax1.bar(df1["Product Name"], df1["Total_Revenue"], color="#4C72B0")
ax1.set_title("Top 20 Best Selling Products")
ax1.set_xlabel("Product")
ax1.set_ylabel("Total Revenue")
plt.xticks(rotation=90)
st.pyplot(fig1)

st.subheader("Most Profitable Products")
df2 = most_profitable_products()
st.dataframe(df2)
fig2, ax2 = plt.subplots(figsize=(12, 4))
ax2.bar(df2["Product Name"], df2["Total_Profit"], color="#55A868")
ax2.set_title("Top 20 Most Profitable Products")
ax2.set_xlabel("Product")
ax2.set_ylabel("Total Profit")
plt.xticks(rotation=90)
st.pyplot(fig2)

st.subheader("Negative Margin Products")
df3 = negative_margin_products()
st.dataframe(df3)
fig3, ax3 = plt.subplots(figsize=(12, 4))
ax3.bar(df3["Product Name"], df3["Total_Profit"], color="#C44E52")
ax3.set_title("Loss Making Products")
ax3.set_xlabel("Product")
ax3.set_ylabel("Total Profit")
plt.xticks(rotation=90)
st.pyplot(fig3)

st.subheader("Profit Margin Analysis")
df4 = product_profit_margin_analysis()
st.dataframe(df4)
fig4, ax4 = plt.subplots()
margin_counts = df4["Margin_Category"].value_counts()
ax4.pie(margin_counts.values, labels=margin_counts.index,
        autopct="%1.1f%%",
        colors=["#55A868", "#4C72B0", "#DD8452", "#C44E52"])
ax4.set_title("Product Margin Distribution")
st.pyplot(fig4)

st.subheader("Pareto Analysis")
df5 = product_pareto_analysis()
st.dataframe(df5)
fig5, ax5 = plt.subplots(figsize=(12, 4))
ax5.bar(df5["Product Name"], df5["Cumulative_Pct"], color="#4C72B0")
ax5.axhline(y=80, color="#C44E52", linestyle="--", label="80% Line")
ax5.set_title("Pareto Analysis — Cumulative Revenue %")
ax5.set_xlabel("Product")
ax5.set_ylabel("Cumulative %")
ax5.legend()
plt.xticks(rotation=90)
st.pyplot(fig5)