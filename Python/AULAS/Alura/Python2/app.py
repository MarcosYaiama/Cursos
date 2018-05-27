# -*- coding: UTF-8 -*-

def cadastrar(nomes):
    print 'Digite o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print '''Digite:
        (1) cadastrar, 
        (2) exibir nomes, 
        (3) remover,
        (4) alterar,
        (5) procurar
        (0) sair'''
        escolha = raw_input()
        if(escolha == '1'):
            cadastrar(nomes)
        elif(escolha == '2'):
            listar(nomes)
        elif(escolha == '3'):
            print 'Qual nome você gostaria de remover?'
            rnome = raw_input()
            remover(nomes, rnome)
        elif escolha == '4':
            alterar(nomes)
        elif escolha == '5':
            procurar(nomes)

def remover(nomes, nome_para_remover):
    print 'Nome %s removido com sucesso' % (nome_para_remover)
    nomes.remove(nome_para_remover)
def listar(nomes):
    print 'Listando nomes'
    for nome in nomes:
        print nome

def alterar(nomes):
    print 'Qual nome você gostaria de alterar?'
    escolha_nome = raw_input()
    if escolha_nome in nomes:
        print 'Digite o novo nome:'
        alteracao_nome = raw_input()
        nomes[nomes.index(escolha_nome)] = alteracao_nome
    else:
        print 'Esse nome não está na lista'

def procurar(nomes):
    print 'Digite o nome que deseja buscar:'
    nome_a_procurar = raw_input()
    if(nome_a_procurar in nomes):
        print 'O resultado %s está na posição %s' % (nome_a_procurar, nomes.index(nome_a_procurar))
    else:
        print 'Nome %s não está cadastrado' % (nome_a_procurar)

menu()