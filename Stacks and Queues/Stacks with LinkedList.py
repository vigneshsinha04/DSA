class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self,data):
        new_Node = Node(data)

        if self.length == 0:
            self.top = new_Node
            self.bottom = self.top
            self.length+=1
        else:   
            holder = self.top
            self.top = new_Node
            self.top.next = holder
            self.length+=1

    def pop(self):
        holder = self.top
        self.top = self.top.next
        self.length-=1
        return holder.data

    def printStack(self):
        if self.length == 1:
            print(self.top.data)
        else:
            temp = self.top
            while temp != None:
                print(temp.data, end=' --> ')
                temp = temp.next
            print()
            print('Length: '+ str(self.length))

stack = Stack()
stack.push('Vignesh')
stack.push('Ajay')
stack.push('Sumathi')
stack.push('Python')
print(stack.peek())
print(stack.pop())
stack.printStack()
print(stack.top.data, stack.bottom.data)