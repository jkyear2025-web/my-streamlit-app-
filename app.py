import streamlit as st

# Set the page title
st.title("My First Streamlit App 🚀")

# Add a simple text header
st.header("Welcome!")

# Add an interactive widget
name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}! Thanks for checking out my app.")