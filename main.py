from fastapi import FastAPI
from database import engine
import models
from routers import url

app = FastAPI()

# create tables
models.Base.metadata.create_all(bind=engine)

# include router
app.include_router(url.router)

@app.get("/")
def home():
    return {"message": "URL Shortener is running"}
