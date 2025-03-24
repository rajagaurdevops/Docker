# Use a specific Ubuntu version for consistency
FROM ubuntu:22.04

# Set working directory
WORKDIR /app

# Install Nginx and clean up unnecessary files
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy web files into the container
COPY default-test/ /var/www/html/

# Ensure correct permissions for Nginx
RUN chown -R www-data:www-data /var/www/html/

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
