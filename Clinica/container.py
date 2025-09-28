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
        self.config(bg="#C6D9E3")
        self.widgets()

    #el tamaño de las ventanas que estan dentro de los botones
    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1200x700+120+20")

        top_level.resizable(False, False)

    def paciente(self):
        self.show_frames(Paciente)

    def profecional(self):
        self.show_frames(Profecional)

    def historial_clinico(self):
        self.show_frames(Historial_clinico)

    def paciente_tratamiento(self):
        self.show_frames(Paciente_tratamiento)
    
    def cita(self):
        self.show_frames(Cita)

    def widgets(self):

        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)   

        btpaciente = tk.Button(
            frame1,
            text="Pacientes",
            bg="#11407E",         # turquesa pastel
            fg="#ffffff",         # blanco
            activebackground="#43A6B1",
            activeforeground="#ffffff",
            font=("Calibri", 20),
            cursor="hand2",
            command=self.paciente
        )
        btpaciente.place(x=540, y=10, width=240, height=60)

        btprofecional = tk.Button(
            frame1,
            text="Profecionales",
            bg="#F4180C",         # naranja pastel
            fg="#ffffff",         # blanco
            activebackground="#E59500",
            activeforeground="#ffffff",
            font=("Calibri", 20),
            cursor="hand2",
            command=self.profecional
        )
        btprofecional.place(x=540, y=90, width=240, height=60)

        bthistorial_clinico = tk.Button(
            frame1,
            text="Historial Clinico",
            bg="#3A2366",         # lila pastel
            fg="#ffffff",         # blanco
            activebackground="#7C4DFF",
            activeforeground="#ffffff",
            font=("Calibri", 20),
            cursor="hand2",
            command=self.historial_clinico
        )
        bthistorial_clinico.place(x=540, y=170, width=240, height=60)

        btpaciente_tratamiento = tk.Button(
            frame1,
            text="Paciente en Tratamiento",
            bg="#1D9022",         # rosa pastel
            fg="#ffffff",         # blanco
            activebackground="#1D9022",
            activeforeground="#ffffff",
            font=("Calibri", 15),
            cursor="hand2",
            command=self.paciente_tratamiento
        )
        btpaciente_tratamiento.place(x=540, y=250, width=240, height=60)

        btcita = tk.Button(
            frame1,
            text="Citas Médicas",
            bg="#407A7D",         # turquesa pastel
            fg="#ffffff",         # blanco  
            activebackground="#43A6B1",
            activeforeground="#ffffff",
            font=("Calibri", 16),
            cursor="hand2",
            command=self.cita
        )
        btcita.place(x=540, y=330, width=240, height=60)

        # Cargar la imagen
        self.logo_image = Image.open("clinica/imagenes/logo.png")
        self.logo_image = self.logo_image.resize((280, 280))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(frame1, image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=100, y=30)