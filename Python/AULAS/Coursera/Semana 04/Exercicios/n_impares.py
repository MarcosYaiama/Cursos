#Impares

i = int(input("Digite o valor de n: "))
n = 0
while i > 0:
    n = n + 1
    if n % 2 != 0:
        print(n)
    else:
        i -= 1
