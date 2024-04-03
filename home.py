import streamlit as st
from langchain.prompts import PromptTemplate

st.title("Hello world!")

st.subheader("Welcome to streamlit")

st.markdown(
    """
    This is a simple example of a streamlit app.
    """
)

st.write("hello")

st.write([1,2,3,4])

st.write({"x": 1})

st.write(PromptTemplate)

p = PromptTemplate.from_template("xxxx")

st.write(p)


st.selectbox("CHoose your model", ("GPT-3","GPT-4"),)