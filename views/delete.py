from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers import productController
from views import products

class Delete:
    def __init__(self, serial_num, name, user_name, user_role):
        self.controller = productController.ProductController()
        self.serial_num= serial_num
        self.name = name
        self.user_name = user_name
        self.user_role = user_role
        self.show()

    def show(self):
        self.root = Tk()
        self.root.title("InventarioSoft - Eliminar")
        self.root.resizable(False, False)
        self.root.withdraw()
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()

        labelCan = Label(self.root, text="¿Seguro que desea eliminar el producto {}?".format(self.name))
        labelCan.grid(row=0, column=0, padx=10, pady=10, sticky=E)

        buttonYes = Button(self.root, text="SI", command=self.yes)
        buttonYes.grid(row=1, column=0, padx=10, pady=10, sticky=E)

        buttonNo = Button(self.root, text="NO", command=self.cancel)
        buttonNo.grid(row=1, column=1, padx=10, pady=10, sticky=E)

        self.root.mainloop()

    def yes(self):
        response = self.controller.delete(self.serial_num)
        if response == 1:
            messagebox.showinfo("InventarioSoft - Eliminacion", "Se ha eliminado correctamente el producto {} del inventario".format(self.name))
            self.close()
            products.Products(self.user_name, self.user_role)
        else:
            messagebox.showinfo("InventarioSoft - Eliminacion", "No se ha podido eliminar el producto, intentalo de nuevo")

    def cancel(self):
        self.close()
        products.Products(self.user_name, self.user_role)

    def close(self):
        self.root.destroy()

#Delete('Administrador')