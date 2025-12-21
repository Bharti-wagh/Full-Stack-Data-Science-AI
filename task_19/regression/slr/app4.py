import streamlit as st

st.title("To-Do App")

task = st.text_input("Enter task")

if st.button("Add Task"):
    st.write("✅ Task Added:", task)