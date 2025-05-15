from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["BoopChat"]
colecao = db["Usuarios"]

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template('cadastro.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    colecao.insert_one({
        "nomeUsuario": nome,
        "email": email,
        "senha": senha
    })

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
