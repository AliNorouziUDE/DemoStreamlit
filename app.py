# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 09:45:14 2025

@author: Ali2
"""
import streamlit as st
import pandas as pd


st.title("Excel File Uploader")

# Upload Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Read Excel file into a DataFrame
        df = pd.read_excel(uploaded_file)

        st.success("File uploaded successfully!")
        st.write("### Preview of Data:")
        st.dataframe(df.head())  # Show first 5 rows
    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload an Excel file to proceed.")
