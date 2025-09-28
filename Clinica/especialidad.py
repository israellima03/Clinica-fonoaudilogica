from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Especialidad(tk.Frame):
    def __init__(self, parent, controlador):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="dddddd")
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(frame1, text="Especialidades", bg="dddddd", fg="black", font=("Arial", 20))
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)