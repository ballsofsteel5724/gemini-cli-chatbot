import streamlit as st
from gem_prompts import start_chat_session

st.set_page_config(page_title = "My AI Chat App", page_icon = "🤖")
st.title('My AI Web Chat')
st.write("Type a message below to start talking!")

if "ai_session" not in st.session_state:
    st.session_state.ai_session = start_chat_session()

if "ui_messages" not in st.session_state:
    st.session_state.ui_messages = []

for message in st.session_state.ui_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.ui_messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response = st.session_state.ai_session.send_message(user_input)
        st.markdown(response.text)

    st.session_state.ui_messages.append({"role": "assistant", "content": response.text})