import random
import string

def pass_generator(min_length : int, number = True, special_char = True):

    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special_char:
        characters += special

    password = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_numbers = True

        if new_char in special:
            has_special = True

        if number:
            meets_criteria = has_numbers

        if special_char:
            meets_criteria = meets_criteria and has_special

    return password


if __name__ == "__main__":

    print("\nPASSWORD GENERATOR")
    print("\nMin lenght of password should be between 5 and 15.")
    
    while True:
        try:
            min_length = int(input("\nEnter min lenght of password > "))
            
            if min_length >= 5 and min_length <= 15:
                has_number = input("Do u wanna to have numbers (y/n)? > ").lower() == "y"
                has_special = input("Do u wanna to have special characters (y/n)? > ").lower() == "y"

                password = pass_generator(min_length, has_number, has_special)
                print(f"\n- [RESULT] Your password is {password}.")

                restart = input("\nRestart (y/n)? > ").lower() == "y"

                if not restart:
                    break
                
            else:
                print("\n- [ERROR] Min length should between 5 and 15.\n")

        except Exception as err:
            print(f"\n- [ERROR] {err}")