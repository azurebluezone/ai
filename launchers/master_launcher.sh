#!/bin/bash
echo "🟡 Installing dependencies..."
pip install -r server/requirements.txt
cd frontend && npm install && cd ..

echo "🟢 Launching MCP server..."
gnome-terminal -- bash -c "cd server/mcp && python3 dispatcher.py; exec bash"

echo "🟢 Launching Backend..."
gnome-terminal -- bash -c "cd server && python3 app.py; exec bash" 