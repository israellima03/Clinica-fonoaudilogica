from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import tkcalendar as tc
from modelo.citaDoa import Cita as CitaModel, guardarDatoCita, editarDatoCita, listarCita, eliminarCita, listarCondicionCita
from modelo.pacienteDao import listarPaciente
from modelo.trabajadorDao import listarPersonal

class Cita(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master.geometry("400x300")  # Más ancho que alto
        self.Id_cita = None
        self.pacientes = listarPaciente()
        self.profesionales = listarPersonal()
        self.camposCita()
        self.deshabilitar()
        self.tablaCita()
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=200)

    def camposCita(self):
        # Labels
        labels = ["Paciente:", "Profesional:", "Fecha:", "Hora:", "Estado:"]
        for i, text in enumerate(labels):
            lbl = tk.Label(self, text=text, bg="#C6D9E3", fg="black")
            lbl.config(font=("Arial", 15, "bold"))
            lbl.grid(column=0, row=i, padx=10, pady=5, sticky="e")

        # Combobox Paciente
        self.svPaciente = tk.StringVar()
        self.comboPaciente = ttk.Combobox(self, textvariable=self.svPaciente, state="readonly", width=28, font=("Arial", 15))
        self.comboPaciente['values'] = [f"{p[1]} {p[2]} {p[3]}" for p in self.pacientes]  # Nombre completo
        self.comboPaciente.grid(column=1, row=0, padx=10, pady=5)

        # Combobox Profesional
        self.svProfesional = tk.StringVar()
        self.comboProfesional = ttk.Combobox(self, textvariable=self.svProfesional, state="readonly", width=28, font=("Arial", 15))
        self.comboProfesional['values'] = [f"{p[1]} {p[2]} {p[3]}" for p in self.profesionales]
        self.comboProfesional.grid(column=1, row=1, padx=10, pady=5)

        self.svFecha = tk.StringVar()
        self.entryFecha = tk.Entry(self, textvariable=self.svFecha, width=30, font=("Arial", 15))
        self.entryFecha.grid(column=1, row=2, padx=10, pady=5)

        self.svHora = tk.StringVar()
        self.entryHora = tk.Entry(self, textvariable=self.svHora, width=30, font=("Arial", 15))
        self.entryHora.grid(column=1, row=3, padx=10, pady=5)

        self.svEstado = tk.StringVar()
        self.entryEstado = tk.Entry(self, textvariable=self.svEstado, width=30, font=("Arial", 15))
        self.entryEstado.grid(column=1, row=4, padx=10, pady=5)

        # Botón Calendario para fecha
        self.btnCalendario = tk.Button(self, text="Calendario", command=self.vistaCalendario,
                                       width=12, font=("Arial", 12, "bold"),
                                       fg="#DAD5D6", bg="#421361", cursor="hand2", activebackground="#BF1AE9")
        self.btnCalendario.grid(column=2, row=2, padx=5, pady=5)

        # Botones CRUD
        self.btnNuevo = tk.Button(self, text="Nuevo", command=self.habilitar,
                                  width=12, font=("Arial", 12, "bold"), bg="#158645", fg="white")
        self.btnNuevo.grid(column=0, row=5, padx=5, pady=5)

        self.btnGuardar = tk.Button(self, text="Guardar", command=self.guardarCita,
                                    width=12, font=("Arial", 12, "bold"), bg="black", fg="white")
        self.btnGuardar.grid(column=1, row=5, padx=5, pady=5)

        self.btnCancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar,
                                     width=12, font=("Arial", 12, "bold"), bg="red", fg="white")
        self.btnCancelar.grid(column=2, row=5, padx=5, pady=5)

        self.btnSalir = tk.Button(self, text="Salir", command=self.volver,
                                  width=12, font=("Arial", 12, "bold"), bg="#10C019", fg="white")
        self.btnSalir.grid(column=3, row=7, padx=10, pady=15, sticky="e")

    def guardarCita(self):
        # Obtener el ID del paciente y profesional seleccionado
        paciente_nombre = self.svPaciente.get()
        profesional_nombre = self.svProfesional.get()
        paciente_id = next((p[0] for p in self.pacientes if f"{p[1]} {p[2]} {p[3]}" == paciente_nombre), None)
        profesional_id = next((p[0] for p in self.profesionales if f"{p[1]} {p[2]} {p[3]}" == profesional_nombre), None)

        cita = CitaModel(
            paciente_id,
            profesional_id,
            self.svFecha.get(),
            self.svHora.get(),
            self.svEstado.get()
        )
        if self.Id_cita is None:
            guardarDatoCita(cita)
        else:
            editarDatoCita(cita, self.Id_cita)
        self.deshabilitar()
        self.tablaCita()

    def habilitar(self):
        self.Id_cita = None
        self.svPaciente.set("")
        self.svProfesional.set("")
        self.svFecha.set("")
        self.svHora.set("")
        self.svEstado.set("")

        self.comboPaciente.config(state="readonly")
        self.comboProfesional.config(state="readonly")
        self.entryFecha.config(state="normal")
        self.entryHora.config(state="normal")
        self.entryEstado.config(state="normal")

        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")

    def deshabilitar(self):
        self.Id_cita = None
        self.svPaciente.set("")
        self.svProfesional.set("")
        self.svFecha.set("")
        self.svHora.set("")
        self.svEstado.set("")

        self.comboPaciente.config(state="disabled")
        self.comboProfesional.config(state="disabled")
        self.entryFecha.config(state="disabled")
        self.entryHora.config(state="disabled")
        self.entryEstado.config(state="disabled")

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")

    def volver(self):
        self.winfo_toplevel().destroy()

    def tablaCita(self, where=""):
        if len(where) > 0:
            self.listaCita = listarCondicionCita(where)
        else:
            self.listaCita = listarCita()

        self.tabla = ttk.Treeview(
            self,
            column=('Id_persona', 'Id_personal', 'Fecha', 'Hora', 'Estado')
        )
        self.tabla.grid(column=0, row=6, columnspan=4, sticky="nsew")

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(column=4, row=6, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='Id')
        self.tabla.heading('#1', text='Id Paciente')
        self.tabla.heading('#2', text='Id Personal')
        self.tabla.heading('#3', text='Fecha')
        self.tabla.heading('#4', text='Hora')
        self.tabla.heading('#5', text='Estado')

        self.tabla.column('#0', width=40, anchor="center")
        self.tabla.column('#1', width=100)
        self.tabla.column('#2', width=100)
        self.tabla.column('#3', width=120)
        self.tabla.column('#4', width=120)
        self.tabla.column('#5', width=100)

        for c in self.listaCita:
            self.tabla.insert('', 0, text=c[0], values=(c[1], c[2], c[3], c[4], c[5]))

        # Botones de tabla
        self.btnEditar = tk.Button(self, text="Editar Cita", command=self.editarCita,
                                   width=20, font=("Arial", 12, "bold"), bg="#1E0075", fg="white")
        self.btnEditar.grid(row=7, column=0, padx=10, pady=5)

        self.btnEliminar = tk.Button(self, text="Eliminar Cita", command=self.eliminarDatoCita,
                                     width=20, font=("Arial", 12, "bold"), bg="#8A0000", fg="white")
        self.btnEliminar.grid(row=7, column=1, padx=10, pady=5)

    def editarCita(self):
        try:
            self.Id_cita = self.tabla.item(self.tabla.selection())['text']
            paciente_id = self.tabla.item(self.tabla.selection())['values'][0]
            profesional_id = self.tabla.item(self.tabla.selection())['values'][1]
            # Buscar nombre por ID
            paciente_nombre = next((f"{p[1]} {p[2]} {p[3]}" for p in self.pacientes if p[0] == paciente_id), "")
            profesional_nombre = next((f"{p[1]} {p[2]} {p[3]}" for p in self.profesionales if p[0] == profesional_id), "")
            self.svPaciente.set(paciente_nombre)
            self.svProfesional.set(profesional_nombre)
            self.svFecha.set(self.tabla.item(self.tabla.selection())['values'][2])
            self.svHora.set(self.tabla.item(self.tabla.selection())['values'][3])
            self.svEstado.set(self.tabla.item(self.tabla.selection())['values'][4])
            self.habilitar()
        except:
            messagebox.showerror("Editar Cita", "Error al editar cita")

    def eliminarDatoCita(self):
        try:
            self.Id_cita = self.tabla.item(self.tabla.selection())['text']
            eliminarCita(self.Id_cita)
            self.tablaCita()
            self.Id_cita = None
        except:
            messagebox.showerror("Eliminar Cita", "Error al eliminar cita")

    def vistaCalendario(self):
        self.calendario = Toplevel(self)
        self.calendario.title("Seleccionar Fecha")
        self.calendario.resizable(0, 0)
        self.calendario.config(bg='#C6D9E3')

        self.svCalendario = tk.StringVar(value="01/01/2024")
        self.calendar = tc.Calendar(self.calendario,
                                   selectmode='day',
                                   year=2024, month=1, day=1,
                                   locale='es_ES',
                                   textvariable=self.svCalendario,
                                   background='#777777',
                                   foreground='#FFFFFF',
                                   headersbackground='#B6DDFE',
                                   cursor='hand2',
                                   date_pattern='dd/mm/yyyy')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column=0)

        # Enviar fecha seleccionada al campo de fecha
        def enviarFecha(*args):
            self.svFecha.set(self.svCalendario.get())
            self.calendario.destroy()

        btnSeleccionar = tk.Button(self.calendario, text="Seleccionar", command=enviarFecha,
                                   width=12, font=("Arial", 12, "bold"), bg="#158645", fg="white")
        btnSeleccionar.grid(row=2, column=0, pady=10)

        # Actualiza fecha cuando se selecciona en el calendario
        self.svCalendario.trace_add('write', lambda *args: self.svFecha.set(self.svCalendario.get()))
