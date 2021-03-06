from models import Jogo, Usuario
from flask_mysqldb import MySQL
SQL_DELETA_JOGO = 'delete from jogo where id = %s'
SQL_JOGO_POR_ID = 'SELECT id, nome, categoria, console from jogo where id = %s'
SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_JOGO = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id = %s'
SQL_BUSCA_JOGOS = 'SELECT id, nome, categoria, console from jogo'
SQL_BUSCA_USUARIOS = 'SELECT * from usuario'
SQL_CRIA_JOGO = 'INSERT into jogo (nome, categoria, console) values (%s, %s, %s)'
SQL_CRIA_USUARIO = 'INSERT into usuario(id, nome, senha) values (%s, %s, %s)'


class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo):
        cursor = self.__db.connection.cursor()
        if (jogo.id):
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria, jogo.console, jogo.id))
        else:            
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid
        self.__db.connection.commit()
        return jogo

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_JOGOS)
        jogos = traduz_jogos(cursor.fetchall())
        return jogos

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_JOGO_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_JOGO, (id, ))
        self.__db.connection.commit()

class UsuarioDao:
    def __init__(self, db):
        self.__db = db
        self.nome = "Nick"

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario
    
    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_USUARIOS)
        usuarios = traduz_user(cursor.fetchall())
        print(usuarios)
        return usuarios

    def novo_usuario(self, usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_USUARIO, (usuario.id, usuario.nome, usuario.senha))
        print(self)
        nome = "Marcos"
        print(self.nome)
        print(nome)
        #self.__db.connect.commit()     #MALDITO ERRO, JAMAIS TE ESQUECEREI!
        self.__db.connection.commit()
def traduz_jogos(jogos):
    def cria_jogo_com_tupla(tupla):
        return Jogo(tupla[1], tupla[2], tupla[3], id=tupla[0])
    return list(map(cria_jogo_com_tupla, jogos))

def traduz_user(usuarios):
    def cria_user_com_tupla(tupla):
        return Usuario(tupla[0], tupla[1], tupla[2])
    return list(map(cria_user_com_tupla, usuarios))

def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
