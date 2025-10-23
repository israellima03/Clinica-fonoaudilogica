from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoEspecialidad(especialidad, Id_especialidad):
    conexion = ConexionDB()
    sql = f"""UPDATE Especialidad SET Nombre_especialidad = '{especialidad.Nombre_especialidad}'
              WHERE Id_especialidad = {Id_especialidad}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Especialidad'
        mensaje = 'Especialidad editada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:        
        title = 'Editar Especialidad'
        mensaje = 'Error al editar especialidad'
        messagebox.showerror(title, mensaje)


def guardarDatoEspecialidad(especialidad):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Especialidad (Nombre_especialidad) 
              VALUES ('{especialidad.Nombre_especialidad}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Especialidad'
        mensaje = 'Especialidad registrada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Especialidad'
        mensaje = 'Error al registrar especialidad'
        messagebox.showerror(title, mensaje)


def listarEspecialidad():
    conexion = ConexionDB()
    listaEspecialidad = []
    sql = "SELECT * FROM Especialidad"
    try:
        conexion.cursor.execute(sql)
        listaEspecialidad = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros'
        messagebox.showerror(title, mensaje)
    return listaEspecialidad


def listarCondicionEspecialidad(where):
    conexion = ConexionDB()
    listaEspecialidad = []
    sql = f"SELECT * FROM Especialidad {where}"
    try:
        conexion.cursor.execute(sql)
        listaEspecialidad = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros con esa condición'
        messagebox.showerror(title, mensaje)
    return listaEspecialidad


def eliminarEspecialidad(Id_especialidad):
    conexion = ConexionDB()
    sql = f"DELETE FROM Especialidad WHERE Id_especialidad={Id_especialidad}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Especialidad'
        mensaje = 'Especialidad eliminada exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Especialidad'
        mensaje = 'Error al eliminar especialidad'
        messagebox.showerror(title, mensaje)


class Especialidad:
    def __init__(self, Nombre_especialidad):
        self.Id_especialidad = None
        self.Nombre_especialidad = Nombre_especialidad

    def __str__(self):
        return f'Especialidad[{self.Nombre_especialidad}]'