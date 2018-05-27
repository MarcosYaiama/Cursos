lista = []
while(1):
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    else:
        lista.append(numero)
tamanho = len(lista)
listaI = lista[::-1]
for i in listaI:
    print(i)
