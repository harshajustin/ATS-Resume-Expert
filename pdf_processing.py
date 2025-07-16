import base64
import io
import pdf2image
import streamlit as st

def process_uploaded_pdf(uploaded_file):
    """
    Converts uploaded PDF into base64-encoded image parts for generative AI processing.
    Supports multi-page PDFs and provides better error handling.
    """
    if not uploaded_file:
        raise FileNotFoundError("No file uploaded.")
    
    try:
        # Show progress for large files
        with st.spinner("Processing PDF..."):
            # Convert PDF to images
            images = pdf2image.convert_from_bytes(
                uploaded_file.read(),
                dpi=200,  # Higher DPI for better quality
                first_page=1,
                last_page=3  # Limit to first 3 pages for performance
            )
            
            if not images:
                raise ValueError("Could not extract any pages from the PDF")
            
            first_page = images[0]
            
            # Convert the first page to a base64-encoded JPEG
            img_byte_arr = io.BytesIO()
            first_page.save(img_byte_arr, format="JPEG", quality=85)
            img_byte_arr = img_byte_arr.getvalue()
            
            # Process all pages for content analysis
            content_parts = []
            for i, img in enumerate(images[:2]):  # Limit to first 2 pages
                img_bytes = io.BytesIO()
                img.save(img_bytes, format="JPEG", quality=85)
                content_parts.append({
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_bytes.getvalue()).decode()
                })

            return {
                "images": images,
                "first_page": first_page,
                "content": content_parts,
                "page_count": len(images),
                "file_size": len(uploaded_file.getvalue()) if hasattr(uploaded_file, 'getvalue') else "Unknown"
            }
            
    except pdf2image.exceptions.PDFInfoNotInstalledError:
        raise ValueError("PDF processing tools not properly installed. Please contact support.")
    except Exception as e:
        raise ValueError(f"Error processing PDF: {str(e)}")

def validate_pdf_file(uploaded_file):
    """
    Validates the uploaded PDF file.
    """
    if not uploaded_file:
        return False, "No file uploaded"
    
    if uploaded_file.type != "application/pdf":
        return False, "File must be a PDF"
    
    # Check file size (limit to 10MB)
    if hasattr(uploaded_file, 'size') and uploaded_file.size > 10 * 1024 * 1024:
        return False, "File size must be less than 10MB"
    
    return True, "Valid PDF file"
