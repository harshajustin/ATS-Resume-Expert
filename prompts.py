def get_prompts(user_mode):
    """
    Return a set of prompts based on whether the user is a recruiter or student.
    """
    if user_mode == "Recruiter":
        return {
            "Percentage Match ": """
            Act as an ATS (Applicant Tracking System) scanner. Analyze the resume and job description to:  
            - Calculate the percentage match with strict accuracy.  
            - Display **only the percentage** match prominently.  
            - Highlight key areas where the resume aligns or falls short against the job description (skills, qualifications, keywords, etc.).  
            Be **extremely strict** in your evaluation, ensuring precise alignment of terms and context. Provide no unnecessary commentary;
            focus solely on the match percentage and critical points.  
            """,

            "Tell Me About the Resume": """
            Assume the role of a seasoned Technical Human Resource Manager with expertise in hiring for technical roles. 
            Carefully review the provided resume in the context of the job description. Identify and elaborate on:
            - The candidate's key strengths and qualifications relevant to the role.
            - Any gaps, weaknesses, or areas for improvement in meeting the job requirements.
            Provide a very concise and professional assessment to guide hiring decisions.
            """
        }
    else:  # For Student Mode
        return {
            "About the Resume": """
            Assume the role of a seasoned Technical Human Resource Manager with expertise in hiring for technical roles. 
            Carefully review the provided resume in the context of the job description. Identify and elaborate on:
            - The candidate's key strengths and qualifications relevant to the role.
            - Any gaps, weaknesses, or areas for improvement in meeting the job requirements.
            Provide a balanced and professional assessment to guide the candidate.
            """,
            "How Can I Improve My Skills": """
            As a career coach specializing in professional development and upskilling, analyze the provided resume and job description. 
            Offer actionable suggestions to enhance the candidate's profile, including:
            - Skills to acquire or improve.
            - Relevant certifications or training programs to pursue.
            - Experiences or projects to undertake that align with industry expectations.
            - Generate this response especially for student not .
            Tailor your advice to help the candidate stand out in their target field.
            """,
            "Percentage Match Resume vs Job Descripition": """
            Act as a highly accurate and analytical ATS (Applicant Tracking System) scanner. 
            Compare the resume against the job description and provide a detailed report, including:
            1. The percentage match between the resume and job requirements.
            2. A list of critical keywords or skills missing from the resume.
            3. Professional recommendations for optimizing the resume to improve alignment with the job description.
            Ensure your feedback is specific, actionable, and focused on maximizing the candidate's chances of selection.
            """,
            "Generate Cold Email": """
            Imagine you are a motivated and resourceful recent graduate eager to make a strong impression on potential employers. 
            Write a concise, professional, and persuasive cold email to the client regarding the specified job. 
            The email should:
            - Convey enthusiasm for the role and alignment with the company's goals.
            - Highlight relevant skills, academic background, and unique contributions.
            - Include personal details such as your full name, degree, and contact information.
            - Be structured, direct, and impactful, leaving a lasting positive impression.
            Tailor the tone to be both professional and approachable.
            """
        }
