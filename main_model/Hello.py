import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# This is the Blue-Mic team presenting you the GUI of our AI/ML model. 👋")

image = Image.open(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\main_model\happiness.jpg')
st.image(image, caption='Happiness')
st.text(" ")

rad=st.sidebar.radio("Navigation",["Happiness Prediction","About"])