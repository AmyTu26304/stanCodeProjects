"""
File: hangman.py
Name: Yi-Chen Tu (Amy Tu)
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program generates a random word and displays in a dashed form to users.
    The users have N_TURNS chances to figure out the characters by guessing an alphabet each round.
    The dashed line will be replaced if the user input is correct.
    A hangman will be displayed at the initial condition and after each wrong guess.
    """
    dashes = ""
    answer = random_word()
    for i in range(len(answer)):
        dashes += "-"
    print("The word looks like " + dashes)     # Print the initial dashes
    n = N_TURNS
    hangman(n)    # Display the image of hangman
    print("You have " + str(n) + " wrong guesses left.")
    while True:
        input_ch = str(input("Your guess: ")).upper()
        if not input_ch.isalpha():    # The input is not alphabetic
            print("Illegal format.")
        elif len(input_ch) != 1:   # More than 1 character was entered
            print("Illegal format.")
        else:
            if input_ch in answer:    # Correct guess
                print("You are correct!")
                dashes = correct_guess(input_ch, dashes, answer)   # The dashes will be renewed with correct inputs
                if dashes == answer:  # The user finds all of the characters in the answer
                    print("You win!!")
                    print("The word was: " + answer)
                    break
            else:      # Wrong guess
                print("There is no " + input_ch + "'s in the word.")
                n -= 1   # The user lost 1 turn of wrong guesses
                hangman(n)
            if n == 0:   # No guesses left
                print("You are completely hung : (")
                print("The word was: " + answer)
                break
            print("The word looks like " + dashes)
            print("You have " + str(n) + " wrong guesses left.")


def correct_guess(input_ch, dashes, answer):
    """
    :param input_ch: str, the correct input character will be revealed
    :param dashes: str, the dashes will be renewed with a correct input character(s)
    :param answer: str, the answer of the game
    :return: str, the renewed string with dashes and correct characters
    """
    ans = ""
    for i in range(len(answer)):      # Renew the dashes with the input character
        ch = answer[i]
        if input_ch == ch:
            ans += ch
        else:
            ans += dashes[i]
    return ans


def hangman(n):
    """
    :param n: int, turns of wrong guesses left
    """
    if n >= 7:
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("＿＿＿")
    elif n == 6:    # head
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |   (  )")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("＿＿＿")
    elif n == 5:    # body
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |   (  )")
        print("  |　　　|")
        print("  |　　　|")
        print("  |")
        print("  |")
        print("＿＿＿")
    elif n == 4:    # left hand
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |   (  )")
        print("  |　　＼|")
        print("  |　　　|")
        print("  |")
        print("  |")
        print("＿＿＿")
    elif n == 3:    # right hand
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |   (  )")
        print("  |　　＼|／")
        print("  |　　　|")
        print("  |")
        print("  |")
        print("＿＿＿")
    elif n == 2:    # left leg
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |   (  )")
        print("  |　　＼|／")
        print("  |　　　|")
        print("  |　　／")
        print("  |")
        print("＿＿＿")
    elif n == 1:    # right leg
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |　　(  )")
        print("  |　　＼|／")
        print("  |　　　|")
        print("  |　　／ ＼")
        print("  |")
        print("＿＿＿")
    else:      # n == 0, display the face, completely hung >_<
        print("  ＝＝＝＝")
        print("  |   　|")
        print("  |　 (>_<)")
        print("  |　　＼|／")
        print("  |　　　|")
        print("  |　　／ ＼")
        print("  |")
        print("＿＿＿")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
