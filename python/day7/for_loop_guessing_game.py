"""
For loop guessing game
Have a computer generated number between 1 and 20 (outside the loop)

next using a for loop give the user 10 chances to guess the number
if the number is guessed right print some message and break out of the loop
"""
import random

number_guess_counter = 0
computer_number = random.randint(1,20)
#print(computer_number)
for i in range(1,11):
    user_guess = int(input("Guess a number between 1 and 20. >> "))

    if user_guess != computer_number:
        number_guess_counter +=1
        print("Guess again. ")

    if number_guess_counter == 10:

        print("Game Over!")

        break

    if user_guess == computer_number:
        print("Good Job!")

        break
