import os
import io
import PyPDF2
import pdfplumber
import docx

def extract_text_from_pdf(file_bytes):
    """
    Extract text from a PDF file.
    Tries pdfplumber first for better layout parsing, falls back to PyPDF2.
    """
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"pdfplumber failed: {e}. Falling back to PyPDF2.")
        try:
            reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e2:
            print(f"PyPDF2 failed: {e2}")
            return None
    
    return text.strip()

def extract_text_from_docx(file_bytes):
    """
    Extract text from a DOCX file.
    """
    try:
        doc = docx.Document(io.BytesIO(file_bytes))
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        print(f"Error extracting from DOCX: {e}")
        return None

def parse_resume(uploaded_file):
    """
    Determine file type and extract text.
    """
    if uploaded_file is None:
        return None
    
    file_type = uploaded_file.name.split('.')[-1].lower()
    file_bytes = uploaded_file.read()
    
    if file_type == 'pdf':
        return extract_text_from_pdf(file_bytes)
    elif file_type in ['doc', 'docx']:
        return extract_text_from_docx(file_bytes)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")
