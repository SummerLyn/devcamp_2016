"""
for _variable___ in ______ :
"""


    #for i in range(0,10):
    #    print(i) #will print 0-9
"""
for i in range(1,101):
    if i % 5 == 0:
        print(i)

for i in range(0,1001):
    print(i)
"""
#getting a sum of a range
num_sum = 0
"""
for i in range(0,101):
    num_sum += i
    #num_sum = num_sum + i
    #is the same thing
    print(num_sum)
"""

#getting sum of only even numbers

for i in range(0,101):
    if i % 2 == 0:
        num_sum += i
print(num_sum)

"""
#getting and printing even numbers
for i in range(0,101):
    if i % 2 == 0:
        print(i)
"""

"""
#adding a number to a list
num_list = []
for i in range(0, 101):
    num_list.insert(i,i)
print(i)

# to add 1 everytime
index = 0
for i in range(200,1000):
    num_list.insert(index, i)
    index += 1
print(num_list)
