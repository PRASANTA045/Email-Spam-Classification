from fastapi import FastAPI, Form
import joblib

app = FastAPI()


model = joblib.load("spam_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Spam Classifier API"}

from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel
import traceback




from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.responses import JSONResponse
import traceback
import logging

app = FastAPI()

# Example: Load your trained model
# from joblib import load
# model = load("spam_model.pkl")

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logging.error(f"Unhandled error: {exc}")
    traceback.print_exc()
    return JSONResponse(
        status_code=500,
        content={"error": "An unexpected error occurred. Please try again later."}
    )

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
        raise http_exc  # Let FastAPI handle known HTTP errors

    except Exception as e:
        # Let global exception handler handle it
        raise e

