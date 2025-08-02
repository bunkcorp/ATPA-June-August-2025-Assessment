#!/usr/bin/env python3
"""
Test script for ATPA MCP Server
"""
import requests
import time
import subprocess
import sys
import os

def test_server():
    """Test if the server is running"""
    try:
        response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running!")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"❌ Server responded with status code: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
        return False
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

def start_server():
    """Start the server"""
    print("🚀 Starting ATPA MCP Server...")
    
    # Try different methods to start the server
    methods = [
        ["python3", "main.py"],
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
    ]
    
    for method in methods:
        try:
            print(f"Trying method: {' '.join(method)}")
            process = subprocess.Popen(method, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Wait a bit for the server to start
            time.sleep(3)
            
            # Test if server is running
            if test_server():
                print("✅ Server started successfully!")
                return process
            else:
                print("❌ Server failed to start with this method")
                process.terminate()
                
        except Exception as e:
            print(f"❌ Error with method {' '.join(method)}: {e}")
            continue
    
    print("❌ All methods failed to start the server")
    return None

def main():
    """Main function"""
    print("=" * 50)
    print("ATPA MCP SERVER TEST")
    print("=" * 50)
    
    # First test if server is already running
    if test_server():
        print("Server is already running!")
        return
    
    # Try to start the server
    process = start_server()
    
    if process:
        print("\n🎉 Server is now running!")
        print("📊 Dashboard: http://127.0.0.1:8000/dashboard")
        print("📚 API Docs: http://127.0.0.1:8000/docs")
        print("🔍 Health: http://127.0.0.1:8000/health")
        
        try:
            # Keep the server running
            process.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping server...")
            process.terminate()
            print("✅ Server stopped")
    else:
        print("❌ Failed to start server")

if __name__ == "__main__":
    main() 