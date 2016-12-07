from Employee import Employee


print(Employee.num_of_employees)
employee_1 = Employee('Luke', 'Skywalker', 100)
print(Employee.num_of_employees)

print(employee_1.pay)
print(employee_1.__dict__)
employee_1.raise_amount = 1.05
employee_1.apply_raise()

print(employee_1.pay)
print(employee_1.__dict__)

employee_2 = Employee('Dane','Jones',1000)
print(Employee.num_of_employees)


for i in Employee.employee_list:
    print(i.pay)
