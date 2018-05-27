from math import sqrt
a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c


if delta < 0:
    print('esta equação não possui raízes reais')
else:
    x = -b + sqrt(delta)
    y = -b - sqrt(delta)
    if delta == 0:
        print('a raiz desta equação é {}'.format(x))
    else:
        if(x > y):
            print('as raízes da equação são {} e {}'.format(y,x))
        else:
            print('as raízes da equação são {} e {}'.format(x,y))