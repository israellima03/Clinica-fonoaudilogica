from .conexion import ConexionDB
from tkinter import messagebox

def editarDatoPersonal(personal, Id_personal):
    conexion = ConexionDB()
    sql = f"""UPDATE Personal SET Nombre = '{personal.Nombre}', 
                Apellido_paterno = '{personal.Apellido_paterno}', 
                Apellido_materno = '{personal.Apellido_materno}', 
                Carnet = '{personal.Carnet}', 
                Edad = '{personal.Edad}', 
                Id_especialidad = '{personal.Id_especialidad}', 
                Telefono = '{personal.Telefono}'
                WHERE Id_personal = {Id_personal}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Personal'
        mensaje = 'Personal editado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:        
        title = 'Editar Personal'
        mensaje = 'Error al editar personal'
        messagebox.showerror(title, mensaje)


def guardarDatoPersonal(personal):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Personal 
            (Nombre, Apellido_paterno, Apellido_materno, Carnet, Edad, Id_especialidad, Telefono) 
            VALUES ('{personal.Nombre}', '{personal.Apellido_paterno}', '{personal.Apellido_materno}', 
            '{personal.Carnet}', '{personal.Edad}', '{personal.Id_especialidad}', '{personal.Telefono}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Personal'
        mensaje = 'Personal registrado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar Personal'
        mensaje = 'Error al registrar personal'
        messagebox.showerror(title, mensaje)


def listarPersonal():
    conexion = ConexionDB()
    listaPersonal = []
    sql = "SELECT * FROM Personal"
    try:
        conexion.cursor.execute(sql)
        listaPersonal = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros'
        messagebox.showerror(title, mensaje)
    return listaPersonal


def listarCondicionPersonal(where):
    conexion = ConexionDB()
    listaPersonal = []
    sql = f"SELECT * FROM Personal {where}"
    try:
        conexion.cursor.execute(sql)
        listaPersonal = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        title = 'Datos'
        mensaje = 'No existen registros con esa condición'
        messagebox.showerror(title, mensaje)
    return listaPersonal


def eliminarPersonal(Id_personal):
    conexion = ConexionDB()
    sql = f"DELETE FROM Personal WHERE Id_personal={Id_personal}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Personal'
        mensaje = 'Personal eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Personal'
        mensaje = 'Error al eliminar personal'
        messagebox.showerror(title, mensaje)


class Personal:
    def __init__(self, Nombre, Apellido_paterno, Apellido_materno, Carnet, Edad, Id_especialidad, Telefono):
        self.Id_personal = None
        self.Nombre = Nombre
        self.Apellido_paterno = Apellido_paterno
        self.Apellido_materno = Apellido_materno
        self.Carnet = Carnet
        self.Edad = Edad
        self.Id_especialidad = Id_especialidad
        self.Telefono = Telefono

    def __str__(self):
        return f'Personal[{self.Nombre}, {self.Apellido_paterno}, {self.Apellido_materno}, {self.Carnet}, {self.Edad}, {self.Id_especialidad}, {self.Telefono}]'
