
from Base_datos import DATABASE as db

from flask import Flask, redirect, render_template, url_for, request, g, session
import flask

app = Flask(__name__)

app.config['SECRET_KEY'] = "qzwxecadsfrtvng"

@app.route("/")
def root ():
   return redirect("Inicio")
@app.route("/Inicio", methods = ["GET", "POST"])
def Inicio ():
   return render_template("Inicio.html")

@app.route("/Iniciar_sesion", methods=["GET", "POST"])
def Iniciar_sesion () :
   if request.method == "GET":
      return render_template("Iniciar_sesion.html")
   else :
      Correo_form = request.form.get("Correo")
      Contraseña_form = request.form.get("Contraseña")

      Database_user = db.Iniciar_sesion(Correo_form, Contraseña_form)

      if type(Database_user) == dict :
         if Database_user["Contraseña"] == Contraseña_form :
            session['Correo'] = Database_user["Correo"]
            session ['Nombre'] = Database_user["Nombre"]
            session ["idUsuario"] = Database_user[ "idUsuario"]
            return redirect(url_for("Resumen"))
         else: 
            return "Contraseña incorrecta"
      return "Correo no encontrado"
      
     
      
  # return render_template ("Iniciar_sesion.html")


@app.route("/Registrarse", methods=["GET", "POST"])
def Registrarse ():
   return render_template ("Registrarse.html")

@app.route("/Añadir_sensor", methods=["GET", "POST"])
def Añadir_sensor ():
   if "idUsuario" in session :
      return render_template ("Añadir_sensor.html")
   else :
      return redirect(url_for('Iniciar_sesion'))
      


@app.route("/Editar_sensor", methods=["GET", "POST"])
def Editar_sensor ():
   if "idUsuario" in session :
      return render_template ("Editar_sensor.html")
   else :
      return redirect(url_for('Iniciar_sesion'))
   

@app.route("/Cambiar_contraseña", methods=["GET", "POST"])
def Cambiar_contraseña ():
   
   if "idUsuario" in session :
      return render_template ("Cambiar_contraseña.html")
   else :
      return redirect(url_for('Iniciar_sesion'))
   
@app.route("/Resumen", methods=["GET", "POST"])
def Resumen ():
   
   if "idUsuario" in session :
      idUsuario = session["idUsuario"]
      Tabla_alertas_activas = db.Ver_alertas_activas(idUsuario)
      Datos_sensores = db.Ver_ultimos_datos(idUsuario)
      return render_template( "Resumen.html", Tabla_alertas_activas = Tabla_alertas_activas, Datos_sensores =Datos_sensores )
   else :
      return redirect(url_for('Iniciar_sesion'))
   
@app.route("/Sensores", methods=["GET", "POST"] )
def Sensores ():
   
   if "idUsuario" in session :
      idUsuario = session["idUsuario"]
      Sensores_activos = db.Ver_sensores_activos(idUsuario)
      return render_template("Sensores.html", Sensores_activos = Sensores_activos)
   else :
      return redirect(url_for('Iniciar_sesion'))
   
   
@app.route("/Alertas", methods=["GET", "POST"])
def Alertas ():
   
   if "idUsuario" in session :
      idUsuario = session["idUsuario"]
      Tabla_alerta =db.Ver_alertas(idUsuario)
      return render_template("Alertas.html",  Tabla_alerta =Tabla_alerta)
   else :
      return redirect(url_for('Iniciar_sesion'))
   
   
@app.route("/Usuario", methods=["GET", "POST"])
def Usuario ():

   if "idUsuario" in session :
      return render_template("Usuario.html")
   else :
      return redirect(url_for('Iniciar_sesion'))
   

@app.route("/Chafa")
def Chafa () :
   session.clear()
   
   return redirect(url_for("Iniciar_sesion"))

