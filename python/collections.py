
courses = ['History', 'Math', 'Physics', 'CompSci']

courses_2 = ['Art', 'Education']
print(courses[:2])
courses.insert(0, courses_2)
courses.extend(courses_2) #adds at the end
courses.remove(['Art', 'Education'])
courses.pop() # returns the last value, does not change the coll
print(courses[0:])

nums = [1, 2, 3, 4, 5]
nums.sort(reverse=True) # sorts and changes the coll
sorted_courses = sorted(courses)
print(max(sorted_courses)) # returns max

print(courses.index("Art")) # returns the index of our searched word


for item in courses:
	print(item)

for index, course in enumerate(courses): #can enumerate items in a coll
	print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

#Immutable - tuples

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

print(tuple_1[0])

#Sets, unordered, only unique members, they are VERY unordered

cs_courses = {'History', 'Math', 'Physics', 'Physics'}
cs_courses1 = {'History', 'Math', "a cat"}
print(cs_courses)
print('Math' in cs_courses)
print(cs_courses.union(cs_courses1))