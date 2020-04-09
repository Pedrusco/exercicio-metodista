 #coding: utf-8


#Classe Aluno com atributos nome, ra e curso
class Aluno:
    nome = "Pedro"
    ra = 288736
    curso="ads"
    
    #construtor recebendo os parametros nome, ra e curso
    def __init__(self, nome="Pedro", ra=288736, curso="ads"):
        self.nome = nome
        self.ra = ra
    
    def __del__(self):
        print("Finalizando")
    
    #Mostra na tela o nome e o ra do aluno
    def mostraAluno(self):
        print("Nome: %s" % self.nome)
        print("R.A.: %d" % self.ra)
