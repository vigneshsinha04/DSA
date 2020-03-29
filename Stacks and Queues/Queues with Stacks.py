class Queue():
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self,data):
		self.instack.append(data)

	def peek(self):
		self.move()
		return self.outstack[-1]

	def dequeue(self):
		self.move()
		self.outstack.pop()

	def move(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())

	def printList(self):
		print(self.outstack)


queue = Queue()
queue.enqueue('Vignesh')
queue.enqueue('Ajay')
queue.enqueue('Sumathi')
queue.enqueue('Python')
print(queue.peek())
queue.dequeue()
queue.printList()
