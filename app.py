from flask import Flask

#cria um objeto da classe Flask
app = Flask(__name__)

#função route() da classe Flask - url
@app.route("/")

#criar uma função para mostrar o primeiro flask
def first_flask():
    return "Eu gosto de programar (às vezes)"

#executar a aplicação no servidor
app.run(debug = True)