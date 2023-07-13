import string

class cypher():

    def __init__(self):
        self.letters = string.ascii_letters
        self.digits = string.digits
        self.characters = self.letters + self.digits

    def cyph(self, text : str, shift_amount : int, operation : str):
        cyph_text = ""

        if operation == "decode":
            shift_amount = shift_amount * -1

        for char in text:
            if char in self.characters:
                position = self.characters.index(char)
                new_position = position + shift_amount
                cyph_text += self.characters[new_position]
            else:
                cyph_text += char

        upper = operation.upper()
        print(f"\n- [{upper}D] message > {cyph_text}")


if __name__ == "__main__":

    print("\nCYPHER PROGRAM\n")
    print("Shift amount must be less than 56.\n")
    cypher = cypher()
    while True:
        text = str(input("Enter message > "))
        shift_amount = int(input("Enter shift amount > "))

        if shift_amount <= 56:
            operation = str(input("Enter encode or decode > "))

            if operation == "encode" or operation == "decode":
                if operation == "encode":
                    cypher.cyph(text, shift_amount, operation)
                    print()
                if operation == "decode":
                    cypher.cyph(text, shift_amount, operation)
                    print()
            else:
                print(f"- [ERROR] Enter mentioned only!\n")

            restart = input("Restart (y/n)? > ").lower() == "y"
            if not restart:
                break
            print()
        else:
            print(f"- [ERROR] Shift amount must be less than 56!\n")