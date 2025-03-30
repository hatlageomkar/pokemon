# Use Alpine Linux as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the script to the container
COPY pokemon.py .

# Install any required dependencies
RUN pip install requests

# Define the command to run the script
ENTRYPOINT ["python", "pokemon.py"]
