import streamlit as st

age = st.number_input("Enter your age",min_value=1,max_value=80,step=1)
st.write(f"Your age is {age}. Welcome to the streamlit world!")
