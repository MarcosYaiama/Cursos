import os
from jogoteca import app


def search_dictionary_item(item, dictionary):
    for dict in dictionary.keys():
        if(item in dict):
            print("{}:\t{}".format(dict,dictionary[dict]))

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