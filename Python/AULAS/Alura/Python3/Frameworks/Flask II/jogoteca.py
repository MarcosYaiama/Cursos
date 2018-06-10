from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
from models import Jogo, Usuario
from dao import JogoDao, UsuarioDao

app = Flask(__name__)
app.secret_key = 'alura'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWD'] = ""
app.config['MYSQL_DB'] = "jogoteca"
app.config['MYSQL_PORT'] = 3306

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
        jogo_dao.salvar(new_game)
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


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/registrar' , methods=['POST',])
def registrar_usuario():
    return render_template('login.html', titulo="Faça seu registro")    

@app.route('/novo_usuario', methods=['POST', 'GET'])
def autenticar_novo_usuario():
    pass


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
    return protege_rota(
        render_template('editar.html', titulo='Editando Jogo', jogo = jogo),
        "login",
        "editar"
    )

@app.route('/atualizar', methods=['POST', ])
def atualizar():
    jogo = Jogo(request.form['nome'],request.form['categoria'], request.form['console'], request.form['id'])
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))

app.run(debug=True)
