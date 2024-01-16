from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from threading import Thread

from random import sample

"""
Definición método para la generación de la contraseña
"""
def generar():
    longitud = passwordSize.get()
    abc_min = "abcdefghijklmnopqrstuvwxyz"
    abc_may = abc_min.upper()
    num = "1234567890"
    car = "{}[]/*+;:,._-Ç&%()=$#@!¡¿?"

    sec = abc_min + abc_may + num + car

    passUn = sample(sec, int(longitud))
    passRes = "".join(passUn)

    instrucciones2 = Label(root, text=passRes)
    instrucciones2.grid(row=3, column=1)

    root.clipboard_clear()
    root.clipboard_append(passRes)

    return passRes

"""
Definición método con información
"""
def popup1():
    MessageBox.showinfo("Youtube Downloader Version", "Version: 1.0\n"
                                                          "Autor: javiiie09")


root = Tk()                         #Definición Interfaz de la ventana
root.config(bd=60)                  #Tamaño de la ventana
root.title("Generador De Contraseñas")    #Nombre de la ventana

"""
Barra superior de opciones
"""
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

"""
Submenú
"""
menubar.add_cascade(label="Archivo", menu=helpmenu)
helpmenu.add_command(label="Versión", command=popup1)
helpmenu.add_command(label="Salir", command=root.destroy)

"""
Cuadro para introducir URL del video y botones de descarga
"""
instrucciones = Label(root, text="Introduce el tamaño de la contraseña")
instrucciones.grid(row=0, column=1)

passwordSize = Entry(root)
passwordSize.grid(row=1, column=1)

boton = Button(root, text="Generar Contraseña", command=generar)
boton.grid(row=2, column=1)


root.mainloop()
