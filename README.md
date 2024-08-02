# Mental Health Chatbot Assignment

This repository contains the implementation of a FastAPI server for a Mental Health Chatbot. The project includes two key functionalities: a Retrieval-Augmented Generation (RAG) endpoint and a classification endpoint. The aim is to assist users by suggesting relevant articles or blog posts based on their mental health queries and classifying data into appropriate categories.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Model Training and Saving](#model-training-and-saving)
- [Docker Deployment](#docker-deployment)
- [Hugging Face Space Deployment](#hugging-face-space-deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project implements a FastAPI server with two main endpoints:
- `/rag`: A Retrieval-Augmented Generation endpoint for suggesting mental health articles.
- `/classification`: A classification endpoint for categorizing input data using a pre-trained Random Forest model.

The goal is to showcase skills in API development, model deployment, and containerization using Docker.

## Features
- **Text Generation**: Uses GPT-Neo for generating article suggestions.
- **Classification**: Implements a Random Forest model for data classification.
- **Dockerization**: Easily deployable using Docker.
- **Hugging Face Integration**: Deployed on Hugging Face Spaces for public access.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
