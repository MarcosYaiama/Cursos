#Fatorial

n = int(input("Digite o valor de n: "))
f = n
if n != 0:
    while f > 0:
        n = f * n
        f = f - 1
else:
    n = 1
print(n)