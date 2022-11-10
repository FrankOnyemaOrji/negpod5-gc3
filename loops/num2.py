#!/usr/bin/python3

letters = input("Enter a string: ").lower().strip()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for i in letters:
    if i not in vowels:
        print(i, end=" ")
    else:
        continue
