from models.product import Product

class ProductController:
    def __init__(self):
        pass

    def getProducts(self):
        producto = Product()
        list = producto.readAll()
        return list

    def sell(self, num_serie, cantidad_a_vender):
        product = Product()
        product.serial_num = num_serie
        result = product.read()
        if result:
            stock = result[0][5]
            name = result[0][1]
            if stock > 0:
                resta = stock - int(cantidad_a_vender)
                if resta >= 0:
                    product.stock = resta
                    product.updateStock()
                    return (resta, name)
                else:
                    return stock
            else:
                return -1

    def buy(self, num_serie, cantidad_a_comprar):
        product = Product()
        product.serial_num = num_serie
        result = product.read()
        if result:
            stock = result[0][5]
            sum = stock + int(cantidad_a_comprar)
            product.stock = sum
            product.updateStock()
            return product.stock


    def add(self, nombre, proveedor, categoria, precio, existencias):
        product = Product()
        product.name_product = nombre
        result = product.read()
        if result:
            return -1
        else:
            product.provider = proveedor
            product.category = categoria
            product.unit_price = precio
            product.stock = existencias
            product.create()
            return product

    def delete(self, num_serie):
        product = Product()
        product.serial_num = num_serie
        result = product.read()
        if result:
            product.delete()
            return 1

