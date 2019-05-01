from models.user import User

class UserController:
    def __init__(self):
        pass

    def login(self, cedula, password):
        user = User()
        user.card_id = cedula
        user.password = password
        resultado = user.read()
        if resultado:
            #rol = resultado[0][4]
            return resultado