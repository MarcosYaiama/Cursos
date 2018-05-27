import forca
import Adivinhacao

def escolhe_jogo():
    print('********************************')
    print('******Escolhe o seu jogo!*******')
    print('********************************')

    print("(1) Forca (2) Advinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        Adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()