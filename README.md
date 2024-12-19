
# ATS Resume Expert

📑 **ATS Resume Expert** is a tool designed to optimize resumes for Applicant Tracking Systems (ATS) by analyzing job descriptions and providing professional feedback. It leverages generative AI to assess and provide suggestions for improving resumes, including how well they align with a given job description, suggestions to improve skills, and more.

## Features

- **ATS Analysis**: Compares resumes with job descriptions and provides an ATS match score.
- **Resume Review**: Evaluates resumes in the context of a job description and provides feedback on strengths and weaknesses.
- **Skills Improvement**: Suggests areas for skill enhancement and professional growth based on the resume and job description.
- **Cold Email Generation**: Generates professional cold emails to send to potential employers.
- **Resume Preview**: Provides a preview of the resume’s first page for easy review.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Running with Docker](#running-with-docker)
4. [Environment Variables](#environment-variables)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

### Requirements

- Python 3.10+
- Streamlit
- Google Generative AI API key (for GPT model interaction)
- Docker (for containerization)

### 1. Clone the Repository

```bash
https://github.com/harshajustin/ATS-Resume-Expert.git
cd ATS-Resume-Expert
```

### 2. Install Dependencies

Use a virtual environment to install the required dependencies.

```bash
pip install -r requirements.txt
```

### 3. Running the Application

Once dependencies are installed, you can start the Streamlit application:

```bash
streamlit run app.py
```

Visit [http://localhost:8501](http://localhost:8501) to interact with the application.

---

## Running with Docker

You can also run the application in a Docker container, which makes it easier to deploy and share the environment.

### 1. Build the Docker Image

Build the Docker image using the `Dockerfile` in the root directory:

```bash
docker build -t ats-resume-expert-container .
```

### 2. Run the Docker Container

Run the Docker container, mapping port `8501` for Streamlit:

```bash
docker run -p 8501:8501 ats-resume-expert-container
```

This will start the application inside a Docker container, and you can access it at [http://localhost:8501](http://localhost:8501).

---

## Environment Variables

The application requires a Google Generative AI API key to function properly. Set the API key as an environment variable in a `.env` file.

### Example `.env` file:

```env
key=YOUR_GOOGLE_GENERATIVE_AI_API_KEY
```

Ensure that this file is placed in the root directory of the project, as the application loads this key using `dotenv`.

---

## Contributing

We welcome contributions! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

### Steps to Contribute:

1. Fork the repository
2. Clone your fork
3. Create a new branch for your changes
4. Make your changes and commit them
5. Push the changes to your fork
6. Submit a pull request to the original repository

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

