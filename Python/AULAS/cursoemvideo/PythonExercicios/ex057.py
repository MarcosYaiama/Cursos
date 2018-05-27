print('\033[0;30m{:=^40}'.format(' DESAFIO 57 '))

valido = False
while(not valido):
    sexo = input('Sexo: ').upper()
    if(sexo == 'M' or sexo == 'F'):
        valido = True
