import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components import load_css
from utils.helpers import init_session_state
from core.ai_engine import chat_with_resume

st.set_page_config(page_title="Chat Assistant", page_icon="💬", layout="wide")
init_session_state()
load_css()

st.title("💬 AI Chat Assistant")

if not st.session_state.resume_text:
    st.warning("Please upload a resume first to chat about it.")
    st.stop()

st.write(f"Ask me anything about your resume for the **{st.session_state.target_role}** role!")

# Display chat messages from history on app rerun
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("E.g., 'How can I make my experience sound more impactful?'"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.spinner("Thinking..."):
        response = chat_with_resume(
            st.session_state.resume_text, 
            st.session_state.chat_history, 
            prompt
        )
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})

if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.rerun()
