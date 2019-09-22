import random

value1 = random.random()
print(value1)
# just a random number between 0 and 1, 0 is inclusive

value2 = random.uniform(1, 10)
print(value2)

value3 = random.randint(1, 6)
print(value3)
# random int values

greetings = ['Hello', 'hi', 'Hey!', 'Howdy', 'Hola']

value4 = random.choice(greetings)
print(value4 + ' George!')
# choise finds a random el from a list

colours = ['Red', 'Green', 'Yellow', 'Black']

results = random.choices(colours, weights=[18, 18, 2, 14], k=10)
# k value - is how many times we want the rand el from the coll
# weights work as probabilities(not the %. These pi add up and each el has pi(el)/pi(cumul))
print(results)

deck = list(range(1, 53))
# print(deck)
random.shuffle(deck)
# print(deck)
# randomly shuffles the coll els

hand = random.sample(deck, k=5)
# random sample of 5 cards from our deck of cards

print(hand)
