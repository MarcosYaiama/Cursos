print('======DESAFIO 017 ======')
'''from math import hypot
cateto_op = float(input('Comprimento do cateto oposto: '))
cateto_ad = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(cateto_ad,cateto_op)))'''



n1 = float(input('Comprimento do cateto oposto:'))
n2 = float(input('Comprimento do cateto adjacente: '))
hip = (n1 ** 2 + n2 ** 2) ** 1/2
'''hip = sqrt(n1 ** 2 + n2 ** 2)'''
print('A hipotenusa vai medir {:.2f}'.format(hip))