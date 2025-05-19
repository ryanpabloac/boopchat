from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

client = MongoClient("mongodb://localhost:27017/")
db = client['BoopChat']
usuarios_collection = db['usuarios']

@app.route("/", methods=['GET'])
def site():
    return render_template('index.html')

@app.route("/retornoSite", methods=['GET'])
def retornoSite():
    return render_template('index.html')

@app.route("/infos", methods=['GET'])
def infos():
    return render_template('infos.html')

@app.route("/cadastro", methods=['GET'])
def formulario_cadastro():
    return render_template('cadastro.html')

@app.route("/login", methods=['GET'])
def formulario_login():
    return render_template('login.html')

@app.route("/cadastro", methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    senha_hash = generate_password_hash(senha)

    if usuarios_collection.find_one({"email": email}):
        return "Email já cadastrado."

    usuarios_collection.insert_one({
        "nome": nome,
        "email": email,
        "senha": senha_hash
    })

    return redirect("/login")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = usuarios_collection.find_one({"email": email})

    if usuario and check_password_hash(usuario["senha"], senha):
        session["usuario_email"] = email
        session["usuario_id"] = str(usuario["_id"])  
        return "funcionou"
    else:
        return "Email ou senha inválidos."

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)