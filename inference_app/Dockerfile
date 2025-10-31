# Base image is pulled
FROM python:3

# Set the working directory inside the image
WORKDIR /usr/src/app 

# Files are copied from the host into the image
COPY /home/isabarrenha/Documents/Portfolio/MATURITY_2_PREQUEL_DOCKER/inference_app .

# Install dependencies, etc.
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run when the container starts
CMD [ "python", "./app.py" ]

# Which network ports the application inside the container will be listening on
EXPOSE 8080

# Execute like this:
## sudo docker build -t ml-app .