import streamlit as st 
from queries.product_analysis import best_selling_products , most_profitable_products , negative_margin_products , product_profit_margin_analysis , product_pareto_analysis


st.title("Module 3 - Product Performance Intellignece ")
st.subheader("Best Selling Products")
df1=best_selling_products()
st.dataframe(df1)

st.subheader("Most Profitable Products")
df2=most_profitable_products()
st.dataframe()


st.subheader("Negative Margin Products")
df3=negative_margin_products()
st.dataframe(df3)

st.subheader("Profit Margin Analysis ")
df4=product_profit_margin_analysis()
st.dataframe(df4)


st.subheader("Pareto Analysis ")
df5=product_pareto_analysis()
st.dataframe(df5)