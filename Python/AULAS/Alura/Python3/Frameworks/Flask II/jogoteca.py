from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
#Importa um arquivo de configuração
app.config.from_pyfile('config.py')

db = MySQL(app)

#Importante ser aqui pois, as views só serão chamadas
#depois da criação do app
from views import *

#Garante que o app só rode quando o jogoteca.py for executado
#Caso contrario o app.run não é executado
if __name__ == '__main__':
    app.run(debug=True)
