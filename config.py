from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables - try multiple paths
# For local development
load_dotenv()  # Look for .env in current directory
load_dotenv('.env')  # Explicitly look for .env file

# Configure generative AI
# Try multiple environment variable names for flexibility
API_KEY = os.getenv("key") or os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Google API Key not found. Please set it in the .env file.")

# Remove any quotes that might have been included
API_KEY = API_KEY.strip('"').strip("'")

genai.configure(api_key=API_KEY)
