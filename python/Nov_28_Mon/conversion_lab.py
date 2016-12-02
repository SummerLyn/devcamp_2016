# this will give me a fail in my doctest
# command line$  python3 -m doctest conversion_lab.py

"""
>>> convert_feet_to_inches(1)
15

>>> convert_inches_to_feet(24)
6

"""


# a function that converts feet to yards


#def convert_feet_to_yard(feet):
"""
Input: will take an integer
Usage: this function will convert this number from feet to yards
Output: will result in yards
"""
#        result = round(feet/3,2)
#        return result


def convert_feet_to_inches(feet):
    """
    Input:
    Usage:
    Output:
    """
    result = round(feet*12,2)
    return result

def convert_inches_to_feet(inches):
    result = round(inches/12,2)
    return result

def main():
    which_convert = int(input("Press 1 to convert feet to inches. Press 2 to convert inches to feet. >> "))

    if which_convert == 1:
            feet = int(input("Enter how many feet to convert to inches. >> "))
            print(convert_feet_to_inches(feet))
    else:
        inches = int(input("Enter how many inches to convert to feet. >> "))
        print(convert_inches_to_feet(inches))

main()
