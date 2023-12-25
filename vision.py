from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as gai

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = gai.GenerativeModel("gemini-pro")

def gemini_text_bot(question):
    if question=="":
        return "Enter a Question"
    response  = model.generate_content(question)
    return response.text



st.set_page_config(page_title="Gemini Text Bot")

st.header("Google Gemini Text Bot")

input  = st.text_input("Input: ",key="input")
submit = st.button("Ask a Question")

if submit:
    rsp = gemini_text_bot(input)
    st.subheader("Response: ")
    st.write(rsp)