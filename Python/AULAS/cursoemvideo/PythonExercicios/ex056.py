print('\033[0;30m{:=^40}'.format(' DESAFIO 56 '))

nome = []
idade = []
sexo = []

for i in range(0,4):
    nome += [input('Nome: ')]
    idade += [int(input('Idade: '))]
    sexo += [input('(M) ou (F) ')]
    print(i)

homem_mais_velho = 0
homem_mais_velho_idade = 0
femeas_menos_vinte = 0
idadeSoma = 0
femea = False
for i in range(0,4):
    idadeSoma += idade[i]
    if(sexo[i] == 'F'):
        if(idade[i] < 20):
           femeas_menos_vinte += 1
           femea = True
    else:
        if(idade[i] > homem_mais_velho_idade):
            homem_mais_velho_idade = idade[i]
            homem_mais_velho = i
            print('HOMEM+VELHO {}'.format(i))
idadeMedia = idadeSoma/4
print('A média das idades é \033[0;32m{}\033[30m'.format(idadeMedia))
print('O homem mais velho é o \033[32m{}\033[30m'.format(nome[homem_mais_velho]))
if(femea):
    if(femeas_menos_vinte < 1):
        print('Nenhuma mulher tem menos que 20 anos')
    else:
        print('\033[32m{}\033[m mulheres com menos de 20 anos.'.format(femeas_menos_vinte))
else:
    print('Não há femeas')