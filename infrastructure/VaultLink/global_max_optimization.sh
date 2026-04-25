#!/data/data/com.termux/files/usr/bin/bash
BASE_DIR="$HOME/infrastructure"
REPOS=$(ls -d "$BASE_DIR"/*/)

for REPO in $REPOS; do
    cd "$REPO" || continue
    # 1. Ensure latest build standard
    mkdir -p .github/workflows
    cp "$HOME/infrastructure/VaultLink/main.yml" ".github/workflows/" 2>/dev/null
    
    # 2. Final Sync to RickRed7 Dashboard
    git add .
    git commit -m "MAX_OPTIMIZATION: Infrastructure Align | SGC-PAT-2026-001" --allow-empty
    git push origin $(git branch --show-current) --force
done
