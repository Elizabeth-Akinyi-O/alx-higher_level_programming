#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp = my_list[:]
    if idx < 0:
        return (tmp)
    if idx > len(my_list) - 1:
        return (tmp)
    tmp[idx] = element
    return (tmp)
