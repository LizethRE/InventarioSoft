import tkinter
from tkinter import *
from tkinter import messagebox
from controllers import productController
from views import products

class Sales:
	def __init__(self, serial_num, name, stock, user_name, user_role):
		self.controller = productController.ProductController()
		self.serial_num = serial_num
		self.name= name
		self.stock = stock
		self.user_name = user_name
		self.user_role= user_role
		self.show()

	def show(self):
		self.root = Tk()
		self.root.title("Venta")
		#icono = Image("photo", file = "./assets/images/inventory.png")
		#self.raiz.tk.call("wm", "iconphoto" ,self.raiz._w, icono)
		self.root.resizable(False, False)

		self.root.withdraw()
		self.root.update_idletasks()
		x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
		y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
		self.root.geometry("+%d+%d" % (x, y))
		self.root.deiconify()

		#inputs y label
		self.numP = StringVar()
		inputNum = Entry(self.root, textvariable = self.numP)
		inputNum.configure(state='readonly')
		inputNum.grid(row = 0, column = 1, padx = 10, pady = 10)
		self.numP.set(self.serial_num)

		labelNum = Label(self.root, text ="Numero de Serie:")
		labelNum.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = E)

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

		labelQua = Label(self.root, text="Cantidad")
		labelQua.grid(row=3, column=0, padx=10, pady=10, sticky=E)

		#botones
		buttonSell = Button(self.root, text ="EFECTUAR VENTA", command = self.toSell)
		buttonSell.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = E)

		buttonExit = Button(self.root, text="CANCELAR", command=self.cancel)
		buttonExit.grid(row=4, column=0, padx=10, pady=10, sticky=E)

		self.root.mainloop()

	def toSell(self):
		if self.numP.get() != '' and self.quantity.get() != '':
			response = self.controller.sell(self.numP.get(), self.quantity.get())
			if type(response) == tuple:
				messagebox.showinfo("InventarioSoft - Venta",
									"Venta exitosa, quedan {} unidades del producto: {}.".format(response[0],
																								 response[1]))
				self.close()
				products.Products(self.user_name, self.user_role)
			elif response >= 0:
				messagebox.showinfo("InventarioSoft - Venta","Unidades insuficientes, solo hay {}".format(response))
			elif response == -1:
				messagebox.showinfo("InventarioSoft - Venta","No hay existencias disponibles para vender.")
		else:
			messagebox.showinfo("InventarioSoft - Venta","Es necesario especificar la cantidad a vender")

	def cancel(self):
		self.close()
		products.Products(self.user_name, self.user_role)

	def close(self):
		self.root.destroy()

#Sales('2', 'Jean', '5', 'Usuario', 'Administrador')