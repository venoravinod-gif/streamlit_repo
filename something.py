#upload homework(only text files allowed")
import streamlit as st

import streamlit as staticmethod
st.title("My file uploader playground")

#upload homework(only text files allowed")
hw_files = st.file_uploader("Upload your HW text files", type = ["txt","pdf"]
                            , accept_multiple_files=True,key="homework")

if hw_files:
  st.write("Your HW files uploaded succesfully")
  for i in hw_files:
    st.write("----",i.name)
    
dr_files = st.file_uploader("Upload your DR files", type = ["png","jpg","jpeg"]
                            , accept_multiple_files=True,key="drawing")

if dr_files:
  st.write("Your DR files uploaded succesfully")
  for i in dr_files:
    st.write("----",i.name,width=200)
