#WORKING WITH DAta
import streamlit as st
import pandas as pd

st.title("Chai Sales Data Analysis")

file= st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Sales Summary")
    st.write(f"Total Cups Sold: {df['Cups_Sold'].sum()}")
    st.write(df.describe())

if file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Filter by", cities)
    filtered_data= df[df['City'] == selected_city]
    st.dataframe(filtered_data)
    