# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:16:45 2021

@author: cmartinez
"""
from tkinter import *
import math as m

# from random import seed
from random import randint


class Window(Frame):
    N = 30
    W = 800
    H = 800
    R = min(W, H) / 2.2
    X0 = (W / 2, H / 2)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.canv = Canvas(width=self.W, height=self.H)
        self.canv.pack()
        self.wheel()

    def wheel(self):
        Colores = ["red", "green", "blue", "cyan", "magenta", "black", "gray",
                   "darkgray", "lightgray", "brown", "lime", "orange", "purple", "pink", "violet"]
        a = [i * m.pi * 2 / self.N for i in range(self.N)]
        x = [
            (self.X0[0] + self.R * m.cos(a[i]),
             self.X0[1] + self.R * m.sin(a[i]))
            for i in range(self.N)
        ]
        for i in range(self.N - 1):
            for j in range(i + 1, self.N):
                self.canv.create_line(
                    x[i][0],
                    x[i][1],
                    x[j][0],
                    x[j][1],
                    fill=Colores[randint(0, len(Colores)-1)],
                )


# seed()
root = Tk()
app = Window(root)
root.mainloop()
