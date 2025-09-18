#colors and formatting with st.markdown()
import streamlit as st
from datetime import date

bday = st.date_input("Pick your birth date",
    min_value = date(1900,1,1),
    max_value = date(2025,12,31)
)

#ask for a fun message
message = st.text_area("Write your bday message:")

#button to create card
if st.button("Make my Card!"):
  if not message.strip():
    st.error("oops! you forgot to type your message")
  else:
    #show card
    st.markdown(f"""
    <h2 style='color:purple;'> Happy Birthday!</h2> "
    <p style = 'font-size:18px; color:black;'> Your Birthday is on: {bday}</p> 
    <p style = 'font-size:18px;color:blue;'>  {message}</p> 
    <p style = 'font-size:18px;color:green;'>  Have the best day ever</p> 
    """, unsafe_allow_html=True)
    st.success("Your bday card is ready!")
