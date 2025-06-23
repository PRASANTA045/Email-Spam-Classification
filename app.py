from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load your model
model = joblib.load("spam_model.pkl")

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory
templates = Jinja2Templates(directory="templates")

# Serve the HTML form
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Handle form submission
@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, text: str = Form(...)):
    result = model.predict([text])
    label = "Spam" if result[0] == 1 else "Not Spam"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "text": text,
        "prediction": label
    })
