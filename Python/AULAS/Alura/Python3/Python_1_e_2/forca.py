def jogar():
    print('********************************')
    print('Bem vindo ao jogo da Forca!')
    print('********************************')

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False
    forca = len(palavra_secreta)
    acertos = []
    posicoes_acertadas = []
    letras_acertadas = []
    for i in range(len(palavra_secreta)):
        letras_acertadas.append('_')
    for i in range(len(palavra_secreta)):
        acertos.append(' _')
    while(not enforcou and not acertou):
        for i in letras_acertadas:
            print(i,end=' ')
        print()
        chute = input("Qual a letra? ")
        chute = chute.strip()
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print('Encontrei a letra {} está na posição {}'.format(letra, index))
                acertos.append(index)
            index += 1
        for i in range(len(palavra_secreta)):
            if i in acertos or i in posicoes_acertadas:
                print(' {}'.format(palavra_secreta[i]), end = '')
                letras_acertadas[i] = palavra_secreta[i]
                if i not in posicoes_acertadas:
                    posicoes_acertadas.append(i)
            else:
                print(' _',end = '')

                letras_acertadas[i] = '_'
        print()
        if(len(posicoes_acertadas) == len(palavra_secreta)):
            print('\033[1;32mParabéns você descobriu a palavra!\033[m')
            break
        print()
        print('jogando...')
    print('FIM DE JOGO')


if(__name__ == "__main__"):
    jogar()
