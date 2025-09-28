
from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPaciente(persona,Id_persona):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona SET Nombre = '{persona.Nombre}', 
                Apellido_paterno = '{persona.Apellido_paterno}', 
                Apellido_materno = '{persona.Apellido_materno}', 
                Carnet = '{persona.Carnet}', 
                Fecha_nacimiento = '{persona.Fecha_nacimiento}', 
                Edad = '{persona.Edad}', 
                Genero = '{persona.Genero}', 
                Telefono = '{persona.Telefono}', 
                Direccion = '{persona.Direccion}'
                where Id_persona = {Id_persona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente Editado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:        
        title = 'Editar Paciente'
        mensaje = 'Error al Editar Paciente'
        messagebox.showerror(title, mensaje)


def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (Nombre, Apellido_paterno, Apellido_materno, Carnet, Fecha_nacimiento, Edad, Genero, Telefono, Direccion) 
            VALUES ('{persona.Nombre}', '{persona.Apellido_paterno}', '{persona.Apellido_materno}', '{persona.Carnet}', '{persona.Fecha_nacimiento}', '{persona.Edad}', '{persona.Genero}', '{persona.Telefono}', '{persona.Direccion}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamento'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje='Error al Registrar al paciente'
        messagebox.showerror(title, mensaje)

def listarPaciente():
    conexion = ConexionDB()

    listarPersona = []
    sql = "SELECT * FROM Persona"
    try:
        conexion.cursor.execute(sql)
        listarPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registro no existenete'
        messagebox.showerror(title, mensaje)
    return listarPersona

def listarCondicion(where):
    conexion = ConexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'Registro no existente'
        messagebox.showerror(title, mensaje)
    return listaPersona


def eliminarPaciente(Id_persona):
    conexion = ConexionDB()
    sql = f"""DELETE FROM Persona WHERE Id_persona={Id_persona}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Paciente'
        mensaje = 'Paciente Eliminado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showerror(title, mensaje)


class Persona:
    def __init__(self, Nombre, Apellido_paterno, Apellido_materno, Carnet, Fecha_nacimiento, Edad, Genero, Telefono, Direccion):
        self.Id_persona = None
        self.Nombre = Nombre
        self.Apellido_paterno = Apellido_paterno
        self.Apellido_materno = Apellido_materno
        self.Carnet = Carnet
        self.Fecha_nacimiento = Fecha_nacimiento
        self.Edad = Edad
        self.Genero = Genero
        self.Telefono = Telefono
        self.Direccion = Direccion

    def __str__(self):
        return f'Persona[ {self.Nombre}, {self.Apellido_paterno}, {self.Apellido_materno}, {self.Carnet}, {self.Fecha_nacimiento}, {self.Edad}, {self.Genero}, {self.Telefono}, {self.Direccion}]'
