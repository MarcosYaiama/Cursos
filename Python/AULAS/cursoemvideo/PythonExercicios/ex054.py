print('{:=^40}'.format(' DESAFIO 54 '))

from datetime import date

maior = 0
menor = 0
ano_atual = date.today().year
for i in range(0,7):
    ano = int(input('Ano: '))
    if(ano_atual - ano < 18):
        menor += 1
    else:
        maior += 1
print('Maiores: {}   Menores: {}'.format(maior,menor))