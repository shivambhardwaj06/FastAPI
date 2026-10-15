from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from routes.query import router as query_router

app = FastAPI(
    title="RAG API",
    description="This is a RAG API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(query_router)

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "RAG Backend running"}