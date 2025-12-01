This repository was created to demonstrate skills in machine learning deployment, specifically showing how a deployment is made using containers.

## What's new here?
- Modularized structure using Docker

## Objectives
- Show how to deploy a machine learning model using containers

## Steps
To make the project more similar to real-life problems, I split it into small tasks.
As the project progresses, I will add the time spent on each task. 

Total time spent:  3 hours and 56 minute
1. Planning how to make this project didactic: 52 minutes
2. Selection of artifacts from previous projects: 17 minutes
3. Testing the application locally: 9 minutes
4. Setting Docker requirements: 29 minutes
5. Configuring the network: 46 minutes
6. Running Docker application: 1 hour and 23 minutes

### Stucturing project
First you need to install the docker desktop on your machine.

Then you need to test it:
> docker --version

> sudo docker run hello-world

> sudo docker run -it ubuntu bash

If everything is fine, now we can start our prologue project.

For this prologue project we will create an docker aplication that will host the inference script of one of the [models que we created before](https://github.com/barrenha95/maturity_1_local_modularized_deploy).

### Setting up the docker container
First you need to create your dockerfile in your app project.
Then you need to configure it according to what you want to execute.

For this example I'm using the python image: https://hub.docker.com/_/python.

If you need more detailed explanations, you can look at the oficial docker docs https://docs.docker.com/get-started/workshop/02_our_app/.

### Building your app
After that build your docker image using:
> sudo docker build -t ml-app .

docker build: The command to start the build process.
-t ml-app: The -t stands for tag, which is just a name you give your image.
. (a single dot): It tells Docker to look for the Dockerfile in the current directory.

Then you execute your docker container:
> sudo docker run ml-app

If you want to check if it's running try on a new terminal window:
> sudo docker ps

And if you want to enter inside the shell you could use this command
> sudo docker exec -it <container_id_or_name> /bin/bash

> sudo docker exec -it a8f09ddf9ab3 /bin/bash

If Docker Desktop isn't opening:
> sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

> systemctl --user restart docker-desktop

### Running your app
The main command you need to run to start your docker container is:

> sudo docker run -d \
> --name inference-app-container \
> -p 8080:8080 \
> ml-app:latest 

-d → run detached (in the background).
--name inference-app-container → assign a human-readable name to the container.
-p 5000:5000 → map host port 5000 → container port 5000.
This means you can open http://localhost:5000 and access whatever service is running inside the container on port 5000.

ml-app (at the end) → the image name to run (previously built via docker build -t ml-app .)

You can check if the container is active
> sudo docker ps -a 

You can stop the docker app
> sudo docker stop $(docker ps -q)

- docker ps -q: Shows active containers with quiet mode (just bring the ids)
- docker stop: Command to stop containers
- $: executes the command inside the parentheses and substitutes its output into the outer command.


Manually remove container when it's stuck and you can see it using the sudo docker ps -a, an reset the docker
> sudo rm -rf /var/lib/docker/containers/e913eb258b5db65beb62e026bb59ac1eec073041d8d8410abd7eacae0089f151

> sudo systemctl restart docker

Next stop = Kubernetes☸ using tools like minikube or kind.
