from contextlib import asynccontextmanager
from fastapi import FastAPI
from Rangmanch.database import create_table
from Rangmanch.routes.reviews import router as review_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan function to create tables when the application starts"""
    create_table()
    print("Database tables created successfully")  # Create tables when the application starts
    yield  # Yield control back to the application  
    print("shutting down") # Cleanup logic can be added here

app = FastAPI(
    title="Rangmanch Reviews API",
    description="API for managing reviews of plays in Rangmanch",
    lifespan = lifespan
)

app.include_router(review_router)

@app.get("/")
def root():
    return {"message":"Welcome To the Rangmanch"}

