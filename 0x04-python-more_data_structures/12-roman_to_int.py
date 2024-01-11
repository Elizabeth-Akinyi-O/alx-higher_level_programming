#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    # define all the available roman numbers using roman_num
    # roman_d is roman number && roman_n is roman integer
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_n = 0
    # loop and convert the roman num into an integer
    for a in range(len(roman_string)):
        if a > 0 and roman_d[roman_string[a]] > roman_d[roman_string[a - 1]]:
            roman_n += roman_d[roman_string[a]] - 2 * \
                        roman_d[roman_string[a - 1]]
        else:
            roman_n += roman_d[roman_string[a]]
    return roman_n
