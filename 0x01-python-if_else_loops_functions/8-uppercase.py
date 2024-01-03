#!/usr/bin/python3
def uppercase(str):
    for i in str: #i is the iterator
        temp = i #temp is the temporary file
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(i) - 32)
        print("{}".format(temp), end='')
    print()
