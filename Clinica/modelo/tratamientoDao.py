from .conexion import ConexionDB
from tkinter import messagebox

class Tratamiento:
    def __init__(self, Nombre_tratamiento, Descripcion):
        self.Id_tratamiento = None
        self.Nombre_tratamiento = Nombre_tratamiento
        self.Descripcion = Descripcion

    def __str__(self):
        return f'Tratamiento[{self.Nombre_tratamiento}]'

def guardarDatoTratamiento(tratamiento):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Tratamiento (Nombre_tratamiento, Descripcion)
              VALUES ('{tratamiento.Nombre_tratamiento}', '{tratamiento.Descripcion}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        messagebox.showinfo('Registrar Tratamiento', 'Tratamiento registrado exitosamente')
    except:
        messagebox.showerror('Registrar Tratamiento', 'Error al registrar tratamiento')

def editarDatoTratamiento(tratamiento, Id_tratamiento):
    conexion = ConexionDB()
    sql = f"""UPDATE Tratamiento SET Nombre_tratamiento = '{tratamiento.Nombre_tratamiento}', 
              Descripcion = '{tratamiento.Descripcion}' WHERE Id_tratamiento = {Id_tratamiento}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Tratamiento'
        mensaje = 'Tratamiento editado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:        
        title = 'Editar Tratamiento'
        mensaje = 'Error al editar tratamiento'
        messagebox.showerror(title, mensaje)

def listarTratamiento():
    conexion = ConexionDB()
    listaTratamiento = []
    sql = "SELECT * FROM Tratamiento"
    try:
        conexion.cursor.execute(sql)
        listaTratamiento = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        messagebox.showerror('Datos', 'No existen registros')
    return listaTratamiento

def listarCondicionTratamiento(where):
    conexion = ConexionDB()
    listaTratamiento = []
    sql = f"SELECT * FROM Tratamiento {where}"
    try:
        conexion.cursor.execute(sql)
        listaTratamiento = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros con esa condición'
        messagebox.showerror(title, mensaje)
    return listaTratamiento

def eliminarTratamiento(Id_tratamiento):
    conexion = ConexionDB()
    sql = f"DELETE FROM Tratamiento WHERE Id_tratamiento={Id_tratamiento}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Tratamiento'
        mensaje = 'Tratamiento eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Tratamiento'
        mensaje = 'Error al eliminar tratamiento'
        messagebox.showerror(title, mensaje)