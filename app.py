# app.py

import streamlit as st

# Title and description
st.title("Simple Streamlit App")
st.write("This is a simple example of a Streamlit app.")

# Input fields
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)

# Display input data
if st.button("Submit"):
    st.write(f"Hello, {name}! You are {age} years old.")

