
#create a guessing gae where the computer generates a number and the user has
#guesses to get the right answer


import random
guess_count = 0

# Printing instructions to the game
print("""Hello! I,(the computer), am thinking of a random number between 1 and 1000.
You have 5 guesses to get it right!""" )

computer_number = random.randint(1, 1001)
print(computer_number)





while guess_count <= 5:
    user_guess = int(input("Guess a number. >> "))
    guess_count += 1
    print(guess_count)

    if guess_count == 5:
        print("You're out of guesses. Womp womp.")
        break
    # update a function give guesses on how close they are "hot/cold"
    #if user_guess > 50 and user_guess

    if user_guess == computer_number:
        print(computer_number, "Congrats, you smarty pants!")
        break
