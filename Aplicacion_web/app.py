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

@app.route("/Development")
def Development ():
   return render_template ("Base_sistema.html")
@app.route("/Resumen")
def Resumen ():
   return render_template("Resumen.html")
@app.route("/Sensores")
def Sensores ():
   return render_template("Sensores.html")
@app.route("/Alertas")
def Alertas ():
   return render_template("Alertas.html")
@app.route("/Usuario")
def USuario ():
   return render_template("Usuario.html")
if __name__ == "__main__" : 
   app.run(debug=True)