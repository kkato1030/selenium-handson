#!/bin/bash

# Variables
USER_POOL_ID="ap-northeast-1_Nq5kEQeuk"  # Modify
CLIENT_ID="3o2t7k5th1euj1hbr2p1qlg3v1"  # Modify
REGION="ap-northeast-1"  # Can Modify
USERNAME_PREFIX="TestUser" # Can Modify
PASSWORD="Passw0rd!" # Can Modify

# Create Users
for i in {1..10}; do
    # Set Attributes
    USERNAME="$USERNAME_PREFIX-$i"
    EMAIL=$(echo $USERNAME | tr '[A-Z]' '[a-z]')"@example.com"
    # Create User
    aws cognito-idp sign-up \
        --region $REGION \
        --client-id $CLIENT_ID \
        --username $USERNAME \
        --password $PASSWORD \
        --user-attributes Name="email",Value=$EMAIL \
    1>/dev/null 2>/dev/null
    if [ $? != 0 ]; then
        echo "[WARN] $USERNAME: Create skipped."
        continue
    fi
    # Confirm User
    aws cognito-idp admin-confirm-sign-up \
        --region $REGION \
        --user-pool-id $USER_POOL_ID \
        --username $USERNAME > /dev/null \
    1>/dev/null 2>/dev/null
    if [ $? != 0 ]; then
        echo "[WARN] $USERNAME: Confirm skipped."
        continue
    fi
    # Change Email Verified
    aws cognito-idp admin-update-user-attributes \
        --region $REGION \
        --user-pool-id $USER_POOL_ID \
        --username $USERNAME \
        --user-attributes Name="email_verified",Value="true" \
    1>/dev/null 2>/dev/null
    if [ $? != 0 ]; then
        echo "[WARN] $USERNAME: Verify Email skipped."
        continue
    fi
    echo "[INFO] $USERNAME: Create succeeded."
done
