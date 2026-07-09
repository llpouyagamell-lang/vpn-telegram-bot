#!/bin/bash
# Build script for Railway
# Automatically runs before deployment

set -e

echo "🔨 Building VPN Store Bot..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating application directories..."
mkdir -p data/uploads
mkdir -p logs

echo "✅ Build completed successfully!"
