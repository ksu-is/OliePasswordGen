import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")
    if length > 128:
        raise ValueError("Password length should not exceed 128 characters.")
    
    # Character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password has at least one character from each pool
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)
if __name__ == "__main__":
    while True:
        try:
            length = int(input("Enter password length (between 4 and 128, or 0 to exit): "))
            if length == 0:
                print("Exiting the program. Goodbye!")
                break
            print("Generated Password:", generate_password(length))
        except ValueError as e:
            print("Error:", e)
