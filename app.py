from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import traceback
import joblib
import logging

app = FastAPI()

# Load the trained spam model
model = joblib.load("spam_model.pkl")

# Mount static folder (for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell FastAPI where to find templates
templates = Jinja2Templates(directory="templates")

# Home route – shows HTML form
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# POST /predict – handles form submission
@app.post("/predict", response_class=HTMLResponse)
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
