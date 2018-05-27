print('{:=^40}'.format(' DESAFIO 44 '))
peso = float(input('\033[30mQual é o seu peso? (Kg)  \033[m'))
altura = float(input('\033[30mQual é a sua altura? (m) \033[m'))
IMC = peso / altura ** 2
print('\033[1;30mSeu Indice de Massa Corpórea é de \033[3;33m{:.1f}\033[m'.format(IMC))
print('\033[1;30mVoce está em \033[m',end='')
if IMC <=  18.5:
    print('\033[1;30m ABAIXO DO PESO NORMAL \033[m')
elif 18.5 >= IMC < 25:#IMC >= 18.5 and IMC < 25
    print('\033[1;32m PESO NORMAL \033[m')
elif 25 <= IMC < 30:#IMC >= 25 and IMC <= 30
    print('\033[1;35;40m SOBREPESO \033[m')
elif 30 <= IMC <= 40:#IMC > 30 and IMC <= 40
    print('\033[1;33;41m OBESIDADE! \033[m')
else:
    print('\033[1;31;40m OBESIDADE MORBIDA, CUIDADO! \033[m')