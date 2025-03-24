# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set the working directory
WORKDIR /app

# Copy install.sh into the container
COPY install.sh /app/install.sh

# Make install.sh executable
RUN chmod +x /app/install.sh

# Run install.sh when the container starts
CMD ["/app/install.sh"]

