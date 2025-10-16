#AI Text Translator tool
import streamlit as st
import google.generativeai as genai

#Gemini API key setup
genai.configure(api_key="AIzaSyBmuVv8rM58WUoV0KjRp08wp-bpGhqOGeE")

#Load Gemini model
model = genai.GenerativeModel("gemini-2.5-pro")

#streamlit app setup
st.set_page_config(page_title="AI Text Translator")

st.title(("AI Text Translator(powered by Gemini"))

st.write("Pick Languages, type text, and get instant translation!")

languages = ["English","French","Spanish","German","Hindi","Chinese","Japanese","Korean"]

source_lang = st.selectbox("Pick your source language",languages)
target_lang = st.selectbox("Pick your target language",languages)

user_text = st.text_area("Type your text to translate")

#translation button
if st.button("Translate Text"):
  if user_text.strip() != "":
    with st.spinner("Translating..."):
      prompt = f"Translate this text from {source_lang} to {target_lang}:\n\n {user_text}"
      response = model.generate_content(prompt)
      translated_text = response.text
      st.success(f"Translation in {target_lang}:")
      st.write(translated_text)

  else:
    st.warning("Please type something to Translate")

st.caption("Made with love using streamlit and Gemini AI")
