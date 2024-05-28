import csv

csv_dict = [
    {'branch': 'cse', 'cgpa': '7.5', 'name': 'sunny', 'year': '1'},
    {'branch': 'ece', 'cgpa': '9.5', 'name': 'Yessu', 'year': '1'},
    {'branch': 'it', 'cgpa': '8.5', 'name': 'sravs', 'year': '2'}
]

# field names

fields = ['name', 'branch', 'cgpa', 'year']
with open('university.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(csv_dict)
