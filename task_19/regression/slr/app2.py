import streamlit as st

st.header("Welcome App") #simple text app
name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋")