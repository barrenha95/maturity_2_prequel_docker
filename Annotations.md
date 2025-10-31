Project: Running model in docker

-- What is docker: 
-- Structuring project: 17 minutes + 9 minutes
-- Running: 48 minutes 
-- Writting article: 8 minutes

# What is docker?
- It's something like a Virtual Machine but instead of simulating the new environment, now you re-use your current environment, but "tricks" the system in a way that each application don't see what the other is using. The resources will be the same, but they will be in an ilusion that are different machines.

- Docker was created for Linux, so the best performance happens in Linux because it has to simulate less things and it will better the machine components

# Stucturing project
First you need to install the docker desktop on your machine.

The you need to test it:
- docker --version
- sudo docker run hello-world
- sudo docker run -it ubuntu bash

If everything is fine, now we can start our prologue project.

For this prologue project we will create an docker aplication that will host the inference script of one of the models que we created before.

Then using another terminal we will make an request.

# Setting up the docker container

First you need to create your dockerfile in your app project.
Then you need to configure it according to what you want to execute.
For this example I'm using the python image: https://hub.docker.com/_/python
If you need more detailed explanations, you can look at the oficial docker docs https://docs.docker.com/get-started/workshop/02_our_app/

After that build your docker image using:
sudo docker build -t ml-app .

docker build: The command to start the build process.
-t ml-app: The -t stands for tag, which is just a name you give your image.
. (a single dot): It tells Docker to look for the Dockerfile in the current directory.

Then you execute your docker container:
sudo docker run ml-app

If you want to check if it's running try on a new terminal window:
sudo docker ps

And if you want to enter inside the shell you could use this command
sudo docker exec -it <container_id_or_name> /bin/bash
sudo docker exec -it a8f09ddf9ab3 /bin/bash


FOR FUTURE ME:
- Create a new repository in the github, it will help you to create content and make it more organized
- Need to create an container for ML Flow and other for the inference


If Docker Desktop isn't opening:
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0
systemctl --user restart docker-desktop

sudo docker run -d \
  --name mlflow-app-container \
  -p 5000:5000 \
  -v /home/isabarrenha/Documents/Portfolio/maturity_2_prequel_docker/mlflow_app/mlruns:/usr/src/app/mlruns \
  mlflow-app \
  mlflow ui --host 0.0.0.0 --port 5000 --backend-store-uri file:///usr/src/app/mlruns --default-artifact-root /usr/src/app/mlruns


-d → run detached (in the background).
--name mlflow-app → assign a human-readable name to the container (you can refer to it later as mlflow-app).
-p 5000:5000 → map host port 5000 → container port 5000.
This means you can open http://localhost:5000 and access whatever service is running inside the container on port 5000.

mlflow-app (at the end) → the image name to run (previously built via docker build -t mlflow-app .).

sudo docker ps -a: Shows active containers

sudo docker stop $(docker ps -q): 
- docker ps -q: Shows active containers with quiet mode (just bring the ids)
- docker stop: Command to stop containers
- $: executes the command inside the parentheses and substitutes its output into the outer command.


sudo rm -rf /var/lib/docker/containers/54241b4bf64ba33261906b3cf1aacc1e49b50028e814afb07a60e76dd3c31bdc
sudo systemctl restart docker
manually remove container when it's stuck and you can see it using the sudo docker ps -a, an reset the docker
