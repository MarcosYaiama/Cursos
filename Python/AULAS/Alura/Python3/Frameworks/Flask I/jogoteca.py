from flask import Flask,render_template, request, redirect, session, flash, url_for
# import os
app = Flask(__name__)
app.secret_key = 'caelum'
class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

class Usuario():
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

jogo1 = Jogo('Super Mario', 'Ação', 'Super Nintendo')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'Super Nintendo')
lista = [jogo1, jogo2, jogo3]

usuario1 = Usuario('luan', 'Luan Marques', '1234')
usuario2 = Usuario('Nico', 'Nico Steppat', '7a1' )
usuario3 = Usuario('flavio', 'Flávio', 'javascript')
usuario4 = Usuario('NicholasWM', 'Nicholas', 'mestra')

usuarios = {usuario1.id: usuario1, usuario2.id: usuario2,usuario3.id: usuario3,usuario4.id: usuario4 }

usuario_atual = ''

formularios = ['nome', 'categoria', 'console']

def protege_conteudo(render, redirecionamento):
    if('usuario_logado' not in session or session['usuario_logado'] == None):
        flash('Faça seu login para poder acessar essa página!')
        return redirect(redirecionamento)
    else:
        return render

@app.route('/')
def index():
    return protege_conteudo(render_template('lista.html',  titulo='Jogos', jogos=lista), url_for('login'))

@app.route('/novo')
def novo():
    return protege_conteudo(render_template("novo.html", titulo='Novo Jogo'), url_for('login', proxima=url_for('novo')))
      
@app.route('/criar', methods=['POST',])
def criar():
    valores_form = {} 
    vazio = False
    atributo = []
    c = 0
    for i in formularios:
        valores_form[i] = request.form[i]
        if(not request.form[i]):
            c += 1
            vazio = True
            atributo.append(i)
    if(not vazio):
        jogo = Jogo(valores_form['nome'].title(), valores_form['categoria'].title(), valores_form['console'].title())
        lista.append(jogo)
        flash("{} foi adicionado com sucesso".format(jogo.nome))
    else:
        flash("Erro! Campo(s) em branco: "+", ".join(str(i.title()) for i in atributo))

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get("proxima")
    return render_template('login.html',titulo='Login', proxima = proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if(request.form['usuario'] in usuarios):
        user = usuarios[request.form['usuario']]
        if(user.senha == request.form['senha']): 
            session['usuario_logado'] = user.nome
            flash('{} logou com sucesso'.format(user.nome.title()))
            proxima_pagina = request.form['proxima']

            print(proxima_pagina)
            return redirect(proxima_pagina)
        else:
            flash('Não logado, tente novamente!')
            return redirect(url_for('login'))
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    global usuario_atual
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    usuario_atual = ''
    return redirect(url_for('login'))

@app.route("/registrar")
def registrar():
    return render_template('registrar.html', titulo="Cadastrar Usuario")

@app.route("/cadastrar", methods=['POST',])
def cadastrar():
    if(request.form['id'] not in usuarios):
        if(request.form["senha"] == request.form["senha_check"]):
            novo_usuario = Usuario(request.form['id'],request.form['usuario'], request.form['senha'])
            usuarios[novo_usuario.id] = novo_usuario
            flash("Usuario {} cadastrado com sucesso".format(novo_usuario.id))
            return redirect(url_for('login'))
        else:
            flash("As senhas não correspondem! Tente novamente!")
            return redirect(url_for('registrar'))
        
    else:
        flash("Nome de usuario já existe!")
        return redirect(url_for('registrar'))


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
app.run(host='127.0.0.1', port=5000, debug="True")