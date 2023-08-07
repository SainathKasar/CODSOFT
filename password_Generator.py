import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars):
    characters = ""

    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        return "Password complexity not selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    satisfied='n'
    length = int(input("Enter password length: "))
    use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Use digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
    while(satisfied=='n'):
        generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        print("Generated Password:", generated_password)
        satisfied=input("Are you satisfied(y/n)? ")

if __name__ == "__main__":
    main()
