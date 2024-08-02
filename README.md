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
