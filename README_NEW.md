# 📑 ATS Resume Expert

A powerful AI-driven tool that helps optimize resumes for Applicant Tracking Systems (ATS) and provides professional feedback for job seekers and recruiters.

## ✨ Features

### For Students/Job Seekers:
- **Resume Analysis**: Comprehensive evaluation against job descriptions
- **Skill Improvement Suggestions**: Actionable advice for professional development
- **ATS Match Percentage**: Precise matching score with improvement areas
- **Cold Email Generator**: Professional outreach email templates

### For Recruiters:
- **Quick Resume Screening**: Efficient candidate evaluation
- **Match Percentage**: Accurate candidate-job fit assessment
- **Batch Processing**: Analyze multiple resumes simultaneously

## 🚀 Recent Improvements

### Enhanced User Experience
- **Interactive UI**: Modern, responsive design with better navigation
- **Progress Tracking**: Real-time processing status with progress bars
- **Error Handling**: Comprehensive error messages and recovery options
- **Multi-page PDF Support**: Analyze resumes with multiple pages

### Performance Optimizations
- **Rate Limiting**: Intelligent API quota management
- **Caching**: Improved response times for repeated analyses
- **File Validation**: Pre-processing validation for better reliability
- **Resource Management**: Optimized memory usage for large files

### Security & Monitoring
- **Logging System**: Comprehensive application monitoring
- **Error Tracking**: Detailed error reporting and analytics
- **Health Checks**: Container health monitoring
- **Security Hardening**: Non-root user execution in containers

## 🛠 Technology Stack

- **Frontend**: Streamlit
- **AI/ML**: Google Gemini 1.5 Flash
- **PDF Processing**: pdf2image, Pillow
- **Containerization**: Docker, Docker Compose
- **Languages**: Python 3.12+

## 📋 Prerequisites

- Docker and Docker Compose
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/harshajustin/ATS-Resume-Expert.git
cd ATS-Resume-Expert
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
key=your_google_gemini_api_key_here
```

### 3. Run with Docker Compose
```bash
docker-compose up --build
```

### 4. Access the Application
Open your browser and navigate to: `http://localhost:8501`

## 🔧 Configuration

### Environment Variables
- `key`: Google Gemini API key (required)
- `GOOGLE_API_KEY`: Alternative API key variable name
- `GEMINI_API_KEY`: Another alternative API key variable name

### API Rate Limits
- **Free Tier**: 15 requests per minute
- **Paid Tier**: Higher limits available ([Upgrade here](https://makersuite.google.com))

## 📖 Usage Guide

### For Job Seekers:
1. Select "Student/Job Seeker" mode
2. Paste the target job description
3. Upload your resume(s) in PDF format
4. Choose analysis type:
   - **About the Resume**: General assessment
   - **Skill Improvement**: Development recommendations
   - **Match Percentage**: ATS compatibility score
   - **Cold Email**: Professional outreach template

### For Recruiters:
1. Select "Recruiter" mode
2. Paste the job description
3. Upload candidate resumes
4. Choose analysis type:
   - **Percentage Match**: Quick compatibility assessment
   - **Resume Review**: Detailed candidate evaluation

## 🎯 Best Practices

### For Better Results:
- **Complete Job Descriptions**: Include all requirements, skills, and qualifications
- **Standard PDF Format**: Use text-based PDFs (avoid image-only documents)
- **File Size**: Keep files under 10MB for optimal processing
- **Multiple Versions**: Test different resume formats to compare results

### Performance Tips:
- Process resumes in smaller batches to avoid rate limits
- Use specific, detailed job descriptions for accurate matching
- Review and implement suggested improvements iteratively

## 🏗 Architecture

```
ATS-Resume-Expert/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and API setup
├── ui.py                 # User interface components
├── pdf_processing.py     # PDF handling and conversion
├── llm_integration.py    # AI/ML integration with rate limiting
├── prompts.py            # AI prompt templates
├── response_display.py   # Result formatting and display
├── logging_utils.py      # Logging and monitoring
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Service orchestration
└── .streamlit/          # Streamlit configuration
    └── config.toml
```

## 🔍 Monitoring & Logs

Application logs are automatically generated in the `logs/` directory with:
- User action tracking
- API usage monitoring
- Error reporting and analytics
- Performance metrics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/harshajustin/ATS-Resume-Expert/issues)
- **Documentation**: Check the [Wiki](https://github.com/harshajustin/ATS-Resume-Expert/wiki) for detailed guides
- **API Limits**: For rate limit issues, consider [upgrading your API plan](https://makersuite.google.com)

## 🙏 Acknowledgments

- Google Gemini AI for powerful language processing
- Streamlit for the amazing web app framework
- pdf2image for reliable PDF processing
- The open-source community for continuous inspiration

---

Made with ❤️ by [Harsha Justin](https://github.com/harshajustin)
