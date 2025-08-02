#!/bin/bash

# Universal ATPA MCP Server Startup Script
# This script can be run from anywhere and will automatically navigate to the correct directory

echo "🚀 Starting ATPA MCP Server..."
echo ""

# Find the mcp_server directory relative to this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MCP_SERVER_DIR="$SCRIPT_DIR/mcp_server"

echo "📁 Looking for mcp_server directory..."
echo "   Script location: $SCRIPT_DIR"
echo "   Expected mcp_server: $MCP_SERVER_DIR"

# Check if mcp_server directory exists
if [ ! -d "$MCP_SERVER_DIR" ]; then
    echo "❌ Error: mcp_server directory not found at $MCP_SERVER_DIR"
    echo "   Current directory: $(pwd)"
    echo "   Please make sure you're running this from the correct location"
    exit 1
fi

# Change to the mcp_server directory
echo "📂 Navigating to mcp_server directory..."
cd "$MCP_SERVER_DIR"

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in mcp_server directory"
    echo "   Current directory: $(pwd)"
    echo "   Files in directory: $(ls -la | head -5)"
    exit 1
fi

echo "✅ Found main.py - we're in the correct directory"
echo ""

# Check if requirements are installed
echo "📦 Checking dependencies..."
if ! python3 -c "import fastapi, uvicorn" 2>/dev/null; then
    echo "⚠️  Some dependencies may be missing. Installing requirements..."
    pip3 install -r requirements.txt
else
    echo "✅ Dependencies appear to be installed"
fi

echo ""
echo "🌐 Starting server on http://127.0.0.1:8000"
echo "📚 API Documentation: http://127.0.0.1:8000/docs"
echo "🎛️  Dashboard: http://127.0.0.1:8000/dashboard"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the server
python3 main.py 