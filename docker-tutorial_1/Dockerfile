# Use an official Python runtime as a parent image
FROM python:3
# Set the working directory to /app
WORKDIR /opt/app

# Copy the current directory contents into the container at /app
ADD . /opt/app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt&& \
    pip install merlinwf
