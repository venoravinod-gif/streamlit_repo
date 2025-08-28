import streamlit as st

name = st.number_input("Enter your age")
if name:
  st.write(f"Hello {name}! Welcome to the streamlit world!")
