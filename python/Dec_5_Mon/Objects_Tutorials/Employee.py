class Employee:

    num_of_employees =0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Summer', 'Bryant', 100000)
emp_2 = Employee('Pete', 'Stewart', 80000)

print(Employee.num_of_employees)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)
#print(Employee.__dict__)



print(emp_1.email)
print(emp_2.email)

#These 2 print statements do the same thing
#print(emp_1.fullname())
#print(Employee.fullname(emp_1))

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
