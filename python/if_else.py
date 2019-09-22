
language = 'Python'

if language == 'Python':
	print('cond was true!')
elif language == 'Clojure':
	print('and clojure!')
else:
	print('No match')

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin page')
else:
	print('Bad Creds..')

a = [1, 2, 3]
print(id(a))
b = [1, 2, 3]
print(id(b))
#is -> (id(a) == id(b)), but they are equal nevertheless

condition = "g" # for empty ones -> false
if condition:
	print('Evaluated to True')
else:
	print('Evaluate to False')

