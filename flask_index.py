from flask import Flask, render_template

#cria um objeto da classe Flask
app = Flask(__name__)

#função route() da classe Flask - url
@app.route("/site")

#criar uma função para mostrar o primeiro flask
def first_webpage():
    return render_template("index.html")

#executar a aplicação no servidor
app.run(debug = True)