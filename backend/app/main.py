"""
FastAPI main application.
AI-Powered Burnout Detection and Recovery Planning Agent
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import init_db
from app.routes import users, assessments, recovery, progress

# Initialize FastAPI app
app = FastAPI(
    title="AI-Powered Burnout Detection API",
    description="RESTful API for burnout assessment and recovery planning",
    version="1.0.0"
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(assessments.router)
app.include_router(recovery.router)
app.include_router(progress.router)


@app.on_event("startup")
async def startup_event():
    """
    Initialize database on startup.
    """
    init_db()


@app.get("/")
def root():
    """
    Root endpoint.
    """
    return {
        "message": "AI-Powered Burnout Detection and Recovery Planning API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "healthy"}
