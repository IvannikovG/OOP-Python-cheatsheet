# Python OOP Tutorial 2


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# We can add something into the existing instance by
# emp_1.first = 'Georgii'
emp_1 = Employee('Georgii', 'Ivannikov', 50000)
emp_1.raise_amount = 1.1
emp_1.apply_raise()
print(emp_1.pay)

# Instances take attributes from their Classes.
# Instance variables can be updated
# self means - referring to the class

emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)
# It is possible to change something in the whole Class
