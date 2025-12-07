#!/bin/bash

echo "Installing dependencies..."
echo ""
echo "Installing Python packages..."
pip install -q -r requirements.txt

echo ""
# Run environment verification
# You must run this step before you spin up the server to ensure the dependency and verify-env success, 
# it will create a local signal lock file to prevent cocurrent lock issue
chmod +x ./verify-env
./verify-env

echo ""
echo "✓ Setup complete"
