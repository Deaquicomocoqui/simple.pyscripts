import string
import random

def generate_password():
    """Generate a secure random password with customizable length and character types."""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    print("=== Password Generator ===\n")
    
    # Get password length
    while True:
        try:
            length = int(input("Enter password length (8-128): "))
            if 8 <= length <= 128:
                break
            else:
                print("❌ Please enter a number between 8 and 128.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    # Get minimum character requirements
    while True:
        try:
            min_special = int(input("Minimum special characters (0-10): "))
            if 0 <= min_special <= min(10, length):
                break
            else:
                print(f"❌ Please enter a number between 0 and {min(10, length)}.")
        except ValueError:
            print("❌ Please enter a valid number.")
    
    # Build character pool and ensure requirements
    all_characters = lowercase + uppercase + digits + special
    password_chars = []
    
    # Add required special characters
    for _ in range(min_special):
        password_chars.append(random.choice(special))
    
    # Add at least one of each other type for security
    remaining = length - min_special
    if remaining >= 3:
        password_chars.append(random.choice(lowercase))
        password_chars.append(random.choice(uppercase))
        password_chars.append(random.choice(digits))
        remaining -= 3
    
    # Fill the rest randomly
    for _ in range(remaining):
        password_chars.append(random.choice(all_characters))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)
    
    # Convert to string
    password = ''.join(password_chars)
    
    print("\n✅ Generated password:")
    print(f"   {password}")
    print(f"\nPassword strength: {len(password)} characters")
    print(f"Special characters: {sum(1 for c in password if c in special)}")
    print(f"Digits: {sum(1 for c in password if c in digits)}")
    print(f"Uppercase: {sum(1 for c in password if c in uppercase)}")
    print(f"Lowercase: {sum(1 for c in password if c in lowercase)}")

if __name__ == "__main__":
    generate_password()
