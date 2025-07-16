import logging
import streamlit as st
from datetime import datetime
import os

# Configure logging
def setup_logging():
    """Setup logging configuration for the application."""
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'{log_dir}/ats_app_{datetime.now().strftime("%Y%m%d")}.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

def log_user_action(action, user_mode, file_count=0, success=True):
    """Log user actions for monitoring and analytics."""
    logger = logging.getLogger(__name__)
    
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "user_mode": user_mode,
        "file_count": file_count,
        "success": success,
        "session_id": st.session_state.get("session_id", "unknown")
    }
    
    if success:
        logger.info(f"User action completed: {log_data}")
    else:
        logger.error(f"User action failed: {log_data}")

def log_api_usage(model_used, tokens_estimated=0, response_time=0):
    """Log API usage for cost monitoring."""
    logger = logging.getLogger(__name__)
    
    usage_data = {
        "timestamp": datetime.now().isoformat(),
        "model": model_used,
        "estimated_tokens": tokens_estimated,
        "response_time_seconds": response_time,
        "session_id": st.session_state.get("session_id", "unknown")
    }
    
    logger.info(f"API usage: {usage_data}")

def handle_error(error, context="Unknown"):
    """Centralized error handling and logging."""
    logger = logging.getLogger(__name__)
    
    error_data = {
        "timestamp": datetime.now().isoformat(),
        "error_type": type(error).__name__,
        "error_message": str(error),
        "context": context,
        "session_id": st.session_state.get("session_id", "unknown")
    }
    
    logger.error(f"Application error: {error_data}")
    
    # User-friendly error display
    if "rate limit" in str(error).lower() or "quota" in str(error).lower():
        return "⚠️ API rate limit reached. Please wait a moment before trying again."
    elif "api key" in str(error).lower():
        return "🔑 API configuration issue. Please check your setup."
    elif "pdf" in str(error).lower():
        return "📄 PDF processing error. Please ensure your file is a valid PDF."
    else:
        return f"❌ An error occurred: {str(error)}"
