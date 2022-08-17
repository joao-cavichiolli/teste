import tkinter as tk

class tela(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.cria_widgets()
    
    def cria_widgets(self):
        self.acao_botao = tk.Button(self)
        self.acao_botao['text'] ="Olá\n(Clique Aqui)"
        self.acao_botao['command']=self.diz_ola
        self.acao_botao.pack(side='top')
        self.sair = tk.Button(self,text="Sair",fg='red',command=self.master.destroy)
        self.sair.pack(side="bottom")
    
    def diz_ola(self):
        print("Ola Testando saida em Shell ou console")
    
window = tk.Tk()
app = tela(master=window)
app.mainloop()