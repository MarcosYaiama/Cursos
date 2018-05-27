import random

def jogar():
    print('********************************')
    print('Bem vindo ao jogo de Advinhação!')
    print('********************************')


    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 3

    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))


    if(nivel == 1):
        total_de_tentativas = 20


    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
        chute_str = input('Digite um numero entre 1 e 100: ')
        chute = int(chute_str)
        print('Você digitou',chute_str)

        condicao = chute < 1 or chute > 100
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto
        acertou = chute == numero_secreto
        if (condicao):
            print('Você deve digitar um numero entre 1 e 100!')
            continue

        if(acertou):
            print('Parabéns! Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto)
            if(menor):
                print('Você errou! O seu chute foi menor que o numero secreto.')
                pontos = pontos - (numero_secreto - chute)
                print("Pontos: {}".format(pontos))
            elif(maior):
                print('Você errou! O seu chute foi maior que o numero secreto.')
                pontos = pontos - (chute - numero_secreto)
                print("Pontos : {}".format(pontos))


    print('Fim de jogo!')
if(__name__ == "__main__"):
    jogar()