#Story Generator tool
import streamlit as st
import google.generativeai as genai

#set Gemini API key
genai.configure(api_key="AIzaSyACpzKhjB4-_ESpBFqt9LZP0-KUPxfXWTk")

#Load gemini model
model = genai.GenerativeModel("gemini-2.5-pro")

#streamlit app
st.set_page_config(page_title="Story Maker",page_icon="📖")

st.title("Make A Story With Gemini")
st.write("Write anything to get started")

#Input box
prompt = st.text_input("Enter your story idea")

#create button to generate story
if st.button("Generate Story"):
  if prompt.strip() != "":
    with st.spinner("Working Behind The Scenes"):
      response = model.generate_content(prompt + "Create a fun and simple story")
      story = response.text
      st.success("Your story is baked:")
      st.write(story)
  else:
    st.warning("Please enter something to get a story") 
#Footer
st.caption("Made with streamlit and Gemini AI")
