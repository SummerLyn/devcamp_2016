"""
Starts With exercise

loop through a list of names or string and add only the values to a list that
start with a user inputted letter

Example

names = ["mathew, "andrew", "tom", "bella", "lisa", "jordan", "mark"]

"""
names = ["mathew" , "andrew", "tom", "bella", "lisa", "jordan", "mark"]
user_name = input("Gimme a letter >> ")
new_list = []

for n in names:
#    print(n[0])
    if n[0] == user_name:
        new_list.append(n)



print(new_list)
