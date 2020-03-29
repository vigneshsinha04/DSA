class Stack():
	def __init__(self):
		self.data = []
		self.length = 0

	def __str__(self):
		return str(self.__dict__)

	def peek(self):
		return self.data[self.length-1]

	def push(self,data):
		self.data.append(data)
		self.length += 1		

	def pop(self):
		item = self.data[self.length-1]
		del self.data[self.length-1]
		self.length -= 1
		return item

stack = Stack()
stack.push('Vignesh')
stack.push('Ajay')
stack.push('Sumathi')
stack.push('Python')
print(stack.peek())
print(stack.pop())
print(stack)