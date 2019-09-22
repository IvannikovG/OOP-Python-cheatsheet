def hello_func1(): #pass is used to leave it for now
	pass

def hello_func(greeting, name="You"):
	return f'{greeting} {name}'

print(hello_func('hey'))

courses = ['Math', 'Art']
info = {'name': 'Jonh', 'age': 22}
#positional and keyweord args
def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
#returns a tuple from the first and from the second arg makes dictionary
student_info(*courses, **info) #it unpacks it

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	"""Return True for leap years, False if it is not. #Docstring"""

	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	"""Return nimber of days in that month in that year"""

	if not 1 <= month <= 12:
		return 'Invalid month'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print(days_in_month(2017, 2))






