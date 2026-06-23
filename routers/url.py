from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import URL
from schemas import URLCreate
import random
import string

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Generate short code
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# ✅ Create short URL
@router.post("/shorten")
def shorten_url(data: URLCreate, db: Session = Depends(get_db)):
    code = generate_code()

    new_url = URL(
        long_url=data.long_url,
        short_code=code
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "short_url": f"http://127.0.0.1:8000/{code}"
    }


# ✅ Redirect
@router.get("/{code}")
def redirect_url(code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == code).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    url.clicks += 1
    db.commit()

    return {"original_url": url.long_url}


# ✅ Stats
@router.get("/stats/{code}")
def get_stats(code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == code).first()

    if not url:
        raise HTTPException(status_code=404, detail="Not found")

    return {
        "long_url": url.long_url,
        "clicks": url.clicks
    }