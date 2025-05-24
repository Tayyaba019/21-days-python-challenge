# Day 5: Password Manager (with Encryption)

## Description

This is a simple command-line password manager that encrypts passwords before storing them and allows you to view or add them securely.

## Features

- Encryption using `cryptography.fernet`
- Secure password storage in a local file
- Easy command-line interface
- Generates and uses a secure key

## How to Use

1. **Generate the Key (only once)**  
   Uncomment the `write_key()` function and run it once to create `key.key`.

2. **Add or View Passwords**  
   Run the script and follow the prompts to add or view saved passwords.

## Example

Would you like to add a new password or view existing ones (view, add), press q to quit? add
Account Name: Gmail
Password: mysecurepass123

Would you like to add a new password or view existing ones (view, add), press q to quit? view
User: Gmail | Password: mysecurepass123