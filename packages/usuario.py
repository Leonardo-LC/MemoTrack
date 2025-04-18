from packages.materia import Materia

class Usuario():
    def __init__(self,nome,matricula,email):
        self.nome = nome
        self.matricula = matricula
        self.materias = []
        self.email = email

    def cadastrar_materia(self, nome_materia,professor,prioridade): #Método para cadastrar matéria
        self.materias.append(Materia(nome_materia,professor,prioridade))