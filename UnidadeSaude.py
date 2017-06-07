from Banco import Banco

class UnidadeSaude(object):
        
    def __init__(self, codigo = 0, nome = ""):
        self.info = {}
        self.codigo = codigo
        self.nome = nome

    def inserirUnidade(self):
        banco = Banco()
        
        try:
            c = banco.conexao.cursor()
   
            c.execute("INSERT INTO unidades (codigo, nome) VALUES (" + self.codigo + ", '" + self.nome + "')")
            
            banco.conexao.commit()
            c.close()
   
            return 1
        except:
            return "Ocorreu um erro na inserção da unidade"

    def buscarUnidades(self):
        banco = Banco()

        try:
            c = banco.conexao.cursor()
   
            c.execute("SELECT codigo, nome, COUNT(*) FROM unidades GROUP BY codigo ORDER BY COUNT(*) DESC")

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
            return "Ocorreu um erro ao buscar as unidades"
