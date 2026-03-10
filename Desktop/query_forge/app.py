import streamlit as st
from utils.db import QueryEngine

engine = QueryEngine("data/superstore.csv")

st.title("Query Forge")
st.write("Total Rows Loaded:", len(engine.df))
st.write("Columns:", engine.columns())