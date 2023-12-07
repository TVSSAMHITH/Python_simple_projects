import random
import string


def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True, special_chars=""):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    characters += special_chars

    if not characters:
        print("Error: No character set selected.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_user_input():
    length = int(input("Enter the desired password length: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'
    special_chars = input("Enter any additional special characters (if any): ")

    return length, uppercase, lowercase, digits, symbols, special_chars


def main():
    print("Welcome to the Advanced Random Password Generator!")

    length, uppercase, lowercase, digits, symbols, special_chars = get_user_input()

    password = generate_password(length, uppercase, lowercase, digits, symbols, special_chars)

    if password:
        print("\nYour generated password is:", password)


if __name__ == "__main__":
    main()
