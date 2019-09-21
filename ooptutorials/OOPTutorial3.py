# OOP Tutorial 3
# Methods: self - normal, cls - Class methods, nothing - static
#normal method is a function related to the class instance
# ->> e.g. change some instance attribute etc.
#class method is a functions related to the class itself
# ->> e.g. make class function is inside Class definition
import datetime


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amount

    @classmethod
    # can be used as alternative constructor
    def from_string(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee.from_string('Fox-Horse-90000')

Employee.set_raise_amount(5)
# emp_1.apply_raise()
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
