import csv

# Writing — csv.DictWriter
rows = [
    {'name': 'Alice', 'score': 92, 'grade': 'A'},
    {'name': 'Bob',   'score': 78, 'grade': 'B'},
]
with open('lap5-5/students.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'score', 'grade'])
    writer.writeheader()
    writer.writerows(rows)