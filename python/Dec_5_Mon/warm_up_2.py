'''
write a function that takes a list as an input and returns a dictionary of the
frenquency count for that list to test. Create a list of random numbers from
1- 100 of size 10,000
print the dictionary
'''
import random


def random_list():
    numbers = []
    for i in range(0,10000):
        rand_num = random.randint(1,100)
        numbers.append(rand_num)
    return numbers




def get_frequency(num_list):
    freq_dict = {}

    for i in num_list:
        freq_dict[i] = freq_dict.get(i, 0) + 1

    return freq_dict

def main():
    numbers = random_list()
    print(get_frequency(numbers))


main()
