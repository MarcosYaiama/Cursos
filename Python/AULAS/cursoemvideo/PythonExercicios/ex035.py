print('======DESAFIO 35 ======')
from math import fabs
print('\033[30m-=-' * 20)
print('\033[30mAnalisador de Triângulos')
print('\033[30m-=-' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

existencia = fabs(b - c) < a and a < b + c

if existencia:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

