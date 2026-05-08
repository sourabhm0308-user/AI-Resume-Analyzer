import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components import load_css, render_card
from utils.helpers import init_session_state

st.set_page_config(page_title="AI Suggestions", page_icon="✨", layout="wide")
init_session_state()
load_css()

st.title("✨ AI Rewrite Suggestions")

if not st.session_state.resume_analysis:
    st.warning("Please upload and analyze a resume first.")
    st.stop()

analysis = st.session_state.resume_analysis

st.markdown("### How to Improve Your Resume")
st.write("Implement these AI-generated suggestions to boost your ATS score and impress recruiters.")

suggestions = analysis.get('suggestions', [])

if suggestions:
    for i, sug in enumerate(suggestions):
        category = sug.get('category', 'General')
        advice = sug.get('advice', '')
        
        st.markdown(f"""
        <div class="custom-card" style="border-left: 4px solid var(--accent-purple);">
            <h4 style="color: var(--accent-purple); margin-top:0;">{category}</h4>
            <p>{advice}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Your resume looks great! No major suggestions at this time.")

st.markdown("---")

st.markdown("### 🎓 Recommended Certifications")
certs = analysis.get('recommended_certifications', [])

if certs:
    render_card("Boost Your Profile with these Certifications", certs, content_type="list")
else:
    st.write("No specific certifications recommended at this time.")
