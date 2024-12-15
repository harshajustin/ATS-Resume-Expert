import streamlit as st

def display_response(title, response):
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

def display_preview(pdf_data, selected_resume):
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
    
        if st.button("Close Full-Screen Preview"):
            st.session_state.fullscreen_preview = None
            
    # Full-screen preview in main app area
    if st.session_state.fullscreen_preview == selected_resume:
        st.image(
            pdf_data["first_page"],
            caption=f"Full-Screen Preview of {selected_resume}",
            use_container_width=True
        )
        
