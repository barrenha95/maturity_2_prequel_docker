# Base image is pulled
FROM python:3.13-slim 

# Set the working directory inside the image
WORKDIR /usr/src/app 

# Files are copied from the host into the image
COPY . .

# Install dependencies, etc.
RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    build-essential \
    python3-dev 
    
# Set environment variables so PyArrow can find the installed C++ libraries    
ENV ARROW_HOME=/usr
ENV LD_LIBRARY_PATH=/usr/lib
ENV PYARROW_BUNDLE_ARROW_CPP=on
ENV PYARROW_BUNDLE_CYTHON_CPP=on

RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run when the container starts
CMD [ "python", "./app.py" ]

# Which network ports the application inside the container will be listening on
EXPOSE 8080

# Execute like this:
## sudo docker build -t ml-app .
