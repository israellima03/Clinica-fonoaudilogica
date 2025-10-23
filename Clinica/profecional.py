from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from modelo.trabajadorDao import Personal as PersonalModel, guardarDatoPersonal, listarPersonal, listarCondicionPersonal, editarDatoPersonal, eliminarPersonal
from modelo.especialidadDao import Especialidad, guardarDatoEspecialidad, listarEspecialidad

class Profecional(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.Id_personal = None
        self.camposPersonal()
        self.deshabilitar()
        self.tablaPersonal()
        self.grid_columnconfigure(0, minsize=150)
        self.grid_columnconfigure(1, minsize=200)

    def camposPersonal(self):
        # Labels
        labels = ["Nombre:", "Apellido Paterno:", "Apellido Materno:", "Carnet:", 
                  "Edad:", "Especialidad:", "Telefono:"]
        for i, text in enumerate(labels):
            lbl = tk.Label(self, text=text, bg="#C6D9E3", fg="black")
            lbl.config(font=("Arial", 15, "bold"))
            lbl.grid(column=0, row=i, padx=10, pady=5, sticky="e")

        # Entradas
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre, width=30, font=("Arial", 15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5)

        self.svApPaterno = tk.StringVar()
        self.entryApPaterno = tk.Entry(self, textvariable=self.svApPaterno, width=30, font=("Arial", 15))
        self.entryApPaterno.grid(column=1, row=1, padx=10, pady=5)

        self.svApMaterno = tk.StringVar()
        self.entryApMaterno = tk.Entry(self, textvariable=self.svApMaterno, width=30, font=("Arial", 15))
        self.entryApMaterno.grid(column=1, row=2, padx=10, pady=5)

        self.svCarnet = tk.StringVar()
        self.entryCarnet = tk.Entry(self, textvariable=self.svCarnet, width=30, font=("Arial", 15))
        self.entryCarnet.grid(column=1, row=3, padx=10, pady=5)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad, width=30, font=("Arial", 15))
        self.entryEdad.grid(column=1, row=4, padx=10, pady=5)

        # Combo Especialidad
        self.svEspecialidad = tk.StringVar()
        self.comboEspecialidad = ttk.Combobox(self, textvariable=self.svEspecialidad, state="readonly", width=28, font=("Arial", 15))
        self.comboEspecialidad.grid(column=1, row=5, padx=10, pady=5)
        self.cargarEspecialidades()

        # Botón para gestionar especialidades
        self.btnEspecialidad = tk.Button(self, text="Gestionar Especialidades", command=self.gestionarEspecialidad,
                                         width=20, font=("Arial", 12, "bold"), bg="#7697A0", fg="white")
        self.btnEspecialidad.grid(column=2, row=5, padx=10, pady=5)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono, width=30, font=("Arial", 15))
        self.entryTelefono.grid(column=1, row=6, padx=10, pady=5)

        # Botones CRUD
        self.btnNuevo = tk.Button(self, text="Nuevo", command=self.habilitar,
                                  width=12, font=("Arial", 12, "bold"), bg="#49769F", fg="white")
        self.btnNuevo.grid(column=0, row=7, padx=5, pady=5)

        self.btnGuardar = tk.Button(self, text="Guardar", command=self.guardarPersonal,
                                    width=12, font=("Arial", 12, "bold"), bg="#49769F", fg="white")
        self.btnGuardar.grid(column=1, row=7, padx=5, pady=5)

        self.btnCancelar = tk.Button(self, text="Cancelar", command=self.deshabilitar,
                                     width=12, font=("Arial", 12, "bold"), bg="#49769F", fg="white")
        self.btnCancelar.grid(column=2, row=7, padx=5, pady=5)

        # 🔹 Botón salir en parte inferior derecha
        self.btnSalir = tk.Button(self, text="Salir", command=self.volver,
                                  width=12, font=("Arial", 12, "bold"), bg="#0A4174", fg="white")
        self.btnSalir.grid(column=3, row=9, padx=10, pady=15, sticky="e")

    def cargarEspecialidades(self):
        especialidades = listarEspecialidad()
        lista = [e[1] for e in especialidades]
        self.comboEspecialidad["values"] = lista

    def gestionarEspecialidad(self):
        top = Toplevel(self)
        top.title("Gestionar Especialidades")
        top.geometry("500x400")
        top.config(bg="#C6D9E3")

        # Label + Entry
        lbl = tk.Label(top, text="Nombre Especialidad:", bg="#C6D9E3", font=("Arial", 12, "bold"))
        lbl.pack(pady=5)
        svEsp = tk.StringVar()
        entry = tk.Entry(top, textvariable=svEsp, font=("Arial", 12))
        entry.pack(pady=5)

        # Treeview
        tabla = ttk.Treeview(top, columns=("ID", "Nombre"), show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Nombre", text="Nombre Especialidad")
        tabla.pack(expand=True, fill="both", pady=10)

        def cargarTabla():
            tabla.delete(*tabla.get_children())
            for e in listarEspecialidad():
                tabla.insert("", "end", values=(e[0], e[1]))

        cargarTabla()

        # ✅ Guardar (nuevo registro)
        def guardarEsp():
            if svEsp.get() == "":
                messagebox.showwarning("Atención", "El nombre no puede estar vacío")
                return
            esp = Especialidad(svEsp.get())
            guardarDatoEspecialidad(esp)
            messagebox.showinfo("Guardar", "Especialidad registrada correctamente")
            svEsp.set("")
            self.cargarEspecialidades()
            cargarTabla()

        # ✅ Editar (actualizar seleccionado)
        def editarEsp():
            try:
                item = tabla.selection()[0]
                esp_id, _ = tabla.item(item, "values")
                if svEsp.get() == "":
                    messagebox.showwarning("Atención", "El nombre no puede estar vacío")
                    return
                from modelo.especialidadDao import editarDatoEspecialidad
                editarDatoEspecialidad(Especialidad(svEsp.get()), esp_id)
                messagebox.showinfo("Editar", "Especialidad actualizada correctamente")
                svEsp.set("")
                self.cargarEspecialidades()
                cargarTabla()
            except:
                messagebox.showerror("Editar Especialidad", "Seleccione una especialidad para editar")

        # ✅ Eliminar
        def eliminarEsp():
            try:
                item = tabla.selection()[0]
                esp_id, nombre = tabla.item(item, "values")
                confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que quieres eliminar '{nombre}'?")
                if confirmar:
                    from modelo.especialidadDao import eliminarEspecialidad
                    eliminarEspecialidad(esp_id)
                    self.cargarEspecialidades()
                    cargarTabla()
                    svEsp.set("")
            except:
                messagebox.showerror("Eliminar Especialidad", "Seleccione una especialidad para eliminar")

        # ✅ Seleccionar fila → mostrar nombre en Entry
        def seleccionarFila(event):
            try:
                item = tabla.selection()[0]
                _, nombre = tabla.item(item, "values")
                svEsp.set(nombre)
            except:
                pass

        tabla.bind("<<TreeviewSelect>>", seleccionarFila)

        # Frame de botones
        frame_btns = tk.Frame(top, bg="#C6D9E3")
        frame_btns.pack(pady=10)

        btnGuardar = tk.Button(frame_btns, text="Guardar", command=guardarEsp,
                               bg="#158645", fg="white", font=("Arial", 12, "bold"), width=12)
        btnGuardar.grid(row=0, column=0, padx=5)

        btnEditar = tk.Button(frame_btns, text="Editar", command=editarEsp,
                              bg="#1E0075", fg="white", font=("Arial", 12, "bold"), width=12)
        btnEditar.grid(row=0, column=1, padx=5)

        btnEliminar = tk.Button(frame_btns, text="Eliminar", command=eliminarEsp,
                                bg="#8A0000", fg="white", font=("Arial", 12, "bold"), width=12)
        btnEliminar.grid(row=0, column=2, padx=5)

    def guardarPersonal(self):
        personal = PersonalModel(
            self.svNombre.get(),
            self.svApPaterno.get(),
            self.svApMaterno.get(),
            self.svCarnet.get(),
            self.svEdad.get(),
            self.svEspecialidad.get(),
            self.svTelefono.get()
        )
        if self.Id_personal is None:
            guardarDatoPersonal(personal)
        else:
            editarDatoPersonal(personal, self.Id_personal)
        self.deshabilitar()
        self.tablaPersonal()

    def habilitar(self):
        self.Id_personal = None
        self.svNombre.set("")
        self.svApPaterno.set("")
        self.svApMaterno.set("")
        self.svCarnet.set("")
        self.svEdad.set("")
        self.svEspecialidad.set("")
        self.svTelefono.set("")

        self.entryNombre.config(state="normal")
        self.entryApPaterno.config(state="normal")
        self.entryApMaterno.config(state="normal")
        self.entryCarnet.config(state="normal")
        self.entryEdad.config(state="normal")
        self.comboEspecialidad.config(state="readonly")
        self.entryTelefono.config(state="normal")

        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")

    def deshabilitar(self):
        self.Id_personal = None
        self.svNombre.set("")
        self.svApPaterno.set("")
        self.svApMaterno.set("")
        self.svCarnet.set("")
        self.svEdad.set("")
        self.svEspecialidad.set("")
        self.svTelefono.set("")

        self.entryNombre.config(state="disabled")
        self.entryApPaterno.config(state="disabled")
        self.entryApMaterno.config(state="disabled")
        self.entryCarnet.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.comboEspecialidad.config(state="disabled")
        self.entryTelefono.config(state="disabled")

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")

    def volver(self):
        self.winfo_toplevel().destroy()

    def tablaPersonal(self, where=""):
        if len(where) > 0:
            self.listaPersonal = listarCondicionPersonal(where)
        else:
            self.listaPersonal = listarPersonal()

        # Tabla ajustada al tamaño de ventana
        self.tabla = ttk.Treeview(
            self,
            column=('Nombre', 'Apellido Paterno', 'Apellido Materno', 'Carnet', 'Edad', 'Especialidad', 'Telefono')
        )
        self.tabla.grid(column=0, row=8, columnspan=4, sticky="nsew")

        # Scrollbar
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(column=4, row=8, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        # Encabezados
        self.tabla.heading('#0', text='Id')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ap Paterno')
        self.tabla.heading('#3', text='Ap Materno')
        self.tabla.heading('#4', text='Carnet')
        self.tabla.heading('#5', text='Edad')
        self.tabla.heading('#6', text='Especialidad')
        self.tabla.heading('#7', text='Telefono')

        # Ajustar ancho de columnas
        self.tabla.column('#0', width=40, anchor="center")
        self.tabla.column('#1', width=150)
        self.tabla.column('#2', width=150)
        self.tabla.column('#3', width=150)
        self.tabla.column('#4', width=100)
        self.tabla.column('#5', width=60, anchor="center")
        self.tabla.column('#6', width=200)
        self.tabla.column('#7', width=150)

        # Insertar datos
        for p in self.listaPersonal:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7]))

        # Expandir tabla en la ventana
        self.grid_rowconfigure(8, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Botones de tabla
        self.btnEditar = tk.Button(self, text="Editar Personal", command=self.editarPersonal,
                                   width=20, font=("Arial", 12, "bold"), bg="#0A4174", fg="white")
        self.btnEditar.grid(row=9, column=0, padx=10, pady=5)

        self.btnEliminar = tk.Button(self, text="Eliminar Personal", command=self.eliminarDatoPersonal,
                                     width=20, font=("Arial", 12, "bold"), bg="#0A4174", fg="white")
        self.btnEliminar.grid(row=9, column=1, padx=10, pady=5)

    def editarPersonal(self):
        try:
            self.Id_personal = self.tabla.item(self.tabla.selection())['text']
            self.svNombre.set(self.tabla.item(self.tabla.selection())['values'][0])
            self.svApPaterno.set(self.tabla.item(self.tabla.selection())['values'][1])
            self.svApMaterno.set(self.tabla.item(self.tabla.selection())['values'][2])
            self.svCarnet.set(self.tabla.item(self.tabla.selection())['values'][3])
            self.svEdad.set(self.tabla.item(self.tabla.selection())['values'][4])
            self.svEspecialidad.set(self.tabla.item(self.tabla.selection())['values'][5])
            self.svTelefono.set(self.tabla.item(self.tabla.selection())['values'][6])
            self.habilitar()
        except:
            messagebox.showerror("Editar Personal", "Error al editar personal")

    def eliminarDatoPersonal(self):
        try:
            self.Id_personal = self.tabla.item(self.tabla.selection())['text']
            eliminarPersonal(self.Id_personal)
            self.tablaPersonal()
            self.Id_personal = None
        except:
            messagebox.showerror("Eliminar Personal", "Error al eliminar personal")
