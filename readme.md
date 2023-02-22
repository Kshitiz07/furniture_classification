
# Project Name: Furniture Classification
This project is focused on classifying images of furniture into three categories: sofa, bed, and chair. The project is built using Python, FAST api and deep learning libraries like torch.

# Docker
To ensure that the code runs smoothly on any system, we have provided a Dockerfile for the project. To use Docker, follow these steps:
    STEPS:
    1. Install Docker on your system.
    2. Navigate to the project directory.
    3. Build the Docker image using the following command: docker build -t cv-classification 
    4. Run the Docker container using the following command: docker run -it -p 8888:8888 cv-classification
    5. docker compose up -d

    To stop the docker run: docker compose down

This will launch a Jupyter notebook server that you can access by navigating to localhost:8888 in your browser.

# Code Structure
The project code is structured as follows:
lua
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

#data/ directory
The data/ directory contains two subdirectories: images/ and training_dataset/. These directories contain the images which we test and the data we trained for the model respectively.

#models/ directory
The models/ directory contains pre-trained models that can be used for prediction.

#notebooks/ directory
The notebooks/ directory contains Jupyter notebooks for the model training.

#src/ directory
The src/ directory contains the Python source code for the project. data.py contains functions for loading and preprocessing data. model.py contains the architecture of the deep learning model. predict.py contains functions for making predictions. train.py contains functions for training the model.

#Dockerfile and #docker-compose.yml file
The Dockerfile is used to build the Docker image for the project.

#Readme.md file
The README.md file contains information about the project and how to use it.

#requirements.txt file
The requirements.txt file lists the Python packages required to run the project.

Running the Code
# To run the code, follow these steps:
    Clone the repository to your local system.
    Install the required Python packages by running pip install -r requirements.txt.
    Download the training and validation datasets and place them in the data/ 
    Run the train.py script to train the model.
    Use the predict.py script to make predictions on new images.

# CICD

# Conclusion
This project provides a simple and efficient way to classify images of furniture using deep learning techniques. With the Docker container, users can run the code on any system without worrying about dependencies. The code structure is designed to be modular and easy to understand, making it easy to modify for other image classification tasks.
If we use more data to train and perform hyper tunning, we can improve the model accuracy. 