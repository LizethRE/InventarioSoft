import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controllers import productController
from views import products

class Increments:
	def __init__(self, user_name, user_role):
		self.controller = productController.ProductController()
		self.user_name= user_name
		self.user_role = user_role
		self.show()

	def show(self):
		self.root = Tk()
		self.root.title("InventarioSoft - Agregar")
		self.root.resizable(False, False)
		self.root.withdraw()
		self.root.update_idletasks()
		x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
		y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
		self.root.geometry("+%d+%d" % (x, y))
		self.root.deiconify()

		#inputs y label
		self.name = StringVar()
		inputNom = Entry(self.root, textvariable = self.name)
		inputNom.grid(row = 0, column = 1, padx = 10, pady = 10)

		labelNom = Label(self.root, text ="Nombre Producto:")
		labelNom.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = E)

		self.provider = StringVar()
		inputPro = Entry(self.root, textvariable = self.provider)
		inputPro.grid(row = 1, column = 1, padx = 10)

		labelPro = Label(self.root, text ="Proveedor:")
		labelPro.grid(row = 1, column = 0, padx = 10, sticky = E)

		self.category = ttk.Combobox(state="readonly")
		self.category.grid(row = 2, column = 1, padx = 10, pady = 10)
		self.category["values"] = ["Bebidas", "Carnes", "Frutas", "Verduras", "Lacteos", "Ropa", "Granos", "Otros"]

		labelCat = Label(self.root, text ="Categoria:")
		labelCat.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = E)

		self.price = StringVar()
		inputPre = Entry(self.root, textvariable = self.price)
		inputPre.grid(row = 3, column = 1, padx = 10)

		labelPre = Label(self.root, text ="Precio:")
		labelPre.grid(row = 3, column = 0, padx = 10, sticky = E)

		self.stock = StringVar()
		inputCan = Entry(self.root, textvariable = self.stock)
		inputCan.grid(row = 4, column = 1, padx = 10, pady = 10)

		labelCan = Label(self.root, text ="Cantidad:")
		labelCan.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = E)
		#botones

		buttonIncrement = Button(self.root, text ="AGREGAR", command = self.increment)
		buttonIncrement.grid(row = 5, column = 1, padx = 10, pady = 10, sticky = E)

		buttonExit = Button(self.root, text="CANCELAR", command=self.cancel)
		buttonExit.grid(row=5, column=0, padx=10, pady=10, sticky=E)

		self.root.mainloop()

	def increment(self):
		name = self.name.get()
		provider = self.provider.get()
		category = self.category.get()
		price = self.price.get()
		stock = self.stock.get()
		if name != '' and provider != '' and category != '' and price != '' and stock != '':
			response = self.controller.add(name, provider, category, price, stock)
			if response != -1:
				messagebox.showinfo("InventarioSoft - Agregar", "Producto agregado correctamente")
				self.close()
				products.Products(self.user_name, self.user_role)
			else:
				self.name.set('')
				messagebox.showinfo("InventarioSoft - Agregar", "Ya existe un producto con el mismo nombre")
		else:
			messagebox.showinfo("InventarioSoft - Agregar", "Se deben llenar todos los campos")

	def cancel(self):
		self.close()
		products.Products(self.user_name, self.user_role)

	def close(self):
		self.root.destroy()