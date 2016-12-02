"""
Using a while loop let a user keep inputing string values
that will be added into a list until they enter the word quit
then exit the loop and print the list
"""
print("""Enter in word word at a time. When you are done,
enter the word quit to exit out of the program.""")

word_list = []

#list_length = len(word_list)

while True:
    user_word = input("What is your word? >>> ")
    word_list.append(user_word)
    if user_word == "quit":
        
        break


print(word_list)
