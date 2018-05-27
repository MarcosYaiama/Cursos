print('{:=^40}'.format(' DESAFIO 49 '))
n1 = int(input('Digite um número para ver sua tabuada:'))
n2 = int(input('Até quanto? '))
print('------------')
for c in range(0,n2+1):
    print('{} x {:2} = {}'.format(n1,  c,  n1*c))
print('------------')