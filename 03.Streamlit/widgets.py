import streamlit as st
import pandas as pd
import numpy as np

st.title("streamlit text input")

name = st.text_input("Enter your name : ")

age = st.slider("select your age : ",0,100,25)

st.write(f"your age is: {age}")

option = ["default","python","java","C++","c"]
choice= st.selectbox("Choose your fav language: ",option)
st.write("you selected ",choice)

if name:
    st.write(f"Hellow ,{name}")
    
    
data = {
    "Name": ["Arpan", "Rahul", "Priya", "Sneha", "Amit"],
    "Age": [24, 25, 23, 22, 26],
    "Marks": [85, 78, 92, 88, 76],
    "City": ["Kolkata", "Delhi", "Mumbai", "Bangalore", "Chennai"]
}
df= pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)




upload_file = st.file_uploader("Choose a csv file",type="csv")
if upload_file is not None:
    df= pd.read_csv(upload_file)
    st.write(df)