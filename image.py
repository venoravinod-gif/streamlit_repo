import streamlit as st
file = st.file_uploader("Upload an image",type=["png","jpg","jpeg"])
if file:
    st.image(file)
