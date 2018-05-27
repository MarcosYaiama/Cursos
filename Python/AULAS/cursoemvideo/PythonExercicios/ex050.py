print('{:=^40}'.format(' DESAFIO 50 '))
s = 0
for c in range(0,6):
    n = int(input('Insira um número: '))
    if(n % 2 == 0):
        s += n
print(s)