print('======DESAFIO 30 ======')

numero = int(input('\033[35mMe diga um número qualquer: \033[m'))
resultado = numero % 2
if(resultado == 0):
    print('O número {} é \033[34mPAR'.format(numero))
else:
    print('O número {} é \033[34mIMPAR'.format(numero))