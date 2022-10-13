# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:16:45 2021

@author: cmartinez
"""


def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


while True:
    year = int(input("Write a year : "))
    if is_leap(year):
        print(f"{year} is a Leap Year")
    else:
        print(f"{year} is NOT a Leap Year")
