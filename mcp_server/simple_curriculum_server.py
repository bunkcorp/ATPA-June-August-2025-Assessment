#!/usr/bin/env python3
"""
Simple test server for ATPA Curriculum functionality
"""

from fastapi import FastAPI
from curriculum import ATPACurriculum
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="ATPA Curriculum Test Server",
    description="Simple test server for curriculum functionality",
    version="1.0.0"
)

# Initialize curriculum
curriculum = ATPACurriculum()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "ATPA Curriculum Test Server",
        "description": "Simple test server for curriculum functionality",
        "endpoints": [
            "/curriculum/overview",
            "/curriculum/search?query=your_search_term",
            "/curriculum/ethical-framework",
            "/curriculum/modeling-techniques",
            "/curriculum/explainability-techniques",
            "/curriculum/data-quality-guidelines"
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

@app.get("/curriculum/explainability-techniques")
async def get_explainability_techniques():
    """Get explainability techniques from Module 4"""
    return curriculum.get_explainability_techniques()

@app.get("/curriculum/data-quality-guidelines")
async def get_data_quality_guidelines():
    """Get data quality guidelines from Module 2"""
    return curriculum.get_data_quality_guidelines()

@app.get("/curriculum/learning-objectives")
async def get_learning_objectives():
    """Get learning objectives for all modules"""
    return curriculum.get_learning_objectives()

@app.get("/curriculum/summary")
async def get_curriculum_summary():
    """Get comprehensive curriculum summary"""
    return curriculum.get_curriculum_summary()

if __name__ == "__main__":
    print("Starting ATPA Curriculum Test Server...")
    print("Server will be available at: http://127.0.0.1:8000")
    print("API documentation at: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000) 