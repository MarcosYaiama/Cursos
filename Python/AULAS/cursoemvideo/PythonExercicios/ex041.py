print('====== DESAFIO 41 ======')
from datetime import date
ano_atual = date.today().year
nascimento = int(input('\033[30mAno de nascimento: '))
idade = ano_atual - nascimento
if nascimento > ano_atual:
    print('Você não é um viajante do tempo, coloque uma data válida!')
else:
    print('O atleta tem {} anos.'.format(idade))
    if idade <= 9:
        print('\033[33mClassificação:\033[7;34;40mMIRIM\033[m')
    elif idade <= 14 and idade > 9:
        print('\033[33mClassificação:\033[7;34;40mINFANTIL\033[m')
    elif idade > 14 and idade <= 19:
        print('\033[33mClassificação:\033[7;34;40mJUNIOR\033[m')
    elif idade > 19 and idade <= 25:
        print('\033[33mClassificação:\033[7;34;40mSÊNIOR\033[m')
    else:
        print('\033[33mClassificação:\033[7;34;40mMASTER\033[m')