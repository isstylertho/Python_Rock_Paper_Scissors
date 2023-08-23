import random


def play():
    """
    Allows user and computer to choose between 1 of 3 letters that indicate a word and determines which letter/word is
    greater than the other.
    :return: string
    """
    user_input = str(input("Please make a choice ('R' for rock, 'P' for paper, or 'S' for scissors): ")).lower()
    computer_input = random.choice(['r', 'p', 's'])
    acceptable_inputs = ['r', 'p', 's']

    while user_input not in acceptable_inputs:
        user_input = str(input("Please try again. You may choose from: 'R' for rock, 'P' for paper, or 'S' for "
                               "scissors: "))

    if user_input == computer_input:
        return "It's a tie"

    # r > s, s > p, p > r

    if (user_input == 'r' and computer_input == 's') or (user_input == 's' and computer_input == 'p') or \
            (user_input == 'p' and computer_input == 'r'):
        return 'You Won!'

    return 'You Lost!'


def main():
    print(play())


main()
