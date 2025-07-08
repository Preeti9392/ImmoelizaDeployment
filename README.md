# ImmoelizaDeployment

Real Estate Price Prediction API
Project Name: ImmoelizaDeployment
## Table of Contents
──> Overview

──> Mission Objectives

──> Key Features

──> Project Structure

──> Technologies Used

──> Local Setup & Installation

──> FastAPI Automatic Documentation

──> Deployment on Render.com


# Overview
This project provides a machine learning model deployed as a FastAPI web API, designed to predict real estate prices for "ImmoEliza Properties." The API allows web developers to integrate our robust regression model into their website by providing property data in a structured JSON format and receiving price predictions. The entire application is containerized using Docker for seamless deployment to cloud platforms like Render.com or Streamit.

# Mission Objectives
Use the pretrained machine learling model to predict the prices of propertied. Create the API using FastAPI, Create Docker Image and deploy it on render. OR
Use Streamlit to Create API and deploy it on Streamlit Cloud.

# Project Structure
The repository is organized into a clear and modular structure to separate concerns:

├── model/

        └── (trained_model.pkl)

├── predict/

        └── prediction.py

├── preprocessing/

         └── cleaning_data.py

├── requirements.txt

├── app.py

├── Dockerfile

├── streamlit_app.py

└── README.md

# Project Structure

model/: Contains the pre-trained machine learning model.

        └──>Contains pkl file of pretrained model.

predict/: Houses the logic for making predictions using the loaded model.

        └──>prediction.py: Contains the predict() function.

preprocessing/: Contains modules for data cleaning and transformation.

        └──>cleaning_data.py: Contains the preprocess() function.

requirements.txt: Lists all Python dependencies.

app.py: The main FastAPI application file, defining API routes.

Dockerfile: Instructions for building the Docker image.

streamlit_app.py: The streamlit API application file.

# Technologies Used

Python 3.10

FastAPI: Web framework for building the API.

Uvicorn: ASGI server for running the FastAPI application.

Pydantic: For data validation and settings management (used by FastAPI).

Scikit-learn / Pandas / NumPy

Docker: For containerization.

Render.com: Cloud platform for deployment.

Streamlit Cloud: For Streamlit Deployment

# Local Setup & Installation

To run this API locally for development or testing:

Clone the repository:

Bash:

        git clone git@github.com:Preeti9392/ImmoelizaDeployment.git

        cd ImmoelizaDeployment

# Create a virtual environment

Bash:

python -m venv venv

On Windows-->        
        .\venv\Scripts\activate

On macOS/Linux-->     
         source venv/bin/activate

# Install dependencies:

pip install -r requirements.txt

# API Endpoints

GET /

GET /predict

POST /predict

Request Body

Response Body (Success)

Response Body (Error)

# DeployedApp Url

On render:

https://immoelizaprediction-latest.onrender.com

On StreamlitCloud:

https://immoelizahousepriceprediction.streamlit.app/

