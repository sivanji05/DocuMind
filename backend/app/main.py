from fastapi  import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, documents
from app.services.es_service import create_index_if_not_exists

import os

from app.db.database import engine
from app.db import models

from dotenv import load_dotenv
load_dotenv()

# Create the tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(documents.router)


origins = [
    "http://localhost:5173",  ]

app.add_middleware(
    CORSMiddleware,
     allow_origins= "http://localhost:5173",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(documents.router, prefix="/api/documents", tags=["Documents"])
app.include_router(documents.router, prefix="/api", tags=["Documents"])


@app.get("/")
def read_root():
    return {"message": "Welcome to DocuMind"}

@app.on_event("startup")
def setup():
    create_index_if_not_exists()