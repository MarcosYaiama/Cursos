x = int(input("Digite um numero: "))
tam = len(str(x))
i = 0
n = 0
m = 10
while(i < tam):
    if(i == 0):
        y = x % m
        n = n + y

    else:
        y = (x // m) % 10
        n = n + y
        m = m * 10
    print(n)
    i += 1
print("A soma de todos os digitos deu: {}".format(n))

