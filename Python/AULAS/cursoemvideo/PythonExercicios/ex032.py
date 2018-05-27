print('======DESAFIO 32 ======')
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('\033[30mO ano de {} é BISSEXTO'.format(ano))
else:
    print('\033[30mO ano de {} NÃO é BISSEXTO'.format(ano))
