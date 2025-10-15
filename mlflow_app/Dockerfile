# Base image is pulled
FROM python:3

# Set the working directory inside the image
WORKDIR /usr/src/app 

# Files are copied from the host into the image
COPY . .

# Install dependencies, etc.
RUN pip install --no-cache-dir -r requirements.txt

# Which network ports the application inside the container will be listening on
EXPOSE 5000

CMD ["mlflow", "ui", "--host", "0.0.0.0", "--port", "5000"]

# Execute like this:
## sudo docker build -t ml-app .