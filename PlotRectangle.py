# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 09:31:25 2021

@author: cmartinez
"""

from tkinter import *


def crear_label():
    Label(root, text="Label creada dinamiamente").pack()


root = Tk()
root.title("Hola Mundo")
root.resizable(1, 1)  # Redimensionar ventana
root.iconbitmap('icono.ico')

frame = Frame(root, width=400, height=300)
frame.pack(fill='x', expand=0)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow", bg="blue", bd=15, relief="ridge")

label = Label(frame, text="Hola mundo x=50,y=100")
# label.pack() #Ajusta automaticamente en el frame
label.place(x=50, y=100)

label2 = Label(frame, text="Hola x=20, y=150")
label2.place(x=20, y=150)

Label(root, text="Otra Eqtiqueta").pack()
Label(root, text="Otra Eqtiqueta2").pack()

Button(root, text="Haz Click", command=crear_label).pack()


#lblNombre = Label(root, text="Nombre ")
#lblNombre.grid(row=0, column=0)
#entryNombre = Entry(root)
#entryNombre.grid(row=0, column=1)

#lblApellidos = Label(root, text="Apellidos ")
#lblApellidos.grid(row=1, column=0)
#entryApellidos = Entry(root)
#entryApellidos.grid(row=1, column=1)


canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_rectangle(50, 50, 450, 450, fill="cyan")
canvas.create_line(20, 275, 480, 275, fill="black")
for i in range(0, 300, 20):
    canvas.create_line(0, 0 + i, 500, 500 - i, fill="red")
canvas.create_oval(60, 60, 440, 440)

root.mainloop()  # Siempre colocar hasta abajo
