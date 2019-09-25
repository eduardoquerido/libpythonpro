from time import sleep

#Atributo Sessao
class Sessao:
    contador=0
    usuarios = []

    #Método salvar do atributo Sessao
    def salvar(self, usuario):
        Sessao.contador+=1
        usuario.id = Sessao.contador
        self.usuarios.append(usuario)

    # Método listar do atributo Sessao
    def listar(self):
        return self.usuarios

    # Método roll_back do atributo Sessao
    def roll_back(self):
        self.usuarios.clear() #Aqui estamos dando rollback nas informações, para que um teste não interfira com outro posteriormente

    # Método fechar do atributo Sessao
    def fechar(self):
        pass

#Atributo Conexao
class Conexao:

   # def __init__(self):
       # sleep(10)
    #Método gerar_sessao do atributo Conexao
    def gerar_sessao(self):
        return Sessao()
    #Método fechar do atributo Conexao
    def fechar(self):
        pass