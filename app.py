import streamlit as st

st.title("Streamlit Exam Practice")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello {name}")
