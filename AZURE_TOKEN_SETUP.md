# Azure Static Web Apps Token Setup Guide

## Getting the Deployment Token from Azure

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to your Static Web App resource (mango-ground-055373503)
3. In the left sidebar, click on "Overview"
4. Look for "Deployment token" or click on "Manage deployment token"
5. Copy the token value (it's a long string)

## Adding/Updating the Token in GitHub

1. Go to your repository: https://github.com/Gen-Plus-group/fixers-in-greece
2. Click on "Settings" (in the repository, not your profile)
3. In the left sidebar, scroll down to "Secrets and variables" → "Actions"
4. Look for a secret named: `AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503`
   
   **If it exists:**
   - Click on it
   - Click "Update secret"
   - Paste the new token from Azure
   - Click "Update secret"
   
   **If it doesn't exist:**
   - Click "New repository secret"
   - Name: `AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503`
   - Secret: Paste the token from Azure
   - Click "Add secret"

## Retry the Deployment

After updating the token:
1. Go to the "Actions" tab in your repository
2. Click on the failed workflow run
3. Click "Re-run all jobs"

The deployment should now work with the valid token.

## Alternative: Check Azure Static Web Apps Extension

If you can't find the deployment token in the Azure Portal:
1. In VS Code, install the "Azure Static Web Apps" extension
2. Sign in to Azure
3. Find your Static Web App
4. Right-click and select "Copy Deployment Token"