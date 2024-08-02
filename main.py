from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import joblib

app = FastAPI()

# Load model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load the saved classification model
model_rf = joblib.load("app/models/random_forest_model.pkl")

# Define input schema for /rag endpoint
class RAGInput(BaseModel):
    prompt: str

# Define input schema for /classification endpoint
class ClassificationInput(BaseModel):
    feature1: float
    feature2: float
    # Add other features as needed

@app.get("/")
async def root():
    return {"message": "Welcome to the Mental Health Chatbot API"}

@app.post("/rag")
async def rag_endpoint(input: RAGInput):
    inputs = tokenizer(input.prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": generated_text}

@app.post("/classification")
async def classify(input: ClassificationInput):
    features = [[input.feature1, input.feature2]]
    prediction = model_rf.predict(features)
    return {"prediction": prediction[0]}
