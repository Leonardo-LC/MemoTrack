#Cria rotas do site (links)
from flask import render_template, url_for
from programa import app
from flask_login import login_required
from programa.forms import FormLogin,FormCriarConta
@app.route("/",methods=["GET","POST"]) #cria uma rota para o site
def homepage():
    formLogin = FormLogin()
    return render_template("homepage.html", form=formLogin)


@app.route("/criarconta",methods=["GET","POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html",form=formcriarconta)


@app.route("/perfil/<usuario>") #<usuario> diz que isto é uma variável
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)