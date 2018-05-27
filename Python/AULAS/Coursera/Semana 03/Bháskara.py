from math import sqrt
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b ** 2 - 4 * a * c
x1 = (-b + sqrt(delta)) / 2 * a
x2 = (-b - sqrt(delta)) / 2 * a
if delta == 0:
    print('A unica raiz é: {}'.format(x1))
else:
    if(delta < 0):
        print("Esse programa não tem raizes")
    else:
        print('Para a = {}, b = {} e c = {}, em Bháskara x1 = {} e x2 = {}'.format(a,b,c,x1,x2))