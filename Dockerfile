# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install required Python libraries
RUN pip install pyfiglet colorama

# Copy your script into the container
COPY comrade_csrf_poc.py .

# Run the script
ENTRYPOINT ["python", "comrade_csrf_poc.py"]
