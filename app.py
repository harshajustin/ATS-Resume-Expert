import streamlit as st
from config import *
from pdf_processing import process_uploaded_pdf
from llm_integration import get_gemini_response
from prompts import get_prompts
from ui import create_streamlit_ui
from response_display import display_response, display_preview, create_summary_dashboard, display_download_options
import time

def main():
    """
    Main application function with enhanced error handling and user experience.
    """
    # Initialize session state variables
    if "results" not in st.session_state:
        st.session_state.results = {}
    if "fullscreen_preview" not in st.session_state:
        st.session_state.fullscreen_preview = None
    if "processing_complete" not in st.session_state:
        st.session_state.processing_complete = False

    # Create the UI
    input_text, uploaded_files, user_mode = create_streamlit_ui()
    
    # Validation
    if not input_text.strip() and uploaded_files:
        st.warning("⚠️ Please provide a job description for accurate analysis.")
    
    # Get prompts based on user mode
    prompts = get_prompts(user_mode)
    actions = list(prompts.keys())
    
    # Action selection with better UI
    st.markdown("### 🎯 Choose Analysis Type")
    selected_action = st.radio("", actions, horizontal=True)

    # Process files only when "Submit" button is clicked
    if st.button("🚀 Analyze Resumes", type="primary", use_container_width=True):
        if not uploaded_files:
            st.error("❌ Please upload at least one resume file.")
            return
            
        if not input_text.strip():
            st.error("❌ Please provide a job description.")
            return

        # Reset processing state
        st.session_state.processing_complete = False
        
        # Show processing info
        st.info("ℹ️ **Free Tier Info**: 15 requests per minute. Processing may be slower to avoid rate limits.")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        total_files = len(uploaded_files)
        processed_files = 0
        
        for i, file in enumerate(uploaded_files[:10]):  # Limit to 10 files
            file_name = file.name
            status_text.text(f"Processing {file_name}... ({i+1}/{total_files})")
            
            # Process PDF if not already processed
            if file_name not in st.session_state.results:
                try:
                    with st.spinner(f"Extracting content from {file_name}..."):
                        pdf_data = process_uploaded_pdf(file)
                        st.session_state.results[file_name] = {
                            "pdf_data": pdf_data,
                            "responses": {}
                        }
                except Exception as e:
                    st.error(f"❌ Error processing {file_name}: {str(e)}")
                    st.session_state.results[file_name] = {"error": f"Error processing resume: {e}"}
                    continue
            
            # Generate AI response for the selected action
            if (file_name in st.session_state.results and 
                "responses" in st.session_state.results[file_name] and
                selected_action not in st.session_state.results[file_name]["responses"]):
                
                try:
                    with st.spinner(f"Analyzing {file_name} with AI..."):
                        pdf_content = st.session_state.results[file_name]["pdf_data"]["content"]
                        response = get_gemini_response(input_text, pdf_content, prompts[selected_action])
                        st.session_state.results[file_name]["responses"][selected_action] = response
                        
                        # Check for rate limiting
                        if any(keyword in response.lower() for keyword in ["rate limit", "wait", "quota"]):
                            st.warning(f"⚠️ Rate limit reached for {file_name}. {response}")
                            break
                            
                except Exception as e:
                    st.error(f"❌ AI analysis failed for {file_name}: {str(e)}")
                    st.session_state.results[file_name]["responses"][selected_action] = f"Error: {str(e)}"
            
            processed_files += 1
            progress_bar.progress(processed_files / total_files)
        
        # Complete processing
        progress_bar.progress(1.0)
        status_text.text("✅ Processing complete!")
        st.session_state.processing_complete = True
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()
        
        st.success("🎉 Analysis completed successfully!")

    # Display summary dashboard
    if st.session_state.results:
        create_summary_dashboard(st.session_state.results)

    # Resume selection and results display
    available_resumes = [
        file_name for file_name, data in st.session_state.results.items()
        if "responses" in data and selected_action in data.get("responses", {})
    ]

    # Sidebar for resume selection
    with st.sidebar:
        st.markdown("### 📋 Resume Selection")
        if available_resumes:
            selected_resume = st.selectbox(
                "Choose a resume to view results:",
                available_resumes,
                help="Select a resume to view its analysis results"
            )
        else:
            selected_resume = None
            if st.session_state.results:
                st.info("No results available for the selected analysis type. Click 'Analyze Resumes' to process.")
            else:
                st.info("Upload resumes and run analysis to see results here.")

    # Display results for selected resume
    if selected_resume:
        if "error" in st.session_state.results[selected_resume]:
            st.error(f"❌ {st.session_state.results[selected_resume]['error']}")
        else:
            responses = st.session_state.results[selected_resume]["responses"]
            pdf_data = st.session_state.results[selected_resume]["pdf_data"]

            # Display preview and response
            display_preview(pdf_data, selected_resume)

            if selected_action in responses:
                display_response(
                    f"📊 {selected_action} - {selected_resume}", 
                    responses[selected_action]
                )
                
                # Add download options for all completed analyses
                display_download_options(responses, selected_resume)
            else:
                st.info("🔄 Click 'Analyze Resumes' to generate analysis for this resume.")

if __name__ == "__main__":
    main()
