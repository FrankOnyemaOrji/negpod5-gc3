#!/usr/bin/python3
"""Python script that converts Roman numerals to integers"""

def roman_to_int(r):
    """Converts Roman numerals to integers"""
    if (r == 'I'):
        return 1
    elif (r == 'V'):
        return 5
    elif (r == 'X'):
        return 10
    elif (r == 'L'):
        return 50
    elif (r == 'C'):
        return 100
    elif (r == 'D'):
        return 500
    elif (r == 'M'):
        return 1000
    else:
        return -1

def romanFigures():
    res = 0
    i = 0
    while (i < len(str)):
        """Get value of symbol s[i]"""
        s1 = roman_to_int(str[i])
        if (i+1 < len(str)):
            s2 = roman_to_int(str[i+1])
            if (s1 >= s2):
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1
        return res



print(romanFigures("III"))
print(romanFigures("LVIII"))
print(romanFigures("MCMXCIV"))
print(romanFigures("XIX"))
print(romanFigures("XVII"))