# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:59:25 2021

@author: cmartinez
"""
from random import random

String = ""

for i in range(40):
    String += str(int(random() * 2))

print(String)
