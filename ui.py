import streamlit as st
from pdf_processing import validate_pdf_file

def create_streamlit_ui():
    """
    Creates the Streamlit interface for ATS Resume Expert with enhanced UI.
    """
    st.set_page_config(
        page_title="ATS Resume Expert",
        page_icon="📑",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Header with better styling
    st.title("📑 ATS Resume Expert")
    st.markdown(
        """
        <div style="padding: 1rem; background-color: #f0f2f6; border-radius: 10px; margin-bottom: 2rem;">
            <h4 style="color: #1f77b4; margin: 0;">🎯 Optimize your resume for Applicant Tracking Systems</h4>
            <p style="margin: 0.5rem 0 0 0; color: #666;">Get professional feedback instantly and improve your job application success rate.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # User mode selection with better styling
    st.markdown("### 👤 Select Your Role")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎯 Recruiter", use_container_width=True):
            st.session_state.user_mode = "Recruiter"
    
    with col2:
        if st.button("🎓 Student/Job Seeker", use_container_width=True):
            st.session_state.user_mode = "Student"
    
    # Initialize user mode if not set
    if "user_mode" not in st.session_state:
        st.session_state.user_mode = "Student"
    
    st.info(f"Current mode: **{st.session_state.user_mode}**")

    # Job description input with better UX
    st.markdown("### 📝 Job Description")
    input_text = st.text_area(
        "Paste the job description here:",
        key="input",
        help="Provide a detailed job description for accurate resume analysis",
        height=150,
        placeholder="Copy and paste the job description you want to match your resume against..."
    )

    # Resume upload with validation
    st.markdown("### 📄 Upload Resumes")
    uploaded_files = st.file_uploader(
        "Choose PDF files (up to 10 files, max 10MB each):",
        type=["pdf"],
        accept_multiple_files=True,
        help="Upload your resume files in PDF format for analysis"
    )

    # File validation and display
    if uploaded_files:
        valid_files = []
        for file in uploaded_files:
            is_valid, message = validate_pdf_file(file)
            if is_valid:
                valid_files.append(file)
                st.success(f"✅ {file.name} - {message}")
            else:
                st.error(f"❌ {file.name} - {message}")
        
        uploaded_files = valid_files

    # Usage tips
    with st.expander("💡 Tips for Better Results"):
        st.markdown("""
        - **Job Description**: Include complete job requirements, skills, and qualifications
        - **Resume Format**: Use standard PDF format with clear text (avoid image-only PDFs)
        - **File Size**: Keep files under 10MB for faster processing
        - **Multiple Resumes**: Upload different versions to compare results
        - **Rate Limits**: Free tier allows 15 requests per minute
        """)

    return input_text, uploaded_files, st.session_state.user_mode
