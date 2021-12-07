import Base_datos as db
from flask import Flask, redirect, render_template, url_for
import flask

app = Flask(__name__)
@app.route("/")
def root ():
   return redirect("Inicio")
@app.route("/Inicio")
def Inicio ():
    return render_template("Inicio.html")

@app.route("/iniciar_sesion")
def Iniciar_sesion () :
   return render_template ("Iniciar_sesion.html")

@app.route("/Registrarse")
def Registrarse ():
   return render_template ("Registrarse.html")

@app.route("/Añadir_sensor")
def Añadir_sensor ():
   return render_template ("Añadir_sensor.html")

@app.route("/Editar_sensor")
def Editar_sensor ():
   return render_template ("Editar_sensor.html")

@app.route("/Cambiar_contraseña")
def Cambiar_contraseña ():
   return render_template ("Cambiar_contraseña.html")