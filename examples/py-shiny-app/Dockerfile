# Use the official Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the Shiny port
EXPOSE 3839

# Command to run the Shiny app with specified host and port
CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "3839"]
