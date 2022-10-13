# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:10:44 2021

@author: cmartinez
"""
# from random import seed
from random import random

# seed()

sString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lLen = len(sString) - 1
for i in range(1, 15):
    NumRandom = int(lLen * random())
    print(f"Random number {i:02d} is {sString[NumRandom]}")
