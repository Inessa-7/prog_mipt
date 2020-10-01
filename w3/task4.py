import json


with open('1.json', 'r') as f:
    a = json.loads(f.read())

a['glossary']['GlossDiv']['GlossList']['GlossEntry']['week'] = 3

with open('answer_task4_1.txt', 'w') as ouf:
    json.dump(a, ouf)

with open('answer_task4_2.txt', 'w') as ouf:
    json.dump(a, ouf)
