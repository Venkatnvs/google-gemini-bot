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



st.set_page_config(page_title="Gemini Text Bot",page_icon="🤖")
st.header("📝 Google Gemini Text Bot")
st.sidebar.markdown(
"""
# 🌟 Gemini Bot

### Welcome to Gemini Bot, your personal gateway to Google's Gemini API.

*Important:* Only 1 request per minute is allowed to ensure optimal performance.

---

**Developer:** N Venkat Swaroop

**GitHub Profile:** [Venkatnvs](https://github.com/Venkatnvs)

**Contact:** [Venkatnvs2005@gmail.com](mailto:venkatnvs2005@gmail.com)

**GitHub Repo:** [`Google Gemini Bot`](https://github.com/Venkatnvs/google-gemini-bot/)

**LICENSE:** [`MIT License`](https://github.com/Venkatnvs/google-gemini-bot/blob/main/LICENSE)
""")
input  = st.text_input("Input: ",key="input")
submit = st.button("Ask a Question")

if submit:
    rsp = gemini_text_bot(input)
    st.subheader("Response: ")
    st.write(rsp)
