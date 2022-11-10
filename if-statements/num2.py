#!/usr/bin/python3
from calendar import monthrange
import datetime

time = datetime.datetime.now()
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month_name = input("Enter a month: ").lower().strip()

try:
    if month_name == 'february':
        num_days = " 28 or 29"
    else:
        num_days = monthrange(time.year, months[month_name])[1]
    print(f"{month_name} has {num_days} days")
except KeyError:
    print("Invalid month")