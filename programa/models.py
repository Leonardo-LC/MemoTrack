#Cria estrutura do banco de dados

from programa import database

class Usuario(database.Model):
    matricula = database.Column()
    username = database.Column()
    email = database.Column()
    senha = database.Column()
    materias = database.Column()

class Materia(database.Model):
    codigo = database.Column()
    nome = database.Column()
    professor = database.Column()
    prioridade = database.Column()
    matricula_usuario = database.Column()