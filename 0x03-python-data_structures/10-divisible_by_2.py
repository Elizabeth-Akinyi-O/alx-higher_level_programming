#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    new_list = []
    for a in range(length):
        if my_list[a] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)