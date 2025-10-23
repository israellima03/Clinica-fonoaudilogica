from .conexion import ConexionDB
from tkinter import messagebox

class Cita:
    def __init__(self, Id_persona, Id_personal, Fecha, Hora, Estado):
        self.Id_cita = None
        self.Id_persona = Id_persona
        self.Id_personal = Id_personal
        self.Fecha = Fecha
        self.Hora = Hora
        self.Estado = Estado

    def __str__(self):
        return f'Cita[{self.Fecha} {self.Hora} - Persona:{self.Id_persona} Personal:{self.Id_personal}]'

def guardarDatoCita(cita):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Cita (Id_persona, Id_personal, Fecha, Hora, Estado)
              VALUES ('{cita.Id_persona}', '{cita.Id_personal}', '{cita.Fecha}', '{cita.Hora}', '{cita.Estado}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Cita'
        mensaje = 'Cita registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Cita'
        mensaje = 'Error al registrar cita'
        messagebox.showerror(title, mensaje)

def editarDatoCita(cita, Id_cita):
    conexion = ConexionDB()
    sql = f"""UPDATE Cita SET Id_persona = '{cita.Id_persona}',
                              Id_personal = '{cita.Id_personal}',
                              Fecha = '{cita.Fecha}',
                              Hora = '{cita.Hora}',
                              Estado = '{cita.Estado}'
              WHERE Id_cita = {Id_cita}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Cita'
        mensaje = 'Cita editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Cita'
        mensaje = 'Error al editar cita'
        messagebox.showerror(title, mensaje)

def listarCita():
    conexion = ConexionDB()
    listaCita = []
    sql = "SELECT * FROM Cita"
    try:
        conexion.cursor.execute(sql)
        listaCita = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros'
        messagebox.showerror(title, mensaje)
    return listaCita

def listarCondicionCita(where):
    conexion = ConexionDB()
    listaCita = []
    sql = f"SELECT * FROM Cita {where}"
    try:
        conexion.cursor.execute(sql)
        listaCita = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros con esa condición'
        messagebox.showerror(title, mensaje)
    return listaCita

def eliminarCita(Id_cita):
    conexion = ConexionDB()
    sql = f"DELETE FROM Cita WHERE Id_cita={Id_cita}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Cita'
        mensaje = 'Cita eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Cita'
        mensaje = 'Error al eliminar cita'
        messagebox.showerror(title, mensaje)