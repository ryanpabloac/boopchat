import sqlite3

class Chat():
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

    def get_chats(self, id):
        chats = []
        self.cursor.execute(f"SELECT * FROM chat WHERE remetente_id = ? or destinatario_id = ?", (id, id))
        chs = self.cursor.fetchall()
        for ch in chs:
            if ch[1] == id:
                tid = int(ch[2])
                self.cursor.execute(f"SELECT nome FROM usuario WHERE id = ?", (tid,))
                name = self.cursor.fetchall()
            elif ch[2] == id:
                tid = int(ch[1])
                self.cursor.execute(f"SELECT nome FROM usuario WHERE id = ?", (tid,))
                name = self.cursor.fetchall()

            if name[0][0] not in chats:
                chats.append(name[0][0])

        self.cursor.close()
        return chats

    def send_msg(self, dest, remet, msg):
        self.cursor.execute("INSERT INTO chat (destinatario_id, remetente_id, mensagem) VALUES (? , ?, ?)", (int(dest), int(remet), str(msg)))
        self.conn.commit()
        self.cursor.close()

    def get_msg(self, dest, remet):
        self.cursor.execute("SELECT * FROM chat WHERE remetente_id = ? and destinatario_id = ?", (remet, dest))
        hist = self.cursor.fetchall()
        self.cursor.close()

        return hist

t = Chat()
A = t.get_msg(dest=1,remet=2)
for a in A:
    print(a)
