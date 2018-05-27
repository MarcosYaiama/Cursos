
def campeonato():
#Chama a função partida() 3 vezes
    i = 1
    pc = 0
    player = 0
    while(i <=3):
        print('**** Rodada {} ****'.format(i))
        r = partida()
        if(r == True):
            pc += 1
        else:
            player += 1
        i += 1
    print('Placar: Você {} X {} Computador'.format(player,pc))


def partida():
    #Pergunta os valores de n e m
    # Decide quem começa o jogo
    #Responsavel por chamar funções
    #Atualiza peças
    #Identifica fim do Jogo

    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    pcJogou = False
    pcGanhou = False
    if(n % (m + 1) == 0):
        print("Voce começa!")
        print()
        n = n - usuario_escolhe_jogada(n,m)
        pcJogou = False
        if(n == 1):
            print("Agora resta uma peça no tabuleiro.")
            print()
        else:
            print("Agora restam",n,"peças no tabuleiro.")
            print()
    else:
        print('Computador começa!')
        print()
        n = n - computador_escolhe_jogada(n,m)
        if(n > 0):
            print("Agora restam", n, "peças no tabuleiro.")
            print()
        pcJogou = True
        if(n == 0):
            pcGanhou = True

    while(n >= 1):
        if(pcJogou):
            n -= usuario_escolhe_jogada(n,m)
            if (n > 0):
                print("Agora restam", n, "peças no tabuleiro.")
                print()
            pcJogou = False
        else:
            n -= computador_escolhe_jogada(n, m)
            if(n > 0):
                print("Agora restam", n, "peças no tabuleiro.")
                print()
            pcJogou = True
            if(n == 0):
                pcGanhou = True

    if(pcGanhou):
        print('Fim do jogo! O computador ganhou!')
    else:
        print('Fim do jogo! Você ganhou!')

    return pcGanhou


def computador_escolhe_jogada(n,m):
    #Deve funcionar sozinha
    #n = numero peças
    #m = numero peças tirar
    if n == m:
        return n
    elif(n > m):
        n2 = n
        numero = m
        while(1):
            n2 = n
            n2 -= numero
            if(n2 % (m+1) == 0 and numero != 0):
                print('O computador tirou {} peças.'.format(numero))
                return numero
            elif(numero < 1):
                if(n > m):
                    return m
                else:
                    break
            numero -= 1
            
        if(m < n):
            print('O computador tirou {} peças.'.format(m))
            return m
    elif(n < m):
        if(n == 1):
            print('O computador tirou uma peça.')
        else:
            print('O computador tirou {} peças.'.format(n))
        return n



def usuario_escolhe_jogada(n, m):
# Deve funcionar sozinha
    jogada = int(input('Quantas peças você vai tirar? '))
    while(jogada > n or not jogada <= m):
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        jogada = int(input('Quantas peças você vai tirar? '))
    if(jogada == 1):
        print('Você tirou uma peça.')
        return jogada
    else:
        print('Você tirou ',jogada,' peças.')
        return jogada



def main():
    print("Bem-vindo ao jogo do NIM! Escolha: \n\n")
    print('1 - para jogar uma partida isolada')
    print('2 - para jogar um campeonato ', end='')
    escolha = int(input())

    if(escolha == 1):
        print('Você escolheu partida isolada')
        partida()

    elif(escolha == 2):
        print('Voce escolheu um campeonato')
        campeonato()
    else:
        while(escolha != 1 or escolha != 2):
            print('Opção inválida, escolha novamente')
            print('1 - para jogar uma partida isolada')
            print('2 - para jogar um campeonato ')
            escolha = int(input())
            if (escolha == 1):
                print('Você escolheu partida isolada')
                partida()
                break
            elif (escolha == 2):
                print('Voce escolheu um campeonato')
                campeonato()
                break
