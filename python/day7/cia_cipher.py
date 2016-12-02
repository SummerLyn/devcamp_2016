"""
Create a CIA Cipher
"""
# this puts a sting into a dictionary
alpha_as_string = "abcdefghijklmnopqrstuvwxyz"

alphabet = list(alpha_as_string)

alpha_dictionary = {}

for i in range(0,len(alphabet)):
    alpha_dictionary[alphabet[i]] = i

# print(alpha_dictionary)

# When a user puts in a word
### Basic
real_word = input("What is your 3 letter single word. >> ")
letter_spots = int(input("Enter in a number. >> "))


real_word_index = alpha_dictionary[real_word[0]]
if (real_word_index + letter_spots) > 25:
    new_word = alphabet[(real_word_index + letter_spots) % 26]
else:
    new_word = alphabet[(real_word_index + letter_spots)]


real_word_index_1 = alpha_dictionary[real_word[1]]
if (real_word_index_1 + letter_spots) > 25:
    new_word_1 = alphabet[(real_word_index_1 + letter_spots) % 26]
else:
    new_word_1 = alphabet[(real_word_index_1 + letter_spots)]


real_word_index_2 = alpha_dictionary[real_word[2]]
if (real_word_index_2 + letter_spots) > 25:
    new_word_2 = alphabet[(real_word_index_2 + letter_spots) % 26]
else:
    new_word_2 = alphabet[(real_word_index_2 + letter_spots)]

print(new_word + new_word_1 + new_word_2)
