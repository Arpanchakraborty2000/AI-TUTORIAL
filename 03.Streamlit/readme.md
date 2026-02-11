# 🚀 Streamlit Complete Guide

## 📌 What is Streamlit?

Streamlit is an open-source Python framework used to build data apps
quickly with minimal code.\
It is widely used for Machine Learning, Data Science, and AI dashboards.

------------------------------------------------------------------------

# 🛠 Installation

``` bash
pip install streamlit
```

Check version:

``` bash
streamlit --version
```

------------------------------------------------------------------------

# ▶️ Running a Streamlit App

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

# 📂 Basic Streamlit App Structure

``` python
import streamlit as st

st.title("My First Streamlit App")
st.write("Hello World!")
```

------------------------------------------------------------------------

# 🧱 All Important Streamlit Functions

## 1️⃣ Text & Display Functions

``` python
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Simple Text")
st.markdown("**Markdown Text**")
st.code("print('Hello')")
st.latex(r"\sum_{i=1}^n i")
```

------------------------------------------------------------------------

## 2️⃣ Data Display

``` python
import pandas as pd

df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})

st.dataframe(df)
st.table(df)
st.json({"key":"value"})
```

------------------------------------------------------------------------

## 3️⃣ Input Widgets

``` python
name = st.text_input("Enter Name")
age = st.number_input("Enter Age", 0, 100)
agree = st.checkbox("I Agree")
gender = st.radio("Select Gender", ["Male","Female"])
option = st.selectbox("Choose Option", ["A","B","C"])
multi = st.multiselect("Select Multiple", ["X","Y","Z"])
slider = st.slider("Select Range", 0, 100, 50)
button = st.button("Click Me")
file = st.file_uploader("Upload File")
```

------------------------------------------------------------------------

## 4️⃣ Layout Functions

``` python
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")

with st.expander("See More"):
    st.write("Hidden Content")
```

------------------------------------------------------------------------

## 5️⃣ Sidebar

``` python
st.sidebar.title("Sidebar")
st.sidebar.selectbox("Choose", ["Option 1","Option 2"])
```

------------------------------------------------------------------------

## 6️⃣ Charts

``` python
import numpy as np

data = np.random.randn(100, 3)
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)
```

------------------------------------------------------------------------

## 7️⃣ Caching

``` python
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")
```

------------------------------------------------------------------------

## 8️⃣ Session State

``` python
if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment"):
    st.session_state.counter += 1

st.write(st.session_state.counter)
```

------------------------------------------------------------------------

## 9️⃣ Forms

``` python
with st.form("my_form"):
    name = st.text_input("Name")
    submit = st.form_submit_button("Submit")
```

------------------------------------------------------------------------

## 🔟 Download Button

``` python
st.download_button("Download", data="Hello", file_name="file.txt")
```

------------------------------------------------------------------------

# 🐳 Run Streamlit in Docker

### Dockerfile

``` dockerfile
FROM python:3.10
WORKDIR /app
COPY . /app
RUN pip install streamlit
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build & Run:

``` bash
docker build -t streamlit-app .
docker run -p 8501:8501 streamlit-app
```

------------------------------------------------------------------------

# ☁ Deploy Streamlit

### Streamlit Community Cloud

Push your code to GitHub → Deploy on Streamlit Cloud.

### AWS EC2

1.  Launch EC2 instance
2.  Install Python & Streamlit
3.  Run app
4.  Open port 8501

------------------------------------------------------------------------

# 🎯 Best Practices

-   Use caching for performance
-   Use sidebar for filters
-   Use session_state for dynamic apps
-   Structure code in functions

------------------------------------------------------------------------

# 📚 Official Documentation

https://docs.streamlit.io/

------------------------------------------------------------------------

# 👨‍💻 Author

Created for learning and development purposes.
