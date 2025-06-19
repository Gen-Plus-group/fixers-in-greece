#!/usr/bin/env python3
"""
Script to update GitHub secret using REST API
Requires: pip install requests pynacl
"""

import os
import sys
import getpass
import requests
from base64 import b64encode
from nacl import encoding, public

# Configuration
OWNER = "Gen-Plus-group"
REPO = "fixers-in-greece"
SECRET_NAME = "AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503"
API_BASE = "https://api.github.com"


def encrypt_secret(public_key: str, secret_value: str) -> str:
    """Encrypt a secret using a public key."""
    public_key_obj = public.PublicKey(
        public_key.encode("utf-8"), encoding.Base64Encoder()
    )
    sealed_box = public.SealedBox(public_key_obj)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


def get_repo_public_key(token: str) -> tuple:
    """Get the repository's public key for secret encryption."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/actions/secrets/public-key"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error getting public key: {response.status_code}")
        print(response.json())
        sys.exit(1)
    
    data = response.json()
    return data["key_id"], data["key"]


def update_secret(token: str, secret_value: str) -> bool:
    """Update the GitHub secret with the encrypted value."""
    # Get public key
    print("Fetching repository public key...")
    key_id, public_key = get_repo_public_key(token)
    
    # Encrypt the secret
    print("Encrypting secret value...")
    encrypted_value = encrypt_secret(public_key, secret_value)
    
    # Update the secret
    print(f"Updating secret '{SECRET_NAME}'...")
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/actions/secrets/{SECRET_NAME}"
    data = {
        "encrypted_value": encrypted_value,
        "key_id": key_id,
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code in [201, 204]:
        return True
    else:
        print(f"Error updating secret: {response.status_code}")
        if response.text:
            print(response.json())
        return False


def verify_secret_exists(token: str) -> bool:
    """Verify the secret exists in the repository."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    
    url = f"{API_BASE}/repos/{OWNER}/{REPO}/actions/secrets/{SECRET_NAME}"
    response = requests.get(url, headers=headers)
    
    return response.status_code == 200


def main():
    print("=== GitHub Secret Update Script (API Method) ===")
    print(f"Repository: {OWNER}/{REPO}")
    print(f"Secret Name: {SECRET_NAME}")
    print()
    
    # Get GitHub token
    github_token = os.environ.get("GITHUB_TOKEN")
    if not github_token:
        print("GitHub Personal Access Token required (with 'repo' scope)")
        print("You can also set GITHUB_TOKEN environment variable")
        github_token = getpass.getpass("Enter GitHub Token: ")
    
    if not github_token:
        print("Error: GitHub token is required")
        sys.exit(1)
    
    # Get the new secret value
    print("\nEnter the new Azure Static Web Apps API Token:")
    secret_value = getpass.getpass("Token value: ")
    
    if not secret_value:
        print("Error: Token value cannot be empty")
        sys.exit(1)
    
    # Update the secret
    try:
        if update_secret(github_token, secret_value):
            print("✓ Secret updated successfully!")
            
            # Verify
            print("\nVerifying secret exists...")
            if verify_secret_exists(github_token):
                print("✓ Secret is present in the repository")
            else:
                print("⚠ Warning: Could not verify secret presence")
            
            print("\n=== Update Complete ===")
            print("Next steps:")
            print("1. Trigger a GitHub Actions workflow to test the new token")
            print("2. Check the Azure Static Web Apps deployment status")
        else:
            print("✗ Failed to update secret")
            sys.exit(1)
            
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nMake sure you have installed the required packages:")
        print("  pip install requests pynacl")
        sys.exit(1)


if __name__ == "__main__":
    main()