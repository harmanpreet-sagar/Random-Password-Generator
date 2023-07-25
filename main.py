# Harmanpreet Singh Sagar
# 04 August 2022
# Random Password Generator

import string
import random

# Creates a list for each of the different components of the password
alphabets = list(string.ascii_letters)
numbers = list(string.digits)
special_char = list(string.punctuation)
characters = list(string.ascii_letters + string.digits + string.punctuation)

# Prints the title of the project
print("Random Password Generator")
print(" ")


# Declare generated random password method
def password_random():
    length = int(input("Enter the length of the password: "))

    while length < 8:
        print("Please enter a value of greater than or equal to 8 to create a secure password")
        # Obtain the length of the desired password
        length = int(input("Enter the length of the password: "))

    # Obtains the number of letters desired by the user
    alphabets_count = int(input("Enter the number of letters desired in the password: "))

    # Ensures that the number of characters falls within the acceptable range
    while alphabets_count > length or alphabets_count < 0:
        print("The number of letters should be in the range of 0 and " + str(length))
        # Obtains the number of letters desired by the user
        alphabets_count = int(input("Enter the number of letters desired in the password: "))

    # Obtains the number of numbers desired by the user
    numbers_count = int(input("Enter the number of digits desired in the password: "))

    # Ensures that the number of characters falls within the acceptable range
    while numbers_count > (length - alphabets_count) or numbers_count < 0:
        print("The number of digits should be in the range of 0 and " + str(length - alphabets_count))
        # Obtains the number of numbers desired by the user
        numbers_count = int(input("Enter the number of digits desired in the password: "))

    # Obtains the number of special characters desired by the user
    special_char_count = int(input("Enter the number of special characters desired in the password: "))

    # Ensures that the number of characters falls within the acceptable range
    while special_char_count > (length - alphabets_count - numbers_count) or special_char_count < 0:
        print("The number of special characters should be in the range of 0 and " + str(length - alphabets_count -
                                                                                        numbers_count))
        # Obtains the number of numbers desired by the user
        special_char_count = int(input("Enter the number of digits desired in the password: "))

    # Sum of all the various password elements as desired by the user
    characters_count = alphabets_count + numbers_count + special_char_count

    # Initializes the password
    password = []

    # Adds the desired amount of random letters in the password
    for alpha in range(alphabets_count):
        password.append(random.choice(alphabets))

    # Adds the desired amount of random numbers in the password
    for num in range(numbers_count):
        password.append(random.choice(numbers))

    # Adds the desired amount of random special characters in the password
    for spec_char in range(special_char_count):
        password.append((random.choice(special_char)))

    # Checks to see if the sum of teh different elements of the password is lesser than the desired password length
    if characters_count < length:
        # Shuffles the characters list
        random.shuffle(characters)
        # Adds the remaining number of random characters into the password
        for pwd in range(length - characters_count):
            password.append(random.choice(characters))

    # Shuffles the password list
    random.shuffle(password)

    # Converts the password into a printable string
    print("Your desired password is: ")
    print("".join(password))

run_program = True

# Ensures the user wants the program to continue after 1 run.
while run_program == True:
    # Invokes the above function
    password_random()
    run_program_user = input("Do you want to generate another password? (Y/N): ")
    if run_program_user in ["Y", "y"]:
        run_program = True
    elif run_program_user in ["N", "n"]:
        run_program = False
        print("Thanks for using this program")
        quit
    else:
        print("Please enter a valid digit: ")
        run_program_user = input("Do you want to generate another password? (Y/N): ")
