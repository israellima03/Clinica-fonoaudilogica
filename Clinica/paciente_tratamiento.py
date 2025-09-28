from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Paciente_tratamiento(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="black", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        titulo = tk.Label(self, text="Pacientes en Tratamiento", bg="#dddddd", fg="black", font=("Arial", 18))
        titulo.pack()
        titulo.place(x=5, y=0, width=1090, height=90)

    