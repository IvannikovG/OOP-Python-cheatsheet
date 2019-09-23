import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    #print(state['name'], state['abbreviation'])
    # prints out python object
    del state['area_codes']
    print(state)

# let`s remove smth from the json and write it to another file
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)
