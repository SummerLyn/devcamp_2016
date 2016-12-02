"""
Taking a user input as an integer and create a dictionary that contains the numbers 1 to n
as the keys and the values being the square of its keys where n is the user inputted integer.

For Example:

user enters the number 5 it will print the following dictionary
{1: 1, 2: 4, 3:9, 4:16, 5:25}

"""
numbers_square = {}

user_input = int(input("Please enter in an integer... >> "))

for num in range(1, (user_input + 1)):
    numbers_square[num] = num**2

print(numbers_square)
