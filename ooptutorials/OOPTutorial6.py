# OOP Tutorial 6
# Setter, getter


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @property  # defined as a method, works as an attribute
    def email(self):
        return f'{self.first}.{self.last}@mail.com'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('Georgii', 'Ivannikov')

emp_1.fullname = 'Jim Benhill'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
