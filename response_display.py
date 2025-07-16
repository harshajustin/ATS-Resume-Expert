import streamlit as st
import re
try:
    from pdf_generator import create_pdf_response, create_multi_analysis_pdf
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

def display_response(title, response):
    """
    Displays the AI-generated response with enhanced formatting.
    """
    st.markdown(f"### {title}")
    
    if not response:
        st.error("❌ No response received from the AI model.")
        return
    
    # Check for rate limiting or error messages
    if any(keyword in response.lower() for keyword in ["rate limit", "quota", "error", "wait"]):
        st.warning(f"⚠️ {response}")
        return
    
    # Format different types of responses
    if "email" in title.lower():
        st.markdown("#### 📧 Generated Cold Email:")
        st.code(response, language="text")
        
        # Add copy button functionality
        if st.button("📋 Copy Email", key=f"copy_{title}"):
            st.success("Email copied to clipboard! (Use Ctrl+C/Cmd+C)")
            
    elif "percentage" in title.lower() or "match" in title.lower():
        # Extract percentage if present
        percentage_match = re.search(r'(\d+)%', response)
        if percentage_match:
            percentage = int(percentage_match.group(1))
            
            # Color-coded percentage display
            if percentage >= 80:
                color = "green"
                status = "Excellent Match! 🎯"
            elif percentage >= 60:
                color = "orange" 
                status = "Good Match 👍"
            else:
                color = "red"
                status = "Needs Improvement 📈"
                
            st.markdown(f"""
            <div style="padding: 1rem; border-radius: 10px; background-color: #{color}20; border-left: 5px solid {color};">
                <h2 style="color: {color}; margin: 0;">{percentage}% Match</h2>
                <p style="margin: 0.5rem 0 0 0; font-weight: bold;">{status}</p>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("#### 📊 Detailed Analysis:")
        st.write(response)
        
    else:
        # Regular response formatting
        st.write(response)
    
    # Add download options for responses
    col1, col2 = st.columns(2)
    
    with col1:
        # PDF Download (preferred)
        if PDF_AVAILABLE:
            try:
                pdf_data, pdf_filename = create_pdf_response(title, response)
                st.download_button(
                    label="📄 Download as PDF",
                    data=pdf_data,
                    file_name=pdf_filename,
                    mime="application/pdf",
                    key=f"download_pdf_{title}"
                )
            except Exception as e:
                st.error(f"PDF generation failed: {str(e)}")
                # Fallback to text download
                st.download_button(
                    label="� Download as Text",
                    data=response,
                    file_name=f"{title.replace(' ', '_')}_response.txt",
                    mime="text/plain",
                    key=f"download_txt_{title}"
                )
        else:
            st.download_button(
                label="📄 Download as Text",
                data=response,
                file_name=f"{title.replace(' ', '_')}_response.txt",
                mime="text/plain",
                key=f"download_txt_{title}"
            )
    
    with col2:
        # Text Download (backup option)
        if PDF_AVAILABLE:
            st.download_button(
                label="📝 Download as Text",
                data=response,
                file_name=f"{title.replace(' ', '_')}_response.txt",
                mime="text/plain",
                key=f"download_txt_backup_{title}"
            )

def display_preview(pdf_data, selected_resume):
    """
    Enhanced resume preview with better navigation.
    """
    # Sidebar preview with file info
    with st.sidebar:
        st.markdown("### 📄 Resume Preview")
        
        # File information
        if "page_count" in pdf_data:
            st.info(f"📑 Pages: {pdf_data['page_count']}")
        if "file_size" in pdf_data:
            st.info(f"📏 Size: {pdf_data['file_size']} bytes")
        
        # Thumbnail preview
        st.image(
            pdf_data["first_page"], 
            caption=f"Preview: {selected_resume}", 
            use_container_width=True
        )
        
        # Control buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔍 Full View", use_container_width=True):
                st.session_state.fullscreen_preview = selected_resume
        with col2:
            if st.button("❌ Close", use_container_width=True):
                st.session_state.fullscreen_preview = None
            
    # Full-screen preview in main area
    if st.session_state.fullscreen_preview == selected_resume:
        st.markdown("### 🔍 Full-Screen Preview")
        
        # Page navigation for multi-page PDFs
        if len(pdf_data["images"]) > 1:
            page_num = st.selectbox(
                "Select page:",
                range(1, len(pdf_data["images"]) + 1),
                format_func=lambda x: f"Page {x}"
            )
            selected_image = pdf_data["images"][page_num - 1]
        else:
            selected_image = pdf_data["first_page"]
            
        st.image(
            selected_image,
            caption=f"Full View: {selected_resume}",
            use_container_width=True
        )

def create_summary_dashboard(results):
    """
    Creates a summary dashboard of all processed resumes.
    """
    if not results:
        return
        
    st.markdown("### 📊 Processing Summary")
    
    total_resumes = len(results)
    processed_resumes = sum(1 for data in results.values() if "responses" in data and data["responses"])
    error_count = sum(1 for data in results.values() if "error" in data)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Resumes", total_resumes)
    with col2:
        st.metric("Successfully Processed", processed_resumes)
    with col3:
        st.metric("Errors", error_count)
        
    if error_count > 0:
        st.warning(f"⚠️ {error_count} resume(s) had processing errors. Check individual results for details.")

def display_download_options(all_responses, resume_name="Resume"):
    """
    Displays enhanced download options for all analyses.
    
    Args:
        all_responses (dict): Dictionary containing all analysis responses
        resume_name (str): Name of the resume being analyzed
    """
    if not all_responses:
        return
    
    st.markdown("### 📥 Download Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📄 Complete Analysis")
        if PDF_AVAILABLE:
            try:
                # Filter out empty responses
                valid_responses = {k: v for k, v in all_responses.items() if v and v.strip()}
                
                if valid_responses:
                    pdf_data, pdf_filename = create_multi_analysis_pdf(
                        valid_responses, 
                        f"{resume_name}_Complete_Analysis"
                    )
                    st.download_button(
                        label="📋 Download Complete Analysis (PDF)",
                        data=pdf_data,
                        file_name=pdf_filename,
                        mime="application/pdf",
                        key="download_complete_pdf",
                        help="Download all analyses in a single, professionally formatted PDF"
                    )
                else:
                    st.info("No completed analyses to download.")
                    
            except Exception as e:
                st.error(f"PDF generation failed: {str(e)}")
        else:
            st.warning("PDF generation not available. Please install reportlab.")
    
    with col2:
        st.markdown("#### 📝 Individual Downloads")
        st.info("Use the download buttons below each analysis section for individual results.")
        
        # Show summary of available downloads
        valid_count = sum(1 for v in all_responses.values() if v and v.strip())
        if valid_count > 0:
            st.success(f"✅ {valid_count} analysis result(s) available for download")
        else:
            st.warning("No completed analyses available")

