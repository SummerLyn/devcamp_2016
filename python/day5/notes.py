"""range slicing

import random

apple = "Green apple"

apple[1:4]
#you'd get ee

[1:], [1:5], [:8]
#####

vowels = ['a', 'e', 'i', 'o', 'u']
letter = random.choice(vowels)

print(letter)
"""
###
#other built in functions
"""
isalpha() #returns if everything in string is a letter
"""

word = input("Enter a word. >> ")

if word.isalpha():
    print("true")
else:
    print("False")

#isdigit()

number = input(" Enter a number. >> ")

if number.isdigit():
    print("true")
else:
    print("false")
