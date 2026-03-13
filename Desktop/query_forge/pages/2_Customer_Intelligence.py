import streamlit as st
import matplotlib.pyplot as plt
from queries.customer_analysis import (
    customer_lifetime_value, repeat_vs_onetime_customers,
    rfm_segmentation, customer_revenue_tiers,
    customer_distribution, customer_distribution_by_category,
    customer_distribution_by_subcategory
)

st.title("Module 2 — Customer Intelligence")

st.subheader("Customer Lifetime Value")
df1 = customer_lifetime_value()
st.dataframe(df1)
fig1, ax1 = plt.subplots(figsize=(12, 4))
ax1.bar(df1["Customer Name"], df1["Total_Sales"], color="#4C72B0")
ax1.set_title("Top 20 Customers by Revenue")
ax1.set_xlabel("Customer")
ax1.set_ylabel("Total Sales")
plt.xticks(rotation=90)
st.pyplot(fig1)

st.subheader("Repeat Vs. One Time Customers")
df2 = repeat_vs_onetime_customers()
st.dataframe(df2)
fig2, ax2 = plt.subplots()
ax2.pie(df2["Customer_Count"], labels=df2["Customer_Type"],
        autopct="%1.1f%%", colors=["#4C72B0", "#DD8452"])
ax2.set_title("Repeat vs One-Time Customers")
st.pyplot(fig2)

st.subheader("RFM Customer Segmentation")
df3 = rfm_segmentation()
st.dataframe(df3)
fig3, ax3 = plt.subplots()
segment_counts = df3["Customer_Segment"].value_counts()
ax3.bar(segment_counts.index, segment_counts.values,
        color=["#55A868", "#4C72B0", "#DD8452", "#C44E52"])
ax3.set_title("Customer Segments by RFM Score")
ax3.set_xlabel("Segment")
ax3.set_ylabel("Number of Customers")
st.pyplot(fig3)

st.subheader("Revenue Contribution by Customer Tier")
df4 = customer_revenue_tiers()
st.dataframe(df4)
fig4, ax4 = plt.subplots()
tier_counts = df4["Customer_Tier"].value_counts()
ax4.pie(tier_counts.values, labels=tier_counts.index,
        autopct="%1.1f%%", colors=["#C0A020", "#C0C0C0", "#CD7F32", "#4C72B0"])
ax4.set_title("Customer Tier Distribution")
st.pyplot(fig4)

st.subheader("Customer Distribution Across Business Dimensions")

st.subheader("Customer Distribution Across Region & Segment")
df5 = customer_distribution()
st.dataframe(df5)
fig5, ax5 = plt.subplots(figsize=(12, 4))
labels = df5["Region"] + " - " + df5["Segment"]
ax5.bar(labels, df5["Total_Customers"], color="#4C72B0")
ax5.set_title("Customer Distribution by Region & Segment")
plt.xticks(rotation=45)
st.pyplot(fig5)

st.subheader("Customer Distribution By Category")
df6 = customer_distribution_by_category()
st.dataframe(df6)
fig6, ax6 = plt.subplots()
ax6.bar(df6["Category"], df6["Total_Customers"],
        color=["#4C72B0", "#DD8452", "#55A868"])
ax6.set_title("Customer Distribution by Category")
ax6.set_xlabel("Category")
ax6.set_ylabel("Total Customers")
st.pyplot(fig6)

st.subheader("Customer Distribution By Sub-Category")
df7 = customer_distribution_by_subcategory()
st.dataframe(df7)
fig7, ax7 = plt.subplots(figsize=(12, 4))
ax7.bar(df7["Sub-Category"], df7["Total_Customers"], color="#4C72B0")
ax7.set_title("Customer Distribution by Sub-Category")
ax7.set_xlabel("Sub-Category")
ax7.set_ylabel("Total Customers")
plt.xticks(rotation=45)
st.pyplot(fig7)