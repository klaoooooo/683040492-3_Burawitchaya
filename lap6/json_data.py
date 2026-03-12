import json

with open('lap5-5/student.json', 'r', encoding='utf-8') as f:
    data = json.load(f)    # parses JSON → Python dict/list

print(data['name'])           # 'Alice'
print(data['score'])          # 92  (int, not string)
print(data['courses'][0])     # 'Math'
print(data['address']['city']) # 'Bangkok'

student = {
    'name': 'Alice',
    'score': 92,
    'passed': True,
    'courses': ['Math', 'Physics', 'CS']
}

with open('lap5-5/student.json', 'w', encoding='utf-8') as f:
    json.dump(student, f, indent=4)  