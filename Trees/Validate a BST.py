class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_Node = Node(data)
        if self.root == None:
            self.root = new_Node
        else:
            curr_Node = self.root
            while True:
                if data < curr_Node.data:
                    if curr_Node.left == None:
                        curr_Node.left = new_Node
                        return
                    else:
                        curr_Node = curr_Node.left

                if data > curr_Node.data:
                    if curr_Node.right == None:
                        curr_Node.right = new_Node
                        return
                    else:
                        curr_Node = curr_Node.right

    def lookup(self,data):
        curr_Node = self.root
        while True:
            if curr_Node == None:
                return False
            if data == curr_Node.data:
                return True
            elif data < curr_Node.data:
                curr_Node = curr_Node.left
            else:
                curr_Node = curr_Node.right

    def printTree(self):
        if self.root != None:
            self.traverse(self.root)

    def traverse(self, curr_Node):
        if curr_Node != None:
            self.traverse(curr_Node.left)
            print(str(curr_Node.data))
            self.traverse(curr_Node.right)

    def inorder(self, curr_Node, mylist):
        if curr_Node != None:
            self.inorder(curr_Node.left, mylist)
            mylist.append(curr_Node.data)
            self.inorder(curr_Node.right, mylist)
        return mylist

    # using inorder traversal
    def isBST(self, root):
        if root == None:
            return False

        inorder = self.inorder(root,[])
        for i in range(len(inorder) - 1):
            if inorder[i] > inorder[i+1]:
                return False
        return True



bst = BinarySearchTree()
bst.insert(10)
bst.insert(8)
bst.insert(9)
bst.insert(3)
bst.insert(12)
bst.insert(11)
bst.insert(14)
print(bst.lookup(99))
print(bst.lookup(12))
bst.printTree()
print(bst.isBST(bst.root))