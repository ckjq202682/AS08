# AS08

# play rock paper scissor against a robot

import random

comp_choice = random.randrange(1, 4)

print("1: Rock")
print("2: Paper")
player_choice = int(input("3: Scissors"))
print(comp_choice)
if player_choice == comp_choice:  # tie
    print("It is a tie!")
elif player_choice == 1:  # rock
    if comp_choice == 2:  # paper
        print("The computer wins!")
    elif comp_choice == 3:  # scissors
        print("You win!")
elif player_choice == 2:  # paper
    if comp_choice == 1:  # rock
        print("You win!")
    elif comp_choice == 3:  # scissors
        print("The computer wins!")
elif player_choice == 3:  # scissors
    if comp_choice == 1:  # rock
        print("The computer wins!")
    elif comp_choice == 2:  # paper
        print("You win!")
