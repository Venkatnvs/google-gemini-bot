from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as gai

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = gai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def gemini_text_bot(question):
    if question=="":
        return "Enter a Question"
    response = chat.send_message(question)
    return response.text

if 'chats' not in st.session_state:
    st.session_state['chats'] = []

st.set_page_config(page_title="Gemini Text Bot",page_icon="🤖")
st.header("Google Gemini Text Bot")

input  = st.text_input("Input: ",key="input")
submit = st.button("Submit")

if submit:
    rsp = gemini_text_bot(input)
    st.session_state['chats'].append(("BOT", rsp))
    st.session_state['chats'].append(("YOU", input))
    st.subheader("Response: ")
    for i, (role, text) in enumerate(reversed(st.session_state['chats'])):
        role_emoji = "👤" if role == "YOU" else "🤖"
        st.write(f"**{role_emoji} {role}:** {text}")
        if (i + 1) % 2 == 0:
            st.write("")