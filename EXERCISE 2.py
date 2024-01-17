"""
WEEK 17
Exercise 2 – Password as a file on your computer 

"""

import hashlib
import os

def hash_file_contents(file_contents):
   # Compute and return the hash of the file contents
    try:
        hasher = hashlib.sha256()
        hasher.update(file_contents.encode('utf-8'))
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error hashing file contents: {e}")
        return None

def register():
    #Registration function
    username = input("Enter your username: ")
    file_path = input("Enter the path of the file to use as your password: ")
    if not os.path.exists(file_path):
        print("File not found. Please try again.")
        return None, None, None

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except Exception as e:
        print(f"Could not read file contents: {e}")
        return None, None, None

    file_hash = hash_file_contents(file_contents)
    if file_hash:
        return username, file_contents, file_hash
    else:
        return None, None, None

def login(stored_username, stored_hash):
    #function for Login process
    username = input("Enter your username: ")
    if username != stored_username:
        print("Invalid username")
        return False

    file_path = input("Enter the path of your password file: ")
    if not os.path.exists(file_path):
        print("invalid password")
        return False

    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except Exception as e:
        print(f"Could not read file contents: {e}")
        return False

    file_hash = hash_file_contents(file_contents)
    if file_hash and file_hash == stored_hash:
        return True
    else:
        print("Invalid password")
        return False

def main():
    # function for registering the user details 
    print("User Registration")
    username, password, stored_hash = register()
    if stored_hash is None:
        print("Registration failed.")
        return

    print(f"\nRegistered User: {username}, Password: {password}, Hashed Password: {stored_hash}")

    # Simulate storing the username and hash
    with open("user_credentials.txt", "w") as f:
        f.write(f"{username}\n{stored_hash}")

    # Login
    print("\nLogin")
    with open("user_credentials.txt", "r") as f:
        stored_username, stored_hash = f.read().split('\n')

    if login(stored_username, stored_hash):
        print("Login successful.")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()
