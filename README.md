# Mental Health Chatbot Assignment

This repository contains the implementation of a FastAPI server for a Mental Health Chatbot. The project includes two key functionalities: a Retrieval-Augmented Generation (RAG) endpoint and a classification endpoint. The aim is to assist users by suggesting relevant articles or blog posts based on their mental health queries and classifying data into appropriate categories.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Endpoints](#endpoints)
6. [Model Training and Saving](#model-training-and-saving)
7. [Docker Deployment](#docker-deployment)
8. [Hugging Face Space Deployment](#hugging-face-space-deployment)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

This project implements a FastAPI server with two main endpoints:

- **/rag**: A Retrieval-Augmented Generation endpoint for suggesting mental health articles.
- **/classification**: A classification endpoint for categorizing input data using a pre-trained Random Forest model.

The goal is to showcase skills in API development, model deployment, and containerization using Docker.

## Features

- **Text Generation**: Uses GPT-Neo for generating article suggestions.
- **Classification**: Implements a Random Forest model for data classification.
- **Dockerization**: Easily deployable using Docker.
- **Hugging Face Integration**: Deployed on Hugging Face Spaces for public access.

## Setup and Installation

### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```
## Setup and Installation

### 3. Install Dependencies

Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 4. Download and Save the Pre-trained Models

Ensure that the necessary models are downloaded and saved in the models/ directory.

- **GPT-Neo for RAG**: Automatically downloaded when running the script.
- **Random Forest Model**: Pre-trained and saved as random_forest_model.pkl.

### Usage
## Running the Server Locally
Once all dependencies are installed, you can run the FastAPI server locally:

```bash

uvicorn main:app --reload
```
## Accessing the API
Navigate to http://127.0.0.1:8000/docs in your browser to access the interactive Swagger UI documentation.

### Endpoints
## - **1. /rag Endpoint**
## Method: POST
Description: Generates a relevant article suggestion based on the user’s mental health query.
## Request:
```json
{
    "prompt": "I'm feeling anxious and need help."
}
```
## Response:
```json

{
    "response": "This is a sample article related to your query."
}
```
## - **2. /classification Endpoint**
## Method: POST
Description: Classifies the input data based on the trained model.
## Request:
```json

{
    "feature1": 1.0,
    "feature2": 2.0
}
```
## Response:
```json

{
    "prediction": "Class A"
}
```
### Model Training and Saving
The Random Forest model was trained using **scikit-learn** on a sample dataset. Below is a brief overview of the training process:

## Train the Model
The model was trained on the provided dataset using **RandomForestClassifier**.
The model achieved an accuracy of 80% on the test set.
## Save the Model
The trained model was saved using joblib for easy deployment:
```python
import joblib
joblib.dump(model, 'models/random_forest_model.pkl')
```
### Docker Deployment
To deploy the FastAPI application using Docker, follow these steps:

- **1. Build the Docker Image**
```bash

docker build -t my-fastapi-app .
```
- **2. Run the Docker Container**
```bash

docker run -p 8000:8000 my-fastapi-app
```
- **3. Test the Application**
Visit http://localhost:8000/docs to test the API via Swagger UI.

### Hugging Face Space Deployment
- **1. Create a Hugging Face Space**
Follow the Hugging Face documentation to create a new space.

- **2. Deploy the Models**
Upload your models and scripts to the Hugging Face space, and configure it to run your FastAPI application.

- **3. Test the Deployment**
Ensure that your API endpoints are functioning correctly in the Hugging Face space.

### Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
