# Javascript Object notation
# Nowadays has no real relation to JS

import json

people_string = '''
{
    "people": [
    {
    "name": "John Smith",
    "phone": "615-555-7164",
    "emails": ["johnsmith@mail.ru", "john.smith@work-place.com"],
    "has_license": false
    },
    {
     "name": "Jane Doe",
     "phone": "560-555-5153",
     "emails": null,
     "has_license": true
    }
  ]
}
'''

data = json.loads(people_string)
# loads a string
# -> converts into python datatypes, in this case - dictionary
# -> also converts elements, null -> None

# lets remove phone and form a new dict

for person in data['people']:
    del person['phone']

# that has changed out python object

# lets make JSON from python object
new_string = json.dumps(data, indent=2)
# for each level indent it twice
print(new_string)

# load method loads the file
with open('states.json') as f:
    data1 = json.load(f)
