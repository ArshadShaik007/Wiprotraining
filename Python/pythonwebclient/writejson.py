import json

# using json.dump() used to write the data to json file

person_dict = {
    "name": "sunny",
    "languages": ["English", "japanese"],
    "married": True,
    "age": 22
}

with open('writingtojson.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
