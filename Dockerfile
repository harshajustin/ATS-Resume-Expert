# Use the latest lightweight Python base image
FROM python:3.12-slim-bookworm

# Install system-level dependencies for PDF processing and web server
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils \
    dnsutils \
    curl \
    wget \
    fontconfig \
    fonts-dejavu-core \
    fonts-liberation \
    fonts-noto \
    libjpeg62-turbo-dev \
    libpng-dev \
    libfreetype6-dev \
    zlib1g-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Create necessary directories
RUN mkdir -p logs .streamlit

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source files
COPY . .

# Create a non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose the correct port
EXPOSE 8080

# Health check - Check if Streamlit is responding on the correct port
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1

# Optimized CMD for production
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true", "--server.enableCORS=true", "--server.enableXsrfProtection=false"]
