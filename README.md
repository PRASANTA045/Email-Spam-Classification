# 📧 Email Spam Detection System (FastAPI + ML)

This project presents a machine learning-based **Email Spam Detection** system built using Python and FastAPI. It classifies emails as **Spam** or **Not Spam (Ham)** using natural language processing (NLP) and a trained Naive Bayes model. The project also includes a REST API for easy integration and deployment.

---

## 🎯 Project Objectives

- Detect whether a given email message is spam or not
- Preprocess and vectorize email text using TF-IDF
- Use Naive Bayes classifier for efficient text classification
- Build a production-ready API using FastAPI
- Provide real-time predictions via web interface or API

---

# 🧰 Tools & Technologies
Python (Scikit-learn, FastAPI, Pydantic)

NLP Preprocessing (TF-IDF)

Pickle (Model Serialization)

Uvicorn (ASGI Server)



## 📁 File Information

- **Model File**: `spam_model.pkl`
- **Vectorizer File**: `vectorizer.pkl`
- **API File**: `app.py`
- **Environment**: Python 3.9+ with virtualenv


---

## 🔑 Key Features

- **TF-IDF Vectorization**
  - Converts email text to numeric features
- **Naive Bayes Classifier**
  - Lightweight and effective for text classification
- **FastAPI Integration**
  - High-performance API with automatic Swagger docs
- **Input Validation**
  - Pydantic models ensure input quality
- **Real-time Prediction**
  - API returns prediction instantly (`Spam` or `Ham`)

---

## 📊 API Endpoints

- `GET /` → Welcome message or HTML form (optional)
- `POST /predict` → Takes email message as input and returns prediction

# Open in browser:
Visit http://127.0.0.1:8000 for the homepage

Visit http://127.0.0.1:8000/docs for API Swagger UI

# 👨‍💻 Created By
Project Author : Prasant Kumar Nayak

Contact: mrprashant218@gmail.com


# 📬 Feedback & Contributions
⭐ Star the repo if you find it useful

🐛 Report bugs via GitHub issues

🤝 Feel free to fork and improve the project




