#!/usr/bin/env python 

import util1

def main():

    x = util1.Utility()

    x.greetUser()

    while True:
        s = input()
        if s == "quit":
            break

        if s == "print":
            x.printTree()
        
        if s == "store":
            x.store()

        if s == "search":
            x.search()

if __name__ == "__main__":
    main()