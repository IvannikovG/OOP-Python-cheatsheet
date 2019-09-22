import datetime

person = {'name': 'Lev', 'age': 234}

sentence1 = 'Hi, my name is {1} and i am {0} years old'.format(
    person['name'], person['age'])
sentence = 'Hi, my name is {} and i am {} years old'.format(
    person['name'], person['age'])
# 0 and 1 are numbers of values that are passed into the format func.
print(sentence)

tag = 'h1'
text = 'This is a headline'
sentence2 = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence2)

sentence2 = 'Hi, my name is {0[name]} and i am {1[age]} years old'.format(
    person, person)
print(sentence2)
sentence3 = 'Hi, my name is {0[0]} and i am {0[1]} years old'.format(
    ['gven', 16])
print(sentence3)


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jack', 22)
sentence4 = 'Hi, my name is {0.name} and i am {0.age} years old'.format(p1)
print(sentence4)

sentence5 = 'Hi, my name is {name} and i am {age} years old'.format(
    name='Jenn', age='30')
print(sentence5)

# Below is the recommended form for dictionaries:

human = {'name': 'Stanis Baratheon', 'age': 44}
sentence6 = 'My name is {name} and i am {age} years old.'.format(**human)
# human is unpacked here
print(sentence6)


for i in range(1, 11):
    sent = 'The value is {:03}'.format(i)
    print(sent)
# in {:} we can padwith {:<this><of this length>}


pi = 3.14159265

sent2 = 'Pi is equal to {:.14f}'.format(pi)
print(sent2)
# some number of decimal places is printed out. if too big number is provided -> pads with 0.


sent3 = '1 MB is equal to {:,.2f} bytes'.format(1000 * 2)
print(sent3)

# Dates
# to puth these %B, %d, %Y - only with documentation
my_date1 = datetime.datetime(2019, 9, 22, 12, 33, 45)

#->2019-09-22 12:33:45

my_date2 = '{:%B %d, %Y}'.format(my_date1)

#->September 22, 2019

print(my_date2)

# March 01, 2016 fell on Tuesday and was the 061 day of the year.
sent4 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
    my_date1)
print(sent4)
