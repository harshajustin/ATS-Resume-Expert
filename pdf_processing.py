import base64
import io
import pdf2image

def process_uploaded_pdf(uploaded_file):
    """
    Converts uploaded PDF into base64-encoded image parts for generative AI processing.
    """
    if not uploaded_file:
        raise FileNotFoundError("No file uploaded.")
    try:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        # Convert the first page to a base64-encoded JPEG
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        return {
            "images": images,  # Store all pages as images
            "first_page": first_page,
            "content": [{
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }]
        }
    except Exception as e:
        raise ValueError(f"Error processing PDF: {e}")
