print('\033[0;30m{:=^40}'.format(' DESAFIO 55 '))
maiorPeso = 0
menorPeso = 0
for i in range(0,5):
    peso = int(input('\t\tPeso: '))
    if(peso > maiorPeso):
        maiorPeso = peso
    else:
        if(peso < menorPeso):
                menorPeso = peso
    if (i == 0):
        menorPeso = peso
print('\tMaior Peso: {} Kilos\n\tMenor Peso: {} Kilos\033[m'.format(maiorPeso,menorPeso))
