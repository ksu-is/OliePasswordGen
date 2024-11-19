import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
 