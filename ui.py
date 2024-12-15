import streamlit as st

from prompts import get_prompts

def create_streamlit_ui():
    """
    Creates the Streamlit interface for ATS Resume Expert.
    """
    st.set_page_config(page_title="ATS Resume Expert", layout="wide")
    st.title("📑 ATS Resume Expert")
    st.markdown(
        "Optimize your resume for Applicant Tracking Systems (ATS) and get professional feedback instantly."
    )

    user_mode = st.radio("Choose user:",["Recruiter","Student"],index=0)

    # Inputs
    input_text = st.text_area(
        "Job Description:",
        key="input",
        help="Paste the job description here for evaluation.",
        height=150
    )
    uploaded_files = st.file_uploader(
        "Upload Your Resumes (PDF format only, up to 10 files):",
        type=["pdf"],
        accept_multiple_files=True
    )

    return input_text, uploaded_files,user_mode
