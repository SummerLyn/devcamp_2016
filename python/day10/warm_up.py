"""
Take a user input and return the last four letter of the word with hastags replacing letters
"""

user_word = input("Good day! Give me a word! >> ")
word_length = len(user_word)
new_word = ''



if word_length <= 4:

    new_word = "#" * word_length
else:

    last_four = user_word[word_length - 4: word_length]
    hashtags = "#" * (word_length - 4)
    new_word = hashtags + last_four

print(new_word)
