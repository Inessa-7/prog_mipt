import csv


with open('table.csv', 'r') as inf:
    reader = csv.reader(inf, delimiter=';')
    data = []
    for i in reader:
        if i != []:
            data.append(i)

l1 = len(data)
l2 = len(data[0])

data.insert(l1 // 2, ['-200'] * l2)
with open('middle_row.csv', 'w') as ouf:
    writer = csv.writer(ouf, delimiter=';')
    writer.writerows(data)
