from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import tkcalendar as tc
from modelo.paciente_tratamientoDao import PersonaTratamiento, guardarDatoPersonaTratamiento, editarDatoPersonaTratamiento, listarPersonaTratamiento, listarCondicionPersonaTratamiento, eliminarPersonaTratamiento
from modelo.pacienteDao import listarPaciente
from modelo.tratamientoDao import listarTratamiento

class Paciente_tratamiento(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master.geometry("900x500")  # Tamaño amplio para la tabla
        self.Id_paciente_tratamiento = None
        self.pacientes = listarPaciente()
        self.tratamientos = listarTratamiento()
        self.camposPacienteTratamiento()
        self.deshabilitar()
        self.tablaPacienteTratamiento()
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=200)

    def camposPacienteTratamiento(self):
        # Labels
        labels = ["Paciente:", "Tratamiento:", "Fecha Inicio:", "Fecha Fin:", "Observaciones:"]
        for i, text in enumerate(labels):
            lbl = tk.Label(self, text=text, bg="#C6D9E3", fg="black")
            lbl.config(font=("Arial", 15, "bold"))
            lbl.grid(column=0, row=i, padx=10, pady=5, sticky="e")

        # Combobox Paciente
        self.svPaciente = tk.StringVar()
        self.comboPaciente = ttk.Combobox(self, textvariable=self.svPaciente, state="readonly", width=28, font=("Arial", 15))
        self.comboPaciente['values'] = [f"{p[1]} {p[2]} {p[3]}" for p in self.pacientes]
        self.comboPaciente.grid(column=1, row=0, padx=10, pady=5)

        # Combobox Tratamiento
        self.svTratamiento = tk.StringVar()
        self.comboTratamiento = ttk.Combobox(self, textvariable=self.svTratamiento, state="readonly", width=28, font=("Arial", 15))
        self.comboTratamiento['values'] = [t[1] for t in self.tratamientos]
        self.comboTratamiento.grid(column=1, row=1, padx=10, pady=5)

        self.svFechaInicio = tk.StringVar()
        self.entryFechaInicio = tk.Entry(self, textvariable=self.svFechaInicio, width=30, font=("Arial", 15))
        self.entryFechaInicio.grid(column=1, row=2, padx=10, pady=5)

        self.svFechaFin = tk.StringVar()
        self.entryFechaFin = tk.Entry(self, textvariable=self.svFechaFin, width=30, font=("Arial", 15))
        self.entryFechaFin.grid(column=1, row=3, padx=10, pady=5)

        self.svObservaciones = tk.StringVar()
        self.entryObservaciones = tk.Entry(self, textvariable=self.svObservaciones, width=30, font=("Arial", 15))
        self.entryObservaciones.grid(column=1, row=4, padx=10, pady=5)

        # Botones CRUD
        self.btnNuevo = tk.Button(self, text="Nuevo", command=self.habilitar,
                                  width=12, font=("Arial", 12, "bold"), bg="#5763D3", fg="white")
        self.btnNuevo.grid(column=0, row=5, padx=5, pady=5)

        self.btnGuardar = tk.Button(self, text="Guardar", command=self.guardarPacienteTratamiento,
                                    width=12, font=("Arial", 12, "bold"), bg="#5763D3", fg="white")
        self.btnGuardar.grid(column=1, row=5, padx=5, pady=5)

        self.btnCancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar,
                                     width=12, font=("Arial", 12, "bold"), bg="#5763D3", fg="white")
        self.btnCancelar.grid(column=2, row=5, padx=5, pady=5)

        self.btnSalir = tk.Button(self, text="Salir", command=self.volver,
                                  width=12, font=("Arial", 12, "bold"), bg="#458948", fg="white")
        self.btnSalir.grid(column=3, row=7, padx=10, pady=15, sticky="e")

        # Botón para gestionar tratamientos
        self.btnGestionarTratamiento = tk.Button(self, text="Gestionar Tratamientos", command=self.gestionarTratamiento,
                                                 width=20, font=("Arial", 12, "bold"), bg="#0F5688", fg="white")
        self.btnGestionarTratamiento.grid(column=2, row=1, padx=10, pady=5)

        # Botón Calendario para Fecha Inicio
        self.btnCalendarioInicio = tk.Button(self, text="Calendario", command=self.vistaCalendarioInicio,
                                             width=12, font=("Arial", 12, "bold"),
                                             fg="#DAD5D6", bg="#27937E", cursor="hand2", activebackground="#BF1AE9")
        self.btnCalendarioInicio.grid(column=2, row=2, padx=5, pady=5)

        # Botón Calendario para Fecha Fin
        self.btnCalendarioFin = tk.Button(self, text="Calendario", command=self.vistaCalendarioFin,
                                          width=12, font=("Arial", 12, "bold"),
                                          fg="#DAD5D6", bg="#27937E", cursor="hand2", activebackground="#BF1AE9")
        self.btnCalendarioFin.grid(column=2, row=3, padx=5, pady=5)

    def guardarPacienteTratamiento(self):
        paciente_nombre = self.svPaciente.get()
        tratamiento_nombre = self.svTratamiento.get()
        paciente_id = next((p[0] for p in self.pacientes if f"{p[1]} {p[2]} {p[3]}" == paciente_nombre), None)
        tratamiento_id = next((t[0] for t in self.tratamientos if t[1] == tratamiento_nombre), None)

        paciente_tratamiento = PersonaTratamiento(
            paciente_id,
            tratamiento_id,
            self.svFechaInicio.get(),
            self.svFechaFin.get(),
            self.svObservaciones.get()
        )
        if self.Id_paciente_tratamiento is None:
            guardarDatoPersonaTratamiento(paciente_tratamiento)
        else:
            editarDatoPersonaTratamiento(paciente_tratamiento, self.Id_paciente_tratamiento)
        self.deshabilitar()
        self.tablaPacienteTratamiento()

    def habilitar(self):
        self.Id_paciente_tratamiento = None
        self.svPaciente.set("")
        self.svTratamiento.set("")
        self.svFechaInicio.set("")
        self.svFechaFin.set("")
        self.svObservaciones.set("")

        self.comboPaciente.config(state="readonly")
        self.comboTratamiento.config(state="readonly")
        self.entryFechaInicio.config(state="normal")
        self.entryFechaFin.config(state="normal")
        self.entryObservaciones.config(state="normal")

        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")

    def deshabilitar(self):
        self.Id_paciente_tratamiento = None
        self.svPaciente.set("")
        self.svTratamiento.set("")
        self.svFechaInicio.set("")
        self.svFechaFin.set("")
        self.svObservaciones.set("")

        self.comboPaciente.config(state="disabled")
        self.comboTratamiento.config(state="disabled")
        self.entryFechaInicio.config(state="disabled")
        self.entryFechaFin.config(state="disabled")
        self.entryObservaciones.config(state="disabled")

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")

    def volver(self):
        self.winfo_toplevel().destroy()

    def tablaPacienteTratamiento(self, where=""):
        if len(where) > 0:
            self.listaPacienteTratamiento = listarCondicionPersonaTratamiento(where)
        else:
            self.listaPacienteTratamiento = listarPersonaTratamiento()

        self.tabla = ttk.Treeview(
            self,
            column=('Paciente', 'Tratamiento', 'Fecha Inicio', 'Fecha Fin', 'Observaciones')
        )
        self.tabla.grid(column=0, row=6, columnspan=4, sticky="nsew")

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(column=4, row=6, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='Id')
        self.tabla.heading('#1', text='Paciente')
        self.tabla.heading('#2', text='Tratamiento')
        self.tabla.heading('#3', text='Fecha Inicio')
        self.tabla.heading('#4', text='Fecha Fin')
        self.tabla.heading('#5', text='Observaciones')

        self.tabla.column('#0', width=40)
        self.tabla.column('#1', width=80)
        self.tabla.column('#2', width=80)
        self.tabla.column('#3', width=200)
        self.tabla.column('#4', width=400)

        for pt in self.listaPacienteTratamiento:
            # pt[0]=id, pt[1]=id_persona, pt[2]=id_tratamiento, pt[3]=fecha_inicio, pt[4]=fecha_fin, pt[5]=observaciones
            paciente_nombre = next((f"{p[1]} {p[2]} {p[3]}" for p in self.pacientes if p[0] == pt[1]), pt[1])
            tratamiento_nombre = next((t[1] for t in self.tratamientos if t[0] == pt[2]), pt[2])
            self.tabla.insert('', 0, text=pt[0], values=(paciente_nombre, tratamiento_nombre, pt[3], pt[4], pt[5]))

        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.btnEditar = tk.Button(self, text="Editar", command=self.editarPacienteTratamiento,
                                   width=20, font=("Arial", 12, "bold"), bg="#38256F", fg="white")
        self.btnEditar.grid(row=7, column=0, padx=10, pady=5)

        self.btnEliminar = tk.Button(self, text="Eliminar", command=self.eliminarDatoPacienteTratamiento,
                                     width=20, font=("Arial", 12, "bold"), bg="#83CF10", fg="white")
        self.btnEliminar.grid(row=7, column=1, padx=10, pady=5)

    def editarPacienteTratamiento(self):
        try:
            self.Id_paciente_tratamiento = self.tabla.item(self.tabla.selection())['text']
            paciente_nombre = self.tabla.item(self.tabla.selection())['values'][0]
            tratamiento_nombre = self.tabla.item(self.tabla.selection())['values'][1]
            fecha_inicio = self.tabla.item(self.tabla.selection())['values'][2]
            fecha_fin = self.tabla.item(self.tabla.selection())['values'][3]
            observaciones = self.tabla.item(self.tabla.selection())['values'][4]

            # Asegura que el nombre existe en el combobox de pacientes
            if paciente_nombre in self.comboPaciente['values']:
                self.svPaciente.set(paciente_nombre)
            else:
                self.svPaciente.set("")

            # Asegura que el nombre existe en el combobox de tratamientos
            if tratamiento_nombre in self.comboTratamiento['values']:
                self.svTratamiento.set(tratamiento_nombre)
            else:
                self.svTratamiento.set("")

            self.svFechaInicio.set(fecha_inicio)
            self.svFechaFin.set(fecha_fin)
            self.svObservaciones.set(observaciones)
            self.comboPaciente.config(state="readonly")
            self.comboTratamiento.config(state="readonly")
            self.entryFechaInicio.config(state="normal")
            self.entryFechaFin.config(state="normal")
            self.entryObservaciones.config(state="normal")
            self.btnGuardar.config(state="normal")
            self.btnCancelar.config(state="normal")
        except Exception as e:
            messagebox.showerror("Editar", f"Error al editar registro\n{e}")

    def eliminarDatoPacienteTratamiento(self):
        try:
            self.Id_paciente_tratamiento = self.tabla.item(self.tabla.selection())['text']
            eliminarPersonaTratamiento(self.Id_paciente_tratamiento)
            self.tablaPacienteTratamiento()
            self.Id_paciente_tratamiento = None
        except:
            messagebox.showerror("Eliminar", "Error al eliminar registro")

    def vistaCalendarioInicio(self):
        calendario = Toplevel(self)
        calendario.title("Seleccionar Fecha de Inicio")
        calendario.resizable(0, 0)
        calendario.geometry("350x300")
        calendario.config(bg='#C6D9E3')

        svCalendario = tk.StringVar(value="01/01/2024")
        calendar = tc.Calendar(calendario,
                               selectmode='day',
                               year=2024, month=1, day=1,
                               locale='es_ES',
                               textvariable=svCalendario,
                               background='#777777',
                               foreground='#FFFFFF',
                               headersbackground='#B6DDFE',
                               cursor='hand2',
                               date_pattern='dd/mm/yyyy')
        calendar.pack(pady=22)

        def enviarFecha():
            self.svFechaInicio.set(svCalendario.get())
            calendario.destroy()

        btnSeleccionar = tk.Button(calendario, text="Seleccionar", command=enviarFecha,
                                   width=12, font=("Arial", 12, "bold"), bg="#158645", fg="white")
        btnSeleccionar.pack(pady=10)

    def vistaCalendarioFin(self):
        calendario = Toplevel(self)
        calendario.title("Seleccionar Fecha de Fin")
        calendario.resizable(0, 0)
        calendario.geometry("350x300")
        calendario.config(bg='#C6D9E3')

        svCalendario = tk.StringVar(value="01/01/2024")
        calendar = tc.Calendar(calendario,
                               selectmode='day',
                               year=2024, month=1, day=1,
                               locale='es_ES',
                               textvariable=svCalendario,
                               background='#777777',
                               foreground='#FFFFFF',
                               headersbackground='#B6DDFE',
                               cursor='hand2',
                               date_pattern='dd/mm/yyyy')
        calendar.pack(pady=22)

        def enviarFecha():
            self.svFechaFin.set(svCalendario.get())
            calendario.destroy()

        btnSeleccionar = tk.Button(calendario, text="Seleccionar", command=enviarFecha,
                                   width=12, font=("Arial", 12, "bold"), bg="#158645", fg="white")
        btnSeleccionar.pack(pady=10)

    def gestionarTratamiento(self):
        top = Toplevel(self)
        top.title("Gestionar Tratamientos")
        top.geometry("1100x500")  # Más ancho que alto
        top.resizable(False, False)
        top.config(bg="#C6D9E3")

        # Label + Entry
        lbl = tk.Label(top, text="Nombre Tratamiento:", bg="#C6D9E3", font=("Arial", 12, "bold"))
        lbl.pack(pady=5)
        svNombre = tk.StringVar()
        entryNombre = tk.Entry(top, textvariable=svNombre, font=("Arial", 12))
        entryNombre.pack(pady=5)

        lblDesc = tk.Label(top, text="Descripción:", bg="#C6D9E3", font=("Arial", 12, "bold"))
        lblDesc.pack(pady=5)
        svDesc = tk.StringVar()
        entryDesc = tk.Entry(top, textvariable=svDesc, font=("Arial", 12))
        entryDesc.pack(pady=5)

        # Treeview
        tabla = ttk.Treeview(top, columns=("ID", "Nombre", "Descripción"), show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Nombre", text="Nombre Tratamiento")
        tabla.heading("Descripción", text="Descripción")
        tabla.column("ID", width=20)
        tabla.column("Nombre", width=200)
        tabla.column("Descripción", width=400)
        tabla.pack(expand=True, fill="both", pady=10)

        def cargarTabla():
            from modelo.tratamientoDao import listarTratamiento
            tabla.delete(*tabla.get_children())
            for t in listarTratamiento():
                tabla.insert("", "end", values=(t[0], t[1], t[2]))

        cargarTabla()

        # Guardar (nuevo registro)
        def guardarTrat():
            if svNombre.get() == "":
                messagebox.showwarning("Atención", "El nombre no puede estar vacío")
                return
            from modelo.tratamientoDao import Tratamiento, guardarDatoTratamiento
            trat = Tratamiento(svNombre.get(), svDesc.get())
            guardarDatoTratamiento(trat)
            svNombre.set("")
            svDesc.set("")
            self.tratamientos = listarTratamiento()
            self.comboTratamiento['values'] = [t[1] for t in self.tratamientos]
            cargarTabla()

        # Editar (actualizar seleccionado)
        def editarTrat():
            try:
                item = tabla.selection()[0]
                trat_id, _, _ = tabla.item(item, "values")
                if svNombre.get() == "":
                    messagebox.showwarning("Atención", "El nombre no puede estar vacío")
                    return
                from modelo.tratamientoDao import Tratamiento, editarDatoTratamiento
                editarDatoTratamiento(Tratamiento(svNombre.get(), svDesc.get()), trat_id)
                svNombre.set("")
                svDesc.set("")
                self.tratamientos = listarTratamiento()
                self.comboTratamiento['values'] = [t[1] for t in self.tratamientos]
                cargarTabla()
            except:
                messagebox.showerror("Editar Tratamiento", "Seleccione un tratamiento para editar")

        # Eliminar
        def eliminarTrat():
            try:
                item = tabla.selection()[0]
                trat_id, nombre, _ = tabla.item(item, "values")
                confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar '{nombre}'?")
                if confirmar:
                    from modelo.tratamientoDao import eliminarTratamiento
                    eliminarTratamiento(trat_id)
                    self.tratamientos = listarTratamiento()
                    self.comboTratamiento['values'] = [t[1] for t in self.tratamientos]
                    svNombre.set("")
                    svDesc.set("")
                    cargarTabla()
            except:
                messagebox.showerror("Eliminar Tratamiento", "Seleccione un tratamiento para eliminar")

        # Seleccionar fila → mostrar datos en Entry
        def seleccionarFila(event):
            try:
                item = tabla.selection()[0]
                _, nombre, desc = tabla.item(item, "values")
                svNombre.set(nombre)
                svDesc.set(desc)
            except:
                pass

        tabla.bind("<<TreeviewSelect>>", seleccionarFila)

        # Frame de botones
        frame_btns = tk.Frame(top, bg="#C6D9E3")
        frame_btns.pack(pady=10)

        btnGuardar = tk.Button(frame_btns, text="Guardar", command=guardarTrat,
                               bg="#2EBA69", fg="white", font=("Arial", 12, "bold"), width=12)
        btnGuardar.grid(row=0, column=0, padx=5)

        btnEditar = tk.Button(frame_btns, text="Editar", command=editarTrat,
                              bg="#3890DC", fg="white", font=("Arial", 12, "bold"), width=12)
        btnEditar.grid(row=0, column=1, padx=5)

        btnEliminar = tk.Button(frame_btns, text="Eliminar", command=eliminarTrat,
                                bg="#6FC432", fg="white", font=("Arial", 12, "bold"), width=12)
        btnEliminar.grid(row=0, column=2, padx=5)

        btnSalir = tk.Button(frame_btns, text="Salir", command=top.destroy,
                             bg="#151774", fg="white", font=("Arial", 12, "bold"), width=12)
        btnSalir.grid(row=0, column=5, padx=5)

        # Botón Nuevo
        def nuevoTrat():
            svNombre.set("")
            svDesc.set("")
            tabla.selection_remove(tabla.selection())

        btnNuevo = tk.Button(frame_btns, text="Nuevo", command=nuevoTrat,
                             bg="#158645", fg="white", font=("Arial", 12, "bold"), width=12)
        btnNuevo.grid(row=0, column=4, padx=5)

        # Botón Cancelar
        def cancelarTrat():
            svNombre.set("")
            svDesc.set("")
            tabla.selection_remove(tabla.selection())

        btnCancelar = tk.Button(frame_btns, text="Cancelar", command=cancelarTrat,
                                bg="#8A0000", fg="white", font=("Arial", 12, "bold"), width=12)
        btnCancelar.grid(row=0, column=3, padx=5)

