# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Run Uvicorn and tell it to import the app object from main
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]