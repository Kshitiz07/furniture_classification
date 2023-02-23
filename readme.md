
# Project Name: Furniture Classification
This project is focused on classifying images of furniture into three categories: sofa, bed, and chair. The project is built using Python, FAST api and deep learning libraries like torch.

# Docker
To ensure that the code runs smoothly on any system, we have provided a Dockerfile for the project. To use Docker, follow these steps:
    STEPS:
    1. Install Docker on your system.
    2. Navigate to the project directory.
    3. Build the Docker image using the following command: docker compose up -d
    [NOTE: As I have mentioned and programmed inside the docker compose file for all url and ports, you can just run the compose command.]
    4. You can see that  project running in the default port i.e localhost:8080/ [Check docker-compose.yml file]
    5. To stop the docker run: docker compose down

# Code Structure
The project code is structured as follows:

```
|-- .github/workflows
|   |-- main.yml/
|-- data/
|   |-- testing_dataset/
|   |-- training_dataset/
|-- models/
|   |-- models.pth
|-- notebooks/
|   |-- trainings.ipynb
|-- src/
|   |-- experiment.py
|   |-- main.py
|   |-- model_runner.py
|-- README.md
|-- docker-compose.yml
|-- Dockerfile
|-- requirements.txt
```
# Explanaition of Directories:
# data/ directory
The data/ directory contains two subdirectories: images/ and training_dataset/. These directories contain the images which we test and the data we trained for the model respectively.

# models/ directory
The models/ directory contains pre-trained models that can be used for prediction.

# notebooks/ directory
The notebooks/ directory contains Jupyter notebooks for the model training.

# src/ directory
The src/ directory contains the Python source code for the project. main.py contains the main API file of the project. model_runner.py contains the different functions to load the model and predict the model. 

# Dockerfile and #docker-compose.yml file
The Dockerfile is used to build the Docker image for the project.

# Readme.md file
The README.md file contains information about the project and how to use it.

# requirements.txt file
The requirements.txt file lists the Python packages required to run the project.

# Running the Code
# To run the code, follow these steps:
    Clone the repository to your local system.
    Install the required Python packages by running pip install -r requirements.txt.
    [optional] Run the training.ipynb file from google collab as it takes less time to train [Personally, I did the same to reduce time. Else you can use the pre-built by default]
    Install Docker on your system.
    Navigate to the project directory.
    Build the Docker image using the following command: docker compose up -d
        [NOTE: As I have mentioned and programmed inside the docker compose file for all url and ports, you can just run the compose command.]
    4. You can see that  project running in the default port i.e localhost:8080/ [Check docker-compose.yml file]
    5. To stop the docker run: docker compose down

# CI/CD
In Github Actions, Continuous Integration pipeline has been created. As soon as we commit on the main branch it trigggeres the github actions. However, for the deployment we don't have cloud server.

# Conclusion
This project provides a simple and efficient way to classify images of furniture using deep learning techniques. With the Docker container, users can run the code on any system without worrying about dependencies. The code structure is designed to be modular and easy to understand, making it easy to modify for other image classification tasks.
If we use more data to train and perform hyper tunning, we can improve the model accuracy. 