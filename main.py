#!/usr/bin/env python 

import util1

def main():

    x = util1.Utility() # Creating an instance of the Utility class, contained in the util1.py file.
    x.greetUser() # Greet the user.

    # A loop that continuously asks for commands until 'quit' is entered.

    while True:
        s = input()
        if s == "quit":
            break

        if s == "print":
            x.printTree()
        
        if s == "store":         # The respective commands in the utility class are called.
            x.store()

        if s == "search":
            x.search()

        if s == "remove":
            x.delete()

        print("Enter a command: ")

if __name__ == "__main__":
    main()