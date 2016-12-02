import random as rand

numbers  =[]

def add_to_numbers():
    number = int(input("Enter num: ")
    for i in range(1, number+1):
        numbers.append(i)


def main():
    add_to_numbers()

    print(numbers)

    numbers.append(55)

    print(numbers)

main()
