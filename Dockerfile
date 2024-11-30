# Use a Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy code and dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8080 for the app
EXPOSE 8080

# Start the Flask app
CMD ["python", "app.py"]
