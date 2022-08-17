from pytkuser import Tabela_cadastro
from tkinter import *

class Cadastro_Cliente:
    def __init__(self, master=None):

        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()



        self.titulo = Label(self.container1, text="Informe o Cadastro :")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack ()

        self.lblidcadastro = Label(self.container2,
        text="idCadastro:", font=self.fonte, width=10)
        self.lblidcadastro.pack(side=LEFT)

        self.txtidcadastro = Entry(self.container2)
        self.txtidcadastro["width"] = 10
        self.txtidcadastro["font"] = self.fonte
        self.txtidcadastro.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarcadastro
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblsobrenome = Label(self.container4, text="Sobrenome:",
        font=self.fonte, width=10)
        self.lblsobrenome.pack(side=LEFT)

        self.txtsobrenome = Entry(self.container4)
        self.txtsobrenome["width"] = 25
        self.txtsobrenome["font"] = self.fonte
        self.txtsobrenome.pack(side=LEFT)

        self.lblcpf= Label(self.container5, text="CPF:",
        font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container5)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)




        self.bntInsert = Button(self.container6, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)


        self.lblmsg = Label(self.container7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Tabela_cadastro()

        user.nome = self.txtnome.get()
        user.sobrenome = self.txtsobrenome.get()
        user.cpf = self.txtcpf.get()
        

        self.lblmsg["text"] = user.insere_user()

        self.txtidcadastro.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtsobrenome.delete(0, END)
        self.txtcpf.delete(0, END)


    def buscarcadastro(self):
        user = Tabela_cadastro()

        id = self.txtidcadastro.get()

        self.lblmsg["text"] = user.selectusuario(id)

        self.txtidcadastro.delete(0, END)
        self.txtidcadastro.insert(INSERT, user.id)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtsobrenome.delete(0, END)
        self.txtsobrenome.insert(INSERT,user.sobrenome)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, user.cpf)



root = Tk()
Cadastro_Cliente(root)
root.mainloop()