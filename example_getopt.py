#!/usr/bin/env python
# getopt module example, feel free to copy the code chunk
# Note: DO NOT name this script getopt.py or getopt.pyc, or else error will occur

# getopt is the module for command line option inputs

import sys, getopt

def main(argv):
    a, b, c = "", "", ""
    try:
        opts, args = getopt.getopt(argv, "ha:b:c:", ["aname=", "bname=", "cname="])
    except getopt.GetoptError:
        print("Error message, this pops up when an undocumented input is entered")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("This is a test function with inputs -a, -b, -c, or --aname/bname/cname")
            sys.exit(2)
        elif opt in ("-a", "--aname"):
            a = arg
        elif opt in ("-b", "--bname"):
            b = arg
        elif opt in ("-c", "--cname"):
            c = arg
    print("The three inputs are: ")
    print("Input a: ", a)
    print("Input b: ", b)
    print("Input c: ", c)

if __name__ == "__main__":
    main(sys.argv[1:])
