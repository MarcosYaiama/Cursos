print('====== DESAFIO 42 ======')
from math import fabs
a = float(input('\033[30mPrimeiro segmento: \033[m'))
b = float(input('\033[30mSegundo segmento: \033[m'))
c = float(input('\033[30mTerceiro segmento: \033[m'))

existencia = fabs(b-c) < a and a < b + c
# Outra possibilidade é:
# a < b + c and b < a + c and c < a + b

if(existencia):
    print('\033[30mOs segmentos acima \033[7;32;40mPODEM FORMAR\033[30m um triângulo ',end='')
    if(a == b == c):#a == b and b == c
        print('\033[1;34;40mEQUILÁTERO\033[m')
    elif(a == b and c != a or a == c and b != c or b == c and c != a):
        print('\033[1;34;40mISÓSCELES\033[m')
    else:# a != b != c != a ou a != b and a != c and b != c
        print('\033[1;34;40mESCALENO\033[m')
else:
    print('\033[30mOs segmentos acima \033[7;31;40mNÃO PODEM FORMAR\033[30m um triângulo!')