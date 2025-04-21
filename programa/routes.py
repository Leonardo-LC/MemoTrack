#Cria rotas do site (links)
from flask import render_template, url_for, redirect
from programa import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from programa.forms import FormLogin,FormCriarConta
from programa.models import Usuario, Materia
@app.route("/",methods=["GET","POST"]) #cria uma rota para o site
def homepage():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", usuario=usuario.username))
    return render_template("homepage.html", form=formLogin)


@app.route("/criarconta",methods=["GET","POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data)
        usuario = Usuario(username=formcriarconta.username.data,
                          senha=senha,
                          email=formcriarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario,remember=True)
        return redirect(url_for("perfil",usuario=usuario.username))
    return render_template("criarconta.html",form=formcriarconta)


@app.route("/perfil/<usuario>") #<usuario> diz que isto é uma variável
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))










