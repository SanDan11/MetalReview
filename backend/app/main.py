from fastapi import FastAPI
from .database import engine, Base
from .routes import albums, reviews

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(albums.router)
app.include_router(reviews.router)

@app.get("/")
def root():
    return {"message": "Welcome to metal review api"}