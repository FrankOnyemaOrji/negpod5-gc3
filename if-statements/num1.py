#!/usr/bin/python3

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Weird")

else: 
    if n >= 2 and n <= 5:
        print(" Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")
    else:
        print("Conditions not provided in the statement")