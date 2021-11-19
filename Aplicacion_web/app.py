import Base_datos as db
from flask import Flask, redirect, render_template, url_for
import flask
app = Flask(__name__)
@app.route("/")
def root ():
   return redirect("home")
@app.route("/home")
def Home ():
    return "Hola mundo"