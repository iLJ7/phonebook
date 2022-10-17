from unicodedata import name
import MyBinaryTree

class Utility:
    def __init__(self):
        self.tree = MyBinaryTree.BT()

    def printTree(self):
        print('Printing the tree')
        self.tree.printTree(self.tree.root)
    
    def greetUser(self):
        print('Welcome to the Phonebook')
        print("------------------------")

    def store(self):
        print('Enter name:')
        name = input()

        print('Enter your address: ')
        address = input()

        print('Enter your number: ')
        number = int(input())

        self.tree.insert(self.tree.root, name, address, number)
        print('Inserted')
    
    def search(self):
        print('Enter:')
        print('1 to search by name')
        print('2 to search by address')
        print('3 to search by number')

        option = input()

        target = ""

        if option == "1":
            print("Enter name to search for: ")
            val = input()
            self.tree.search(self.tree.root, val, 1)
        
        elif option == "2":
            print("Enter address to search for: ")
            val = input()
            self.tree.search(self.tree.root, val, 2)
        
        elif option == "3":
            print("Enter number to search for: ")
            val = input()
            self.tree.search(self.tree.root, val, 3)
        
        else:
            target = ""

        #if option == "1":
        #    if node.name == val:
        #        print(val)
        
        #if option == "2":
        #    if node.address == val:
        #        print(val)

        #if option == "3":
        #    if node.number == val:
        #       print(val)