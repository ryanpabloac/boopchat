import sqlite3
from scripts import chating

from flask import Flask, request, render_template, redirect, session, url_for, jsonify
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
    dest = session.get("d_username")
    user = session.get("usuario_id")

    chat = chating.Chat()
    chats = chat.get_chats(session["usuario_id"])
    
    conn = sqlite3.connect("BoopChat.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM usuario WHERE id = ?", (user, ))
    usuario = cursor.fetchone()
    conn.close()

    msg = request.args.get('msg')
    if msg: 

        try:
            destinatario = session["destinatario_id"][0]
        except:
            destinatario = session["destinatario_id"]

        chat = chating.Chat()
        msgs = chat.get_msg(dest=destinatario, remet=user) 
        return render_template('chat.html', chats=chats, msgs=msgs, user=usuario[0], dest=dest)
        
    else:  
        return render_template('chat.html', chats=chats, user=usuario, dest=dest)
        

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
    return redirect("/")

@app.route("/chat", methods=["POST"])
def chat():
    conn = sqlite3.connect("BoopChat.db")
    cursor = conn.cursor()

    if request.headers.get('X-Requested-With') =='XMLHttpRequest':
        data = request.get_json()
        d_username = data.get('d_username')

        session['d_username'] = d_username
        cursor.execute("SELECT id FROM usuario WHERE nome = ?", (d_username,))
        destinatario_id = cursor.fetchone()

        cursor.execute("SELECT nome FROM usuario WHERE id = ?", (session['usuario_id'], ))
        usuario = cursor.fetchone()

        if not destinatario_id:
            return redirect(url_for("errors", tipo_erro=404, erro="Destinatário não identificado"))
        
        session['destinatario_id'] = destinatario_id

        chat = chating.Chat()
        msgs = chat.get_msg(dest=session["destinatario_id"][0], remet=session['usuario_id'])
        messages = []
        for msg in msgs:
            if msg[1] == session['usuario_id']:
                messages.append({
                    "remetente": usuario[0],
                    "mensagem": msg[3],
                    'data': msg[4]
                })
            else:
                messages.append({
                    "remetente": d_username,
                    "mensagem": msg[3],
                    'data': msg[4]
                })  

        return messages

    else:
        mensagem = request.form.get("mensagem")
        usuario_id = session.get("usuario_id")
        destinatario_nome = session.get("d_username")

        cursor.execute("SELECT id FROM usuario WHERE nome = ?", (destinatario_nome,))
        destinatario_id = cursor.fetchone()
        if not destinatario_id:
            return redirect(url_for("errors", tipo_erro=404, erro="Destinatário não identificado"))
        if not usuario_id:
            return redirect(url_for("errors", tipo_erro=401, erro="Usuário não autenticado"))
        

        cursor.execute("INSERT INTO chat (remetente_id, destinatario_id, mensagem) VALUES (?, ?, ?);",(usuario_id, destinatario_id[0], mensagem))
        conn.commit()
        conn.close()
        return redirect("/chat" + "?msg=True")

@app.route("/newchat", methods=["POST"])
def newchat():
    email = request.form.get('email')
    mensagem = request.form.get('msg')

    chat = chating.Chat()
    dest_id = chat.confirm_user(email)

    if dest_id == None:
        return redirect(url_for("errors", tipo_erro=404, erro="Destinatário não encontrado"))
    
    session["destinatario_id"] = dest_id
    chat.send_msg(dest_id, session["usuario_id"], mensagem)
    
    return redirect(f"/chat")

@app.route("/erro")
def errors():
    tipo_erro = request.args.get('tipo_erro')
    erro = request.args.get('erro')
    return render_template("erros.html", tipo_erro=tipo_erro, erro=erro)

@app.errorhandler(404)
def not_found(e):
    return render_template('erros.html', tipo_erro=404, erro="Página não encontrada"), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
