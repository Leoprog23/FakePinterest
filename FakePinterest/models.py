# Criar a estrutura do banco de dados:
from FakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario)) # Retornanod um usuário específico

class Usuario(database.Model, UserMixin): # O database.Model é o que permite a criação da classe no formato em que o banco de dados irá entender, vai permitir criar uma tabela no banco de dados
    id = database.Column(database.Integer, primary_key=True) # Criando uma coluna no banco de dados
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    fotos = database.relationship("Foto", backref="usuario", lazy=True) # Não será uma coluna, será uma relação das tabelas


class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criação = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer,database.ForeignKey('usuario.id'), nullable=False)
