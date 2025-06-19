#!/bin/bash

# Update Azure Static Web Apps Token Script
# This script updates the GitHub secret for Azure deployment

echo "🔐 Updating Azure Static Web Apps Token"
echo "======================================="

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI."
    echo "Please run: gh auth login"
    exit 1
fi

# Repository details
REPO="Gen-Plus-group/fixers-in-greece"
SECRET_NAME="AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503"
TOKEN="c79fa88dd6dad46ef01f23568dd7b7f606ba45d0b12b1e0458425f7c90b35ca706-6280324d-82f8-42bf-83a8-1bbdb04cab5c0030706055373503"

echo "📝 Repository: $REPO"
echo "🔑 Secret Name: $SECRET_NAME"
echo ""

# Update the secret
echo "🔄 Updating secret..."
echo "$TOKEN" | gh secret set "$SECRET_NAME" --repo "$REPO"

if [ $? -eq 0 ]; then
    echo "✅ Secret updated successfully!"
    echo ""
    echo "🚀 Next steps:"
    echo "1. Go to: https://github.com/$REPO/actions"
    echo "2. Find the failed workflow run"
    echo "3. Click 'Re-run all jobs'"
    echo ""
    echo "The deployment should now work with the updated token!"
else
    echo "❌ Failed to update secret."
    echo "Please check your permissions and try again."
    exit 1
fi