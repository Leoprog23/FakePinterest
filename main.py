# Para criar o ambiente virtual com o intuito de utilização e criação do site, você precisar passar os comandos abaixo:

    # CTRL + SHIFT + P --> Cria o ambiente virtual
    # nome-do-ambiente\Scripts\activate --> Altera para o ambiente virtual
    # nome-do-ambiente\Scripts\deactivate --> Desativa o ambiente virtual
    # Se o site possuir um banco de dados, passar como "pip install flask-sqlalchemy" --> Gestor do SQL que vai permitir integrar em um banco de dados
    # Para fazer gerenciamento de senhas, passar como "pip install flask-login flask-bcrypt"
    # Utilize, também, o "pip install flask-wtf e o pip install email_validator"

# Colocando o site no ar:
from FakePinterest import app

if __name__ == "__main__":
    app.run(debug=False) # Todas as alterações que fizermos no código, serão enviadas para interface do site se passar o parâmetro "debug=True"