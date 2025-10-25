import streamlit as st
import google.generativeai as genai
import PyPDF2
genai.configure(api_key="AIzaSyAnn_UrQdTnTi5LMy1H7CG_w-77QwRA7ZI")

model = genai.GenerativeModel("gemini-2.5-pro")

st.set_page_config(page_title="PDF Chatbot using Gemini")
st.title("PDF Chatbot using Gemini")
st.write("Upload a PDF, then ask questions from it")

#this creates a button that lets user upload a pdf file
pdf_file = st.file_uploader("Upload your pdf file",type=['pdf'])

if pdf_file is not None:
  pdf_reader = PyPDF2.PdfReader(pdf_file)#it reads the uploaded pdf
  full_text = ""

  for i in pdf_reader.pages: #10 pages
    full_text = full_text + i.extract_text()
  st.success("The file is uploaded correctly")
  context = ("Use info from full text to answer:" + full_text)  

  #Adding the question
  question = st.text_input("Ask Question about PDF.")

  #Getting the answer
  if st.button("Get Answer"):
    if question.strip():
      with st.spinner("Thinking"):
        response = model.generate_content(context + "Question\n" + question)
        answer = response.text
        st.success("\n Here is the answer")
        st.write(answer)
    else:
      st.warning("Please enter question")  
st.caption("Made with streamlit and Gemini Pro")

