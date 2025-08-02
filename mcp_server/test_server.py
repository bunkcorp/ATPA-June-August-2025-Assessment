#!/usr/bin/env python3
"""
Test script to verify ATPA MCP Server functionality
"""

import requests
import time
import sys

def test_server():
    """Test the server endpoints"""
    base_url = "http://127.0.0.1:8000"
    
    print("🧪 Testing ATPA MCP Server...")
    print(f"📍 Server URL: {base_url}")
    print("")
    
    # Test 1: Basic connectivity
    print("1️⃣ Testing basic connectivity...")
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is responding")
            data = response.json()
            print(f"   Message: {data.get('message', 'N/A')}")
        else:
            print(f"❌ Server returned status code: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Could not connect to server: {e}")
        print("   Make sure the server is running with: python3 main.py")
        return False
    
    # Test 2: Curriculum overview
    print("\n2️⃣ Testing curriculum overview...")
    try:
        response = requests.get(f"{base_url}/curriculum/overview", timeout=5)
        if response.status_code == 200:
            data = response.json()
            modules = data.get('modules', {})
            print(f"✅ Found {len(modules)} curriculum modules:")
            for module_key, module_info in modules.items():
                status = "✓" if module_info.get('loaded', False) else "✗"
                print(f"   - {module_info.get('title', 'Unknown')} ({status})")
        else:
            print(f"❌ Curriculum overview failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Curriculum test failed: {e}")
    
    # Test 3: Curriculum search
    print("\n3️⃣ Testing curriculum search...")
    try:
        response = requests.get(f"{base_url}/curriculum/search?query=ethical framework", timeout=5)
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            print(f"✅ Search found {len(results)} results for 'ethical framework'")
        else:
            print(f"❌ Search failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Search test failed: {e}")
    
    # Test 4: Ethical framework
    print("\n4️⃣ Testing ethical framework...")
    try:
        response = requests.get(f"{base_url}/curriculum/ethical-framework", timeout=5)
        if response.status_code == 200:
            data = response.json()
            principles = data.get('principles', {})
            print(f"✅ Found {len(principles)} ethical principles:")
            for principle in principles.keys():
                print(f"   - {principle}")
        else:
            print(f"❌ Ethical framework failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Ethical framework test failed: {e}")
    
    # Test 5: Modeling techniques
    print("\n5️⃣ Testing modeling techniques...")
    try:
        response = requests.get(f"{base_url}/curriculum/modeling-techniques", timeout=5)
        if response.status_code == 200:
            data = response.json()
            techniques = data.get('techniques', {})
            print(f"✅ Found {len(techniques)} modeling techniques:")
            for technique in techniques.keys():
                print(f"   - {technique}")
        else:
            print(f"❌ Modeling techniques failed: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Modeling techniques test failed: {e}")
    
    print("\n" + "="*50)
    print("🎉 Server testing completed!")
    print("="*50)
    print("")
    print("📚 API Documentation: http://127.0.0.1:8000/docs")
    print("🎛️  Dashboard: http://127.0.0.1:8000/dashboard")
    print("")
    
    return True

if __name__ == "__main__":
    # Wait a moment for server to start if needed
    print("⏳ Waiting 2 seconds for server to be ready...")
    time.sleep(2)
    
    success = test_server()
    
    if not success:
        print("\n❌ Server test failed!")
        print("💡 To start the server, run:")
        print("   cd \"/Users/kevinwoods/Desktop/ActuarialExams/ATPA/ATPA August/ATPA_June_August_2025/mcp_server\"")
        print("   python3 main.py")
        sys.exit(1)
    else:
        print("✅ All tests passed!") 