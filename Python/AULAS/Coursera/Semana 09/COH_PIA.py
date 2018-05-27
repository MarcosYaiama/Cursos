import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
       textos.append(texto)
       i += 1
       texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
       del sentencas[-1]
       return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
       p = palavra.lower()
       if p in freq:
           if freq[p] == 1:
               unicas -= 1
           freq[p] += 1
       else:
           freq[p] = 1
           unicas += 1
    return unicas
def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
       p = palavra.lower()
       if p in freq:
           freq[p] += 1
       else:
           freq[p] = 1
    return len(freq)
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass



#Minhas Fun?es
#textos = le_textos()
#sentencas = calcula_senteças(textos)    #Uma lista onde cada indice representa as sentenças de um texto, 3 textos, 3 listas de sentenças
#frases = calcula_frases(sentecas)       #Uma lista que pega as listas de sentenças e as transforma em frases, se mantem, 3 textos, 3 listas de frases
#palavras = calcula_palavras(frases)     #Uma lista que pega as listas de frases e as transforma em palavras, se mantem, 3 textos, 3 listas de palavras

def calcula_palavras(lista):
    lista_palavras = 0
    

def calcula_frases(lista):
    lista_frases_por_texto = 0
    for texto in lista:
        listagem = separa_frases(texto)
        lista_frases_por_texto.append(listagem)
    return lista_frases_por_texto



def calcula_sentencas(lista):
    sentenca = 0
    for text in lista:
        senteca.append(separa_sentencas(text))
    return sentenca

def tamanho_medio_de_palavras(lista):
    return 0
