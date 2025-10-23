from .conexion import ConexionDB
from tkinter import messagebox

class HistorialClinico:
    def __init__(self, Id_persona, Id_personal, Fecha, Hora, Diagnostico, Observaciones):
        self.Id_persona = Id_persona
        self.Id_personal = Id_personal
        self.Fecha = Fecha
        self.Hora = Hora
        self.Diagnostico = Diagnostico
        self.Observaciones = Observaciones

def guardarHistorial(historial):
    conexion = ConexionDB()
    sql = """INSERT INTO Historial_Clinico (Id_persona, Id_personal, Fecha, Hora, Diagnostico, Observaciones)
             VALUES (?, ?, ?, ?, ?, ?)"""
    conexion.cursor.execute(sql, (historial.Id_persona, historial.Id_personal, historial.Fecha, historial.Hora, historial.Diagnostico, historial.Observaciones))
    conexion.cerrarConexion()

def listarHistorial(Id_persona=None):
    conexion = ConexionDB()
    if Id_persona:
        conexion.cursor.execute("SELECT * FROM Historial_Clinico WHERE Id_persona=?", (Id_persona,))
    else:
        conexion.cursor.execute("SELECT * FROM Historial_Clinico")
    datos = conexion.cursor.fetchall()
    conexion.cerrarConexion()
    return datos

def editarHistorial(historial, Id_historial):
    conexion = ConexionDB()
    sql = """UPDATE Historial_Clinico SET Id_persona=?, Id_personal=?, Fecha=?, Hora=?, Diagnostico=?, Observaciones=?
             WHERE Id_historial=?"""
    conexion.cursor.execute(sql, (historial.Id_persona, historial.Id_personal, historial.Fecha, historial.Hora, historial.Diagnostico, historial.Observaciones, Id_historial))
    conexion.cerrarConexion()

def eliminarHistorial(Id_historial):
    conexion = ConexionDB()
    conexion.cursor.execute("DELETE FROM Historial_Clinico WHERE Id_historial=?", (Id_historial,))
    conexion.cerrarConexion()
