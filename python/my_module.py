
print('Imported my_module...')

test = 'Test string'

def find_index(to_search, target):
	'''Find the index of a value'''
	for i, value in enumerate(to_search):
		if value == target:
			return 1

	return -1