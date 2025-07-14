
'''
Password Manager  
A basic terminal-based password manager.
It stores and retrieves passwords securely.  
The `cryptography` module is used for encryption, and the encryption key is saved in a file.
'''
import json
from cryptography.fernet import Fernet

# Generate encryption key (run once)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

# Load the encryption key
def load_key():
    return open("key.key", "rb").read()

# Save a new password
def save_password(website, username, password):
    f = Fernet(load_key())
    encrypted = f.encrypt(password.encode())
    with open("passwords.json", "a") as file:
        entry = {"website": website, "username": username, "password": encrypted.decode()}
        file.write(json.dumps(entry) + "\n")

# View all saved passwords
def view_passwords():
    f = Fernet(load_key())
    with open("passwords.json", "r") as file:
        for line in file:
            data = json.loads(line.strip())
            pwd = f.decrypt(data['password'].encode()).decode()
            print(f"{data['website']} | {data['username']} | {pwd}")

# Example usage:
# write_key()  # Run only once to create the key
# save_password("github", "deniz", "12345")
# view_passwords()

