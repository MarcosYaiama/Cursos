n = int(input("Digite um número inteiro: "))
i = n
primos = True
while i > 0:
    if i != n and i != 1:
        if n % i == 0:
            primos = False

    i -= 1
if(primos):
    print('primo')
else:
    print('não primo')
