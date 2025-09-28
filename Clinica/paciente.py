from tkinter import *
import tkinter as tk 
from tkinter import Button, ttk, scrolledtext, Toplevel
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listarPaciente, editarDatoPaciente, eliminarPaciente
from tkinter import ttk, messagebox
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date

class Paciente(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
##        self.widgets()
        self.Id_persona = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()
        self.grid_columnconfigure(0, minsize=150)  # Columna de etiquetas
        self.grid_columnconfigure(1, minsize=200)  # Columna de entradas
        self.grid_columnconfigure(2, minsize=120)  # Columna del buscador etiqueta
        self.grid_columnconfigure(3, minsize=150)  # Columna del buscador entry
        self.grid_columnconfigure(4, minsize=100)  # Columna del botón buscar

##    def widgets(self):

##        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="black", highlightthickness=1)
##        frame1.pack()
##        frame1.place(x=0, y=0, width=1100, height=100)

 ##       titulo = tk.Label(self, text="Paciente", bg="#dddddd", fg="black", font=("Arial", 20))
 ##       titulo.pack()
 ##       titulo.place(x=5, y=0, width=1090, height=90)

    def camposPaciente(self):
        self.lbNombre = tk.Label(self, text="Nombre:  ",bg="#C6D9E3", fg="black")
        self.lbNombre.config(font=("Arial", 15, "bold"))
        self.lbNombre.grid(column=0, row=0,padx=10, pady=5)

        self.lb1ApPaterno = tk.Label(self, text="Apellido Paterno:  ",bg="#C6D9E3", fg="black")
        self.lb1ApPaterno.config(font=("Arial", 15, "bold"))
        self.lb1ApPaterno.grid(column=0, row=1,padx=10, pady=5)

        self.lblApMaterno = tk.Label(self, text="Apellido Materno:  ",bg="#C6D9E3", fg="black")
        self.lblApMaterno.config(font=("Arial", 15, "bold"))
        self.lblApMaterno.grid(column=0, row=2,padx=10, pady=5)

        self.lblCi= tk.Label(self, text="Carnet:  ",bg="#C6D9E3", fg="black")
        self.lblCi.config(font=("Arial", 15, "bold"))
        self.lblCi.grid(column=0, row=3,padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text="Fecha de Nacimiento:  ",bg="#C6D9E3", fg="black")
        self.lblFechNacimiento.config(font=("Arial", 15, "bold"))
        self.lblFechNacimiento.grid(column=0, row=4,padx=10, pady=5)

        self.lblEdad = tk.Label(self, text="Edad",bg="#C6D9E3", fg="black")
        self.lblEdad.config(font=("Arial", 15, "bold"))
        self.lblEdad.grid(column=0, row=5,padx=10, pady=5)

        self.lblGenero = tk.Label(self, text="Genero:  ",bg="#C6D9E3", fg="black")
        self.lblGenero.config(font=("Arial", 15, "bold"))
        self.lblGenero.grid(column=0, row=6,padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text="Telefono:  ",bg="#C6D9E3", fg="black")
        self.lblTelefono.config(font=("Arial", 15, "bold"))
        self.lblTelefono.grid(column=0, row=7,padx=10, pady=5)

        self.lblDireccion = tk.Label(self, text="Direccion:  ",bg="#C6D9E3", fg="black")
        self.lblDireccion.config(font=("Arial", 15, "bold"))
        self.lblDireccion.grid(column=0, row=8,padx=10, pady=5)

        # entrys o entradas de texto
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self,textvariable=self.svNombre)
        self.entryNombre.config(width=30, font=("Arial", 15))
        self.entryNombre.grid(column=1, row=0,padx=10, pady=5)
        
        self.svApPaterno = tk.StringVar()
        self.entryApPaterno = tk.Entry(self, textvariable=self.svApPaterno)
        self.entryApPaterno.config(width=30, font=("Arial", 15))
        self.entryApPaterno.grid(column=1, row=1,padx=10, pady=5)

        self.svApMaterno = tk.StringVar()
        self.entryApMaterno = tk.Entry(self, textvariable=self.svApMaterno)
        self.entryApMaterno.config(width=30, font=("Arial", 15))
        self.entryApMaterno.grid(column=1, row=2,padx=10, pady=5)

        self.svCi = tk.StringVar()
        self.entryCi = tk.Entry(self, textvariable=self.svCi)
        self.entryCi.config(width=30, font=("Arial", 15))
        self.entryCi.grid(column=1, row=3,padx=10, pady=5)

        self.svFechNacimiento = tk.StringVar()
        self.entryFechNacimiento = tk.Entry(self, textvariable=self.svFechNacimiento)
        self.entryFechNacimiento.config(width=30, font=("Arial", 15))
        self.entryFechNacimiento.grid(column=1, row=4,padx=10, pady=5)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=30, font=("Arial", 15))
        self.entryEdad.grid(column=1, row=5,padx=10, pady=5)

        self.svGenero = tk.StringVar()
        self.entryGenero = tk.Entry(self, textvariable=self.svGenero)
        self.entryGenero.config(width=30, font=("Arial", 15))
        self.entryGenero.grid(column=1, row=6,padx=10, pady=5)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=30, font=("Arial", 15))
        self.entryTelefono.grid(column=1, row=7,padx=10, pady=5)

        self.svDireccion = tk.StringVar()
        self.entryDireccion = tk.Entry(self, textvariable=self.svDireccion)
        self.entryDireccion.config(width=30, font=("Arial", 15))
        self.entryDireccion.grid(column=1, row=8,padx=10, pady=5)

        #botones
        # Frame para contener los botones
        btn_frame = tk.Frame(self, bg="#C6D9E3")
        btn_frame.grid(column=0, row=9, columnspan=2, pady=10)  # ocupa dos columnas y se centra

         #botones
        # Frame para contener los botones
        btn_frame1 = tk.Frame(self, bg="#C6D9E3")
        btn_frame1.grid(column=2, row=2, padx=(10,2))  # ocupa dos columnas y se centra

        btn_frame2 = tk.Frame(self, bg="#C6D9E3")
        btn_frame2.grid(column=3, row=2, padx=(10,2))  # ocupa dos columnas y se centra

        btn_frame3 = tk.Frame(self, bg="#C6D9E3")
        btn_frame3.grid(column=2, row=4, padx=(10,1))  # ocupa dos columnas y se centra


        # Botón Nuevo
        self.btnNuevo = tk.Button(btn_frame, text="Nuevo",command=self.habilitar,
                          width=12, font=("Arial", 12, "bold"),
                          fg="#DAD5D6", bg="#158645",
                          cursor="hand2", activebackground="#35BD6F")
        self.btnNuevo.pack(side="left", padx=5)  # 👈 espacio más pequeño

        # Botón Guardar
        self.btnGuardar = tk.Button(btn_frame, text="Guardar",command=self.guardarPaciente,
                            width=12, font=("Arial", 12, "bold"),
                            fg="#DAD5D6", bg="#000000",
                            cursor="hand2", activebackground="#5F5F5F")
        self.btnGuardar.pack(side="left", padx=5)

        # Botón Cancelar
        self.btnCancelar = tk.Button(btn_frame, text="Cancelar",command=self.deshabilitar,
                             width=12, font=("Arial", 12, "bold"),
                             fg="#DAD5D6", bg="#C41010",
                             cursor="hand2", activebackground="#C83D3D")
        self.btnCancelar.pack(side="left", padx=5)

        #Buscador
        # Label Buscar Carnet
        # Buscador de carnet
        self.lblBuscarCarnet = tk.Label(self, text="Buscar Carnet: ", bg="#C6D9E3", fg="black")
        self.lblBuscarCarnet.config(font=("Arial", 15, "bold"))
        self.lblBuscarCarnet.grid(column=2, row=0, padx=(10,2), pady=5)  # solo 2px de separación

        self.lblBuscarApellido = tk.Label(self, text="Buscar Apellido: ", bg="#C6D9E3", fg="black")
        self.lblBuscarApellido.config(font=("Arial", 15, "bold"))
        self.lblBuscarApellido.grid(column=2, row=1, padx=(10,2), pady=5)  # solo 2px de separación
        #Entradas
        self.svBuscarCarnet = tk.StringVar()
        self.entryBuscarCarnet = tk.Entry(self, textvariable=self.svBuscarCarnet)
        self.entryBuscarCarnet.config(width=15, font=("Arial", 15))
        self.entryBuscarCarnet.grid(column=3, row=0, padx=(10,2), pady=5)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=15, font=("Arial", 15))
        self.entryBuscarApellido.grid(column=3, row=1, padx=(10,2), pady=5)

        #Buscador
        self.btnBuscarCondicion = tk.Button(btn_frame1, text="Buscar", command=self.buscarCondicion ,
                             width=12, font=("Arial", 12, "bold"),
                             fg="#DAD5D6", bg="#078409",
                             cursor="hand2", activebackground="#31AA16")
        self.btnBuscarCondicion.pack(side="left", padx=5)
        #Buscador
        self.btnLimpiarBuscador = tk.Button(btn_frame2, text="Limpiar", command=self.limpiarBuscador ,
                             width=12, font=("Arial", 12, "bold"),
                             fg="#DAD5D6", bg="#1E8D8D",
                             cursor="hand2", activebackground="#08E6FF")
        self.btnLimpiarBuscador.pack(side="left", padx=5)

        #Calendario
        self.btnCalendario = tk.Button(btn_frame3, text="Calendario",command=self.vistaCalendario,
                             width=12, font=("Arial", 12, "bold"),
                             fg="#DAD5D6", bg="#421361",
                             cursor="hand2", activebackground="#BF1AE9")
        self.btnCalendario.pack(side="left", padx=5)

    def vistaCalendario(self):
        self.calendario = Toplevel()
        self.calendario.title("FECHA DE NACIMIENTO")
        self.calendario.resizable(0,0)
        self.calendario.config(bg='#C6D9E3')

        self.svCalendario = StringVar(value="01/01/1990")
        self.calendar = tc.Calendar(self.calendario,
                                   selectmode='day',
                                   year=1990, month=1, day=1,
                                   locale='es_ES',   # mejor 'es_ES' que 'es_US'
                                   textvariable=self.svCalendario,
                                   background='#777777',
                                   foreground='#FFFFFF',
                                   headersbackground='#B6DDFE',
                                   cursor='hand2',
                                   date_pattern='dd/mm/yyyy')  # ojo con Y vs y)
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1,column=0)
        #enviar fecha a entrada
        self.svCalendario.trace_add('write', self.enviarFecha)

    def enviarFecha(self, *args):
        self.svFechNacimiento.set(''+ self.svCalendario.get())
        if len(self.calendar.get_date()) > 1:
            self.svCalendario.trace('w', self.calcularEdad)

    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d/%m/%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)
    
    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarCarnet.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarCarnet.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1 "
            if (len(self.svBuscarCarnet.get())) > 0:
                where = "WHERE Carnet = "+ self.svBuscarCarnet.get()+ ""
            if (len(self.svBuscarApellido.get())) > 0:
                where = " WHERE  Apellido_paterno LIKE '"+ self.svBuscarApellido.get()+"%'"

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()


    def guardarPaciente(self):
        persona = Persona( 
            self.svNombre.get(),
            self.svApPaterno.get(),
            self.svApMaterno.get(),
            self.svCi.get(),
            self.svFechNacimiento.get(),
            self.svEdad.get(),
            self.svGenero.get(),
            self.svTelefono.get(),
            self.svDireccion.get()
        )
        if self.Id_persona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.Id_persona)

        self.deshabilitar()
        self.tablaPaciente()

    def habilitar(self):
        #self.Id_persona = None
        self.svNombre.set("")
        self.svApPaterno.set("")
        self.svApMaterno.set("")
        self.svCi.set("")
        self.svFechNacimiento.set("")
        self.svEdad.set("")
        self.svGenero.set("")
        self.svTelefono.set("")
        self.svDireccion.set("")

        self.entryNombre.config(state="normal")
        self.entryApPaterno.config(state="normal")
        self.entryApMaterno.config(state="normal")
        self.entryCi.config(state="normal")
        self.entryFechNacimiento.config(state="normal")
        self.entryEdad.config(state="normal")
        self.entryGenero.config(state="normal")
        self.entryTelefono.config(state="normal")
        self.entryDireccion.config(state="normal")

        self.btnGuardar.config(state="normal")
        self.btnCancelar.config(state="normal")
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.Id_persona = None
        self.svNombre.set("")
        self.svApPaterno.set("")
        self.svApMaterno.set("")
        self.svCi.set("")
        self.svFechNacimiento.set("")
        self.svEdad.set("")
        self.svGenero.set("")
        self.svTelefono.set("")
        self.svDireccion.set("")

        self.entryNombre.config(state="disabled")
        self.entryApPaterno.config(state="disabled")
        self.entryApMaterno.config(state="disabled")
        self.entryCi.config(state="disabled")
        self.entryFechNacimiento.config(state="disabled")
        self.entryEdad.config(state="disabled")
        self.entryGenero.config(state="disabled")
        self.entryTelefono.config(state="disabled")
        self.entryDireccion.config(state="disabled")

        self.btnGuardar.config(state="disabled")
        self.btnCancelar.config(state="disabled")
        self.btnCalendario.config(state='disabled')
    

    def volver(self):
        # Cierra el Toplevel que contiene este Frame
        self.winfo_toplevel().destroy()


    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listarPaciente()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'Apellido Paterno', 'Apellido Materno', 'Carnet', 'Fecha Nacimiento', 'Edad', 'Genero', 'Telefono', 'Direccion'))
        self.tabla.grid(column=0 ,row=10, columnspan=10, sticky='nse')
       
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(column=11, row=10, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0', text='Id')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ap Paterno')
        self.tabla.heading('#3', text='Ap Materno')
        self.tabla.heading('#4', text='Carnet')
        self.tabla.heading('#5', text='F. Nacimiento')
        self.tabla.heading('#6', text='Edad')
        self.tabla.heading('#7', text='Genero')
        self.tabla.heading('#8', text='Telefono')
        self.tabla.heading('#9', text='Direccion')

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=150)
        self.tabla.column('#2', anchor=W, width=120)
        self.tabla.column('#3', anchor=W, width=120)
        self.tabla.column('#4', anchor=W, width=80)
        self.tabla.column('#5', anchor=W, width=100)
        self.tabla.column('#6', anchor=W, width=80)
        self.tabla.column('#7', anchor=W, width=150)
        self.tabla.column('#8', anchor=W, width=85)
        self.tabla.column('#9', anchor=W, width=210)
        
        for p in self.listaPersona:

            self.tabla.insert('',0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9]), tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command= self.editarPaciente)
        self.btnEditarPaciente.config(width=20, font=('Arial',12 ,'bold'), fg='#DAD5D6',bg='#1E0075', activebackground='#9379E0', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarDatoPaciente)
        self.btnEliminarPaciente.config(width=20, font=('Arial',12 ,'bold'), fg='#DAD5D6',bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente')
        self.btnHistorialPaciente.config(width=20, font=('Arial',12 ,'bold'), fg='#DAD5D6',bg='#007C79', activebackground='#99F2f0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)
        
        self.btnSalir= tk.Button(self, text='Salir',command=self.volver)
        self.btnSalir.config(width=10, font=('Arial',12 ,'bold'), fg='#DAD5D6',bg="#10C019", activebackground="#489228", cursor='hand2')
        self.btnSalir.grid(row=11, column=3, padx=10, pady=5)

    def editarPaciente(self):
        try:
            self.Id_persona = self.tabla.item(self.tabla.selection())['text']#Trae el Id
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.carnetPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.generoPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.direccionPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApPaterno.insert(0, self.apPaternoPaciente)
            self.entryApMaterno.insert(0, self.apMaternoPaciente)
            self.entryCi.insert(0, self.carnetPaciente)
            self.entryFechNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryGenero.insert(0, self.generoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)
            self.entryDireccion.insert(0, self.direccionPaciente)
        except:
            title = 'Editar Paciene'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)

    def eliminarDatoPaciente(self):
        try:
            self.Id_persona=self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.Id_persona)
            self.tablaPaciente()
            self.Id_persona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'Error al elimar paciente'
            messagebox.showerror(title, mensaje)

            

            


        
