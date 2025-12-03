import google.generativeai as genai
import os
import time
from dotenv import load_dotenv

# Rate limiting variables
last_request_time = 0
request_count = 0
RATE_LIMIT = 14  # Stay under 15 requests per minute
RATE_WINDOW = 60  # 60 seconds

def rate_limit_check():
    """Check and enforce rate limiting"""
    global last_request_time, request_count
    
    current_time = time.time()
    
    # Reset counter if a minute has passed
    if current_time - last_request_time >= RATE_WINDOW:
        request_count = 0
        last_request_time = current_time
    
    # If we've hit the limit, wait
    if request_count >= RATE_LIMIT:
        wait_time = RATE_WINDOW - (current_time - last_request_time)
        if wait_time > 0:
            return f"Rate limit reached. Please wait {wait_time:.1f} seconds before trying again."
    
    request_count += 1
    return None

def get_gemini_response(input_text, pdf_content, prompt):
    """
    Sends the input text, PDF content, and prompt to the Gemini generative AI model.
    """
    try:
        # Check rate limiting first
        rate_limit_error = rate_limit_check()
        if rate_limit_error:
            return rate_limit_error
        
        # Ensure environment variables are loaded
        load_dotenv()
        api_key = os.getenv("key")
        
        if not api_key:
            return "Error: API key not found in environment variables."
        
        # Remove any quotes and configure
        api_key = api_key.strip('"').strip("'")
        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "quota" in error_msg.lower():
            return "⚠️ Rate limit exceeded. Please wait a moment and try again. Consider upgrading to a paid plan for higher limits."
        return f"Error generating response: {e}"
