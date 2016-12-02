"""
1) Generate a list with 100 items of random numbers from (0,1000) using a for loop
"""

import random
"""
random_list = []

for i in range(0,100):
    random_number = random.randint(0,1000)
    #add list to a list
    random_list.insert(i,random_number)

print(random_list)
"""
"""

2) using a for loop find the max number in the list and
    print "The max number is: " + max numbers
"""
"""
random_list = []

index = 0
for i in range(0,101):
    random_number = random.randint(0,1000)
    #add list to a list
    random_list.insert(index,random_number)
    index += 1
    # find the max number in the random list

max_number = random_list[0] #grabs the very first index in the list

for i in range(0,len(random_list)):
    current_num = random_list[i] # interates through i 

    if current_num > max_number:
        max_number = current_num

print("The max number is: ", max_number)
"""
"""
3) Find the minimum
"""
"""
random_list = []

index = 0
for i in range(0,101):
    random_number = random.randint(0,1000)
    random_list.insert(index, random_number)
    index += 1

min_number = random_list[0]

for i in range(0, len(random_list)):
    current_min_num = random_list[i]

    if current_min_num < min_number:
        min_number = current_min_num
print("The min number is: ", min_number)
"""

"""
4) Find the sum of the entire list
"""

random_list = []
sum_index = 0

for i in range(0,101):
    random_number = random.randint(0,1000)
    #add list to a list
    random_list.insert(i,random_number)

for i in range(0,101):
    sum_index += random_list[i]

print(sum_index)
print(sum(random_list))
