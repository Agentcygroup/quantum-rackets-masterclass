#!/bin/bash
echo "🚀 Launching TOTALITY stack..."
python3 sovereign/agents/langgraph_bridge.py &
python3 sovereign/agents/heartbeat_dashboard.py &
