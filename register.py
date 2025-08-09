
import validations
import lib

def register():

    name= input("Enter your name: ")
    while not validations.is_vaild_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your name: ")
    
    email = input("Enter your email: ")
    while not validations.is_valid_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")
    
    while True:
        password = input("Enter your password: ")

        if not validations.is_valid_password(password):
            print("Invalid password. Please enter a valid password.\n")
            continue 

        confirum_password = input("Confirm your password: ")

        if confirum_password != password:
            print("Passwords do not match. Please start again.\n")
            continue  

        print("Password set successfully!")
        break  


    hashed_password = lib.hash_password(password)

    phone_number = input("Enter your phone number: ")
    while not validations.is_valid_phone_number(phone_number):
        print("Invalid phone number. Please enter a valid phone number.")
        phone_number = input("Enter your phone number: ")

    with open('.users.txt', 'a') as file:
        file.write(f"{name},{email},{hashed_password},{phone_number}\n")
    print("Registration successful!")



if __name__ == "__main__":
    print("This module is not meant to be run directly.")