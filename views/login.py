from tkinter import *
from tkinter import messagebox
from controllers import loginController
from views import products

class Login:
    def __init__(self):
        self.controller = loginController.UserController()
        self.show()

    def show(self):
        self.root = Tk()
        self.root.title("InventarioSoft - Login")
        icono = Image("photo", file = "./assets/images/inventory.png")
        self.root.tk.call("wm", "iconphoto", self.root._w, "-default", icono)
        self.root.resizable(False, False)
        myFrame = Frame(self.root, width = 345, height = 390)
        myFrame.pack()
        self.root.withdraw()
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2
        self.root.geometry("+%d+%d" % (x, y))
        self.root.deiconify()
        myImage = PhotoImage(file = "./assets/images/inventoryB.png")
        Label(myFrame, image = myImage).place(x = 107, y = 20)

        self.card_id = StringVar()
        cuadroCed = Entry(myFrame, textvariable = self.card_id)
        cuadroCed.place(x = 130, y = 170)

        labelCed = Label(myFrame, text = "Cedula:")
        labelCed.place(x = 57, y = 170)

        self.password = StringVar()
        cuadroPass = Entry(myFrame, textvariable = self.password)
        cuadroPass.place(x = 130, y = 210)
        cuadroPass.config(show = "*")

        labelPass = Label(myFrame,text = "Password:")
        labelPass.place(x = 40, y = 210)
        # botones
        buttonLogin = Button(myFrame, text="INGRESAR", command=self.login)
        buttonLogin.place(x=130, y=290)

        buttonClose = Button(myFrame, text="SALIR", command=self.close)
        buttonClose.place(x=145, y=340)

        self.root.mainloop()

    def login(self):
        response = self.controller.login(self.card_id.get(), self.password.get())
        if response:
            name_complete = "{} {}".format(response[0][2], response[0][3])
            rol = response[0][4]
            self.close()
            products.Products(name_complete, rol)
        else:
            self.password.set('')
            messagebox.showinfo("InventarioSoft - Login", "Datos invalidos, por favor intentalo de nuevo..")

    def close(self):
        self.root.destroy()
