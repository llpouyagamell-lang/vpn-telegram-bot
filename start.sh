#!/bin/bash
# Startup script for Railway
# Runs after build, handles database initialization

set -e

echo "🚀 Starting VPN Store Bot on Railway..."

# Initialize database if needed
echo "🗄️  Checking database..."
python3 -c "
import asyncio
from database.base import DatabaseManager
print('Initializing database...')
asyncio.run(DatabaseManager.init_db())
print('Database ready ✓')
" || echo "Database initialization skipped"

# Start the application
echo "▶️  Starting application..."
exec python3 -m main
