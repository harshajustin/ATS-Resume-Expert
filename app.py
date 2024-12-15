import streamlit as st
from config import *
from pdf_processing import process_uploaded_pdf
from llm_integration import get_gemini_response
from prompts import get_prompts
from ui import create_streamlit_ui
from response_display import display_response, display_preview

def main():
    # Initialize session state variables if they are not already set
    if "results" not in st.session_state:
        st.session_state.results = {}

    if "fullscreen_preview" not in st.session_state:
        st.session_state.fullscreen_preview = None  # Tracks the resume to show in full screen
    

    # Create the UI
    input_text, uploaded_files,user_mode  = create_streamlit_ui()
    prompts = get_prompts(user_mode)
    # Buttons for user actions
    actions = list(prompts.keys())
    selected_action = st.radio("Choose an Action:", actions, horizontal=True)

    # Process files only when "Submit" button is clicked
    if st.button("Submit"):
        if uploaded_files:
            for file in uploaded_files[:10]:  # Limit to 10 files
                file_name = file.name
                if file_name not in st.session_state.results:
                    try:
                        pdf_data = process_uploaded_pdf(file)
                        st.session_state.results[file_name] = {
                            "pdf_data": pdf_data,
                            "responses": {}
                        }
                    except Exception as e:
                        st.session_state.results[file_name] = {"error": f"Error processing resume: {e}"}
                
                # Compute only for the selected action
                if selected_action not in st.session_state.results[file_name]["responses"]:
                    pdf_content = st.session_state.results[file_name]["pdf_data"]["content"]
                    response = get_gemini_response(input_text, pdf_content, prompts[selected_action])
                    st.session_state.results[file_name]["responses"][selected_action] = response
            
            st.success("Action processed successfully!")
        else:
            st.warning("Please upload resumes to proceed.")

    # Check if results are available for the selected action
    available_resumes = [
        file_name for file_name, data in st.session_state.results.items()
        if selected_action in data.get("responses", {})
    ]

    # Move the resume selection into the sidebar
    with st.sidebar:
        if available_resumes:
            selected_resume = st.selectbox("Select a Resume to View Results:", available_resumes)
        else:
            selected_resume = None  # No available resumes to display

    # Display results for the selected action only if outputs are processed
    if selected_resume:
        if "error" in st.session_state.results[selected_resume]:
            st.error(st.session_state.results[selected_resume]["error"])
        else:
            responses = st.session_state.results[selected_resume]["responses"]
            pdf_data = st.session_state.results[selected_resume]["pdf_data"]

            # Display preview and response
            display_preview(pdf_data, selected_resume)

            if selected_action in responses:
                display_response(f"Result for {selected_resume} ({selected_action}):", responses[selected_action])
    else:
        if st.session_state.results:
            st.info("No processed results available for the selected action. Please click 'Submit' to process resumes.")

if __name__ == "__main__":
    main()
