#!/bin/bash

# --- CONFIGURATION ---
PROJECT_DIR="$HOME/MLHPortfolioSite"

echo "🚀 Starting Redeployment Sequence..."

# 1. Navigate to project folder
echo "📂 Navigating to repository..."
cd "$PROJECT_DIR" || { echo "❌ Error: Project directory not found!"; exit 1; }

# 2. Pull latest code from GitHub
echo "🔄 Fetching and resetting code to match GitHub main branch..."
git fetch && git reset origin/main --hard

# Restore .env file (git reset --hard wipes it since it's in .gitignore)
if [ -f "$HOME/mlh-env" ]; then
    echo "🔑 Restoring .env file from backup..."
    cp "$HOME/mlh-env" "$PROJECT_DIR/.env"
fi

# 3. Spin down existing containers
echo "🐳 Spinning down existing containers..."
docker compose -f docker-compose.prod.yml down

# 4. Build and spin up containers
echo "🏗️  Building and spinning up containers..."
docker compose -f docker-compose.prod.yml up -d --build

echo "✅ Redeployment Complete! Live portfolio site has been successfully updated."
