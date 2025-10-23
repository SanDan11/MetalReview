from fastapi import FastAPI
from .routes import albums
from .database.db_setup import engine, Base

app = FastAPI(
    title="Metal Review API",
    description="An API for reviewing metal albums",
    version="1.0.0"
)

app.include_router(albums.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to metal review api"}