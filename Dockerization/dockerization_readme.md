## To dockerize our python application we need;

- A Dockerfile (Docker Image) consisting all instruction to build a container
- All scripts and related files of our application
- A requirements.txt file which list down all library and packages used in a python application

## How to create a dockerfile

Dockerfile is bascially a set of instruction of replicating the enviroment needed to run your python application. So to create that we first need a base Image which is nothing but an OS user space minus the kernel.

So here is our dockerfile, let's see it closely

```
# Here we are using python:3.8-slim as our base image as it ligh weight and
# and also serve our need of python
FROM python:3.8-slim

# This is where it will copy all required files from our local directory
# to docker container
COPY predict.py /usr/app/
COPY SVC_model.p /usr/app/
COPY requirements.txt /usr/app/

# changing working directory
WORKDIR /usr/app/

# installing dependencies
RUN pip install -r requirements.txt

# Here we are running our python application's executable file
CMD ["python", "predict.py" ]
```

## Building docker container

So to build a docker container from docker image we need to run the following commnad

> `docker build -t <name of container> <location of your docker image>`

so in our case we can run

> `docker build -t predict_stroke .`

After running this docker will start exectuing all instruction one by one and it will take some time.

## Pushing docker container to dockerhub

Dockerhub is a place where you can host your docker container for free and anyone from anywhere can pull it and use it.

So to push it on dockerhub you can do the following;

1. create a dockerhub account you don't have already
2. in your terminal run `docker login` and enter your credentials.
3. After that we need to tag our container which we want to push it on dockerhub. Which we can be done with the following command

   > `docker tag <your container name> <your dockerhub username>/<your container name>`

   Which in our case looks like this

   > `docker tag predict_stroke aman4004/predict_stroke

4. After tagging you can push it by this command

   > `docker push <your dockerhub username>/<your container name>`

   which in our case looks like this

   > `docker push aman4004/predict_stroke`

   It will take some time and will push the container on dockerhub

### Pulling docker container

Once you push your docker container to docker hub anyone can pull it from anywhere using this command

> `docker pull <your dockerhub username>/<your container name>`
