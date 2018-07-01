import os
#ARQUIVO DE CONFIGURAÇÃO
SECRET_KEY = 'alura'

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PASSWD = ""
MYSQL_DB = "jogoteca"
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
SEND_FILE_MAX_AGE_DEFAULT = 0
