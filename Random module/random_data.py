import random

first_names = ['John', 'Jane', 'Jada', 'Troy', 'Davis', 'Karl', 'Nina', 'Samuel', 'Brad', 'Tomas', 'Janine', 'Roberto', 'Carlos',
               'Charles', 'Joe', 'Mary', 'Sarah', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson',
              'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Carlos', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park',
                'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Braavos', 'Rivia', 'Narnia', 'King`s Landing', 'Winterfell',
               'High Peak', 'Hammerfell', 'Moscweiler', 'Saint-Jonas', 'Silent Hill', 'Pan-Land']

regions = ['Moscow region', 'Taymyr region', 'Kavkaz region',
           'North region', 'South region', 'Yakutia region', 'Central region']

with open('random_people.txt', 'a') as new_file:
    for num in range(5):

        first = random.choice(first_names)
        last = random.choice(last_names)
        phone = f'+7-495-{random.randint(100, 999)}-{random.randint(1000, 9999)}'
        email = f'{first.lower()}{last.lower()}@mail.ru'
        street = random.choice(street_names)
        street_num = random.randint(1, 60)
        city = random.choice(fake_cities)
        address = f'{street} St. {street_num}, {city}, {random.choice(regions)}'
        zipcode = random.randint(100000, 200000)

        new_file.write(f'\n{first} {last}\n{email}\n{phone}\n{address}\nZipcode - {zipcode}\n')

new_file.close()
