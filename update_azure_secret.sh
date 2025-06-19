#!/bin/bash

# Script to update Azure Static Web Apps API Token in GitHub Secrets
# Repository: Gen-Plus-group/fixers-in-greece

SECRET_NAME="AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503"
REPO="Gen-Plus-group/fixers-in-greece"

echo "=== GitHub Secret Update Script ==="
echo "Repository: $REPO"
echo "Secret Name: $SECRET_NAME"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed."
    echo "Please install it from: https://cli.github.com/"
    echo ""
    echo "Installation commands:"
    echo "  - Ubuntu/Debian: sudo apt install gh"
    echo "  - macOS: brew install gh"
    echo "  - Windows: winget install --id GitHub.cli"
    exit 1
fi

# Check authentication status
echo "Checking GitHub CLI authentication..."
if ! gh auth status &> /dev/null; then
    echo "Error: Not authenticated with GitHub CLI."
    echo "Please run: gh auth login"
    exit 1
fi

echo "✓ GitHub CLI is authenticated"
echo ""

# Prompt for the token value
echo "Please enter the new Azure Static Web Apps API Token:"
echo "(Input will be hidden for security)"
read -s TOKEN_VALUE
echo ""

if [ -z "$TOKEN_VALUE" ]; then
    echo "Error: Token value cannot be empty"
    exit 1
fi

# Update the secret
echo "Updating secret in GitHub..."
if echo "$TOKEN_VALUE" | gh secret set "$SECRET_NAME" --repo "$REPO"; then
    echo "✓ Secret updated successfully!"
    echo ""
    
    # Verify the secret exists
    echo "Verifying secret exists..."
    if gh secret list --repo "$REPO" | grep -q "$SECRET_NAME"; then
        echo "✓ Secret '$SECRET_NAME' is present in the repository"
    else
        echo "⚠ Warning: Could not verify secret presence"
    fi
else
    echo "✗ Failed to update secret"
    exit 1
fi

echo ""
echo "=== Update Complete ==="
echo "The secret has been updated in the repository."
echo "Next steps:"
echo "1. Trigger a GitHub Actions workflow to test the new token"
echo "2. Check the Azure Static Web Apps deployment status"
echo ""
echo "Note: Secret values are masked in GitHub Actions logs for security."