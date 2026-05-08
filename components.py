import streamlit as st
import time
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components import load_css
from utils.helpers import init_session_state, reset_session_state, get_common_roles
from core.parser import parse_resume
from core.ai_engine import analyze_resume

st.set_page_config(page_title="Upload Resume", page_icon="📤", layout="wide")
init_session_state()
load_css()

st.title("📤 Upload Your Resume")

# Target Role Selection
st.markdown("### Step 1: Select Target Role")
target_role = st.selectbox(
    "What job role are you applying for?",
    options=get_common_roles(),
    index=get_common_roles().index(st.session_state.target_role) if st.session_state.target_role in get_common_roles() else 0
)

# File Uploader
st.markdown("### Step 2: Upload Document")
uploaded_file = st.file_uploader("Drag and drop your PDF or DOCX file here", type=["pdf", "docx"])

if uploaded_file is not None:
    if st.button("Analyze Resume", use_container_width=True, type="primary"):
        reset_session_state()
        st.session_state.target_role = target_role
        st.session_state.file_name = uploaded_file.name
        
        with st.spinner("Extracting text from document..."):
            try:
                resume_text = parse_resume(uploaded_file)
                if not resume_text or len(resume_text.strip()) < 50:
                    st.error("Could not extract enough text from the document. Please ensure it's a valid text-based PDF or DOCX.")
                    st.stop()
                st.session_state.resume_text = resume_text
            except Exception as e:
                st.error(f"Error parsing document: {e}")
                st.stop()
        
        with st.spinner(f"Analyzing resume for the '{target_role}' role using Gemini AI..."):
            try:
                analysis = analyze_resume(resume_text, target_role)
                if analysis:
                    st.session_state.resume_analysis = analysis
                    st.success("Analysis complete! Navigate to the Dashboard to view results.")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Failed to generate analysis. Check API key or try again.")
            except Exception as e:
                st.error(f"Error during AI analysis: {e}")

# If already analyzed, show status
if st.session_state.resume_analysis:
    st.info(f"Currently analyzing: **{st.session_state.file_name}** for **{st.session_state.target_role}**")
    if st.button("Clear Data and Start Over"):
        reset_session_state()
        st.rerun()
