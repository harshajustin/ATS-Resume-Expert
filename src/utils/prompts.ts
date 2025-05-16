export const getPrompts = (userMode: 'Recruiter' | 'Student') => {
  if (userMode === 'Recruiter') {
    return {
      "Percentage Match": `Act as an ATS (Applicant Tracking System) scanner. Analyze the resume and job description to calculate the percentage match with strict accuracy.`,
      "Tell Me About the Resume": `Assume the role of a seasoned Technical Human Resource Manager with expertise in hiring for technical roles.`,
    };
  } else {
    return {
      "About the Resume": `Assume the role of a seasoned Technical Human Resource Manager with expertise in hiring for technical roles.`,
      "How Can I Improve My Skills": `As a career coach specializing in professional development and upskilling, analyze the provided resume and job description.`,
      "Percentage Match Resume vs Job Description": `Act as a highly accurate and analytical ATS (Applicant Tracking System) scanner.`,
      "Generate Cold Email": `Write a concise, professional, and persuasive cold email to the client regarding the specified job.`,
    };
  }
};