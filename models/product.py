
from connection.db import DBConn

class Product:
    def __init__(self):
        self.serial_num = 0
        self.name_product = ''
        self.provider = ''
        self.category = ''
        self.unit_price = 0
        self.stock = 0
        self.db = DBConn()

    def create(self):
        #crear un nuevo registro
        query = "INSERT INTO Producto ( nombreproducto, proveedor, categoria, preciounidad, cantidadexistente) VALUES (%s, %s, %s, %s, %s)"
        values = (self.name_product, self.provider, self.category, self.unit_price, self.stock)
        self.db.execute(query, values, False)

    def update(self):
        #Actualizar un registro existente
        query = "UPDATE Producto SET nombreproducto = %s, proveedor = %s, categoria = %s, preciounidad = %s, cantidadexistente = %s WHERE num_serie = %s"
        values = (self.name_product, self.provider, self.category, self.unit_price, self.stock, self.serial_num)
        return self.db.execute(query, values, False)

    def updateStock(self):
        #Actualizar un registro existente
        query = "UPDATE Producto SET cantidadexistente = %s WHERE num_serie = %s"
        values = (self.stock, self.serial_num)
        return self.db.execute(query, values, False)

    def readAll(self):
        #Leer todos los registros
        query = "SELECT * FROM Producto"
        return self.db.execute(query, '', True)

    def read(self):
        query = "SELECT * FROM Producto WHERE num_serie = %s"
        values = (self.serial_num,)
        return self.db.execute(query, values, True)

    def readName(self):
        query = "SELECT * FROM Producto WHERE nombreproducto = %s"
        values = (self.name_product,)
        return self.db.execute(query, values, True)

    def delete(self):
        #Elimina uno o todos los registros
        query = "DELETE FROM Producto WHERE num_serie = %s"
        values = (self.serial_num,)
        return self.db.execute(query, values, False)
