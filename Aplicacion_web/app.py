
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
   return render_template("Inicio.html", Titulo="Inicio")

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
            session ["Numero"] = Database_user[ "Numero_telefono"]

            return redirect(url_for("Resumen"))
         else: 
            return redirect(url_for('Iniciar_sesion'))
      return redirect(url_for('Inicio'))
      
     
      
  # return render_template ("Iniciar_sesion.html")


@app.route("/Registrarse", methods=["GET", "POST"])
def Registrarse ():
   if request.method == 'GET' :
      return render_template ("Registrarse.html")
   if request.method == "POST" :
      Contraseña = request.form.get("Contraseña") 
      Numero =  request.form.get("Numero")
      Correo =  request.form.get("Correo")
      Nombre = request.form.get("Nombre")
      db.Registrarse(Correo, Contraseña, Numero, Nombre)
      return redirect (url_for("Iniciar_sesion"))

@app.route("/Añadir_sensor", methods=["GET", "POST"])
def Añadir_sensor ():
   
      if "idUsuario" in session :
         if request.method == "GET":
            return render_template ("Añadir_sensor.html")
         else : 
            Nombre =  request.form.get("Nombre")
            Numero_sensor = request.form.get("Numero_de_sensor")
            Ubicacion = request.form.get("Ubicación")
            idUsuario = session["idUsuario"]
            db.Crear_sensor(idUsuario,Numero_sensor, Ubicacion, Nombre)

            return redirect(url_for("Resumen"))
         
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
      if request.method == "GET" :
         return render_template ("Cambiar_contraseña.html")
      if request.method == "POST" :
         idUsuario = session["idUsuario"]
         Contraseña_1 = request.form.get("Contraseña_1")
         Contraseña_2 = request.form.get("Contraseña_2")
         if Contraseña_1 == Contraseña_2 :
            db.Cambiar_contraseña(Contraseña_2, idUsuario)
            return redirect(url_for("Usuario"))
   else :
      return redirect(url_for('Iniciar_sesion'))
   
@app.route("/Resumen", methods=["GET", "POST"])
def Resumen ():
   
   if "idUsuario" in session :
      idUsuario = session["idUsuario"]
      Tabla_alertas_activas = db.Ver_alertas_activas(idUsuario)
      Datos_sensores = db.Ver_ultimos_datos(idUsuario)
      return render_template( "Resumen.html", Tabla_alertas_activas = Tabla_alertas_activas, Datos_sensores =Datos_sensores, Titulo ="Resumen" )
   else :
      return redirect(url_for('Iniciar_sesion'))
   
@app.route("/Sensores", methods=["GET", "POST"] )
def Sensores ():
   
   if "idUsuario" in session :
      idUsuario = session["idUsuario"]
      Sensores_activos = db.Ver_sensores_activos(idUsuario)
      return render_template("Sensores.html", Sensores_activos = Sensores_activos,  Titulo ="Sensores")
   else :
      return redirect(url_for('Iniciar_sesion'))
   
   
@app.route("/Alertas", methods=["GET", "POST"])
def Alertas ():
   
   if "idUsuario" in session :
         if request.method == "GET" :
            idUsuario = session["idUsuario"]
            Tabla_alerta =db.Ver_alertas(idUsuario)

            return render_template("Alertas.html",  Tabla_alerta =Tabla_alerta, Titulo ="Alertas")
         else : 
            if request.form.get("Accion") == "Desactivar" :
               Alerta_id = request.form.get("Alerta_id")
               db.Descativar_alerta(Alerta_id)

               return redirect(url_for("Alertas"))

            if request.form.get("Accion") == "Activar" :
               Alerta_id = request.form.get("Alerta_id")
               db.Activar_alerta(Alerta_id)

               return redirect (url_for("Alertas"))
   else :
      return redirect(url_for('Iniciar_sesion'))
   
   
@app.route("/Usuario", methods=["GET", "POST"])
def Usuario ():
   if "idUsuario" in session :
      if request.method == "GET" :
         Nombre = session["Nombre"]
         Numero = session["Numero"]

         return render_template("Usuario.html", Nombre = Nombre, Numero = Numero, Titulo ="Usuario")

      if request.method == "POST" :
         if request.form.get("Accion") == "Actualizar datos" :

            idUsuario = session["idUsuario"]
            Nombre_form = request.form.get("Nombre")
            Telefono_form = request.form.get ("Numero")
            session["Nombre"] = Nombre_form
            session["Numero"] = Telefono_form
            db.Actualizar_datos(Nombre_form, Telefono_form, idUsuario)

            return redirect(url_for("Usuario"))

         if request.form.get("Accion") == "Cambiar contraseña" :
            idUsuario = session["idUsuario"]

            return redirect(url_for("Cambiar_contraseña"))

         if request.form.get("Accion") == "Eliminar usuario" :
               idUsuario = session["idUsuario"]
               db.Eliminar_usuario(idUsuario)
               session.clear()
               return redirect (url_for("Iniciar_sesion"))
   else :
      return redirect(url_for('Iniciar_sesion'))
   
@app.route("/Estadisticas", methods = ["GET"])
def Estadisticas () :
   return render_template("Estadisticas.html",Titulo="Estadisticas")

@app.route("/Recomendaciones", methods = ["GET"])
def Recomendaciones () :
   return render_template("Recomendaciones.html", Titulo="Recomendaciones")
  

@app.route("/Chafa")
def Chafa () :
   session.clear()
   
   return redirect(url_for("Iniciar_sesion"))


@app.errorhandler(404)
def page_not_found(e):
   
    return redirect(url_for("Inicio"))
    
