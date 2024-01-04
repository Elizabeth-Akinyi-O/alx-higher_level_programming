#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_int = 0
    for a in range(1, len(argv)):
        sum_int += int(argv[a])
    print("{}".format(sum_int))
