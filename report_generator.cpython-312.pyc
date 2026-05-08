import streamlit as st
import os

def load_css():
    """Injects custom CSS into the Streamlit app."""
    css_path = os.path.join(os.path.dirname(__file__), 'styles.css')
    try:
        with open(css_path, 'r') as f:
            css = f.read()
            st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS not found.")

def render_card(title, content, content_type="text"):
    """
    Renders a custom HTML card.
    """
    html = f"""
    <div class="custom-card">
        <h3>{title}</h3>
    """
    
    if content_type == "text":
        html += f"<p>{content}</p>"
    elif content_type == "skills":
        skills_html = ""
        for skill in content:
            skills_html += f'<span class="skill-badge">{skill}</span>'
        html += f"<div>{skills_html}</div>"
    elif content_type == "missing_skills":
        skills_html = ""
        for skill in content:
            skills_html += f'<span class="skill-badge missing">{skill}</span>'
        html += f"<div>{skills_html}</div>"
    elif content_type == "list":
        list_html = "<ul>"
        for item in content:
            list_html += f"<li>{item}</li>"
        list_html += "</ul>"
        html += list_html
        
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_metric_card(title, value, subtitle=""):
    """Renders a card specifically for highlighting a large metric."""
    html = f"""
    <div class="custom-card" style="text-align: center;">
        <h4 style="color: var(--text-secondary); margin-bottom: 0;">{title}</h4>
        <div class="metric-value">{value}</div>
        <p style="color: var(--text-secondary); font-size: 0.9rem;">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
