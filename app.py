import streamlit as st
import pandas as pd

st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Simple text")
st.write("Any data")
st.markdown("**Bold Text**")

age = st.number_input("Enter age", 0, 100)
st.write(age)
rating= st.slider("rate",0,10)
st.write(rating)

if st.button("Click Me"):
  st.write("Button Clicked")

marks = pd.Series([78, 85, 92])
print(marks)
