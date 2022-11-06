# We create our node class, which models the tree.
# When an instance of the node class is initialised, it is given a name, address and number.
# Its left and right child are set to None.

class Node:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number
        
        self.right = self.left = None

# Our binary tree class models the binary tree.
# When initialised, its root is set to none.

class BT:
    def __init__(self):
        self.root = None
        self.matches = 0    # The matches attribute indicates whether a match has been found during the search.
                            # For each match found in the phonebook, we increment the matches variable by 1.

    # Our node which prints the tree.
    def printEntry(self, node):
        print("Name: " + node.name)
        print("Address: " + node.address)
        print("Number: " + str(node.number))

    # Our recursive insert function.
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

    # Our function to print the entire tree, using preorder traversal.
    def printTree(self, node):
        if node is not None:
            print(node.name, node.address, node.number)
            self.printTree(node.left)
            self.printTree(node.right)
        
    # Our function to search by name.
    def searchName(self, node, val):
        if self.compareNames(node.name, val):
            self.printEntry(node)
            self.matches += 1

        if node.left:
            self.searchName(node.left, val)

        if node.right:
            self.searchName(node.right, val)

    # Our function to search by number.
    def searchNumber(self, node, val):
        if self.compareNumbers(node.number, int(val)):
            self.printEntry(node)
            self.matches += 1

        if node.left:
            self.searchNumber(node.left, val)
        
        if node.right:
            self.searchNumber(node.right, val)

    # A function to compare two strings, to eliminate lowercase/uppercase permutations.
    def compareNames(self, a, b):
        return a.lower() == b.lower()

    # A function to compare two integers.
    def compareNumbers(self, a, b):
        return a == b
    
    # Our recursive delete function.
    def deleteNode(self, node, val):
        if not node:
            return None
        
        if self.compareNames(node.name, val):
            print('Match found')
            if not node.left and not node.right:
                return None
            
            if not node.left and node.right:
                return node.right
            
            if not node.right and node.left:
                return node.left
        
        elif node.left:
            node.left = self.deleteNode(node.left, val)
        
        else:
            node.right = self.deleteNode(node.right, val)
        
        return node