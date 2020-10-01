import csv


with open('table.csv', 'r') as inf:
    reader = csv.reader(inf, delimiter=';')
    data = []
    for i in reader:
        if i != []:
            data.append(i)

data[0].append('my_col')
for i in range(1, len(data)):
    data[i].append('True')

with open('new_col.csv', 'w') as ouf:
    writer = csv.writer(ouf, delimiter=';')
    writer.writerows(data)
