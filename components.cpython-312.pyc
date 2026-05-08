import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components import load_css, render_card
from utils.helpers import init_session_state
from utils.report_generator import generate_pdf_report

st.set_page_config(page_title="Detailed Report", page_icon="📑", layout="wide")
init_session_state()
load_css()

st.title("📑 Skills & Detailed Report")

if not st.session_state.resume_analysis:
    st.warning("Please upload and analyze a resume first.")
    st.stop()

analysis = st.session_state.resume_analysis

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🟢 Detected Skills")
    detected = analysis.get('detected_skills', [])
    if detected:
        render_card("Skills Found in Resume", detected, content_type="skills")
    else:
        st.info("No explicit skills detected.")

with col2:
    st.markdown("### 🔴 Missing Skills")
    missing = analysis.get('missing_skills', [])
    if missing:
        render_card(f"Crucial Skills Missing for {st.session_state.target_role}", missing, content_type="missing_skills")
    else:
        st.success("Great job! No major missing skills detected for this role.")

st.markdown("---")

st.markdown("### 📥 Download PDF Report")
st.write("Get a complete summary of your ATS score, skills gap, and improvement suggestions in a printable PDF format.")

if st.button("Generate & Download PDF Report", type="primary"):
    with st.spinner("Generating PDF..."):
        try:
            pdf_path = generate_pdf_report(analysis)
            with open(pdf_path, "rb") as file:
                btn = st.download_button(
                    label="Download Report Now",
                    data=file,
                    file_name="AI_Resume_Report.pdf",
                    mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Failed to generate PDF: {e}")
