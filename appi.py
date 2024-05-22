import streamlit as st
import pandas as pd

st.text("Streamlit App my_first_app")
st.header("App header")

st.header("My First App")

st.text("Streamlit App my_first_app")
st.header("App header")

st.header("My First App")

st.text("Streamlit App my_first_app")
st.header("App header")

st.header("My First App")
uploaded_file = st.file_uploader("Choose a file")

df1=pd.read_excel(uploaded_file)
