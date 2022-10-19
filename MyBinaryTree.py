class Node:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number
        
        self.right = self.left = None

class BT:
    def __init__(self):
        self.root = None
        self.matches = 0    # The matches attribute indicates whether a match has been found during the search.
                            # For each match found in the phonebook, we increment the matches variable by 1.

    def printEntry(self, node):
        print("Name: " + node.name)
        print("Address: " + node.address)
        print("Number: " + str(node.number))

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

        if int(type) == 1:

            if self.compareNames(node.name, val):
                self.printEntry(node)
                self.matches += 1

        elif int(type) == 2:
            
            if self.compareNames(node.address, val):
                self.printEntry(node)
                self.matches += 1

        elif int(type) == 3:

            try:
                if node.number == int(val):
                    self.printEntry(node)
                    self.matches += 1

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
    
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if root.val == key:
            #4 possibilities

            if not root.left and not root.right:
                return None
            
            if not root.left and root.right:
                return root.right
            
            if not root.right and root.left:
                return root.left
        
        
            