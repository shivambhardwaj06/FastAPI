from fastapi import FastAPI, Request
import uvicorn
from datetime import date
app = FastAPI(

    title="My FastAPI Application",
    description=("This is a sample FastAPI application with custom title and description."
                 " It demonstrates how to set up a FastAPI app with metadata."),
    version="1.0.0",
    docs_url="/docs",  # Custom URL for Swagger UI
    redoc_url="/redoc",  # Custom URL for ReDoc
    openapi_url="/openapi.json"  # Custom URL for OpenAPI schema
)

@app.get("/")
def read_root():
    """Root endpoint that returns a welcome message."""
    # FastAPI converts this dict into JSON
    return {"message": "Welcome to My FastAPI Application!", "status": "success"}

@app.get("/about")
def about():
    """Returns API Metadata"""
    return {
        "service" : "My FastAPI Application",
        "team" : "Development Team",
        "region" : "Global",
        "version" : "1.0.0"
    }

@app.get("/public/info")
def infoaboutme():
    """My personal Information"""
    return {
        "name":"Shivam Bhardwaj",
        "pursueing" : "Bachelor of Technology",
        "cgpa" : "7.2",
        "sem" : "3rd Sem"
    }

@app.get("/public/status")
def status():
    """My public status"""
    return {
        "today" : date.today(),
        "mood" : "Happy",
        "quote" : "Radhe Radhe"
    }

@app.get("/debug/request-info")
async def request_info(request: Request):
    """Inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params)
    }

#  How we make our docs more efficient

@app.get(
    "/public/info/summary",
    summary="Get a summary of the API",
    description=(
        "Returns all orders that are currently being prepared or are out for delivery"
    ),
    tags=["summary"],
    response_description="A summary of the API's purpose and functionality",
    deprecated=False

)
def get_summary():
    """ This docstring also appears in docs"""
    return {
        "goal" : [
            {
                "title": "Provide a simple and efficient API",
                "description": "The API should be easy to use and understand, with clear endpoints and responses."
            },
            {
                "title": "Demonstrate FastAPI features",
                "description": "Showcase the capabilities of FastAPI, including automatic documentation, request validation, and more."
            }
        ]
    }
