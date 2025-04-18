class Materia():
    def __init__(self,nome_materia,professor,prioridade):
        self.nome_materia = nome_materia
        self.professor = professor
        self.prioridade = prioridade

    def info(self):
        return f'Matéria: {self.nome_materia} - Professor: {self.professor} - Prioridade: {self.prioridade}'
