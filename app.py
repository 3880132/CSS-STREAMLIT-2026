

import streamlit as st

st.title("CSS 2026")

st.header("Day 3 Assignment")

st.title("My First Streamlit App")

#st.write("Hello, Streamlit!")

st.header("Number selection")

number = st.slider("Pick a number", 1, 100)

st.write(f"You picked: {number}")