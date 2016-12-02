# this is rock paper scissors using if, elif, and else statements



player_1_choice = input("Player 1, what do you choose? Rock, Paper, Scissors? ").lower()
player_2_choice = input("Player 2, what do you choose? Rock, Paper, Scissors? ").lower()

# if both choices are the same - tie game
if player_1_choice == player_2_choice:
    print("You tied!")

# player 1 choice combiniations
elif player_1_choice == "rock" and player_2_choice != "scissors":
    print("Player 1, You got covered - you lost!")

elif player_1_choice == "paper" and (player_2_choice != "rock" and player_2_choice != "scissors"):
    print("Player 1, paper beats Rock")

elif player_1_choice == "scissors" and player_2_choice != "rock":
    print("Player 1, WOOHOO - you sliced it!")

# player 2 choice combiniations
elif player_2_choice == "rock" and player_1_choice != "scissors":
    print("Player 2, you got covered, you lose!")

elif player_2_choice == "paper" and player_1_choice != "rock":
    print("Player 2, paper beats Rock")

elif player_2_choice == "scissors" and player_1_choice != "rock":
    print("Player 2, you sliced it! WOOHOO!")


#elif player_1_choice == ""
# want to discern which beats which
"""
paper =
rock =
scissors =
"""

#if player_1_name
