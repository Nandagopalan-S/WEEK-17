"""
WEEK 17
Exercise 3 – A toy one-time-password (OTP) generator 

"""

import hashlib
import os
import datetime

def hash_password(password, salt):
    # Hashes the password with a salt
    hasher = hashlib.sha256()
    hasher.update((password + salt).encode('utf-8'))
    return hasher.hexdigest()

def update_hsp(hsp):
    # this line updates HSP with the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    hasher = hashlib.sha256()
    hasher.update((hsp + current_time).encode('utf-8'))
    return hasher.hexdigest()

def get_otp(hsp):
   # The system produces a one-time password using the final six bytes of HSP.
    return hsp[-6:]

def register():
    # Procedure for Registration
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    salt = os.urandom(16).hex()  # Generate a random salt
    hsp = hash_password(password, salt)
    return username, password, hsp, salt

def login(username, password, stored_hsp, salt):
    # Procedure for user authentication 
    entered_username = input("Enter your username: ")
    if entered_username != username:
        print("Invalid username.")
        return False

    entered_password = input("Enter your password: ")
    if entered_password != password:
        print("Invalid password.")
        return False

   # HSP Update
    updated_hsp = update_hsp(stored_hsp)

    # Generate OTP
    otp = get_otp(updated_hsp)
    print(f"OTP (simulated SMS): {otp}")

    # The user provides the OTP.
    entered_otp = input("Enter the OTP: ")
    if entered_otp == otp:
        print("Login successful.")
        return True
    else:
        print("Invalid OTP.")
        return False

def main():
    # Registration
    print("Registration")
    username, password, hsp, salt = register()
    print(f"Registration successful.\nRegistered User: {username}")
    print(f"Hashed Password: {hsp}")
    print(f"Salt: {salt}")

    # Login
    print("\nLogin")
    if not login(username, password, hsp, salt):
        print("Login failed.")

if __name__ == "__main__":
    main()
