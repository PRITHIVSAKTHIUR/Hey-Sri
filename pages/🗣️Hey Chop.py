
import streamlit as st
import voice_assistant
from streamlit_chat import message
import time

st.set_page_config( layout="wide",page_title="ChatterDog Chop",page_icon='🎙️')
st.title("Hey Sri 🎙️ ")
listen_btn = st.button("Try Saying ...")
if listen_btn:
    go = 1
    while(go):
        with st.spinner("Recording User Voice ..."):
            #time.sleep(5)
            voice_data = voice_assistant.record_audio("Recording")
        message(voice_data,is_user=True)
        go=voice_assistant.respond(voice_data)