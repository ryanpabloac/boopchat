import sqlite3

conn = sqlite3.connect('BoopChat.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mensagem (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    remetente_id INTEGER NOT NULL,
    destinatario_id INTEGER NOT NULL,
    mensagem TEXT NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (remetente_id) REFERENCES usuario(id),
    FOREIGN KEY (destinatario_id) REFERENCES usuario(id)
);
''')


conn.commit()
conn.close()