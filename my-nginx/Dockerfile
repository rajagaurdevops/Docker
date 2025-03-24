FROM nginx:latest

WORKDIR /app

# Copy web application files into the container
COPY . /usr/share/nginx/html


# Expose port 80 for http
EXPOSE 80

# start nginx
CMD [ "nginx", "-g", "daemon off" ]




