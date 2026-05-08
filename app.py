import streamlit as st
import os
import sys

# Ensure custom modules can be imported
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ui.components import load_css
from utils.helpers import init_session_state

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State
init_session_state()

# Load Custom CSS
load_css()

# Home Page Content
st.title("Welcome to the AI Resume Analyzer Agent 🚀")

st.markdown("""
<div style='text-align: center; margin-top: 2rem; margin-bottom: 2rem;'>
    <h3 style='color: var(--text-secondary);'>Optimize your resume and land your dream job.</h3>
    <p style='font-size: 1.1rem;'>
        This advanced ATS system uses the Gemini AI to analyze your resume against industry standards, 
        detect missing skills, and provide actionable rewrite suggestions.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='custom-card' style='text-align: center; height: 250px;'>
        <div style='font-size: 3rem; margin-bottom: 10px;'>📊</div>
        <h4>ATS Scoring</h4>
        <p style='color: var(--text-secondary);'>Get an accurate ATS score based on keywords, readability, and impact.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='custom-card' style='text-align: center; height: 250px;'>
        <div style='font-size: 3rem; margin-bottom: 10px;'>🎯</div>
        <h4>Skill Gap Analysis</h4>
        <p style='color: var(--text-secondary);'>Identify exactly which skills you are missing for your target role.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='custom-card' style='text-align: center; height: 250px;'>
        <div style='font-size: 3rem; margin-bottom: 10px;'>✨</div>
        <h4>AI Rewrite Suggestions</h4>
        <p style='color: var(--text-secondary);'>Receive smart suggestions to improve bullet points and summaries.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.1);'><br>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <h3>Ready to get started?</h3>
    <p>Navigate to <b>1. Upload Resume</b> in the sidebar to begin.</p>
</div>
""", unsafe_allow_html=True)
