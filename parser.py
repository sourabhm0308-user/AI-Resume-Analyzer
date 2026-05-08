import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        raise ValueError("Please set a valid GEMINI_API_KEY in the .env file.")
    genai.configure(api_key=api_key)

def generate_with_fallback(prompt):
    """
    Attempts to generate content using available models.
    Automatically prioritizes 'flash' models (higher free tier quotas) 
    over 'pro' models, and automatically falls back if a Quota Exceeded (429) error occurs.
    """
    configure_gemini()
    models = list(genai.list_models())
    valid_models = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
    
    # Sort models: prefer 'flash', then anything else, put 'pro' models last
    valid_models.sort(key=lambda x: ('flash' not in x.lower(), 'pro' in x.lower(), x))
    
    last_error = None
    
    for model_name in valid_models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            error_str = str(e).lower()
            last_error = e
            # If we hit a quota limit, rate limit, or not found error, try the next model
            if 'quota' in error_str or '429' in error_str or '404' in error_str or '403' in error_str:
                continue
            else:
                # If it's a different kind of error, raise it immediately
                raise e
                
    raise Exception(f"All available models exhausted their quotas or failed. Last error: {last_error}")

def analyze_resume(resume_text, target_role="General"):
    """
    Analyzes the resume text against a target role using Gemini.
    Returns a parsed JSON dictionary containing the analysis.
    """
    prompt = f"""
    You are an expert ATS (Applicant Tracking System) and AI Resume Reviewer.
    I will provide you with the extracted text from a resume and a target job role.
    
    Target Role: {target_role}
    
    Resume Text:
    {resume_text}
    
    Analyze the resume thoroughly and provide the output EXACTLY as a valid JSON object with the following structure. Do not include any markdown formatting like ```json or ```, just the raw JSON string.

    {{
      "ats_score": <integer between 0 and 100>,
      "match_percentage": <integer between 0 and 100 representing how well it fits the Target Role>,
      "summary": "<A brief professional evaluation of the resume>",
      "strengths": ["<strength 1>", "<strength 2>", ...],
      "weaknesses": ["<weakness 1>", "<weakness 2>", ...],
      "detected_skills": ["<skill 1>", "<skill 2>", ...],
      "missing_skills": ["<missing skill 1 for the role>", "<missing skill 2>", ...],
      "suggestions": [
        {{
          "category": "<e.g., Formatting, Content, Impact>",
          "advice": "<Specific advice to improve>"
        }},
        ...
      ],
      "recommended_certifications": ["<cert 1>", "<cert 2>", ...]
    }}
    """
    
    try:
        response_text = generate_with_fallback(prompt)
        
        # Clean up potential markdown formatting
        text = response_text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        
        try:
            analysis_result = json.loads(text.strip())
            return analysis_result
        except json.JSONDecodeError as e:
            error_msg = f"JSON Decode Error: {e}. Raw Response: {text}"
            raise ValueError(error_msg)
            
    except Exception as e:
        raise e

def chat_with_resume(resume_text, chat_history, new_question):
    """
    Allows user to ask questions about their resume.
    """
    context = f"You are a helpful career advisor. Here is the user's resume:\n\n{resume_text}\n\n"
    
    # Construct conversation history
    history_prompt = context
    for msg in chat_history:
        role = "User" if msg["role"] == "user" else "Advisor"
        history_prompt += f"{role}: {msg['content']}\n"
    
    history_prompt += f"User: {new_question}\nAdvisor:"
    
    try:
        return generate_with_fallback(history_prompt)
    except Exception as e:
        return f"Error communicating with AI: {e}"
