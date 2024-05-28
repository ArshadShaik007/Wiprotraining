import json

#Using json.load
with open('samplejson.json', 'r') as f:
    data = json.load(f)

print(data)
