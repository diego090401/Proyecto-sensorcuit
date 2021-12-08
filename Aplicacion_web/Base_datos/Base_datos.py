import mysql.connector
from mysql.connector import cursor

class DATABASE():
    DATAB = mysql.connector.connect(
    host = "sensorcuit.cyuavfc10r3q.us-east-2.rds.amazonaws.com",
    user = "Diego_0904",
    password = 'HepsuMI0QeS223Cphghh',
    database = 'Proyecto',
    )
    cursor = DATAB.cursor()
    

    def Iniciar_sesion (DATAB= DATAB, cursor=cursor):
        pass
    def Registrarse(DATAB= DATAB, cursor=cursor):
        pass
    def Ver_alertas_activas(DATAB= DATAB, cursor=cursor):
        pass
    def Ver_ultimos_datos(DATAB= DATAB, cursor=cursor):
        pass
    def Ver_sensores_activos(DATAB= DATAB, cursor=cursor):
        pass
    def Crear_sensor(DATAB= DATAB, cursor=cursor):
        pass
    def Descativar_alerta(DATAB= DATAB, cursor=cursor):
        pass
    def Activar_alerta(DATAB= DATAB, cursor=cursor):
        pass
    def Actualizar_datos(DATAB= DATAB, cursor=cursor):
        pass
    def Cambiar_contraseña(DATAB= DATAB, cursor=cursor):
        pass        
    def Eliminar_usuario(DATAB= DATAB, cursor=cursor):
        pass

