#!/usr/bin/env python3
"""
Robust ATPA MCP Server Startup Script
Handles port conflicts and provides clear error messages
"""
import os
import sys
import signal
import subprocess
import time
import socket
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_port_available(port):
    """Check if a port is available"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('localhost', port))
            return True
    except OSError:
        return False

def kill_process_on_port(port):
    """Kill any process using the specified port"""
    try:
        # Find processes using the port
        result = subprocess.run(['lsof', '-ti', f':{port}'], 
                              capture_output=True, text=True)
        if result.stdout.strip():
            pids = result.stdout.strip().split('\n')
            for pid in pids:
                if pid:
                    logger.info(f"Killing process {pid} on port {port}")
                    os.kill(int(pid), signal.SIGKILL)
            time.sleep(2)  # Wait for processes to terminate
            return True
    except Exception as e:
        logger.warning(f"Could not kill process on port {port}: {e}")
    return False

def check_dependencies():
    """Check if all required dependencies are available"""
    required_packages = [
        'fastapi', 'uvicorn', 'pandas', 'numpy', 'scikit-learn', 
        'shap', 'requests', 'jinja2'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        logger.error(f"Missing required packages: {', '.join(missing_packages)}")
        logger.info("Installing missing packages...")
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing_packages, 
                         check=True)
            logger.info("Dependencies installed successfully!")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install dependencies: {e}")
            return False
    
    return True

def check_data_files():
    """Check if required data files exist"""
    data_dir = Path("../Task1_DataPrep")
    required_files = [
        data_dir / "incidents.csv",
        data_dir / "arrestee.csv"
    ]
    
    missing_files = [f for f in required_files if not f.exists()]
    if missing_files:
        logger.error(f"Missing required data files: {[f.name for f in missing_files]}")
        return False
    
    logger.info("All required data files found!")
    return True

def start_server(port=8000, host="0.0.0.0"):
    """Start the FastAPI server with robust error handling"""
    
    logger.info("ATPA MCP Server Startup")
    logger.info("=" * 50)
    
    # Check dependencies
    logger.info("Checking dependencies...")
    if not check_dependencies():
        logger.error("Dependency check failed. Exiting.")
        return False
    
    # Check data files
    logger.info("Checking data files...")
    if not check_data_files():
        logger.error("Data file check failed. Exiting.")
        return False
    
    # Check if port is available
    if not check_port_available(port):
        logger.warning(f"Port {port} is already in use. Attempting to kill existing processes...")
        if not kill_process_on_port(port):
            logger.error(f"Could not free port {port}. Please manually kill processes using this port.")
            return False
    
    # Start the server
    logger.info("Starting server...")
    logger.info("Starting ATPA MCP Server...")
    logger.info(f"Server will be available at: http://{host}:{port}")
    logger.info(f"Dashboard will be available at: http://{host}:{port}/dashboard")
    logger.info(f"API documentation will be available at: http://{host}:{port}/docs")
    logger.info("Press Ctrl+C to stop the server")
    
    try:
        # Use uvicorn to start the server
        cmd = [
            sys.executable, '-m', 'uvicorn', 
            'main:app', 
            '--host', host, 
            '--port', str(port),
            '--reload'
        ]
        
        logger.info(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Server failed to start: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error starting server: {e}")
        return False

def main():
    """Main entry point"""
    # Change to the script directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Parse command line arguments
    port = 8000
    host = "0.0.0.0"
    
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            logger.error("Port must be a number")
            sys.exit(1)
    
    if len(sys.argv) > 2:
        host = sys.argv[2]
    
    # Start the server
    success = start_server(port, host)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main() 