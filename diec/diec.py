#!/usr/bin/python3
"""Python script that converts Roman numerals to integers"""

def roman_to_int(roman_string):
    """Converts Roman numerals to integers"""
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_dict[roman_string[i]] > roman_dict[roman_string[i - 1]]:
            num += roman_dict[roman_string[i]] - 2 * roman_dict[roman_string[i - 1]]
        else:
            num += roman_dict[roman_string[i]]
    return num
