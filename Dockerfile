FROM python:3.11-slim AS builder

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libffi-dev \
    build-essential \
    python3-dev \
    cython3 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a smaller final runtime image
FROM python:3.11-slim

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local /usr/local

# Set the working directory
WORKDIR /app

# Copy application source code
COPY . .

# Expose the application port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
