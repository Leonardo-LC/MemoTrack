#Cria rotas do site (links)
from flask import render_template, url_for
from programa import app

@app.route("/") #cria uma rota para o site
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") #<usuario> diz que isto é uma variável
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)