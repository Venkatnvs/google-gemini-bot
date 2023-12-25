from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as gai
from PIL import Image

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = gai.GenerativeModel("gemini-pro-vision")
chat = model.start_chat(history=[])

def gemini_img_bot(input,image):
    if input!="":
        response = chat.send_message([input,image])
    else:
        response = chat.send_message(image)
    return response.text

if 'chats_pro' not in st.session_state:
    st.session_state['chats_pro'] = []

st.set_page_config(page_title="Gemini Image Bot",page_icon="🤖")
st.header("🏞 Google Gemini Image Bot")
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
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
submit = st.button("Tell me about the image")

if submit:
    rsp = gemini_img_bot(input,image)
    st.session_state['chats_pro'].append(("BOT", {"text": rsp}))
    st.session_state['chats_pro'].append(("YOU", {"text": input, "image": image}))
    st.subheader("Response: ")
    for i, (role, content) in enumerate(reversed(st.session_state['chats_pro'])):
        role_emoji = "👤" if role == "YOU" else "🤖"
        st.write(f"**{role_emoji} {role}:** {content['text']}")
        if "image" in content:
            st.image(content["image"], caption="Uploaded Image.", use_column_width=True)
        if (i + 1) % 2 == 0:
            st.write("")