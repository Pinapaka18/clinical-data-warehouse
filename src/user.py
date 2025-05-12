# src/user.py

import csv
import os

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role.lower()

    def __str__(self):
        return f"User(username='{self.username}', role='{self.role}')"

def authenticate_user(username, password, credentials_file):
    if not os.path.exists(credentials_file):
        print("Credentials file not found.")
        return None

    try:
        with open(credentials_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'].strip() == username and row['password'].strip() == password:
                    return User(username, row['role'].strip())
    except Exception as e:
        print(f"Error reading credentials: {e}")
    return None
