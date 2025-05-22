import random
import string

def random_string(length=7):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_user():
    first_name = random_string(5).capitalize()
    last_name = random_string(6).capitalize()
    email = f"{random_string(6)}@gmail.com"
    password = "myPassword"

    return {
    "firstName": first_name,
    "lastName": last_name,
    "email": email,
    "password": password
}

def partial_update_data():
    first_name = random_string(5).capitalize()
    last_name = random_string(6).capitalize()

    return {
        "firstName": first_name,
        "lastName": last_name,
    }

