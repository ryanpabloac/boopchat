import sqlite3

class chat():
    def __init__(self):
        self.conn = sqlite3.connect("BoopChat.db")
        self.cursor = self.__conn__.cursor()

    @property
    def conn(self):
        return self.__conn__ 
    
    @conn.setter
    def conn(self, connection): 
        self.__conn__ = connection

    @property 
    def cursor(self):
        return self.__cursor__
    
    @cursor.setter
    def cursor(self, crs):
        self.__cursor__ = crs

    def get_name(self, id):
        # chat = []
        # msg, tipo
        self.cursor.execute(f"SELECT * FROM chat WHERE remetente_id = ? or destinatario_id = ?", (id, id))
        chats = self.cursor.fetchall()
        self.cursor.close()
        return chats

    def insert(self, dest, remet, msg):
        self.cursor.execute("INSERT INTO chat (destinatario_id, remetente_id, mensagem) VALUES (? , ?, ?)", (int(dest), int(remet), str(msg)))
        self.conn.commit()
        self.cursor.close()

    def get_msg(self, dest, remet):
       self.cursor.execute("SELECT * FROM chat WHERE remetente_id = ? and destinatario_id = ?", (remet, dest))
       hist = self.cursor.fetchall()
       self.cursor.close()


test = chat()

print(test.get_chats(1))

""" 

[X] - Conectar com o banco
[ ] - Pegar mensagems que o usuario tem
[ ] - Armazenar o nome do usuario que ele esta conversando
[ ] - Passar o nome do usuario que ele esta conversando
[ ] - Printar no front 

"""
