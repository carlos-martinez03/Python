# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:31:25 2021

@author: cmartinez
"""

from tkinter import *
from random import random

# seed()
root = Tk()
Width = 1024
Height = 768
canvas = Canvas(root, width=Width, height=Height)
canvas.pack()

Colores = ["red", "blue", "gray", "green", "black"]
for i in range(1500):
    x = int(Width * random())
    y = int(Height * random())
    size = int(20 * random())
    canvas.create_oval(x, y, x + size, y + size, fill=Colores[int(5 * random())])

root.mainloop()
