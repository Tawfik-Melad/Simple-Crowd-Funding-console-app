print("you want to create a new account wirte yes")
input_value = input()
if input_value.lower() == "yes":
    from register import register
    register()

email = input("Enter your email: ")
password = input("Enter your password: ")
from login import login
import datetime
user = login(email, password)
if user is None:
    print("Login failed. Please check your credentials or register a new account.")
    exit(1)

print(f"Welcome to the application! {user[0]}")

import lib




while True:
    print("\nChoose an option:")
    print("1. Create a new project fund raise campaign")
    print("2. View all projects")
    print("3. Edit your project")
    print("4. Delete your project")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        lib.create_project(email)
    elif choice == "2":
        lib.view_projects()
    elif choice == "3":
        lib.update_project(email)
    elif choice == "4":
        lib.delete_project(email)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")


