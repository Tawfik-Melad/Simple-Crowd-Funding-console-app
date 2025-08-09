def is_vaild_name(name):
    if isinstance(name, str) and len(name) > 0  and name.isalpha():
        return True
    return False

def is_valid_email(email):

    with open('.users.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            if email in user:
                print("Email already exists.")
                return False

    if isinstance(email, str) and "@" in email and "." in email:
        return True
    
    return False

def is_valid_password(password):
    if isinstance(password, str) and len(password) >= 8:
        return True
    return False


def is_valid_phone_number(phone_number):
    if isinstance(phone_number, str) and len(phone_number) == 11 and phone_number.isdigit() and phone_number.startswith('01'):
        return True
    return False