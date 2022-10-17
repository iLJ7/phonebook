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
        print('If you would like to search for a number, :')