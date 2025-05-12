import streamlit as st
import pandas as pd

# Load data from CSV file
data = pd.read_csv("data.csv")

# Display title
st.title("Simple Streamlit App")
st.write("This is a simple Streamlit app displaying a dataset!")

# Show the dataframe
st.write(data)
