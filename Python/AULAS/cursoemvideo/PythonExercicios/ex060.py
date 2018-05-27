print('\033[0;30m{:=^40}'.format(' DESAFIO 60 '))


n = int(input('Insira um número: '))
resposta = n

for i in range(1, n):
    resposta *= i
print(resposta)
