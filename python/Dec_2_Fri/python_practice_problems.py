'''
Question 1:
Write a function which will find all such numbers by 7 but are not a multiple of 5,
between a user inputed lower bound and a user inputed upper bound (both included)


Question 2:
Write a Python function that accepts a string and calculate the number of digits
and letters.

Sample Data: Hello23Hello
Expected output:
Letters 10
Digits 2 -
'''

#Question 1
def main():
    numbers = []
    lower_bound_input = int(input(" Give me your low number. >> "))
    upper_bound_input = int(input(" Give me your high number. >> "))

    for i in range(lower_bound_input, upper_bound_input + 1):
        if i % 5 != 0 and i % 7 == 0:
            numbers.append(i)
    print(numbers)

main()



#Question 2
lett_cout = 0
digit_count = 0
user_input = input("Giv me a number and letter.")
"""
### NEED TO FIX THIS!
def digits_letters(word):
    letters = []
    digits = []

for i in usr_input:
    if i.isalpha():
        lett_cout +=1
    elif i.isdigit():
        digit_count +=1
return(l)
"""
