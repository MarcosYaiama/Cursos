from math import radians,tan,sin,cos
print('======DESAFIO 018 ======')
n1 = float(input('Digite um ângulo: '))

s = sin(radians(n1))
c = cos(radians(n1))
t = tan(radians(n1))

print("O ângulo de {} tem SENO de {:.2f}".format(n1,s))
print("O ângulo de {} tem COSSENO de {:.2f}".format(n1,c))
print("O ângulo de {} tem TANGENTE de {:.2f}".format(n1,t))

