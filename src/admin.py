import os
from getpass import getpass
from dotenv import load_dotenv

def setup_admin():
    if not os.path.exists(".env"):
        username = input("Create admin username: ")
        password = getpass("Create admin password: ")
        with open(".env", "w") as file:
            file.write(f"ADMIN_USERNAME={username}\nADMIN_PASSWORD={password}\n")

def admin_login():
    load_dotenv()
    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")
    
    while True:
        username = input("\nEnter admin username: ")
        password = getpass("Enter admin password: ")
        
        if username == admin_username and password == admin_password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials! Try again.\n")
