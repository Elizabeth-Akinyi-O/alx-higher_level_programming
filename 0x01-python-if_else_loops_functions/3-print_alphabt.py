#!/usr/bin/python3
for a in range(97, 123):
    if a in [101, 113]:
        continue
    print("{}".format(chr(a)), end = '')
