from random import choice
print('VAMOS JOGAR PEDRA, PAPEL OU TESOURA?')
# PEDINDO O NOME DO JOGADOR, EU DEI AO COMPUTADOR O NOME DE BILL
nome = str(input('Digite o nome do Jogador: ')).strip()
computador = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = 1
#COMPARANDO A ESCOLHA DO JOGADOR
while escolha == 1 :
    jogador = str(input('Escolha: Pedra, Papel ou Tesoura: ')).strip().upper()
    if jogador == 'PEDRA' or jogador == 'PAPEL' or jogador == 'TESOURA':
         escolha = 0

if escolha == 0 :
    esComputer = choice(computador)
    if esComputer == jogador:
        print('{} escolheu {} e o Bill escolheu {}, Temos um empate!!'.format(nome, jogador, esComputer))
        # BILL VENCE
    elif esComputer == 'PEDRA' and jogador == 'TESOURA':
        print('Bill ecolheu {} e {} escolheu {}, Bill venceu!!'.format(esComputer, nome, jogador))
    elif esComputer == 'TESOURA' and jogador == 'PAPEL':
        print('Bill ecolheu {} e {} escolheu {}, Bill venceu!!'.format(esComputer,nome, jogador))
    elif esComputer == 'PAPEL' and jogador == 'PEDRA':
        print('Bill ecolheu {} e {} escolheu {}, Bill venceu!!'.format(esComputer,nome, jogador))
        # JOGADOR VENCE
    elif jogador == 'PEDRA' and esComputer == 'TESOURA' :
        print('{} escolheu {} e Bill escolheu {}, você venceu!!'.format(nome, jogador, esComputer))
    elif jogador == 'TESOURA' and esComputer == 'PAPEL' :
        print('{} escolheu {} e Bill escolheu {}, você venceu!!'.format(nome, jogador, esComputer))
    elif jogador == 'PAPEL' and esComputer == 'PEDRA':
        print('{} escolheu {} e Bill escolheu {}, você venceu!!'.format(nome, jogador, esComputer))﻿