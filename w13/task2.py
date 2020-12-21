import pickle
from collections import ChainMap
import json


class MyClass:
	def __init__(self, name, surname, is_hired):
			self.name = name
			self.surname = surname
			self.is_hired = is_hired

	
def my_func():
	return 'Hello'

	
ser = []

try:
	with open('list_of_serializables.md', 'r') as inf:
		ser.append(pickle.dumps(inf))
except TypeError as err:
	print(err)

ser.extend([pickle.dumps(range(10)), pickle.dumps(print), 
			pickle.dumps(json.dumps), pickle.dumps(ChainMap), 
			pickle.dumps(my_func), pickle.dumps(MyClass)])
			
for i in pickle.loads(ser[0]):
		print(i)

pickle.loads(ser[1])('print is  working')

print(pickle.loads(ser[2])(MyClass('name', 'sur', True).__dict__))

print(pickle.loads(ser[3])())

print(pickle.loads(ser[4])())

print(pickle.loads(ser[5])('name', 'surname', False))