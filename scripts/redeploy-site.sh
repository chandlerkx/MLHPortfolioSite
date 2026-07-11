#!/bin/bash

# --- CONFIGURATION MATCHING YOUR FILES ---
PROJECT_DIR="$HOME/MLHPortfolioSite"
VENV_DIR="$PROJECT_DIR/python3-virtualenv"

echo "🚀 Starting Full-Stack Redeployment Sequence..."

# 1. Kill any existing tmux sessions running your server background instances
echo "🛑 Stopping existing tmux sessions..."
tmux kill-server 2>/dev/null || true

# 2. Navigate to project root directory
echo "📂 Navigating to repository..."
cd "$PROJECT_DIR" || { echo "❌ Error: Project directory not found!"; exit 1; }

# 3. Pull down fresh code from GitHub and force-clear untracked file discrepancies
echo "🔄 Fetching and resetting code to match GitHub main branch..."
git fetch --all
git reset origin/main --hard

# 3b. Restore .env file (git reset --hard wipes it since it's in .gitignore)
if [ -f "$HOME/mlh-env" ]; then
    echo "🔑 Restoring .env file from backup..."
    cp "$HOME/mlh-env" "$PROJECT_DIR/.env"
fi

# 4. Compile the React Frontend Assets
echo "⚛️ Navigating to frontend and compiling React assets..."
cd "$PROJECT_DIR/frontend" || { echo "❌ Error: frontend directory not found!"; exit 1; }
npm install
npm run build

# 5. Handle Flask Backend Python Environment
echo "📦 Returning to root and updating Python dependencies..."
cd "$PROJECT_DIR"
source "$VENV_DIR/bin/activate"
pip install -r requirements.txt

# 6. Start a new detached TMUX session to host the production backend process
echo "⚡ Starting production server inside a detached TMUX session..."
tmux new-session -d -s portfolio-site

# Pass execution instructions directly to the background virtual pane environment
tmux send-keys -t portfolio-site "cd $PROJECT_DIR" C-m
tmux send-keys -t portfolio-site "source python3-virtualenv/bin/activate" C-m
# Runs your application start file (adjust "flask run" if you use "python3 app.py")
tmux send-keys -t portfolio-site "flask run --host=0.0.0.0" C-m

echo "✅ Redeployment Complete! Live portfolio site has been successfully updated."
