# this is rock paper scissors using if, elif, and else statements
#this one plays the computer


import random

player_1_choice = input("Player 1, what do you choose? Rock, Paper, Scissors? ").lower()
computer_choice_list = ["rock", "paper", "scissors"]

#len(computer_choice_list) - don't need this since we know it 3

random_number = random.randint(0 , 2)
# variable name = a random integer with a range index between 0 and 2 since there are 3 choices
computer_choice = computer_choice_list[random_number]
print("Computer chose", computer_choice)


# if both choices are the same - tie game
if player_1_choice == computer_choice:
    print("You tied!")
# player 1 choice combiniations
elif player_1_choice == "rock" and computer_choice != "scissors":
    print("Player 1, You got covered - you lost!")

elif player_1_choice == "paper" and (computer_choice != "rock" and computer_choice != "scissors"):
    print("Player 1, paper beats Rock")

elif player_1_choice == "scissors" and computer_choice != "rock":
    print("Player 1, WOOHOO - you sliced it!")

# computer choice combiniations
elif computer_choice == "rock" and player_1_choice != "scissors":
    print("Computer, you got covered, you lose!")

elif computer_choice == "paper" and player_1_choice != "rock":
    print("Computer, paper beats Rock")

elif computer_choice == "scissors" and player_1_choice != "rock":
    print("Computer, you sliced it! WOOHOO!")


#elif player_1_choice == ""
# want to discern which beats which
"""
paper =
rock =
scissors =
"""

#if player_1_name
