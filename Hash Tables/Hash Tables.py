import random
class HashTable():
	def __init__(self):
		self.data= ['None']*50
		self.addressList= []
		self.add = -1

	def __str__(self):
		return str(self.__dict__)

	# Python uses open addressing
	def _hash(self):
		self.add +=1
		return self.add
		# while True:
		# 	add = random.randint(0,49)
		# 	if add not in self.addressList:
		# 		return add


	def set(self, keys, values):
		address = self._hash()
		self.data[address] = [keys, values]
		self.addressList.append(address)

	def get(self, keys):
		for i in self.data:
			if i[0] == keys:
				return i[1]

	def keys(self):
		key_list = []
		for j in self.data:
			key_list.append(j[0])
		return key_list


has = HashTable()
has.set('Vignesh', 1996)
has.set('Hector', 300)
has.set('Ajith', 1976)
has.set('Ajay', 1975)
print(has.get('Ajith'))
print(has.keys())
print(has)