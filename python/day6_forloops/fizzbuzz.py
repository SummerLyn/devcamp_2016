"""
Print all numbers from 1 to 100
If the number is divisible by 3 print FIZZ
If the number is divisible by 5 print BUZZ
If the number is divisible by 3 and 5 print FizzBuzz
"""


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
            print("Fizz")
            
    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)
