from packages.materia import Materia

class Usuario():
    def __init__(self,nome,matricula,email):
        self.nome = nome
        self.matricula = matricula
        self.materias = []
        self.email = email

    def cadastrar_materia(self, nome_materia,professor,prioridade): #Método para cadastrar matéria
        for materia in self.materias:
            if materia.nome_materia == nome_materia:
                print(f'A matéria {nome_materia} já foi adicionada anteriormente.')
                return
        self.materias.append(Materia(nome_materia, professor, prioridade))
        print(f'A matéria {nome_materia} foi adicionada com sucesso.')

    def remover_materia(self,materia_removida): #Método para remover matérias
        for materia in self.materias:
            if materia.nome_materia == materia_removida:
                self.materias.remove(materia)
                print(f'A matéria {materia_removida} foi removida com sucesso')
                return #Termina o código aqui
        print(f'A matéria {materia_removida} não foi encontrada.')
