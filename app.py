import sqlite3
from scripts import chating

from flask import Flask, request, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

@app.route("/", methods=['GET'])
def site():
    return render_template('index.html')

@app.route("/retornoSite", methods=['GET'])
def retornoSite():
    return render_template('index.html')

@app.route("/cadastro", methods=['GET'])
def formularioCadastro():
    return render_template('cadastro.html')

@app.route("/login", methods=['GET'])
def formularioLogin():
    return render_template('login.html')

@app.route("/chat", methods=['GET'])
def formularioChat():
    chat = chating.Chat()
    chats = chat.get_chats(session["usuario_id"])
    return render_template('chat.html', chats=chats)

@app.route("/cadastro", methods=['POST'])
def cadastro():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    senha_hash = generate_password_hash(senha)

    try:
        conn = sqlite3.connect('BoopChat.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
        conn.commit()
        conn.close()
        return redirect("/login")
    except sqlite3.IntegrityError:
        return "Email já cadastrado."

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    senha = request.form.get("senha")

    conn = sqlite3.connect("BoopChat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, senha FROM usuario WHERE email = ?", (email, ))
    usuario = cursor.fetchone()
    conn.close()

    if usuario and check_password_hash(usuario[1], senha):
        session["usuario_email"] = email
        session["usuario_id"] = usuario[0]
        return redirect("/chat")
    else:
        return "Email ou senha inválidos."

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/retornoSite")

@app.route("/chat", methods=["POST"])
def chat():
    mensagem = request.form.get("mensagem")
    usuario_id = session.get("usuario_id")

    if not usuario_id:
        return "Usuário não autenticado", 401

    conn = sqlite3.connect("BoopChat.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO mensagem (usuario_id, mensagem) VALUES (?, ?)",(usuario_id, mensagem))
    conn.commit()
    conn.close()
    return redirect("/chat" )


if __name__ == '__main__':
    app.run(debug=True)
