import streamlit as st
from PIL import Image



st.title('サプーアプリ')
st.caption('これはサプー画面用のテストアプリです')


# 画像
image = Image.open('.\data\IMG_1784.JPG')
st.image(image,width=200)
