#upload homework(only text files allowed")
dr_files = st.file_uploader("Upload your DR files", type = ["png","jpg","jpeg"]
                            , accept_multiple_files=True,key="drawing")

if dr_files:
  st.write("Your DR files uploaded succesfully")
  for i in dr_files:
    st.write("----",i.name,width=200)
