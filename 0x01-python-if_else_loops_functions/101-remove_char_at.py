#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    a = 0
    for character in str:
        if a != n:
            new += str[a]
        a += 1
    return (new)
