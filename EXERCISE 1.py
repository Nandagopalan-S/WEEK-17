"""
WEEK 17
Exercise 1 – Password with emojis 

"""

def input_password(prompt):
    return input(prompt)

def verify_password(password, verify):
    return password == verify

def main():
    password = input_password("Enter your password (with emojis): ")
    verify = input_password("Re-enter your password for verification: ")

    if verify_password(password, verify):
        print("Password verified successfully!")
        print("Your password is:", password)
    else:
        print("Passwords do not match. Please try again.")

if __name__ == "__main__":
    main()
