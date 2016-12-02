# Take the first and last letter of the string and replace the middle part of
# the word with the lenght of every other letter.

user_input_fun = input(" Give me a fun word. >>")

#user_input_shorter = input("Enter in a shorter word. >>")

if len(user_input_fun) < 3:
    print("Error!")

else:
    print(user_input_fun[0] + str(len(user_input_fun)- 2) + user_input_fun[len(user_input_fun)- 1])
