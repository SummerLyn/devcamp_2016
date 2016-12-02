
"""
create a randomly generated computer number then take a user input number (as an int)
and check if the user guessed the number right. If they did, print a congrats message,
if they didn't print how far off they were off by.

Example
number = 21
user guess = 10

print "sorry off by 11"
(hint look up up built in function abs())

"""
import random



random_computer_number = random.randint(0, 1000)
user_number_guess = int(input("Choose a whole number between 0 and 1000. >> "))

if user_number_guess == random_computer_number:
    print("Congrats!")

elif user_number_guess != random_computer_number:
    print("Good guess, but you are off by", abs(random_computer_number - user_number_guess))
