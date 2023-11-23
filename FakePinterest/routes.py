from flask import render_template, url_for, redirect
from FakePinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.models import Usuario, Foto
from FakePinterest.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename

# Criando uma rota, assim conseguimos criar o caminho do site:

@app.route("/", methods=["GET", "POST"]) # Deve-se passar o que vem depois do domínio principal, como é a homepage, crie com o "/"

def homepage(): # A função que vai exibir a página inicial
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formLogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha.encode("utf-8"), formLogin.senha.data):
            login_user(usuario)
            return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("homepage.html", form=formLogin) # Utilizando o código HTML criado na pasta template

@app.route("/criarconta", methods=["GET", "POST"])

def criarconta():
    formCriarConta = FormCriarConta()
    if formCriarConta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formCriarConta.senha.data).decode("utf-8")
        usuario = Usuario(username=formCriarConta.username.data, senha=senha, email=formCriarConta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html",form=formCriarConta)

# Para cada novo link que for criado, deve-se passar outro "@app.route" junto a outra função:

@app.route("/perfil/<id_usuario>", methods=["GET", "POST"]) # A tag <usuário> diz para o python que ela é uma variável, ou seja, ela pode ser dinâmica
@login_required
def perfil(id_usuario): # Pela tag ser uma variável, deve-se passar a mesma dentro da função
    if int(id_usuario) == int(current_user.id):
        form_foto = FormFoto()
        if form_foto.validate_on_submit():
            arquivo = form_foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # Salvar o arquivo na pasta Fotos_post:
            caminho = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            arquivo.save(caminho)
            # Registrar esse arquivo no banco de dados:
            foto = Foto(imagem=nome_seguro, id_usuario=current_user.id)
            database.session.add(foto) # Adicionar a foto no banco de dados
            database.session.commit() # Salvando a foto no banco de dados
        return render_template("perfil.html", usuario=current_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None) # Utilizando o código HTML criado na pasta template

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criação).all()
    return render_template("feed.html", fotos=fotos)
