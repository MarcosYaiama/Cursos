def maior_elemento(lista):
    maior = 0
    for i in lista:
        if maior == 0:
            maior = i
        else:
            if i > maior:
                maior = i
    return maior        
    
