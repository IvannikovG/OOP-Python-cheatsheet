# OOP Tutorial 5
# Magick methods


class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f'{self.first} {self.last}'

    def email(self):
        return f'{self.first}.{self.last}@mail.com'

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount

    def __repr__(self):
        '''allows to REPResent the instance'''
        return f'Employee: {self.first} {self.last} payment:{self.pay}'

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email())


emp_1 = Employee('Georgii', 'Ivannikov', 90000)
emp_2 = Employee('Test', 'Employee', 60000)
emp_3 = Employee('Vishik', 'Sablukova', 85000)
emp_3 = Employee('Natalya', 'Bistan', 8500)

print(repr(emp_3).__len__())
print(emp_3)
