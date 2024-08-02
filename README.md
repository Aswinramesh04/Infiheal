# Mental Health Chatbot Assignment

This repository contains the implementation of a FastAPI server for a Mental Health Chatbot. The project includes two key functionalities: a Retrieval-Augmented Generation (RAG) endpoint and a classification endpoint. The aim is to assist users by suggesting relevant articles or blog posts based on their mental health queries and classifying data into appropriate categories.

# Table of Contents
1. Project Overview
2. Features
3. Setup and Installation
4. Usage
5. Endpoints
6. Model Training and Saving
7. Docker Deployment
8. Hugging Face Space Deployment
9. Contributing
10. License

## Project Overview
*This project implements a FastAPI server with two main endpoints:

+/rag: A Retrieval-Augmented Generation endpoint for suggesting mental health articles.
+/classification: A classification endpoint for categorizing input data using a pre-trained Random Forest model.
The goal is to showcase skills in API development, model deployment, and containerization using Docker.

# Features
**Text Generation**: Uses GPT-Neo for generating article suggestions.
**Classification**: Implements a Random Forest model for data classification.
**Dockerization**: Easily deployable using Docker.
**Hugging Face Integration**: Deployed on Hugging Face Spaces for public access.

# Setup and Installation
1. **Clone the Repository**

git clone https://github.com/your-username/mental-health-chatbot.git
cd mental-health-chatbot
