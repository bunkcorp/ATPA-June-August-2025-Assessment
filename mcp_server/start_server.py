#!/usr/bin/env python3
"""
Startup script for ATPA MCP Server
"""
import os
import sys
import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'fastapi', 'uvicorn', 'pandas', 'numpy', 'openpyxl', 
        'plotly', 'matplotlib', 'seaborn', 'scikit-learn'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        logger.error(f"Missing required packages: {', '.join(missing_packages)}")
        logger.info("Installing missing packages...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            logger.info("Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            logger.error("Failed to install dependencies. Please run: pip install -r requirements.txt")
            return False
    
    return True

def check_data_files():
    """Check if required data files exist"""
    data_dir = Path("../Task1_DataPrep")
    required_files = [
        "Data_Dictionary.xlsx",
        "incidents.csv", 
        "arrestee.csv"
    ]
    
    missing_files = []
    for file in required_files:
        file_path = data_dir / file
        if not file_path.exists():
            missing_files.append(str(file_path))
    
    if missing_files:
        logger.error(f"Missing required data files:")
        for file in missing_files:
            logger.error(f"  - {file}")
        logger.error("Please ensure all data files are in the ../Task1_DataPrep directory")
        return False
    
    logger.info("All required data files found!")
    return True

def start_server():
    """Start the FastAPI server"""
    try:
        logger.info("Starting ATPA MCP Server...")
        logger.info("Server will be available at: http://localhost:8000")
        logger.info("Dashboard will be available at: http://localhost:8000/dashboard")
        logger.info("API documentation will be available at: http://localhost:8000/docs")
        logger.info("Press Ctrl+C to stop the server")
        
        # Start the server
        subprocess.run([sys.executable, "main.py"])
        
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Error starting server: {e}")
        return False
    
    return True

def main():
    """Main function"""
    logger.info("ATPA MCP Server Startup")
    logger.info("=" * 50)
    
    # Check if we're in the right directory
    if not Path("main.py").exists():
        logger.error("main.py not found. Please run this script from the mcp_server directory.")
        return False
    
    # Check dependencies
    logger.info("Checking dependencies...")
    if not check_dependencies():
        return False
    
    # Check data files
    logger.info("Checking data files...")
    if not check_data_files():
        return False
    
    # Start server
    logger.info("Starting server...")
    return start_server()

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 