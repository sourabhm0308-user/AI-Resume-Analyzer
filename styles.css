import streamlit as st
import plotly.graph_objects as go
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ui.components import load_css, render_metric_card
from utils.helpers import init_session_state

st.set_page_config(page_title="Analysis Dashboard", page_icon="📊", layout="wide")
init_session_state()
load_css()

st.title("📊 Analysis Dashboard")

if not st.session_state.resume_analysis:
    st.warning("Please upload and analyze a resume first.")
    st.page_link("pages/1_Upload_Resume.py", label="Go to Upload Page")
    st.stop()

analysis = st.session_state.resume_analysis

# --- Top Row: Metrics ---
col1, col2 = st.columns(2)

with col1:
    ats_score = analysis.get('ats_score', 0)
    fig_ats = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = ats_score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "ATS Score", 'font': {'size': 24, 'color': '#e2e8f0'}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#8b5cf6"},
            'bgcolor': "rgba(255,255,255,0.05)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.1)",
            'steps': [
                {'range': [0, 40], 'color': 'rgba(239, 68, 68, 0.3)'},
                {'range': [40, 70], 'color': 'rgba(245, 158, 11, 0.3)'},
                {'range': [70, 100], 'color': 'rgba(16, 185, 129, 0.3)'}
            ],
        }
    ))
    fig_ats.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#e2e8f0"}, height=300)
    st.plotly_chart(fig_ats, use_container_width=True)

with col2:
    match_pct = analysis.get('match_percentage', 0)
    fig_match = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = match_pct,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Job Match: {st.session_state.target_role}", 'font': {'size': 24, 'color': '#e2e8f0'}},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#3b82f6"},
            'bgcolor': "rgba(255,255,255,0.05)",
            'steps': [
                {'range': [0, 50], 'color': 'rgba(239, 68, 68, 0.3)'},
                {'range': [50, 80], 'color': 'rgba(245, 158, 11, 0.3)'},
                {'range': [80, 100], 'color': 'rgba(16, 185, 129, 0.3)'}
            ],
        }
    ))
    fig_match.update_layout(paper_bgcolor="rgba(0,0,0,0)", font={'color': "#e2e8f0"}, height=300)
    st.plotly_chart(fig_match, use_container_width=True)

# --- Summary Section ---
st.markdown("### Professional Summary Evaluation")
st.info(analysis.get('summary', 'No summary generated.'))

# --- Quick Overview ---
st.markdown("### Quick Overview")
c1, c2 = st.columns(2)
with c1:
    with st.expander("✅ Top Strengths", expanded=True):
        for item in analysis.get('strengths', []):
            st.markdown(f"- {item}")
with c2:
    with st.expander("⚠️ Critical Weaknesses", expanded=True):
        for item in analysis.get('weaknesses', []):
            st.markdown(f"- {item}")
