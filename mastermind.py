import random

COLORS = ["R", "G", "Y", "B", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():

    while True:
        guess = input("Enter guess code > ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color {color}. Try again.")
                break
    
        else:
            break

    return guess

def check_code(guess, real_code):

    colors_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in colors_counts:
            colors_counts[color] = 0
        colors_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            colors_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in colors_counts and colors_counts[guess_color] > 0:
            incorrect_pos += 1
            colors_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind, u have {TRIES} to guess the code...")
    print(f"The valid colors are ", *COLORS)

    code = generate_code()

    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"U guess the code in {attempts} tries.")
            break

        print(f"Correct pos : {correct_pos} & Incorrect pos : {incorrect_pos}")

    else:
        print(f"U ran out of tries. Code : ", *code)

if __name__ == "__main__":
    game()