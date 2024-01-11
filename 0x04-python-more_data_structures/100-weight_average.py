#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    ave = 0
    div = 0
    for tupl in my_list:
        ave += tupl[0] * tupl[1]
        div += tupl[1]
    return float(ave / div)
