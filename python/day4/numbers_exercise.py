"""
List generation:

generate a list from two random numbers:
the lower random number being from 3 to 10, the higher random number being from 50 to 100

next print the max, min, and sum of the list.

Part 2

Use % division to return the middle element of the list.
"""
import random

lower_random_number = random.randint(3,10)
higher_random_number = random.randint(50,100)

random_numbers = list(range(lower_random_number, (higher_random_number)))
# range will render 2 numbers while a list for the range will render the
# numbers from the lower_random_number to the higher_random_number

print('The list:{}'.format(random_numbers))

max_number = max(random_numbers)
min_number = min(random_numbers)
sum_num_list = sum(random_numbers)

print('Min Number: {}'.format(min_number))
print('Max Number: {}'.format(max_number))
print('Sum of Number List: {}'.format(sum_num_list))

"""
Part 2

Use % division to return the middle element of the list.
"""

#division:
# // returns type = int, (2, always rounds down)
# / returns type = float, (2.8183520262)

# determine if the list length is even, return the 2 (or more if you want) middle numbers.

if len(random_numbers) % 2 == 0:
    half_1 = random_numbers[len(random_numbers)//2-1]
    half_2 = random_numbers[len(random_numbers)//2]
    print('Your median of both halves: {}, {}'.format(half_2, half_1))
else:
    #returns just one median number
    median = random_numbers[len(random_numbers)//2]
    print('Median: {}'.format(median))
