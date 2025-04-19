from flask import Flask

app = Flask(__name__) #recomendação

@app.route("/") #cria uma rota para o site
def homepage():
    return "teste"
if __name__ == "__main__": #faz com que o site não rode ao ser importado
    app.run(debug=True)