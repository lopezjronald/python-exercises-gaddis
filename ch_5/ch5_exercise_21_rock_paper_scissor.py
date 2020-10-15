"""
21. Rock, Paper, Scissors Game
Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.
The program should work as follows:
1. When the program begins, a random number in the range of 1 through 3 is generated.
If the number is 1, then the computer has chosen rock. If the number is 2, then the
computer has chosen paper. If the number is 3, then the computer has chosen scissors.
(Don’t display the computer’s choice yet.)
2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the keyboard.
3. The computer’s choice is displayed.
4. A winner is selected according to the following rules:
• If one player chooses rock and the other player chooses scissors, then rock wins.
(Rock smashes scissors.)
• If one player chooses scissors and the other player chooses paper, then scissors wins.
(Scissors cuts paper.)
• If one player chooses paper and the other player chooses rock, then paper wins.
(Paper wraps rock.)
• If both players make the same choice, the game must be played again to determine
the winner.
"""


def rock_paper_scissor(choice):
    if choice == 1:
        choice = 'rock'
    elif choice == 2:
        choice = 'paper'
    else:
        choice = 'scissors'
    return choice


def computer_choice():
    from random import randint
    computer_attack = randint(1, 3)
    return rock_paper_scissor(computer_attack)


def player_choice():
    while True:
        print("1: Rock\n2: Paper\n3: Scissors")
        try:
            choice = int(input())
        except:
            print("Invalid Entry")
            continue
        if choice < 1 or choice > 3:
            print("Invalid Entry")
            continue
        else:
            return rock_paper_scissor(choice)


def winner(computer, player):
    if (
            computer == 'scissors' and player == 'paper') or (
            computer == 'paper' and player == 'rock') or (
            computer == 'rock' and player == 'scissors'
    ):
        return 'Computer'
    elif (
            player == 'scissors' and computer == 'paper') or (
            player == 'paper' and computer == 'rock') or (
            player == 'rock' and computer == 'scissors'
    ):
        return 'Player'
    else:
        return 'Draw'


def display_result(computer, player):
    print(f"Computer: {computer.title()}")
    print(f"Player: {player.title()}")
    if winner(computer, player).lower() == 'draw':
        print("Draw!")
    else:
        print(f"The winner is {winner(computer, player)}!")


def continue_playing():
    while True:
        try:
            play = input("Continue Playing? (y for yes, n for no): ")
            play = play.lower()
        except:
            print("Invalid Entry")
            continue

        if play == 'y' or play == 'n':
            return play
        else:
            print("Invalid Entry")


def main():
    play = True
    while play:
        computer = computer_choice()
        player = player_choice()
        display_result(computer, player)
        if continue_playing() == 'n':
            play = False


main()
