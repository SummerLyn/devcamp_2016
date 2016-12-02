### using break and continue
"""
num_list = list(range(1,11))
# num_list = [1,2,3,4,5,6,7,8,9,10] same thing
for i in range(0,len(num_list)):
    if num_list[i] % 2 == 0:

        continue
    else:
        print(num_list)

for i in range(0,len(num_list)):
    if num_list[i] == 5:

        break

    print(num_list[i])

"""
### find the sum of the list
import random

numbers = []

index = 0

for i in range(0,100):
    num = random.randint(100,1000)
    numbers.insert(index,num)
    index += 1

num_sum = 0

for i in range(0,len(numbers)):
    num_sum += numbers[i]
print(num_sum)

'''
### IMPORTANT ###
for i in range(0,2)
    print(i)
i will = 0
#it's going to print i as a number
#use use the [] the get the value from a list


#called a for each loop - i will always be the value of the index
numbers = [3,8,9,20,35]
    for i in numbers:
        #i 0 will be 3

word = "classroom"
    for i in word:
        print(i)

### using range - i will always be the start of the index
for i in range(0,len(word)):
    print(word[i])
