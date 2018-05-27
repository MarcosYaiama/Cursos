x = int(input("Digite um número: "))
tam = len(str(x))
anterior = 0
i = 0
n1 = 0
m = 10
saoIguais = False
while i < tam:
    if(i == 0):
        anterior = x % 10
    else:
        n1 = x // m % 10
        m *= 10
        if n1 == anterior:
            saoIguais = True
        anterior = n1
    i += 1
if saoIguais:
    print('sim')
else:
    print('não')

