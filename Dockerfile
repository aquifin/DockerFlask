# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /api-flask

# Copy the necessary files and directories into the container
COPY . /api-flask

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
#CMD ["python", "app.py"]

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

