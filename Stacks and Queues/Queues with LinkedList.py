class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class Queues():
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first.data

	def enqueue(self, data):
		new_Node = Node(data)
		if self.length == 0:
			self.first = new_Node
			self.last = self.first
			self.length+=1

		else:
			self.last.next = new_Node
			self.last = new_Node
			self.length+=1

	def dequeue(self):
		if self.length == 1:
			self.first = None
			self.length -=1
			return
		popped_item = self.first
		self.first = popped_item.next
		self.length-=1

	def printQueue(self):
		temp = self.first

		while temp !=None:
			print(temp.data,end=' --> ')
			temp = temp.next
		print()
		print('Length: '+ str(self.length))

queue = Queues()
queue.enqueue('Vignesh')
queue.enqueue('Ajay')
queue.enqueue('Sumathi')
queue.enqueue('Python')
queue.dequeue()
print(queue.peek())
queue.printQueue()