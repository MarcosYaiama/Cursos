print('======DESAFIO 28 ======')
from random import randint
from time import sleep
print('\033[33m-=-' * 20)
print('\033[34m Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[33m-=-' * 20)

jogador = int(input('\033[30m Em que número eu pensei? '))
computador = randint(0,5)
print('\033[35m PROCESSANDO...')
sleep(3)

if(jogador == computador):
    print('\033[33m PARABÉNS! Você conseguiu me vencer!')
else:
    print('\033[31m GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))