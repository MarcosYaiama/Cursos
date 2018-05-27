from random import choice
print('VAMOS JOGAR PEDRA, PAPEL OU TESOURA?')
# PEDINDO O NOME DO JOGADOR, EU DEI AO COMPUTADOR O NOME DE BILL
nome = str(input('Digite o nome do Jogador: ')).strip()
computador = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = 1
# COMPARANDO A ESCOLHA DO JOGADOR
while escolha == 1:
    jogador = str(input('Escolha: Pedra, Papel ou Tesoura: ')).strip().upper()
    if jogador == 'PEDRA' or jogador == 'PAPEL' or jogador == 'TESOURA':
        escolha = 0
else:
    esComputer = choice(computador)
    if esComputer == jogador:
        print('{} escolheu {} e o Bill escolheu {}, Temos um empate!!'.format(nome, jogador, esComputer))
    else:
        if (esComputer == 'PEDRA' and jogador == 'TESOURA') or \
         (esComputer == 'TESOURA' and jogador == 'PAPEL') or \
         (esComputer == 'PAPEL' and jogador == 'PEDRA'):
            winner = 'Bill'
        else:
            winner = 'você'
        print('{} escolheu {} e Bill escolheu {}, {} venceu!!'.format(nome, jogador, esComputer, winner))﻿