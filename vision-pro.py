from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as gai
from PIL import Image

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = gai.GenerativeModel("gemini-pro-vision")

def gemini_img_bot(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text



st.set_page_config(page_title="Gemini Image Bot",page_icon="🤖")
st.header("Google Gemini Image Bot")
input  = st.text_input("Input: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
submit = st.button("Tell me about the image")

if submit:
    rsp = gemini_img_bot(input,image)
    st.subheader("Response: ")
    st.write(rsp)