print('\033[0;30m{:=^40}'.format(' DESAFIO 58 '))

from random import randint

numero_secreto = randint(0,10)
acertou = False
tentativa = 0
while(not acertou):
    resposta = int(input('Qual o número que eu pensei?'))
    if(resposta == numero_secreto):
        acertou = True
    tentativa += 1
print('Você acertou o número em \033[1;33m{}\033[m tentativa(s)'.format(tentativa))