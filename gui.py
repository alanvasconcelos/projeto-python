from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.widget2 = Frame(master)
        self.widget2["pady"] = 20
        self.widget2.pack()

        self.widget3 = Frame(master)
        self.widget3["pady"] = 10
        self.widget3.pack()
        
        self.relatorio = Button(self.widget1, width=50, bg="#ccc")
        self.relatorio["text"] = "Gerar Relatório de Unidades mais Procuradas"
        self.relatorio["command"] = self.gerarRelatorio
        self.relatorio.pack()

        self.msg1 = Label(self.widget2, text="Informe suas coordenandas").pack()
        self.msg2 = Label(self.widget2, text="Latitude: ").pack()

        self.latitude = Entry(self.widget2)
        self.latitude.pack()
        
        self.msg3 = Label(self.widget2, text="Longitude: ").pack()

        self.longitude = Entry(self.widget2)
        self.longitude.pack()
        
        self.procurar = Button(self.widget2, bg="#ccc", text="Procurar")
        self.procurar["command"] = self.procurarUnidade        
        self.procurar.pack()

        self.msg3 = Label(self.widget3, text="Unidades de saúde mais próximas").pack()

        self.result = Text(self.widget3, width=45, height=5)
        self.result.pack()

    def gerarRelatorio():
        pass

    def procurarUnidade():
        pass
    
root = Tk()
Application(root)
root.mainloop()
