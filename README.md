# AI Resume Analyzer Agent

A professional, modern, visually attractive, and fully functional AI-powered Resume Analyzer built with Streamlit and Gemini API.

## Features
- Drag-and-drop resume upload (PDF & DOCX)
- Automated Text Extraction
- AI Resume Analysis & ATS Score Generation
- Missing Skills Detection & Suggestions
- Job Match Percentage calculation
- Downloadable PDF Reports

## Installation

1. Clone or download this repository.
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download spaCy model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
5. Set up your `.env` file with your `GEMINI_API_KEY`.
6. Run the application:
   ```bash
   streamlit run app.py
   ```
