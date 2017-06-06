from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        
        self.relatorio = Button(self.widget1, width=50, bg="#ccc")
        self.relatorio["text"] = "Gerar Relatório de Unidades mais Procuradas"
        self.relatorio["command"] = self.gerarRelatorio
        self.relatorio.pack()

        self.msg1 = Label(self.widget1, text="Informe suas coordenandas")
        self.msg1.pack()

        self.procurar = Button(self.widget1, bg="#ccc", text="Procurar")
        self.procurar["command"] = self.procurarUnidade
        self.procurar.pack()

        self.msg2 = Label(self.widget1, text="Unidades de saúde mais próximas")
        self.msg2.pack()

        self.result = Text(self.widget1, width=45, height=5)        
        self.result.pack()

    def gerarRelatorio():


    def procurarUnidade():
        
    
root = Tk()
Application(root)
root.mainloop()
