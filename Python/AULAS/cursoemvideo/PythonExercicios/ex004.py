print('======DESAFIO 04 ======')
n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
esp = n.isspace()
num = n.isnumeric()
alfab = n.isalpha()
alfan = n.isalnum()
maius = n.isupper()
minus = n.islower()
dec = n.isdecimal()
digit = n.isdigit()
ident = n.isidentifier()
prin = n.isprintable()
cap = n.istitle()

print('Só tem espaços? {}'.format(esp))
print('É um número? {}'.format(num))
print('É alfabético? {}'.format(alfab))
print('É alfanumérico? {}'.format(alfan))
print('Está em maiúsculas {}?'.format(maius))
print('Está em minúsculas? {}'.format(minus))
print(f'Está capitalizada? {cap}')

