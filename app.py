from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import traceback
import logging
import joblib

app = FastAPI()

# Load your trained model
model = joblib.load("spam_model.pkl")

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Spam Classifier API"}

# Global exception handler
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred. Please try again later."}
    )

# Prediction route
@app.post("/predict")
def predict(text: str = Form(...)):
    try:
        if not text or text.strip() == "":
            raise HTTPException(status_code=400, detail="Text input cannot be empty.")

        prediction = model.predict([text])[0]  # Model must be preloaded
        result = "Spam" if prediction == 1 else "Not Spam"
        return {"prediction": result}

    except ValueError as ve:
        raise HTTPException(status_code=422, detail=f"Invalid value: {ve}")

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        raise e  # Let global handler catch it
