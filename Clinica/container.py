from tkinter import *
import tkinter as tk 
from paciente import Paciente
from profecional import Profecional
from historial_clinico import Historial_clinico
from paciente_tratamiento import Paciente_tratamiento
from cita import Cita
from PIL import Image, ImageTk

class Container(tk.Frame):
    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.controlador = controlador
        self.pack()  
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C5DAE6")
        self.widgets()

    #el tamaño de las ventanas que estan dentro de los botones
    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C5DAE6")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1200x700+120+20")

        top_level.resizable(False, False)

    def paciente(self):
        self.show_frames(Paciente)

    def profecional(self):
        self.show_frames(Profecional)


    def paciente_tratamiento(self):
        self.show_frames(Paciente_tratamiento)
    
    def cita(self):
        self.show_frames(Cita)

    def widgets(self):

        frame1 = tk.Frame(self, bg="#C5DAE6")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        # Parámetros de alineación
        button_width = 240
        button_height = 60
        x_pos = 540
        y_start = 10
        space = 20

        botones = [
            ("Pacientes", self.paciente, "#02457A", 20),
            ("Profesionales", self.profecional, "#02457A", 20),
            ("Paciente en Tratamiento", self.paciente_tratamiento, "#02457A", 15),
            ("Citas Médicas", self.cita, "#02457A", 16)
        ]

        for i, (texto, comando, color, font_size) in enumerate(botones):
            btn = tk.Button(
                frame1,
                text=texto,
                bg=color,
                fg="#ffffff",
                activebackground=color,
                activeforeground="#ffffff",
                font=("Calibri", font_size),
                cursor="hand2",
                command=comando
            )
            btn.place(
                x=x_pos,
                y=y_start + i * (button_height + space),
                width=button_width,
                height=button_height
            )

        # Cargar la imagen
        self.logo_image = Image.open("clinica/imagenes/logo.png")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C5DAE6")
        self.logo_label.place(x=100, y=30)