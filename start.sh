#!/bin/bash

# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# Start script for Render Worker
# ===========================================

echo "===================================="
echo "🚀 Starting Ajnabi Music Bot..."
echo "===================================="
echo ""

# Python virtual environment check
if [ -d "venv" ]; then
    echo "✅ Activating virtual environment..."
    source venv/bin/activate
else
    echo "⚠️ No virtual environment found, using system Python"
fi

# Install/Update requirements
echo ""
echo "📦 Installing/Updating requirements..."
pip install -r requirements.txt --quiet

# Environment variables check
echo ""
echo "🔍 Checking environment variables..."
if [ -z "$API_ID" ]; then
    echo "❌ API_ID not set!"
    exit 1
fi
if [ -z "$API_HASH" ]; then
    echo "❌ API_HASH not set!"
    exit 1
fi
if [ -z "$BOT_TOKEN" ]; then
    echo "❌ BOT_TOKEN not set!"
    exit 1
fi
echo "✅ All required variables set!"

# Create log directory if not exists
mkdir -p logs

# Start the bot
echo ""
echo "===================================="
echo "✅ Bot starting at $(date)"
echo "===================================="
echo ""

# Main command - bot start
python3 -m AjnabiMusic

# Keep exit code
exit_code=$?

if [ $exit_code -ne 0 ]; then
    echo ""
    echo "❌ Bot crashed with exit code: $exit_code"
    echo "Restarting in 5 seconds..."
    sleep 5
    exec bash start  # Restart
else
    echo ""
    echo "✅ Bot stopped normally at $(date)"
fi
