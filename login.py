import lib


def login(email, password):
    
    with open('.users.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            user_data = user.strip().split(',')
            if user_data[1] == email:
                hashed_password = lib.hash_password(password)
                if hashed_password == user_data[2]:
                    print("Login successful!")
                    return user_data
                else:
                    print("Invalid password.")
                    return 
    print("Email not found.")
    return 