print('======DESAFIO 26 ======')
nome = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {}'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A') + 1))

