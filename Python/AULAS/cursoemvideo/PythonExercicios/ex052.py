print('{:=^40}'.format(' DESAFIO 52 '))

n = int(input('Digite um número inteiro: '))
primo = True
for i in range(1, n+1):
    if(i != 1 and i != n):
        if(n % i == 0):
            primo = False
    print('N: {}    I: {}'. format(n,i),'\n',n % i == 0)
    print('Primo: {}'.format(primo))
    if(not primo):
        break
if(primo):
    print('É primo')
else:
    print('Não é primo')