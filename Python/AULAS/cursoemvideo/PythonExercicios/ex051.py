print('{:=^40}'.format(' DESAFIO 51 '))

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(1,11):
    progressao = primeiro_termo + razao * (i - 1)
    print(progressao)