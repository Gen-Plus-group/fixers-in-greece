# Guide to Update GitHub Secret: AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503

This guide provides methods to update the GitHub secret for Azure Static Web Apps deployment.

## Method 1: Using GitHub CLI (gh)

### Prerequisites
- Install GitHub CLI: https://cli.github.com/
- Authenticate with: `gh auth login`

### Commands to Update the Secret

1. **Interactive mode** (most secure - prompts for value):
```bash
gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503
```

2. **From environment variable**:
```bash
export AZURE_TOKEN="your-token-value-here"
gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503 --body "$AZURE_TOKEN"
```

3. **From file**:
```bash
echo "your-token-value-here" > token.txt
gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503 < token.txt
rm token.txt  # Clean up
```

4. **For specific repository**:
```bash
gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503 \
  --repo Gen-Plus-group/fixers-in-greece \
  --body "your-token-value-here"
```

### Verify the Secret Exists
```bash
gh secret list --repo Gen-Plus-group/fixers-in-greece
```

## Method 2: Using GitHub REST API

### Prerequisites
- GitHub Personal Access Token with `repo` scope
- `curl` and `jq` installed
- Base64 and sodium encryption tools

### Step 1: Get Repository Public Key
```bash
GITHUB_TOKEN="your-personal-access-token"
OWNER="Gen-Plus-group"
REPO="fixers-in-greece"

# Get public key
PUBLIC_KEY_RESPONSE=$(curl -s \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/$OWNER/$REPO/actions/secrets/public-key)

KEY_ID=$(echo $PUBLIC_KEY_RESPONSE | jq -r '.key_id')
PUBLIC_KEY=$(echo $PUBLIC_KEY_RESPONSE | jq -r '.key')
```

### Step 2: Encrypt the Secret Value
For this step, you need to use sodium encryption. Here's a Python script example:

```python
from base64 import b64encode
from nacl import encoding, public

def encrypt_secret(public_key: str, secret_value: str) -> str:
    """Encrypt a secret using a public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")

# Usage
public_key = "YOUR_PUBLIC_KEY_HERE"
secret_value = "your-azure-token-value"
encrypted_value = encrypt_secret(public_key, secret_value)
print(encrypted_value)
```

### Step 3: Update the Secret
```bash
SECRET_NAME="AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503"
ENCRYPTED_VALUE="your-encrypted-value-here"

curl -X PUT \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github+json" \
  https://api.github.com/repos/$OWNER/$REPO/actions/secrets/$SECRET_NAME \
  -d "{\"encrypted_value\":\"$ENCRYPTED_VALUE\",\"key_id\":\"$KEY_ID\"}"
```

## Method 3: Using GitHub Web Interface

1. Navigate to: https://github.com/Gen-Plus-group/fixers-in-greece
2. Go to Settings → Secrets and variables → Actions
3. Find `AZURE_STATIC_WEB_APPS_API_TOKEN_MANGO_GROUND_055373503`
4. Click "Update" 
5. Paste the new token value
6. Click "Update secret"

## Security Best Practices

1. **Never commit secrets to code**
2. **Use environment variables or secure vaults**
3. **Rotate tokens regularly**
4. **Delete temporary files containing secrets**
5. **Use minimal required permissions**

## Verification

After updating, verify the secret is working by:
1. Triggering a GitHub Actions workflow that uses this secret
2. Checking the workflow run logs (secret values will be masked)
3. Verifying Azure Static Web Apps deployment succeeds

## Troubleshooting

- **Permission Denied**: Ensure you have write access to the repository
- **Secret Not Found**: Check the secret name spelling
- **Authentication Failed**: Verify your GitHub token has `repo` scope
- **Encryption Error**: Ensure you're using the correct public key

## Additional Resources

- [GitHub CLI Documentation](https://cli.github.com/manual/gh_secret_set)
- [GitHub REST API - Actions Secrets](https://docs.github.com/en/rest/actions/secrets)
- [GitHub Actions - Using Secrets](https://docs.github.com/actions/security-guides/encrypted-secrets)