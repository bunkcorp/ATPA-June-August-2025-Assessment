#!/bin/bash

# Universal ATPA Curriculum Test Script
# This script can be run from anywhere and will automatically navigate to the correct directory

echo "🧪 Testing ATPA Curriculum Functionality..."
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

# Check if test_curriculum.py exists
if [ ! -f "test_curriculum.py" ]; then
    echo "❌ Error: test_curriculum.py not found in mcp_server directory"
    echo "   Current directory: $(pwd)"
    echo "   Files in directory: $(ls -la | head -5)"
    exit 1
fi

echo "✅ Found test_curriculum.py - running curriculum tests..."
echo ""

# Run the curriculum test
python3 test_curriculum.py 