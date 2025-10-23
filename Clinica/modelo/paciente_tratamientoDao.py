from .conexion import ConexionDB
from tkinter import messagebox

class PersonaTratamiento:
    def __init__(self, Id_persona, Id_tratamiento, Fecha_inicio, Fecha_fin, Estado):
        self.Id_pertratamiento = None
        self.Id_persona = Id_persona
        self.Id_tratamiento = Id_tratamiento
        self.Fecha_inicio = Fecha_inicio
        self.Fecha_fin = Fecha_fin
        self.Estado = Estado

    def __str__(self):
        return f'PersonaTratamiento[Persona={self.Id_persona}, Tratamiento={self.Id_tratamiento}]'

def guardarDatoPersonaTratamiento(persona_tratamiento):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona_Tratamiento (Id_persona, Id_tratamiento, Fecha_inicio, Fecha_fin, Estado)
              VALUES ('{persona_tratamiento.Id_persona}', '{persona_tratamiento.Id_tratamiento}', 
                      '{persona_tratamiento.Fecha_inicio}', '{persona_tratamiento.Fecha_fin}', 
                      '{persona_tratamiento.Estado}')"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Persona-Tratamiento'
        mensaje = 'Registro realizado exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Registrar Persona-Tratamiento'
        mensaje = f'Error al registrar\n{e}'
        messagebox.showerror(title, mensaje)

def editarDatoPersonaTratamiento(persona_tratamiento, Id_pertratamiento):
    conexion = ConexionDB()
    sql = f"""UPDATE Persona_Tratamiento SET Id_persona='{persona_tratamiento.Id_persona}', 
              Id_tratamiento='{persona_tratamiento.Id_tratamiento}', 
              Fecha_inicio='{persona_tratamiento.Fecha_inicio}', 
              Fecha_fin='{persona_tratamiento.Fecha_fin}', 
              Estado='{persona_tratamiento.Estado}'
              WHERE Id_pertratamiento={Id_pertratamiento}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Persona-Tratamiento'
        mensaje = 'Registro editado exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Editar Persona-Tratamiento'
        mensaje = f'Error al editar\n{e}'
        messagebox.showerror(title, mensaje)

def listarPersonaTratamiento():
    conexion = ConexionDB()
    lista = []
    sql = "SELECT * FROM Persona_Tratamiento"
    try:
        conexion.cursor.execute(sql)
        lista = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except Exception as e:
        title = 'Datos'
        mensaje = f'No existen registros\n{e}'
        messagebox.showerror(title, mensaje)
    return lista

def listarCondicionPersonaTratamiento(where):
    conexion = ConexionDB()
    lista = []
    sql = f"SELECT * FROM Persona_Tratamiento {where}"
    try:
        conexion.cursor.execute(sql)
        lista = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except Exception as e:
        title = 'Datos'
        mensaje = f'No existen registros con esa condición\n{e}'
        messagebox.showerror(title, mensaje)
    return lista

def eliminarPersonaTratamiento(Id_pertratamiento):
    conexion = ConexionDB()
    sql = f"DELETE FROM Persona_Tratamiento WHERE Id_pertratamiento={Id_pertratamiento}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Persona-Tratamiento'
        mensaje = 'Registro eliminado exitosamente'
        messagebox.showinfo(title, mensaje)
    except Exception as e:
        title = 'Eliminar Persona-Tratamiento'
        mensaje = f'Error al eliminar\n{e}'
        messagebox.showerror(title, mensaje)