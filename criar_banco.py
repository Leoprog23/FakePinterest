from FakePinterest import database, app
from FakePinterest.models import Usuario, Foto
# Criando o banco de dados:

with app.app_context():
    database.create_all()