#Somar todos os numeros do digito

n = int(input("Digite um número inteiro: "))
tam = len(str(n))
nAnterior = 0
m = 10
s = 0

while tam > 0:
    if tam == len(str(n)):
        s = n % 10
    else:
        s = (n // m % 10) + s
        m *= 10
    tam -= 1
print(s)