from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
#Puxa a configuração de um Arquivo Python externo
app.config.from_pyfile('config.py')

db = MySQL(app)

#Importante ser aqui pois, as views só serão chamadas
#depois da criação do app
from views import *

#Só executa o código quando ele for executado
#O app.run não é executado quando esse arquivo é puxado em um import
if __name__ == '__main__':
    app.run(debug=True)
