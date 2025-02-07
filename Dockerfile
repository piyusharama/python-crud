# Dockerfile
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the application port
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
