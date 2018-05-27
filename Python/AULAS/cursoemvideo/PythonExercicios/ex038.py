print('======DESAFIO 38 ======')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('\033[31m-\033[m O \033[1;31mPRIMEIRO\033[m valor é\033[1;34m MAIOR!')
elif n2 > n1:
    print('\033[31m-\033[mO \033[1;31mSEGUNDO\033[m valor é\033[1;34m MAIOR!')
else:
    print('\033[1;31m-NÃO EXISTE\033[m valor maior, os dois são \033[1;34mIGUAIS\033[m')