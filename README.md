# 🔗 URL Shortener (FastAPI)

A simple and scalable URL shortener built using FastAPI.

## 🚀 Features

- Shorten long URLs
- Unique short code generation
- Redirect to original URL
- Track number of clicks
- REST API with FastAPI

## 🧱 Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Python

## 📌 API Endpoints

### 1. Shorten URL

POST /shorten

Request:
{
  "long_url": "https://example.com"
}

Response:
{
  "short_url": "http://127.0.0.1:8000/abc123"
}

---

### 2. Redirect

GET /{short_code}

Redirects to original URL.

---

### 3. Stats

GET /stats/{short_code}

Response:
{
  "long_url": "...",
  "clicks": 10
}

---

## ▶️ Run Project

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
