# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade pip && pip install jupyter

# install jupyter kernel
RUN pip install -r requirements.txt

RUN python -m ipykernel install --user