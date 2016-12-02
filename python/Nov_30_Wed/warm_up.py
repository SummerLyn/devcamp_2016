"""
Implement a function that take as input three variables, and returns the largest of three numbers.
Do this without using the Python max() function!

The goal of this exercise is to think abut some internals that Python normally takes care of for usself.
All you need is some variables and if statements!
"""



def largest_number(num1, num2, num3):
    '''
    Input: takes in three variable Inputs
    Usage: finds the largest of three numbers
    Output: returns the largest of the 3 numbers
    '''


    if (num1 >= num2) and (num2 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2
    else:
        return num3

        # 2 lines of code for same thing
        #numbers = [num1, num2, num3]
        #return sorted(numbers)[len(numbers) - 1]


print(largest_number(3,2,1))
