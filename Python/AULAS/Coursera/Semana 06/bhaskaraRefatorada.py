from math import sqrt


def delta(a, b, c):
    return b ** 2 - 4 * a * c
def main():
    a = float(input("Digite o valor de a:  "))
    b = float(input("Digite o valor de b:  "))
    c = float(input("Digite o valor de c:  "))
    imprime_raizes(a,b,c)

def imprime_raizes(a,b,c):
    d = delta(a, b, c)
    if d == 0:
        x = -b + sqrt(d)
        print('a unica raiz desta equação é {}'.format(x))
    else:

        if d < 0:
            print('esta equação não possui raízes reais')
        else:
            raiz1 = (-b + sqrt(d))/(2 * a)
            raiz2 = (-b - sqrt(d))/(2 * a)
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
