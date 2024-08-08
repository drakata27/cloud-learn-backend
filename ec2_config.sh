#!/bin/bash

# Update the package list
sudo apt-get update

# Upgrade installed packages
sudo apt-get -y upgrade

# Install Docker
sudo apt-get install -y docker.io

# Enable Docker to start on boot
sudo systemctl enable docker

# Start Docker service
sudo systemctl start docker

# Pull the Docker image from Docker Hub
sudo docker pull drakata27/cloud-learn-backend:latest

# Run the Docker container
sudo docker run -d -p 8000:80 drakata27/cloud-learn-backend:latest