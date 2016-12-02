"""
List = []
Dictionary = {}
"""

fruits = ["apple", "banana", "pear", "dragon fruit"]



print(fruits)
"""
to print an index print(fruits[2])
"""
print(fruits[0])

print(fruits[2])

fruits.insert(4, "banana")
#inserts another fruit on index 4
print(fruits)


"""

my_dict = {key: value}

"""

name_address_dict = {"Summer": "1234 1st St", "Johnboy": "543 Happy Ave"}

print(name_address_dict)

#print(name_address_dict["Summer"])

name_address_dict["George"] = "888 road drive"

print(name_address_dict)

#SET - a same thing as list but doesn't allow doubles


my_list = ["apple", "banana", "orange", "banana", "apple"]

print(my_list)

my_set = set(my_list)

print(my_set)


class_ages = {"ajaz": 37}

class_ages["Emmanual"] = 24

print(class_ages)

class_ages_list = [21,23,23,24,56,11,23]

class_ages_set =set(class_ages_list)

print(class_ages_list)
print(class_ages_set)
