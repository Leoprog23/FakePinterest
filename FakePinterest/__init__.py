from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

# Criando o site, a aplicação:

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")# Pegando o link do banco de dados virtual utilizado pelo Render
app.config["SECRET_KEY"] = "df406478193049f187564a3a4da5f8dc"
app.config["UPLOAD_FOLDER"] = "static/Fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"
# Importando os outros arquivos para utilização:

from FakePinterest import routes