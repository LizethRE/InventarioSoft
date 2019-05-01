from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers import productController
from views import products

class Buy:
    def __init__(self, serial_num, name, stock, user_name, user_rol):
        self.controller = productController.ProductController()
        self.serial_num = serial_num
        self.name = name
        self.stock = stock
        self.user_name= user_name
        self.user_role = user_rol
        self.show()

    def show(self):
        self.root = Tk()
        self.root.title("Compra")
        self.root.resizable(False, False)

        self.root.withdraw()
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()

        # inputs y label
        self.numP = StringVar()
        inputNum = Entry(self.root, textvariable=self.numP)
        inputNum.configure(state='readonly')
        inputNum.grid(row=0, column=1, padx=10, pady=10)
        self.numP.set(self.serial_num)

        labelNum = Label(self.root, text="Numero de Serie:")
        labelNum.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        self.nom = StringVar()
        inputNom = Entry(self.root, textvariable=self.nom)
        inputNom.configure(state='readonly')
        inputNom.grid(row=1, column=1, padx=10)
        self.nom.set(self.name)

        labelNom = Label(self.root, text="Nombre:")
        labelNom.grid(row=1, column=0, padx=10, sticky=E)

        self.stock_now = StringVar()
        inputExist = Entry(self.root, textvariable=self.stock_now)
        inputExist.configure(state='readonly')
        inputExist.grid(row=2, column=1, padx=10, pady=10)
        self.stock_now.set(self.stock)

        labelStock = Label(self.root, text="Existencias:")
        labelStock.grid(row=2, column=0, padx=10, pady=10, sticky=E)

        self.quantity = StringVar()
        inputQua = Entry(self.root, textvariable=self.quantity)
        inputQua.grid(row=3, column=1, padx=10, pady=10)

        labelQua = Label(self.root, text="Cantidad a comprar:")
        labelQua.grid(row=3, column=0, padx=10, pady=10, sticky=E)

        # botones
        buttonBuy = Button(self.root, text="EFECTUAR COMPRA", command=self.toBuy)
        buttonBuy.grid(row=4, column=1, padx=10, pady=10, sticky=E)

        buttonExit = Button(self.root, text="CANCELAR", command=self.cancel)
        buttonExit.grid(row=4, column=0, padx=10, pady=10, sticky=E)

        self.root.mainloop()

    def toBuy(self):
        if self.numP.get() != '' and self.quantity.get() != '':
            response = self.controller.buy(self.numP.get(), self.quantity.get())
            if response:
                messagebox.showinfo("InventarioSoft - Compra",
                                    "Compra exitosa, ahora hay {} unidades del producto: {}.".format(response, self.name))
                self.close()
                products.Products(self.user_name, self.user_role)
        else:
            messagebox.showinfo("InventarioSoft - Compra", "Es necesario especificar la cantidad a comprar")

    def close(self):
        self.root.destroy()

    def cancel(self):
        self.close()
        products.Products(self.user_name, self.user_role)

#Buy('1', 'Camisa','5', 'Admin')