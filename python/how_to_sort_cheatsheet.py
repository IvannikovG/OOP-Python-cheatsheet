
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
print('Already sorted:', s_li)
# returns a new sorted list
# sorted accepts the second parameter -> how to sort
# ->
print('Reversed:', sorted(li, reverse=True))

li.sort()
# will change the original coll. returns already sorted
# works as sorted

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple:', s_tup)

di = {'name': 'George', 'job': 'Visual Coputing', 'age': None, 'os': 'mac'}

print(sorted(di))  # will sort by key

nums = [-6, -5, -4, 1, 2, 3]

print(sorted(nums, key=abs), 'second arg is a func')


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}-{self.age}${self.salary}'


e1 = Employee('Karl', 23, 70000)
e2 = Employee('Sarah', 26, 80000)
e3 = Employee('Sven', 25, 90000)

employees = [e1, e2, e3]


def e_sort(emp):
    return emp.salary


s_employees = sorted(employees, key=e_sort, reverse=True)
s_employees2 = sorted(employees, key=lambda e: e.name)

print(s_employees2)
