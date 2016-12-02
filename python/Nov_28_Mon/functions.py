
"""
def add_two_num(num1,num2):
    result = num1 + num2
    return result


number1 = int(input("Enter a number"))
number2 = int(input("Enter another number"))

add_two_num(number1, number2)
"""
'''
name = 'David'

def greeting():
    return 'Hello ' + name


print(greeting())

def main():
    name = 'David'
    print(greeting())
'''

# a function that converts feet to yards


def convert_feet_to_yard(feet):
        result = round(feet/3,2)
        return result


def main():
    feet = int(input("Enter how many feet to convert to yards. >> "))
    print(convert_feet_to_yard(feet))

main()
