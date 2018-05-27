print('\033[0;30m{:=^40}'.format(' DESAFIO 59 '))

n1 = int(input('Insira um número: '))
n2 = int(input('Insira um número: '))

sair = False
while(not sair):
    print('''
    \033[1;31m[1]\033[0;30m SOMAR\n
    \033[1;31m[2]\033[0;30m MULTIPLICAR\n
    \033[1;31m[3]\033[0;30m MAIOR\n
    \033[1;31m[4]\033[0;30m NOVOS NÚMEROS\n
    \033[1;31m[5]\033[0;30m SAIR DO PROGRAMA\n
    \n\n\t''')

    resposta_programa = 0
    resposta_usuario = int(input())
    if(resposta_usuario == 1):
        resposta_programa = n1 + n2
    elif(resposta_usuario == 2):
        resposta_programa = n1 * n2
    elif(resposta_usuario == 3):
        if(n1 > n2):
            resposta_programa = n1
        elif(n1 < n2):
            resposta_programa = n2
        else:
            resposta_programa = 'São iguais'
    elif(resposta_usuario == 4):
        n1 = int(input())
        n2 = int(input())
    elif(resposta_usuario == 5):
        sair = True
    print(resposta_programa + '\n\n\')