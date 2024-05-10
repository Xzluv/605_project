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
    - The container then runs my python script and outputs the results to the location where I previously mounted it `/output`.


## Rapidminer Process

![Process](/Process.png)


- Statistics：在此步骤中，对数据进行统计分析，以便了解数据的基本特征和分布。
- Replace Missing Values：这一步骤处理数据中的缺失值，可能通过插值、删除或用平均值/中位数填充等方式进行。
- Set Role：设定数据中各列的角色，在此数据集中y是标签。


- Generate Attributes：我用这个操作符构建了一个“总负债情况”的派生特征，通过个人贷款+住房贷款计算得来，以组合来增强模型的预测能力。
- Select Attributes：选择重要的特征用于模型训练，这可能基于特征重要性或其他选择标准。
- Discretize：将连续变量离散化，以适应某些模型的需求，或简化数据结构。
- Nominal to Numerical：将名义特征（类别变量）转换为数值，以便可以用于数学模型。
- Normalize：对数据进行归一化或标准化处理，确保不同特征的尺度一致，有助于模型更好地学习和预测。
- Split Data：将数据分割为训练集和测试集，这通常用于评估模型的泛化能力。

下面的部分是用机器学习的算法进行二元分类，于Python不同，为了测试不同算法模型的好坏，在Rapidminer上我所选择的算法是神经网络。

- Neural Net：使用神经网络进行模型训练。
- Apply Model：将训练好的模型应用到新数据上，进行预测。
- Performance：评估模型的性能，通常包括准确度、召回率、精确率等指标。

## Python Script Overview

这个Python脚本（605_pro.py）是为了在Rapidminer处理过的数据的基础上执行一个完整的机器学习流程，使用与在Rapidminer中的不同的算法——随机森林分类器来解决一个二元分类问题。以此不同模型上的性能。

- 它首先加载由Rapidminer处理过的CSV格式的数据集，省去了数据处理的麻烦。然后按照一定比例（8:2）将数据分割成训练集和测试集。数据预处理包括将分类标签转换为二进制形式，并对特征进行适当的转换。

- 接下来，脚本使用随机森林模型进行训练，模型的参数已经预设或可以根据需要调整。训练完成后，脚本使用测试集数据评估模型的性能，计算准确率、精确率、召回率和F1分数等指标，并生成混淆矩阵和ROC曲线来进一步分析模型表现。

```
# Instantiate the model
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf_classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_classifier.predict(X_test)
```

- 此外，脚本还包括一个特征重要性的分析，帮助理解哪些特征对预测结果有较大的影响。这个脚本为机
  器学习的二元分类问题提供了一个全面的解决方案，适用于需要精确控制数据处理和模型评估步骤的场景。


![Confusion_Matrix](/Confusion_Matrix.png)
- 这是模型的混淆矩阵。它展示了真实类别与模型预测类别之间的关系

![ROC](/ROC%20Curve.png)
- 这是模型的接收器操作特征（ROC）曲线，曲线下面积（AUC）为0.90，表明模型具有较好的区分正负样本的能力。

![Weight](/Feature_Importance.png)
- 这个图显示了随机森林模型中各特征的重要性。通过这种方式，我们可以看出哪些特征对于预测结果更为关键。比如图中最顶部的特征具有最高的重要性

## Conclusion

