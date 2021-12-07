"""
Matermind
computer generate 4 colors out of 6, user has to guess these colors in order and is given feedback
Michael Pham
Oct 2021
"""

def print_colors(color_list):
    accumulator_string = color_list[0]
    for i in range(1, len(color_list)):
        accumulator_string = accumulator_string + ", " + color_list[i]
    #print(color_list[0], color_list[1], color_list[2], color_list[3], color_list[4], color_list[5])
    print(accumulator_string)
    return

def get_guess(colors):
    print("Please enter four legal colors.  Your choices are:")
    print_colors(colors)
    guess1 = input("Enter color 1: ")

    while True:
        if guess1 not in colors:
            print("Please enter four legal colors.  Your choices are:")
            print_colors(colors)
            guess1 = input("Enter color 1: ")
        elif guess1 in colors:
            break

    guess2 = input("Enter color 2: ")
    while True:
        if guess2 not in colors:
            print("Please enter four legal colors.  Your choices are:")
            print_colors(colors)
            guess2 = input("Enter color 2: ")
        elif guess2 in colors:
            break

    guess3 = input("Enter color 3: ")
    while True:
        if guess3 not in colors:
            print("Please enter four legal colors.  Your choices are:")
            print_colors(colors)
            guess3 = input("Enter color 3: ")
        elif guess3 in colors:
            break

    guess4 = input("Enter color 4: ")
    while True:
        if guess4 not in colors:
            print("Please enter four legal colors.  Your choices are:")
            print_colors(colors)
            guess4 = input("Enter color 4: ")
        elif guess4 in colors:
            break

    guess_list = [guess1, guess2, guess3, guess4]
    print("You guessed:")
    print_colors(guess_list)
    return guess_list


def generate_code(colors):
    from random import choice
    color1 = choice(colors)
    color2 = choice(colors)
    color3 = choice(colors)
    color4 = choice(colors)

    secret_list = [color1, color2, color3, color4]
    return secret_list


def exact_matches(secret_list, guess_list, status_list):

    int_exact_matches = 0

    for i in range(4):
        if secret_list[i] != guess_list[i]:
            status_list.append("nuthin")
        elif secret_list[i] == guess_list[i]:
            status_list.append("exact")


    accumulator = 0
    for i in range(4):
        if status_list[i] == "exact":
            accumulator = accumulator + 1

    return accumulator


def inexact_matches(secret_list, guess_list, status_list):

    accumulator = 0

    for i in range(4):
        if status_list[i] == "exact" :
            3+5
        else:
            for f in range(4):
                if guess_list[i] == secret_list[f] and status_list[f] != "inexact" and status_list[f] != "exact":
                    accumulator = accumulator + 1
                    status_list[f] = "inexact"
                    break


    return accumulator


def print_introduction():
    print("Welcome to Mastermind!")
    print("Your goal is to guess a sequence of four colors")
    print("Each color can be blue, turquoise, cyan, sapphire, teal, lapis")
    print("Then I'll tell you how many times you guessed the correct color")
    print("in the correct position, and how many times you guessed the")
    print("correct color, but in the wrong position.")
    print("You have ten turns to guess the correct sequence. good luck!")

def is_game_over(num_exact_matches, turn):
    if num_exact_matches == 4:
        return True
    elif turn == 9:
        return True

def player_won(num_exact_matches):
    if num_exact_matches == 4:
        return True

def main():
    print_introduction()
    all_colors_list = ["blue", "turquoise", "cyan", "sapphire", "teal", "lapis"]
    secret_list = generate_code(all_colors_list)
    #print(secret_list)

    for i in range(10):
        print("Turn %d" %(i+1))
        guess_list = get_guess(all_colors_list)

        status_list = []
        exact = exact_matches(secret_list, guess_list, status_list)
        print("exact matches %s" %(exact))
        inexact = inexact_matches(secret_list, guess_list, status_list)
        print("inexact matches %s" %(inexact))

        game_over = is_game_over(exact, i)
        win = player_won(exact)
        if game_over == True:
            print("the answer was:")
            print(secret_list)
            if win == True:
                print("you won")
                print("it took you %d tries to win" %(i+1))
                break

            else:
                break


main()