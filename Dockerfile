# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install --no-cache-dir scikit-learn
RUN pip install pandas   
RUN pip install flask
RUN pip install requests
RUN pip install matplotlib
# RUN pip install yaml


# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port Flask is running on
EXPOSE 5000

# Run the command to start the Flask server
CMD ["flask", "run", "--host=0.0.0.0"]
