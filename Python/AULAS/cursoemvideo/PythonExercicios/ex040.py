print('====== DESAFIO 40 ======')
nota1 = float(input('\033[30mPrimeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) /2

print('\033[30mTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1 ,nota2 ,media))

print('O aluno está ',end='')
if(media < 5.0):
    print('\033[7;31;40mREPROVADO\033[m',end='')
elif(7 > media >= 5.0):#OU (media >=5 and media < 7)
    print('de \033[7;33;40mRECUPERAÇÃO\033[m',end='')
else:
    print('\033[7;32;40mAPROVADO\033[m',end='')
