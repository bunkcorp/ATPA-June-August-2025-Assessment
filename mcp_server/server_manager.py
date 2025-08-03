#!/usr/bin/env python3
"""
ATPA MCP Server Manager
Provides utilities to manage the server startup, status, and troubleshooting
"""
import os
import sys
import time
import requests
import subprocess
import signal
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ServerManager:
    def __init__(self, port=8000, host="localhost"):
        self.port = port
        self.host = host
        self.base_url = f"http://{host}:{port}"
        
    def check_server_status(self):
        """Check if the server is running and responding"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            if response.status_code == 200:
                return True, "Server is running and healthy"
            else:
                return False, f"Server responded with status {response.status_code}"
        except requests.exceptions.ConnectionError:
            return False, "Server is not running or not accessible"
        except requests.exceptions.Timeout:
            return False, "Server request timed out"
        except Exception as e:
            return False, f"Error checking server: {e}"
    
    def check_port_usage(self):
        """Check what's using the port"""
        try:
            result = subprocess.run(['lsof', '-i', f':{self.port}'], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                return True, result.stdout.strip()
            else:
                return False, f"Port {self.port} is not in use"
        except Exception as e:
            return False, f"Error checking port usage: {e}"
    
    def kill_server(self):
        """Kill any process using the server port"""
        try:
            result = subprocess.run(['lsof', '-ti', f':{self.port}'], 
                                  capture_output=True, text=True)
            if result.stdout.strip():
                pids = result.stdout.strip().split('\n')
                for pid in pids:
                    if pid:
                        logger.info(f"Killing process {pid}")
                        os.kill(int(pid), signal.SIGKILL)
                time.sleep(2)
                return True, f"Killed {len(pids)} process(es)"
            else:
                return False, "No processes found on port"
        except Exception as e:
            return False, f"Error killing server: {e}"
    
    def start_server_alternative(self):
        """Alternative server startup method"""
        try:
            # Change to the script directory
            script_dir = Path(__file__).parent
            os.chdir(script_dir)
            
            # Try different startup methods
            methods = [
                # Method 1: Direct uvicorn
                [sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', str(self.port)],
                # Method 2: With reload
                [sys.executable, '-m', 'uvicorn', 'main:app', '--host', '0.0.0.0', '--port', str(self.port), '--reload'],
                # Method 3: Direct python execution
                [sys.executable, 'main.py']
            ]
            
            for i, cmd in enumerate(methods, 1):
                logger.info(f"Trying startup method {i}: {' '.join(cmd)}")
                try:
                    subprocess.run(cmd, check=True)
                    return True, f"Server started successfully with method {i}"
                except subprocess.CalledProcessError as e:
                    logger.warning(f"Method {i} failed: {e}")
                    continue
                except KeyboardInterrupt:
                    logger.info("Server startup interrupted by user")
                    return True, "Server startup interrupted"
            
            return False, "All startup methods failed"
            
        except Exception as e:
            return False, f"Error in alternative startup: {e}"
    
    def test_endpoints(self):
        """Test key server endpoints"""
        endpoints = [
            "/health",
            "/api/status", 
            "/tasks/status",
            "/docs"
        ]
        
        results = {}
        for endpoint in endpoints:
            try:
                response = requests.get(f"{self.base_url}{endpoint}", timeout=5)
                results[endpoint] = {
                    "status_code": response.status_code,
                    "working": response.status_code == 200
                }
            except Exception as e:
                results[endpoint] = {
                    "error": str(e),
                    "working": False
                }
        
        return results

def main():
    """Main function for server management"""
    manager = ServerManager()
    
    print("ATPA MCP Server Manager")
    print("=" * 40)
    
    # Check current status
    print("\n1. Checking server status...")
    is_running, status_msg = manager.check_server_status()
    print(f"   Status: {'✅ Running' if is_running else '❌ Not running'}")
    print(f"   Details: {status_msg}")
    
    # Check port usage
    print("\n2. Checking port usage...")
    port_in_use, port_info = manager.check_port_usage()
    print(f"   Port {manager.port}: {'🔒 In use' if port_in_use else '✅ Available'}")
    if port_in_use:
        print(f"   Details:\n{port_info}")
    
    # If server is not running, offer to start it
    if not is_running:
        print("\n3. Server startup options:")
        print("   a) Use start_server.py (recommended)")
        print("   b) Try alternative startup method")
        print("   c) Kill existing processes and retry")
        
        choice = input("\nEnter choice (a/b/c) or press Enter to exit: ").lower().strip()
        
        if choice == 'a':
            print("\nStarting server with start_server.py...")
            subprocess.run([sys.executable, "start_server.py"])
        elif choice == 'b':
            print("\nTrying alternative startup method...")
            success, msg = manager.start_server_alternative()
            print(f"Result: {msg}")
        elif choice == 'c':
            print("\nKilling existing processes...")
            success, msg = manager.kill_server()
            print(f"Result: {msg}")
            if success:
                print("Retrying server startup...")
                subprocess.run([sys.executable, "start_server.py"])
    
    # Test endpoints if server is running
    if is_running:
        print("\n4. Testing server endpoints...")
        results = manager.test_endpoints()
        for endpoint, result in results.items():
            status = "✅" if result.get("working", False) else "❌"
            print(f"   {status} {endpoint}: {result}")

if __name__ == "__main__":
    main() 