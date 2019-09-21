# OOP Tutorial 4
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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)  # prev args are handled by parent cls
        self.prog_lang = prog_lang

    def show_lang(self):
        return self.prog_lang


dev_1 = Developer('Georgii', 'Ivannikov', 90000, 'python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
# print(help(Developer))
print(dev_2.fullname())


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ('-->', emp.fullname())


man_1 = Manager("Christian", 'Hjorth', 600000, [dev_1, dev_2])

man_1.print_emps()

print(man_1.email())

print(issubclass(Developer, Employee))
