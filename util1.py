from unicodedata import name
import MyBinaryTree
import time

class Utility:
    def __init__(self):
        self.tree = MyBinaryTree.BT()

    def printTree(self):
        print('Printing the tree')
        self.tree.printTree(self.tree.root)
    
    def greetUser(self):
        print('Welcome to the Phonebook')

        print('------------------------')

        time.sleep(1)
        print('The following commands are available:')
        time.sleep(1)
        print('store')
        time.sleep(1)
        print('search')
        time.sleep(1)
        print('remove')
        time.sleep(1)
        print('print')
        time.sleep(1)

        print('Type your command and press enter.')

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

        self.tree.matches = 0

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
    
        if self.tree.matches == 0:
            print('Nothing found!')
        
    def delete(self):
        print('Enter:')
        print('1 to delete by name')
        print('2 to delete by address')
        print('3 to delete by number')

        option = input()

        self.tree.matches = 0

        if option == "1":
            print("Enter name to delete: ")
            val = input()
            self.tree.deleteNode(self.tree.root, val)
        
        elif option == "2":
            print("Enter address to delete: ")
            val = input()
            self.tree.deleteNode(self.tree.root, val)
        
        elif option == "3":
            print("Enter number to delete: ")
            val = input()
            self.tree.deleteNode(self.tree.root, val)
        
        print('Contact deleted, if it existed.')