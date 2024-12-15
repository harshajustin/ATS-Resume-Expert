import google.generativeai as genai

def get_gemini_response(input_text, pdf_content, prompt):
    """
    Sends the input text, PDF content, and prompt to the Gemini generative AI model.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
    except Exception as e:
        return f"Error generating response: {e}"
