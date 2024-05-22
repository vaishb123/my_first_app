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
fkonzept = st.file_uploader("Upload a file", type=["csv", "xlsx", "txt"])
if fkonzept:
    wb = openpyxl.load_workbook(fkonzept, read_only=True)
    st.info(f"File uploaded: {fkonzept.name}")
    st.info(f"Sheet names: {wb.sheetnames}")
