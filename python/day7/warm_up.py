'''
1) Create random generated list with 100 number anywhere from 100 to 100-90
Using a for loop

2) write another for loop to iterate over that list and count the number of even
numbers in the list.
'''
import random

random_list = []

index = 0
for i in range(0,100):
    random_numbers = random.randint(100,1000)
    random_list.insert(i,random_numbers)
    index +=1
print(random_list)

# for loop to create the even numbers and count how many
even_numbers = 0
'''
for k in range(0, len(random_list)):
    if random_list[k] % 2 == 0:
        even_numbers += 1
print(even_numbers)

'''
for k in random_list:
    if k % 2 == 0:
        even_numbers += 1
print(even_numbers)
