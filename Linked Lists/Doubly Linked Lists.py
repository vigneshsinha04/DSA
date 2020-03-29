class Node():
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList():
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self,data):
		new_Node = Node(data)
		if self.head == None:
			self.head = new_Node
			self.tail = self.head
			self.length = 1
		else:
			self.tail.next = new_Node
			new_Node.prev = self.tail
			self.tail = new_Node
			self.length +=1

	def prepend(self, data):
		new_Node = Node(data)
		self.head.prev = new_Node
		new_Node.next = self.head
		self.head = new_Node
		self.length+=1

	def insert(self,index,data):
		if index == 0:
			self.prepend(data)
			return

		if index > self.length-1:
			self.append(data)
			return

		i = 0
		new_Node = Node(data)
		leader = self.head

		while i<self.length:
			if i == index-1:
				holder = leader.next
				leader.next = new_Node
				new_Node.next = holder
				new_Node.prev = leader
				holder.prev = new_Node
				self.length+=1
			i+=1
			leader = leader.next

	def remove(self,index):
		if index == 0:
			self.head = self.head.next
			self.head.prev = None
			self.length -=1
			return
		if index == self.length-1:
			self.tail = self.tail.prev
			self.tail.next = None
			self.length -= 1
			return

		i=0
		leader = self.head

		while i<self.length:
			if i == index-1:
				holder = leader.next.next
				leader.next = holder
				holder.prev = leader
				self.length-=1
				break
			i+=1
			leader = leader.next

	def printList(self):
		while self.head!=None:
			print(str(self.head.data), end=' ')
			self.head = self.head.next
		print()
		print('Length is: '+ str(self.length))


double_li = DoublyLinkedList()
double_li.append('Vignesh')
double_li.append('Ajay')
double_li.append('Sumathi')
double_li.prepend('Hector')
double_li.insert(0,'PUBG')
double_li.insert(5,'Python')
double_li.insert(3,'Test')
double_li.remove(3)
print(double_li.head.data)
print(double_li.tail.data)
double_li.printList()