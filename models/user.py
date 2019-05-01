from connection.db import DBConn

class User:
    def __init__(self):
        self.id_usuario = 0
        self.card_id = ''
        self.name = ''
        self.last_name = ''
        self.role = ''
        self.password = ''
        self.db = DBConn()

    def readAll(self):
        #Leer todos los registros
        query = "SELECT * FROM Usuario"
        return self.db.execute(query, True)

    def read(self):
        query = "SELECT * FROM Usuario WHERE cedula = %s AND password = MD5(%s)"
        values = (self.card_id, self.password)
        return self.db.execute(query, values, True)