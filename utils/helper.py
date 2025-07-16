import random
import string
import time

def generate_password():
    length = random.choice([9, 10])  # случайная длина: 9 или 10
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def generate_email():
    email = str(time.time()) + "@fakemail.org"
    return email

