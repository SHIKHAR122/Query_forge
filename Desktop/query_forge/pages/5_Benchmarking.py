import streamlit as st
from queries.benchmarking import benchmark_all_queries

st.title("Query Benchmarking")
st.write("Execution time for all queries in the system.")

with st.spinner("Running all queries..."):
    df = benchmark_all_queries()

st.dataframe(df)
st.bar_chart(df.set_index("Query")["Execution_Time_Seconds"])