
# 🎯 ATS Resume Expert

<div align="center">

![ATS Resume Expert](https://img.shields.io/badge/ATS-Resume%20Expert-blue?style=for-the-badge&logo=resume&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AI](https://img.shields.io/badge/AI-Powered-green?style=for-the-badge&logo=openai&logoColor=white)

**A powerful AI-driven tool to optimize resumes for Applicant Tracking Systems (ATS) and enhance job application success rates.**

[🎥 Watch Demo](https://www.linkedin.com/posts/harsha-vardhan-027413304_resumewriting-jobsearch-ai-activity-7275429042898587648-sjQe?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEB8Te0BMkMgzs1xBYmT-I1uI87qQrQ5dvU) • [📚 Documentation](#documentation) • [🚀 Live Demo](https://resume.edulearn.studio/)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🔧 Technologies Used](#-technologies-used)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🐳 Docker Deployment](#-docker-deployment)
- [☁️ Cloud Deployment](#️-cloud-deployment)
- [🔑 Environment Variables](#-environment-variables)
- [📖 Usage Guide](#-usage-guide)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

---

## ✨ Features

### 🎯 **Core Functionality**
- **📊 ATS Score Analysis**: Get detailed compatibility scores between your resume and job descriptions
- **🔍 Resume Review**: Comprehensive evaluation with AI-powered feedback and suggestions
- **🎓 Skills Enhancement**: Personalized recommendations for professional growth
- **📧 Cold Email Generator**: Professional outreach emails tailored to specific roles
- **📄 PDF Export**: Download analysis reports in professional PDF format
- **🖼️ Resume Preview**: Visual preview of your resume's first page

### 🤖 **AI-Powered Insights**
- **Smart Matching**: Advanced algorithms to match resume content with job requirements
- **Keyword Optimization**: Identify and suggest relevant keywords for better ATS performance
- **Industry-Specific Analysis**: Tailored feedback based on job roles and industries
- **Real-time Processing**: Instant analysis and feedback generation

### 🎨 **User Experience**
- **Intuitive Interface**: Clean, professional Streamlit-based UI
- **Responsive Design**: Optimized for desktop and mobile devices
- **Multi-format Support**: Supports PDF, DOC, and DOCX resume formats
- **Progress Tracking**: Visual indicators for analysis progress

---

## 🔧 Technologies Used

<div align="center">

| Category | Technologies |
|----------|-------------|
| **Frontend** | Streamlit, HTML, CSS |
| **Backend** | Python 3.10+ |
| **AI/ML** | Google Generative AI (Gemini) |
| **Document Processing** | PyPDF2, python-docx, Pillow |
| **PDF Generation** | ReportLab |
| **Deployment** | Docker, DigitalOcean |
| **Environment** | python-dotenv |

</div>

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10 or higher
- Google Generative AI API key
- Git (for cloning the repository)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/harshajustin/ATS-Resume-Expert.git
cd ATS-Resume-Expert
```

### 2️⃣ Set Up Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```env
key=YOUR_GOOGLE_GENERATIVE_AI_API_KEY
```

### 4️⃣ Run the Application
```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) to access the application.

---

## 📦 Installation

### System Requirements
- **Operating System**: Windows 10+, macOS 10.15+, or Linux
- **Python**: 3.10 or higher
- **Memory**: 4GB RAM minimum, 8GB recommended
- **Storage**: 1GB free space

### Detailed Installation Steps

1. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install System Dependencies** (Linux/macOS)
   ```bash
   # For PDF processing
   sudo apt-get install poppler-utils  # Ubuntu/Debian
   # or
   brew install poppler  # macOS
   ```

3. **Verify Installation**
   ```bash
   python -c "import streamlit; print('Streamlit version:', streamlit.__version__)"
   ```

---

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)
```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in detached mode
docker-compose up -d
```

### Manual Docker Commands
```bash
# Build the Docker image
docker build -t ats-resume-expert .

# Run the container
docker run -p 8080:8080 
  -e key=YOUR_GOOGLE_GENERATIVE_AI_API_KEY 
  ats-resume-expert
```

### Docker Image Details
- **Base Image**: `python:3.12-slim-bookworm`
- **Exposed Port**: 8080
- **Health Check**: Configured with 30s intervals
- **Security**: Runs as non-root user

---

## ☁️ Cloud Deployment

### DigitalOcean App Platform

1. **Fork this repository** to your GitHub account

2. **Connect to DigitalOcean**:
   - Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)
   - Create a new app from GitHub
   - Select your forked repository

3. **Configure Environment Variables**:
   ```
   key=YOUR_GOOGLE_GENERATIVE_AI_API_KEY
   ```

4. **Deploy Settings**:
   - **Build Command**: Auto-detected (Dockerfile)
   - **Run Command**: Auto-detected
   - **Port**: 8080
   - **Health Check**: Enabled

### Alternative Deployment Options
- **Heroku**: Use the provided `Dockerfile`
- **AWS ECS**: Container-ready deployment
- **Google Cloud Run**: Serverless container deployment
- **Azure Container Instances**: Quick container deployment

---

## 🔑 Environment Variables

### Required Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `key` | Google Generative AI API key | `AIzaSyC...` |

### Optional Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `STREAMLIT_SERVER_PORT` | Server port | `8080` |
| `STREAMLIT_SERVER_ADDRESS` | Server address | `0.0.0.0` |

### Getting Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key to your `.env` file

---

## 📖 Usage Guide

### Step-by-Step Process

1. **📄 Upload Resume**
   - Drag and drop your resume file (PDF, DOC, DOCX)
   - Wait for the file to be processed

2. **📝 Enter Job Description**
   - Copy and paste the job description
   - Ensure it contains key requirements and qualifications

3. **🔍 Choose Analysis Type**
   - **ATS Score**: Get compatibility percentage
   - **Resume Review**: Detailed feedback and suggestions
   - **Skills Improvement**: Enhancement recommendations
   - **Cold Email**: Generate professional outreach emails

4. **📊 Review Results**
   - Read through AI-generated insights
   - Download PDF reports for future reference
   - Implement suggested improvements

### Pro Tips
- **Use specific job descriptions** for better analysis
- **Update your resume** based on feedback before applying
- **Save PDF reports** to track improvements over time
- **Test multiple job descriptions** to optimize for different roles

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Report Bugs**: Create detailed issue reports
- 💡 **Suggest Features**: Propose new functionality
- 📝 **Improve Documentation**: Help others understand the project
- 🔧 **Submit Code**: Fix bugs or add features

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Run tests: `pytest tests/`
5. Submit a pull request

### Code Standards
- Follow PEP 8 style guidelines
- Add docstrings to functions
- Write tests for new features
- Update documentation as needed

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ **Commercial use allowed**
- ✅ **Modification allowed**
- ✅ **Distribution allowed**
- ✅ **Private use allowed**
- ❌ **No warranty provided**

---

## 👨‍💻 Author

<div align="center">

**Harsha Vardhan**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harsha-vardhan-027413304/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/harshajustin)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)

*Passionate about AI-driven solutions for career development and job search optimization.*

</div>

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ by [Harsha Vardhan](https://github.com/harshajustin)

</div>




