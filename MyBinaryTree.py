class Node:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number
        
        self.right = self.left = None

class BT:

    def __init__(self):
        self.root = None

    def insert(self, node, name, address, number):
        if node is None:
            self.root = Node(name, address, number)
    
        else:
            if node.left is not None:
                self.insert(node.left, name, address, number)
        
            else:
                node.left = Node(name, address, number)

    def printTree(self, node):
        if node is not None:
            print(node.name, node.address, node.number)
            self.printTree(node.left)
            self.printTree(node.right)
        