class Graph:
	def __init__(self):
		self.numnodes = 0
		self.adjacentLists = {}

	def __str__(self):
		return str(self.__dict__)

	def addNode(self, node):
		self.adjacentLists[node] = []
		self.numnodes += 1

	def addEdge(self, node1, node2):
		self.adjacentLists[node1].append(node2)
		self.adjacentLists[node2].append(node1)

	def showConnections(self):
		for k,v in self.adjacentLists.items():
			print(k,v)

graph = Graph()
graph.addNode('0')
graph.addNode('1')
graph.addNode('2')
graph.addNode('3')
graph.addNode('4')
graph.addNode('5')
graph.addNode('6')
graph.addEdge('0','1')
graph.addEdge('0','2')
graph.addEdge('1','2')
graph.addEdge('1','3')
graph.addEdge('2','4')
graph.addEdge('3','4')
graph.addEdge('4','5')
graph.addEdge('5','6')
# print(graph)
graph.showConnections()