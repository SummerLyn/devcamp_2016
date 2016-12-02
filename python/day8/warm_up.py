"""
Problem 2

Take a string user input and using a for loop
print all the vowels in the string
"""

user_word = input("Give me a word. >> ")
vowels = "aeiou"

"""
for i in user_word:
    if i in vowels:
        print(i)
"""
"""
Problem 3

Take a string user input and using a for loop print all consonants in the string

"""
for k in user_word:
    if k not in vowels:
        print(k)
