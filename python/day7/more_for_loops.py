#use for range loop and then for each loop to print
word_list = ["a","b","c","d","e","f","g"]

# for each loop
for i in word_list:
    print(i)

# for loop using range

for i in range(0,len(word_list)):
    print(word_list[i])


#get user input
#loop through string and print value
#if value is a vowel break out of loop

user_input = input("Give me a word. >> ")
vowels = ("aeiou")
#can also cast as a list - list("aeiou")

for i in user_input:
    if i in vowels:

        break

    print(i)
