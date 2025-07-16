# Use the latest lightweight Python base image
FROM python:3.12-slim-bookworm

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils \
    dnsutils \
    curl \
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

# Expose Streamlit's default port
EXPOSE 8501

# Health check - Check if Streamlit is responding
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/ || exit 1

# Optimized CMD for production
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true", "--server.enableCORS=false"]
