'''
Implement the random.choice function to randomly choose an item from the list.
'''

import random


def random_item(item_list):
    rand_index = random.randint(0, len(item_list) -1)

    return item_list[rand_index]



def main():
    numbers = [1,2,3,4,5,6,7,8]
    print(random_item(numbers))

main()
