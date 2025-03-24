# Use Ubuntu as the base image
FROM ubuntu:latest

# Set working directory
WORKDIR /app

# Set the maintainer information (optional)
LABEL maintainer="devops@example.com"

# Update package list and install Nginx
RUN apt-get update && apt-get install -y nginx

# Copy web files into the container
COPY default-test/ /var/www/html/

# Expose port 80 for HTTP
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

