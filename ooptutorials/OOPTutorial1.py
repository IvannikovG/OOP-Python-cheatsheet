# Python OOP Tutorial 1
# method - function, associated with a Class
# attribute - values, specific to a Class and saved there


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@gmail.com'

    def fullname(self):
        return f'{self.first} {self.last}'


# We can add something into the existing instance by
# emp_1.first = 'Georgii'
emp_1 = Employee('Georgii', 'Ivannikov', 50000)

print(emp_1.fullname())
