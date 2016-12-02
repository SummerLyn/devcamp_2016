"""
Create a program asks for a _single_ English word and translates it to **Pig Latin**.
It prints out the input word and the resulting translation like the example below.

Rules:

1. If the first letter is a consonant, move it to the end.
1. Add "ay" to the end of that.
1. If the first letter is a vowel, just ad "yay" to the end.

"""

single_word = input("Let's do some Pig Latin! Choose a single English word. >> ").lower()
vowels = list('aeiouy')
starting_letter = single_word[0]
ending_letters = single_word[1:]
ay_ending = "ay"
yay_ending = "yay"

if single_word[0] in vowels:
    pig_word = starting_letter + ending_letters + str(yay_ending)
else:
    pig_word = ending_letters + starting_letter + str(ay_ending)
print(pig_word)
