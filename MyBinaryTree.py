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
        
            elif node.right is not None:
                self.insert(node.right, name, address, number)

            else:
                node.left = Node(name, address, number)

    def printTree(self, node):
        if node is not None:
            print(node.name, node.address, node.number)
            self.printTree(node.left)
            self.printTree(node.right)
        
    def search(self, node, val, type):

        if self.compareNames(node.name, val):
            print("Name: " + node.name)
            print("Address: " + node.address)
            print("Number: " + str(node.number))

        if self.compareNames(node.address, val):
            print("Name: " + node.name)
            print("Address: " + node.address)
            print("Number: " + str(node.number))
        
        try:
            if node.number == int(val):
                print("Name: " + node.name)
                print("Address: " + node.address)
                print("Number: " + str(node.number))

        except ValueError:
            pass

        if node.left:
            self.search(node.left, val, type)

        if node.right:
            self.search(node.right, val, type)

    def compareNames(self, a, b):
        return a.lower() == b.lower()
    
    def compareAddresses(self, a, b):
        return a.lower() == b.lower()

    def compareNumbers(self, a, b):
        return a == b
