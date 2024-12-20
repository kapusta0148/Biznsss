import random
import string

def generate_unique_codes():
    characters = string.ascii_letters + string.digits + string.punctuation
    password1 = ''.join(random.choice(characters) for _ in range(8))
    return password1