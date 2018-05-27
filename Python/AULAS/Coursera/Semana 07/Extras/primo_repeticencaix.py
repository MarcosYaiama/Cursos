n = int(input("Digite um numero inteiro: "))
def éPrimo(x):
    fator = 2
    primo = False
    while x % fator != 0 and fator < x:
        fator += 1
        primo = True
    return primo

while n > 0:
    if éPrimo(n):
        print(n, "é primo!")
    else:
        print(n, "não é primo :-(")
    n = int(input("Digite um numero inteiro: "))


