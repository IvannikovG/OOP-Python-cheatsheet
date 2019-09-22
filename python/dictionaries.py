
student = {"name": 'John', 'age': 25, 'courses': ['Math', 'CS']}
print(student.get('age'))
print(student.get('phone'))
print(student.get('phone', 'Not found'))
student['phone'] = '555-5555'
print(student)
student.update({'name': 'Jane', 'age': 23})
print(student)
del student['name']
print(student)

for key in student.keys():
	print(key)

print(student.items()) #seq of elements (key: value)

for x, y in student.items():
	print(x, y)