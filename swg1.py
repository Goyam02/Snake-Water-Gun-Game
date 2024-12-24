import random
from colorama import init,Fore,Style
init(autoreset=True)

def swg():
    print(Fore.CYAN + "Welcome to the Snake Water Gun!!")
    Rounds=int(input(Fore.YELLOW + "Enter the number of rounds you want to play:"))
    print(Fore.CYAN + f"Yoy have {Rounds} chances to play this game")
    print(Fore.CYAN + "You have to choose from the following: ")
    print(Fore.GREEN + "Snake, Water & Gun")
    print(Fore.MAGENTA + "The rules are as follows:")
    print(Fore.MAGENTA + "Snake vs Water: Snake wins")
    print(Fore.MAGENTA + "Water vs Gun: Water wins")
    print(Fore.MAGENTA + "Gun vs Snake: Gun wins")
    print(Fore.MAGENTA + "If both players choose the same, then the game is a tie")
    print(Fore.CYAN + "You will be playing against the computer")

    choices = ["Snake", "Water", "Gun"]
    user_score = 0
    computer_score = 0
    for i in range(Rounds):
        print(Fore.BLUE + f"\nRound {i+1} of {Rounds}")
        print(Fore.YELLOW + "Enter your choice:")
        user_choice = input().lower().capitalize()
        while user_choice not in choices:
            print(Fore.RED + "Invalid Choice. Please enter again:")
            user_choice = input().lower().capitalize()
        computer_choice = random.choice(choices)
        print(Fore.CYAN + "Computer's choice:", computer_choice)
        if user_choice == "Snake" and computer_choice == "Water":
            print(Fore.GREEN + "You win")
            user_score += 1
        elif user_choice == "Water" and computer_choice == "Gun":
            print(Fore.GREEN + "You win")
            user_score += 1
        elif user_choice == "Gun" and computer_choice == "Snake":
            print(Fore.GREEN + "You win")
            user_score += 1
        elif user_choice == computer_choice:
            print(Fore.YELLOW + "It's a tie")
        else:
            print(Fore.RED + "Computer wins")
            computer_score += 1
    print(Fore.CYAN +"\nFinal Scores:")
    print(Fore.GREEN + "Your score:", user_score)
    print(Fore.RED + "Computer's score:", computer_score)
    if user_score > computer_score:
        print(Fore.GREEN + "Congratulatins! You win the game!")
    elif user_score < computer_score:
        print(Fore.RED + "Computer wins the game! Better luck next time!")
    else:
        print(Fore.YELLOW + "The game is a tie")
    print(Fore.CYAN + "Thank you for playing the game")
swg()
