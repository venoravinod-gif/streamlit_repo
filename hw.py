#Homework Helper squad
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBmuVv8rM58WUoV0KjRp08wp-bpGhqOGeE")

model = genai.GenerativeModel("gemini-2.5-pro")

st.set_page_config(page_title="Homework Helper squad")
st.title("Homework Helper squad - AI friends to help you!")

#Agent workflows
#Math Agent section
if agent == "Math Agent":
  st.subheader("Math Agent")
  question = st.text_input("Enter your Math question:")
  if st.button("Ask Math Agent"):
    if question.strip():
      prompt = f"Explain and solve this math problem for a child: {question}"
      response = model.generate_content(prompt)
      st.success(response.text)
    else: 
       st.warning("Please type a Math problem")

  elif agent == "Grammar Agent":
    st.subheader("Grammar Agent") 
  text = st.text_area("Paste your sentence or paragraph here:")
  if st.button("Ask Grammar Agent"):
    if text.strip():
      prompt = f"Check grammar and spelling in this text, and explain corrections simply: {text}"
      response = model.generate_content(prompt)
      st.success(response.text)
    else: 
       st.warning("Please paste something for checking")

  elif agent == "Explainer Agent":
    st.subheader("Explainer Agent") 
  topic = st.text_input("What should I explain:")
  if st.button("Ask Explainer Agent"):
    if topic.strip():
      prompt = f"Explain this topic in simple words for a 10 year old kid: {topic}"
      response = model.generate_content(prompt)
      st.success(response.text)
    else: 
       st.warning("Please enter a topic to explain")
