import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from controllers import productController
from views import sales,increments, delete, buy, login

class Products:
    def __init__(self, user_name, user_role):
        self.controller = productController.ProductController()
        self.user_name= user_name
        self.user_role = user_role
        self.showProducts()

    def showProducts(self):
        self.root = Tk()
        self.root.title("InventarioSoft - Products")
        self.root.geometry("1060x500")
        self.root.resizable(False, False)

        labelfont = ("arial", 12, "bold")
        title = Label(self.root, text ="PRODUCTOS")
        title.grid(row = 0, column = 2, pady = 10)
        title.config(fg = "black", font = labelfont)

        subLabel = ("arial", 10, "bold")
        subtitle = Label(self.root, text="Cuenta: {} - {}".format(self.user_name, self.user_role))
        subtitle.grid(row=0, column=1, pady=10)
        subtitle.config(fg="black", font=subLabel)

        esp = Label(self.root, text ="-----")
        esp.grid(row = 0, column = 0)
        esp.config(font = 30, fg = "gray85")

        esp2 = Label(self.root, text ="-----")
        esp2.grid(row = 0, column = 6)
        esp2.config(font = 30, fg = "gray85")
        # Tabla
        self.table = ttk.Treeview(columns = ("", "", "", ""), height = 19)
        self.table.grid(row = 1, column = 1, columnspan = 4)
        self.table.heading("#0", text ="Nombre del Producto", anchor = CENTER)
        self.table.column("#0", minwidth = 180, width = 200)
        self.table.heading("#1", text ="Proveedor", anchor = CENTER)
        self.table.column("#1", minwidth = 70, width = 200)
        self.table.heading("#2", text ="Categoria", anchor = CENTER)
        self.table.column("#2", minwidth = 0, width = 200)
        self.table.heading("#3", text ="Precio", anchor = CENTER)
        self.table.column("#3", minwidth = 0, width = 200)
        self.table.heading("#4", text ="Cantidad", anchor = CENTER)
        self.table.column("#4", minwidth = 0, width = 200)

        self.toList()
        #botones
        btnLogout = Button(text = "CERRAR SESION", command=self.logout).grid(row = 0, column = 4)
        if self.user_role == 'Administrador':
            btnSell = Button(text = "VENDER", command=self.sell).grid(row = 2, column = 1, sticky =W + E)
            btnAdd = Button(text = "AGREGAR", command=self.add).grid(row = 2, column = 2, sticky = W + E)
            btnBuy = Button(text = "COMPRAR EXISTENCIAS", command=self.buy).grid(row = 2, column = 3, sticky = W + E)
            btnDelete = Button(text = "ELIMINAR DEL INVENTARIO", command=self.delete).grid(row = 2, column = 4, sticky = W + E)
        elif self.user_role == 'Cajero':
            btnSell = Button(text="VENDER", command=self.sell).grid(row=2, column=2, sticky=W + E)
            btnBuy = Button(text="COMPRAR EXISTENCIAS", command=self.buy).grid(row=2, column=3, sticky=W + E)

        self.root.mainloop()

    def toList(self):
        products = self.controller.getProducts()
        for product in products:
            self.table.insert("", 1000, iid=product[0], text = product[1], values = (product[2], product[3], '${}'.format(product[4]), product[5]))

    def sell(self):
        selected = self.table.selection()
        if len(selected) == 1:
            serial_num = selected[0]
            name = self.table.item(selected).get('text')
            stock = self.table.item(selected).get('values')[3]
            self.close()
            sales.Sales(serial_num, name, stock, self.user_name, self.user_role)
        else:
            messagebox.showinfo("InventarioSoft - Productos","No ha selecccionado ninguno, o ha seleccinado mas de uno")

    def buy(self):
        selected = self.table.selection()
        if len(selected) == 1:
            serial_num = selected[0]
            name = self.table.item(selected).get('text')
            stock = self.table.item(selected).get('values')[3]
            self.close()
            buy.Buy(serial_num, name, stock, self.user_name, self.user_role)
        else:
            messagebox.showinfo("InventarioSoft - Productos","No ha selecccionado ninguno, o ha seleccinado mas de uno")

    def delete(self):
        selected = self.table.selection()
        if len(selected) == 1:
            serial_num = selected[0]
            name = self.table.item(selected).get('text')
            self.close()
            delete.Delete(serial_num, name, self.user_name, self.user_role)
        else:
            messagebox.showinfo("InventarioSoft - Productos","No ha selecccionado ninguno, o ha seleccinado mas de uno")

    def add(self):
        self.close()
        increments.Increments(self.user_name, self.user_role)

    def logout(self):
        self.close()
        login.Login()

    def close(self):
        self.root.destroy()

#Products('Gerson','Cajero')