import string
import random

def generate_password(length):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + special

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length must be at least 1. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        another = input("Do you want to generate another password? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
