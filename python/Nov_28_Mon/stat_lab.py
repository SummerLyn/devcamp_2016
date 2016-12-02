
"""
Write a function that returns a list of numbers from 1 to 100

using that list as an input for all the following functions

create all the following functions and doctest for each one before moving to the next
    Max
    Min
    Range
    Sum
    Average

Next create another function that generates a list of 100 random numbers between 1 and 1000

Use this list for the following function as input

create a stat function that takes a list as an input and prints the Max, min, Range, Sum,
Average using the functions you created

call this function in the main method
"""



def create_list():
    numbers = []
    for i in range(1,101):
        numbers.append(i)
    return numbers
    #numbers = list(range(1,101))
number_list = create_list()


#print(number_list)

def get_max(number_list):
    '''
    >>> number_list = create_list()
    >>> get_max(number_list)
    43
    '''
    return(max(number_list))

#print(get_max(number_list))

def get_min(number_list):
    '''
    >>> numbers_list = create_list()
    >>> get_min(number_list)
    23
    '''
    return(min(number_list))


def get_range(number_list):
    '''
    Inputs: list of numbers
    Usage: gets the range of a list
    Output: Max value of list minus min value of list

    >>> numbers_list = create_list()
    >>> get_range(number_list)
    98
    '''
    return get_max(number_list) - get_min(number_list)
