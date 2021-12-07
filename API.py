from fastapi import FastAPI
import mysql.connector
from mysql.connector import cursor
#creando la aplicacion de fastapi
app = FastAPI()

#Creando la coneccion a la base de datos 
DATAB = mysql.connector.connect(
    host = "sensorcuit.cyuavfc10r3q.us-east-2.rds.amazonaws.com",
    user = "Diego_0904",
    password = 'HepsuMI0QeS223Cphghh',
    database = 'Proyecto',
    )
cursor = DATAB.cursor()
@app.get("/")
def root ( ):
    return "Bienvenido a la api para el proyecto sensorcuit, para poder hacer uso de esta api tiene que dirigirse al path/Nuevos_datos/ y colocar los datos del sensor separados por un /"

@app.post("/Nuevos_datos/{idSensor}/{Temperatura}/{Concentracion_humo}")
def insertar_datos(idSensor,Temperatura,Concentracion_humo):
    Nuevos_datos = (idSensor, Temperatura, Concentracion_humo)
    Insertar_inforamacion = "insert into Informacion_suministrada_por_sensores (idSensor, Temperatura, Concentracion_humo) values (%s, %s, %s)"
    cursor.execute(Insertar_inforamacion, Nuevos_datos)
    DATAB.commit()
    return "Exito"


