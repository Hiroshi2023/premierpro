import streamlit as st
import pandas as pd

#Upload un fichier
st.title('Upload dun fichier')
image = st.file_uploader('**Please unload an image**',type=["png","jpg"])
if image:
    st.image(image)

video = st.file_uploader('**Please upload a video**', type=["avi","mp4"])
if video:
    st.video(video)

#Slider
st.slider('**This is a slider**', min_value=20, max_value=60,value=30)

#Text input
st.text_input("Enter a text to be traduced")

#Text area
st.text_area('Course description')
#Date input
st.date_input('Enter your registration date:')