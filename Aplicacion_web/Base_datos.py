import mysql.connector
from mysql.connector import cursor


class DATABASE():
    DATAB = mysql.connector.connect(
    host = "sensorcuit.cyuavfc10r3q.us-east-2.rds.amazonaws.com",
    user = "Diego_0904",
    password = 'HepsuMI0QeS223Cphghh',
    database = 'Proyecto',
    )
    cursor = DATAB.cursor(dictionary=True)
    

    def Iniciar_sesion (Correo, Contraseña, DATAB= DATAB, cursor=cursor):
        Query = " select * from Usuario where Correo = %s"
        Values = (Correo,)
        cursor.execute(Query, Values)
        Iniciar_sesion = cursor.fetchone()

        return Iniciar_sesion
    def Registrarse(Correo, Contraseña,Numero_telefono, Nombre, DATAB= DATAB, cursor=cursor):
        Query = "insert into Usuario( Correo, Contraseña, Numero_telefono, Nombre ) values (%s, %s, %s, %s)"
        Values = (Correo, Contraseña, Numero_telefono, Nombre)
        cursor.execute(Query,Values)
        DATAB.commit()

    def Ver_alertas_activas(idUsuario, DATAB= DATAB, cursor=cursor):
        Query = " select iss.* from Usuario u inner join Sensor s on s.idUsuario = u.idUsuario inner join Alerta iss on iss.id_sensor = s.idSensor where u.idUsuario = %s and iss.Estatus = 1;"
        Values = (idUsuario,)
        cursor.execute(Query, Values)
        Alertas_activas = cursor.fetchall()

        return Alertas_activas 
    def Ver_alertas(idUsuario, DATAB= DATAB, cursor=cursor):
        Query = " select iss.* from Usuario u inner join Sensor s on s.idUsuario = u.idUsuario inner join Alerta iss on iss.id_sensor = s.idSensor where u.idUsuario = %s ;"
        Values = (idUsuario,)
        cursor.execute(Query, Values)
        Alertas = cursor.fetchall()

        return Alertas 
    def Ver_ultimos_datos(idUsuario, DATAB= DATAB, cursor=cursor):
        Query = "select iss.* from Usuario u inner join Sensor s on s.idUsuario = u.idUsuario inner join Informacion_suministrada_por_sensores iss on iss.IdSensor = s.idSensor where u.idUsuario = %s;"
        Values= (idUsuario,)
        cursor.execute(Query,Values)
        Datos = cursor.fetchall()

        return Datos

    def Ver_sensores_activos(idUsuario, DATAB= DATAB, cursor=cursor):
        Query = "select * from Sensor where idUsuario = %s and Estado = 1 "
        Values = (idUsuario,)
        cursor.execute(Query, Values)
        Sensores_activos = cursor.fetchall()

        return Sensores_activos

    def Crear_sensor(idUsuario, idSensor, Ubicacion, Nombre, DATAB= DATAB, cursor=cursor):
        Query = "Insert into Sensor (IdUsuario, idSensor, Ubicacion, Nombre) values(%s, %s, %s, %s)"
        Values = (idUsuario, idSensor, Ubicacion, Nombre)
        cursor.execute(Query, Values)
        DATAB.commit()

    def Descativar_alerta(Alerta_id, DATAB= DATAB, cursor=cursor):
        Query = "update Alerta set Estatus = 0 where Alerta_id = %s"
        Values = (Alerta_id,)
        cursor.execute(Query, Values)
        DATAB.commit()

    def Activar_alerta(Alerta_id, DATAB= DATAB, cursor=cursor):
        Query = "update Alerta set Estatus = 1 where Alerta_id = %s"
        Values = (Alerta_id,)
        cursor.execute(Query, Values)
        DATAB.commit()

    def Actualizar_datos(Nombre, Numero_telefono ,idUsuario, DATAB= DATAB, cursor=cursor):
        Query = "update Usuario set Nombre = %s where idUsuario = %s"
        Values = (Nombre,idUsuario)
        cursor.execute(Query, Values)

        Query = "update Usuario set Numero_telefono = %s where idUsuario = %s"
        Values = (Numero_telefono,idUsuario)
        cursor.execute(Query, Values)

        DATAB.commit()
    def Cambiar_contraseña(Contraseña, idUsuario, DATAB= DATAB, cursor=cursor):
        Query = "update Usuario set Contraseña = %s where idUsuario = %s"
        Values = (Contraseña,idUsuario)
        cursor.execute(Query, Values)
        DATAB.commit()
    def Eliminar_usuario(Usuario_id, DATAB= DATAB, cursor=cursor):
        Query = "delete from Usuario where idUsuario = %s"
        Values = (Usuario_id,)
        cursor.execute(Query,Values)
        DATAB.commit()

