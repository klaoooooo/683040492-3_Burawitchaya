import csv

with open('lap5-5/students.csv.', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for i in reader:
        print(i)

