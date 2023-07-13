def validator(password : str):

    if len(password) > 5 and len(password) < 15:

        lowercase = False
        uppercase = False
        number = False
        special_char = False

        for char in password:

            if (char.islower()):
                lowercase = True

            if (char.isupper()):
                uppercase = True

            if (char.isdigit()):
                number = True

            if (not char.isalnum()):
                special_char = True

        return lowercase and uppercase and number and special_char
    
if __name__ == "__main__":

    print("\nPassword Validator")
    print("\nStrong password should include \n-Lowercase, \n-Uppercase, \n-Digits and \n-Special characters.")
    while True:
        password = str(input("\nEnter password > "))
        result = validator(password)

        if result:
            print(f"\nYour password {password} is strong.")
        else:
            print(f"\nYour password {password} is not strong enough.")

        restart = input("\nWanna try again? (y/n) > ").lower() == "y"

        if not restart:
            break