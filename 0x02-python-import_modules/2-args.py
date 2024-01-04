#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = len(argv) - 1
    if  a < 1:
        print("{} arguments:".format(a))
    elif a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))

    for b in range(a):
        print("{}: {:s}".format(b + 1, argv[b + 1]))
