print('{:=^40}'.format(' DESAFIO 44 '))
from time import sleep
from random import randint
print('\033[30m-=-\033[m' * 20)
print('\033[7;30mBEM VINDO AO NOSSO JOGO DE JOKENPO\033[m')
print('\033[30m-=-\033[m' * 20)

print('Digite sua escolha:')
print('(1)PEDRA     (2)PAPEL        (3)TESOURA')
player = int(input('Qual é a sua jogada? '))
computador = randint(1,3)
pedra = 1
papel = 2
tesoura = 3
venceu = 0
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print(40 * '-=')
if(computador == player):
    print('O computador fez a mesma jogada que você!')
    print('\033[1;30;44mEMPATE\033[m')
    venceu = 2
elif(computador == pedra and player == papel):
    print('Computador jogou \033[1;30mPEDRA\033[m')
    print('PAPEL VENCE PEDRA, \033[7;32;40mVOCÊ VENCEU\033[m')
    venceu = 1
elif(player == pedra and computador == papel):
    print('O computador jogou \033[1;30mPAPEL\033[m')
    print('PAPEL VENCE PEDRA, \033[7;31;40mVOCÊ PERDEU\033[m')
    venceu = 0
elif(computador == pedra and player == tesoura):
    print('O computador jogou \033[1;30mPEDRA\033[m')
    print('PEDRA QUEBRA TESOURA, \033[7;31;40mVOCÊ PERDEU!\033[m')
    venceu = 0
elif(player == pedra and computador == tesoura):
    print('O computador jogou \033[1;30mTESOURA\033[m')
    print('PEDRA QUEBRA TESOURA, \033[7;32;40mVOCÊ VENCEU!\033[m')
    venceu = 1
elif(computador == papel and player == tesoura):
    print('O computador jogou \033[1;30mPAPEL\033[m')
    print('TESOURA CORTA PAPEL, \033[7;32;40mVOCÊ VENCEU!\033[m')
    venceu = 1
elif(player == papel and computador == tesoura):
    print('O computador jogou \033[1;30mTESOURA\033[m')
    print('TESOURA CORTA PAPEL, \033[7;31;40mVOCÊ PERDEU!\033[m')
    venceu = 0
print(40 * '-=')

if(venceu):
    print('JOGADOR VENCE')
elif(not venceu):
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
