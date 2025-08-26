
import streamlit as st


#main title
st.title("This is the Main title")
#section heading
st.header("This is the section heading")
#sub heading
st.subheader("This is the subheading")

#Normal paragraph
st.write("This is my normal para. It's great for description")

st.markdown(
    """
    **I am the bold text**, *I am in Italic*,
    and a [link to Google](https://www.google.com/)
    """,
    unsafe_allow_html=True
)
#permission to use html tages in markdown
