import streamlit as st

# Initialize session state for full-screen preview if not already set
if "fullscreen_preview" not in st.session_state:
    st.session_state.fullscreen_preview = None

def display_response1(title, response):
    """
    Displays the AI-generated response in the Streamlit app.
    """
    st.subheader(title)
    if response:
        if "Email" in title:
            st.code(response, language="text")
        else:
            st.write(response)
    else:
        st.error("No response received from the AI model.")

def display_preview1(pdf_data, selected_resume):
    """
    Displays resume preview in full screen or sidebar.
    """
    # Sidebar preview
    with st.sidebar:
        st.image(
            pdf_data["first_page"], 
            caption=f"Preview of {selected_resume}", 
            use_container_width=True
        )
        # Full-screen preview button
        if st.button("Show Full-Screen Preview"):
            st.session_state.fullscreen_preview = selected_resume
    
    # Full-screen preview in main app area
    if st.session_state.fullscreen_preview == selected_resume:
        st.image(
            pdf_data["first_page"],
            caption=f"Full-Screen Preview of {selected_resume}",
            use_container_width=True
        )
        if st.button("Close Full-Screen Preview"):
            st.session_state.fullscreen_preview = None

# Example usage
# Replace `pdf_data` and `selected_resume` with your actual data
pdf_data = {"first_page": "path/to/image_or_placeholder.png"}
selected_resume = "Resume 1"

st.title("Resume Preview App")
display_preview(pdf_data, selected_resume)
