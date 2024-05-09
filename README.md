# Data Mining With Rapidminer

## Author info

- Author: Lichen Zhang
- GitHub account: Xzluv
- UMD email: lzhang33@umd.edu
- Personal email: z478671360@gmail.com

## Description

Explore RapidMiner for data mining and analysis. Choose a dataset and perform data preprocessing, transformation, and visualization using RapidMiner's visual interface. Apply a machine learning algorithm for classification or clustering. Analyze and interpret the results. Explore different techniques and create a complex project.

## Technologies

### Rapidminer: 

- RapidMiner is a comprehensive data science platform known for its extensive capabilities in |machine learning, predictive analytics, and data mining. 
- RapidMiner excels in providing an end-to-end environment for data science tasks. It integrates various stages of the data science lifecycle, from data preparation and exploration to model building and deployment.
- Support for major scripting languages such as Python and R, allowing for advanced customizability​.
- Unlike many other data science platforms, RapidMiner provides a holistic solution that is highly automated, reducing the need for manual coding. This makes it particularly appealing to non-technical users, termed "citizen data scientists," who can leverage its powerful capabilities without a deep programming background.
- RapidMiner also differentiates itself by integrating seamlessly with a wide array of data sources and providing capabilities for handling big data through its extension, RapidMiner Radoop
- User-friendly with a strong emphasis on GUI-based workflow design.
- Broad compatibility with various data types and extensive integration options.
- Strong community support and a marketplace for sharing extensions and plugins.
- In our study of big data systems, we have discussed the importance of versatile tools that
  can handle the analytical and operational aspects of data science projects.RapidMiner's 
  capabilities are closely related to these topics, particularly its handling of data, support
  for model validation techniques such as automated machine learning (AutoML),
  cross-validation, and the use of supervised and unsupervised learning methods。

### Docker: 

- Docker is a platform designed to make it easier to create, deploy, and run applications by
  using containers.
- Docker streamlines the development process by allowing developers to work in standardized 
  environments using local containers which provide your applications and services. 
-  Docker can use Dockerfile to build images automatically by reading the instructions from a Dockerfile, a text document that contains all the commands a user could call on the command line to assemble an image.
- The Dockerfile specifies the use of an official Python runtime as the base image, and copies the Python script into the container. The resulting Docker image encapsulates the entire project, making it easily deployable and scalable.
- Docker provides Docker Compose, a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, networks, and volumes, and then with a single command, you create and start all the services from your configuration​ 

## Docker implementation

- The Docker system designed for this project follows a logical sequence to
  ensure a smooth and consistent environment for both development and deployment

- Let's delve into the intricacies of the Docker system logic:

- Project Setup:
  - Begin with organizing your project files within a directory structure. The
    main files include:
    - `605_pro.py`: Contains the python
      code for fetching user profiles with Redis caching.
    - `Dockerfile`: Includes instructions for building a Docker image for the
      project.
    - `Docker-compose.yaml`: Defines services, networks, and volumes for Docker
      containers.

- Dockerfile Configuration:
  - Start by setting up the Dockerfile with the following steps:
    - **FROM**: Utilize an official Python runtime as the base image `python:3.7`
    - **WORKDIR**: Set the working directory in the container to `/app`.
    - **COPY**: Copy the project files into the container.
    - **RUN**: Install necessary dependencies (scikit-learn,pandas,matplotlib and seaborn) using pip.
    - **VOLUMN**: Mounting a data volume `/input` and `/output`
    - **CMD**: Specify the default command to run the Python script.
  
- Docker-compose.yaml Configuration:
  - Configure the docker-compose.yaml file to define the services required for
    the project:
    - Define service: Python.
    - Configure the Python service:
      - `version: '3'`: This specifies the version of the Docker Compose file format.
      - `services`: This section defines the services that make up the application. In this  case,there is only one service named server.
      - `build: src`This tells Docker Compose to build the Docker image for the service using   
        the Dockerfile located in the `src` directory relative to the Docker Compose file. 
        This is useful for creating custom images tailored to specific services
      - `volumes` This part of the configuration mounts volumes into the container:
        - `./input:/input`: This mounts the input directory from the host machine to the /input directory inside the container. This is useful for providing input data to the application running in the container.
        - `./output:/output`: Similarly, this mounts the output directory from the host machine to the /output directory inside the container. This setup allows the application to write output data back to the host.

- Building the Docker Image And Running the Docker Containers:
  - Execute `docker-compose up --build`. It is a very useful command when working with Docker Compose, as it both builds (or rebuilds) images for services that have a build configuration specified in the docker-compose.yml file and then starts the containers. 
    - Building Images: The `--build` option forces Docker Compose to build the images for the services defined in the docker-compose.yml file before starting the containers.
    - Starting Containers: After building the images, Docker Compose proceeds to create and start the containers based on the configurations specified in the docker-compose.yml file.
    - This includes setting up volumes and other settings that are defined for the services before.

- 
