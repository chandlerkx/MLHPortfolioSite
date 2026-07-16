#!/bin/bash

# --- CONFIGURATION ---
PROJECT_DIR="$HOME/MLHPortfolioSite"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"

echo "🚀 Starting Redeployment Sequence..."

# 1. Navigate to project folder
echo "📂 Navigating to repository..."
cd "$PROJECT_DIR" || { echo "❌ Error: Project directory not found!"; exit 1; }

# 2. Pull latest code from GitHub
echo "🔄 Fetching and resetting code to match GitHub main branch..."
git fetch --all
git reset origin/main --hard

# Restore .env file (git reset --hard wipes it since it's in .gitignore)
if [ -f "$HOME/mlh-env" ]; then
    echo "🔑 Restoring .env file from backup..."
    cp "$HOME/mlh-env" "$PROJECT_DIR/.env"
fi

# 3. Enter the python virtual environment and install python dependencies
echo "📦 Updating Python dependencies..."
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt

# 4. Run the test suite before deploying
echo "🧪 Running test suite..."
TESTING=true python -m unittest discover -v tests

if [ $? -ne 0 ]; then
    echo "❌ Tests failed! Aborting deployment to prevent production downtime."
    exit 1
fi

echo "✅ All tests passed!"

# 5. Restart myportfolio service
echo "⚡ Restarting myportfolio service..."
sudo systemctl restart myportfolio

echo "✅ Redeployment Complete! Live portfolio site has been successfully updated."
