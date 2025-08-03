#!/usr/bin/env python3
"""
Minimal working server for ATPA Curriculum functionality
"""

from fastapi import FastAPI
from curriculum import ATPACurriculum
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="ATPA Curriculum Server",
    description="Working server for curriculum functionality",
    version="1.0.0"
)

# Initialize curriculum
print("Loading ATPA Curriculum...")
curriculum = ATPACurriculum()
print("Curriculum loaded successfully!")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "ATPA Curriculum Server is running!",
        "status": "success",
        "endpoints": [
            "/curriculum/overview",
            "/curriculum/search?query=your_search_term",
            "/curriculum/ethical-framework",
            "/curriculum/modeling-techniques"
        ]
    }

@app.get("/curriculum/overview")
async def get_curriculum_overview():
    """Get overview of all ATPA modules"""
    return curriculum.get_module_overview()

@app.get("/curriculum/search")
async def search_curriculum(query: str):
    """Search across all modules for specific content"""
    return curriculum.search_curriculum(query)

@app.get("/curriculum/ethical-framework")
async def get_ethical_framework():
    """Get detailed ethical framework from Module 1"""
    return curriculum.get_ethical_framework_details()

@app.get("/curriculum/modeling-techniques")
async def get_modeling_techniques():
    """Get modeling techniques from Module 3"""
    return curriculum.get_modeling_techniques()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "curriculum_loaded": True}

if __name__ == "__main__":
    print("🚀 Starting ATPA Curriculum Server...")
    print("📍 Server will be available at: http://127.0.0.1:8000")
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("")
    print("Press Ctrl+C to stop the server")
    print("")
    
    uvicorn.run(app, host="127.0.0.1", port=8000) 