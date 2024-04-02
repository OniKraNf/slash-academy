# Use a Python base image
FROM python:3.12.1

# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the port
EXPOSE 8000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
