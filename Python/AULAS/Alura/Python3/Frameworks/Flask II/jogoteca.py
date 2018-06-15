from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
from flask_mysqldb import MySQL
from models import Jogo, Usuario
from dao import JogoDao, UsuarioDao
from time import time

import os

app = Flask(__name__)
#Puxa a configuração de um Arquivo Python externo
app.config.from_pyfile('config.py')

db = MySQL(app)
jogo_dao = JogoDao(db)

usuario_dao = UsuarioDao(db)

def protege_rota(render, redirecionamento, proxima):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for(redirecionamento, proxima=url_for(proxima)))
    return render

@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/usuarios")
def users_list():
    lista = usuario_dao.listar()
    return render_template('lista_usuario.html', titulo='Usuarios', usuarios=lista)
   
@app.route('/novo')
def novo():
    return protege_rota(
        render_template('novo.html', titulo='Novo Jogo'),
        "login",
        "novo"
    )


@app.route('/criar', methods=['POST',])
def criar():
    vazio = False
    formularios_cria_jogo = ["nome", "categoria", "console"]
    
    
    for i in formularios_cria_jogo:
        formulario = request.form[i]
        if(not formulario):
            vazio = True
            break
    
    if(not vazio):
        new_game = Jogo(request.form["nome"], request.form["categoria"], request.form["console"])
        flash("Jogo {} salvo com sucesso".format(new_game.nome))
        error = False
        jogo = jogo_dao.salvar(new_game)
        arquivo = request.files["arquivo"]                                      #Pega arquivos do request
        arquivo.save('{}/capa{}-{}.jpg'.format(app.config['UPLOAD_PATH'],jogo.id, time())) #Diz aonde o arquivo será salvo e o nome do arquivo
        return redirect(url_for('index'))
    else:
        error = True
        flash("Existem campos não preenchidos")
    return redirect(url_for('novo'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima, titulo="Faça seu login")


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            session['usuario_nome'] = usuario.nome
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Não logado, tente novamente!')
            return redirect(url_for('login'))
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/registrar' , methods=['POST', 'GET'])
def registrar_usuario():
    registro_usuario="true"
    return render_template('login.html', titulo="Faça seu registro",)    

@app.route('/novo_usuario', methods=['POST', 'GET'])
def autenticar_novo_usuario():
    id = str(request.form['id'])
    nome = str(request.form['usuario'])
    senha = str(request.form['senha'])
    #FAZER VERIFICAÇÃO DE SENHA DEPOIS !!!!!!!!!!!!!!
    if(usuario_dao.buscar_por_id(request.form['id'])):
        flash("Nome de Identificação já está em uso!")
        return render_template("login.html", registro_usuario=True, titulo="Faça seu registro")
    else:
        new_user = Usuario(id, nome, senha)
        usuario_dao.novo_usuario(new_user)
        return redirect(url_for("users_list"))
            

@app.route('/remover', methods=['POST', ])
def deletar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash("Você precisa estar logado para remover esse item")
        return redirect(url_for("login", proxima=url_for("index")))
    else:
        id = request.form["jogo"]
        jogo_dao.deletar(id)
        flash("Jogo removido com Sucesso")
        return redirect(url_for("index"))

#Pega o parametro passado pela URI, diz o tipo e já o 
# passa para a função como parametro
@app.route('/editar/<int:id>')
def editar(id):
    jogo = jogo_dao.busca_por_id(id)
    nome_imagem = recupera_imagem(id)
    return protege_rota(
        render_template('editar.html', titulo='Editando Jogo',
                         jogo = jogo, capa_jogo = nome_imagem),
        "login",
        "editar"
    )

@app.route('/atualizar', methods=['POST', ])
def atualizar():
    jogo = Jogo(request.form['nome'],request.form['categoria'], request.form['console'], request.form['id'])
    jogo_dao.salvar(jogo)
    deleta_arquivo(jogo.id)
    request.files["arquivo"].save("{}/capa{}-{}.jpg".format(app.config["UPLOAD_PATH"], jogo.id, time()))
    return redirect(url_for('index'))

#Pega o parametro chamado nome_arquivo via GET
#  e aramazena em uma variavel de mesmo nome 
@app.route('/uploads/<nome_arquivo>')
#Passa o parametro recebido via GET 
# como argumento para a função
def imagem(nome_arquivo):
    return send_from_directory("uploads", nome_arquivo)

#Pega a imagem na pasta uploads
def recupera_imagem(id):
    #Pega todos os arquivos do diretorio
    for nome_arquivo in os.listdir(app.config["UPLOAD_PATH"]):
        #Procura pelo arquivo que contenha a string
        if("capa{}".format(id) in nome_arquivo):
            print(nome_arquivo)
            return nome_arquivo

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    #remove o arquivo, o join concatena os paths
    os.remove(os.path.join(app.config["UPLOAD_PATH"], arquivo))

app.run(debug=True)
