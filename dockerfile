# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install required libraries
RUN pip install requests

# Run the script
CMD ["python", "analyzer.py"]