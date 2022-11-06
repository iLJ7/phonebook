import MyBinaryTree
import time

# Our utility class, which facilitates commands on the binary tree.

class Utility:

    # We initialise our tree.
    def __init__(self):
        self.tree = MyBinaryTree.BT() 

    # We call our myBinaryTree print function.
    def printTree(self):
        print('Printing the tree')
        self.tree.printTree(self.tree.root)
    
    # We greet the user.
    def greetUser(self):
        print('Welcome to the Phonebook')

        print('------------------------')

        time.sleep(1)
        print('The following commands are available:')
        time.sleep(1)
        print('print')
        time.sleep(1)
        print('search')
        time.sleep(1)
        print('store')
        time.sleep(1)
        print('remove')
        time.sleep(1)

        print('Enter a command: ')

    # Our store function, which processes input and passes it to the bianry tree insert function.
    def store(self):
        print('Enter name:')
        name = input()

        print('Enter your address: ')
        address = input()

        print('Enter your number: ')
        number = int(input())

        self.tree.insert(self.tree.root, name, address, number)
        print('Inserted')
    
    # Our search function, which passes the relevant data to the recursive search function.
    def search(self):
        print('Enter:')
        print('1 to search by name')
        print('2 to search by number')

        option = input()

        self.tree.matches = 0

        if option == "1":
            print("Enter name to search for: ")
            val = input()
            self.tree.searchName(self.tree.root, val)
        
        elif option == "2":
            print("Enter number to search for: ")
            val = input()
            self.tree.searchNumber(self.tree.root, val)
    
        if self.tree.matches == 0:
            print('Nothing found!')
        
    # Our delete function, which passes the relevant data to the recursive delete function.
    def delete(self):
        print('Enter:')
        print('1 to delete by name')
        print('2 to delete by number')

        option = input()

        if option == "1":
            print("Enter name to delete: ")
            val = input()
            self.tree.deleteNode(self.tree.root, val)
        
        elif option == "2":
            print("Enter number to delete: ")
            val = input()
            self.tree.deleteNode(self.tree.root, val)
        
        print('Contact deleted, if it existed.')