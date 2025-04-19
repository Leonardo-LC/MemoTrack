from flask import Flask, render_template, url_for

app = Flask(__name__) #recomendação

@app.route("/") #cria uma rota para o site
def homepage():
    return render_template("homepage.html")

@app.route("/perfil/<usuario>") #<usuario> diz que isto é uma variável
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)



if __name__ == "__main__": #faz com que o site não rode ao ser importado
    app.run(debug=True)