#!/bin/bash

# ATPA MCP Server Startup Script
# This script ensures the server is started from the correct directory

echo "🚀 Starting ATPA MCP Server..."
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📁 Working directory: $SCRIPT_DIR"

# Change to the script directory
cd "$SCRIPT_DIR"

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in current directory"
    echo "   Current directory: $(pwd)"
    echo "   Make sure you're running this script from the mcp_server directory"
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