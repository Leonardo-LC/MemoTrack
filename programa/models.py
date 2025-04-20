#Cria estrutura do banco de dados
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from programa import database, login_manager

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    matricula = database.Column(database.String, nullable=False)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

    materias = relationship("Materia",backref="usuario", lazy=True)

class Materia(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    professor = database.Column(database.String, nullable=False)
    prioridade = database.Column(database.Integer, nullable=False)

    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)