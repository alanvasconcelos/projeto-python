from Banco import Banco

class UnidadeSaude(object):
        
    def __init__(self, codigo = 0, nome = "", qtd = 0):
        self.info = {}
        self.codigo = codigo
        self.nome = nome
        self.qtd = qtd

    def inserirUnidade(self):
        banco = Banco()
        
        try:
            c = banco.conexao.cursor()
   
            c.execute("INSERT INTO unidades VALUES ('" + self.codigo + "', '" + self.nome + "', " + self.qtd + ")")
            
            banco.conexao.commit()
            c.close()
   
            return 1
        except:
            return "Ocorreu um erro na inserção da unidade"

    def buscarUnidades(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
   
            c.execute("SELECT * FROM unidades ORDER BY qtd")

            unidades = []
            for linha in c:
                unidade = []
                unidade.append(linha[0])
                unidade.append(linha[1])
                unidade.append(linha[2])
                unidades.append(unidade)
   
            c.close()
   
            return unidades
        except:
            return "Ocorreu um erro ao buscas as unidades"
