import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)


    st.subheader("Data Preview")
    st.write(df.head)

    st.subheader("Data Description")
    st.write(df.describe())

    st.subheader("Filter Data")
    column = df.columns.tolist()
    selected_column = st.selectbox("Select Column to filter:", column)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value:", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis:", column)
    y_column = st.selectbox("Select y-axis:", column)

    if st.button("Generate Plot"):
       st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Please upload a CSV file.")       