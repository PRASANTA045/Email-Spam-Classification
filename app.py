# app.py

from fastapi import FastAPI, Form
import joblib

app = FastAPI()

# ✅ Load the correct model file
model = joblib.load("spam_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Spam Classifier API"}

@app.post("/predict")
def predict(text: str = Form(...)):
    prediction = model.predict([text])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return {"prediction": result}
