import sqlite3

class Banco():
    def __init__(self):
        conexao = sqlite3.connect('banco.db')
        self.createTable()
   
    def createTable(self):
        c = self.conexao.cursor()
   
        c.execute("""create table if not exists unidades (
                       codigo integer primary key,
                       nome text,
                       qtd integer)""")
        
        self.conexao.commit()
        c.close()
