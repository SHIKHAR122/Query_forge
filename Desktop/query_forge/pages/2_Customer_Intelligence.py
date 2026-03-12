import streamlit as st
from queries.customer_analysis import customer_lifetime_value,repeat_vs_onetime_customers,rfm_segmentation, customer_revenue_tiers,customer_distribution,customer_distribution_by_category,customer_distribution_by_subcategory

st.title("Module 2 — Customer Intelligence")

st.subheader("Customer Lifetime Value")
df1 = customer_lifetime_value()
st.dataframe(df1)


st.subheader("Repeat Vs. One Time Customers")
df2=repeat_vs_onetime_customers()
st.dataframe(df2)


st.subheader("RFM Customer Segmentation")
df3=rfm_segmentation()
st.dataframe(df3)

st.subheader("Revenue Contribution by Customer Tier")
df4= customer_revenue_tiers()
st.dataframe(df4)

st.subheader("Customer Distribution Across Business Dimensions : ")
st.subheader("Customer Distribution across region ")
df5=customer_distribution()
st.dataframe(df5)



st.subheader("Customer Distribution By Category")
df6=customer_distribution_by_category()
st.dataframe(df6)


st.subheader("Customer Distrbution By Sub-Category")
df7=customer_distribution_by_subcategory()
st.dataframe(df7)