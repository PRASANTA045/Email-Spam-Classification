from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import traceback
import joblib
import logging

app = FastAPI()

# Load model
model = joblib.load("spam_model.pkl")

# Mount static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates folder
templates = Jinja2Templates(directory="templates")

# Home route → Renders HTML form
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Predict route
@app.post("/predict")
async def predict(request: Request, text: str = Form(...)):
    try:
        prediction = model.predict([text])[0]
        result = "Spam" if prediction == 1 else "Not Spam"
        return templates.TemplateResponse("index.html", {
            "request": request,
            "result": result,
            "input": text
        })
    except Exception as e:
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail="Internal Server Error")
