#Cria estrutura do banco de dados
from sqlalchemy.orm import relationship

from programa import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    matricula = database.Column(database.String, nullable=False)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    materias = relationship()

class Materia(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    professor = database.Column(database.String, nullable=False)
    prioridade = database.Column(database.Integer, nullable=False)

    usuario_id = database.Column()