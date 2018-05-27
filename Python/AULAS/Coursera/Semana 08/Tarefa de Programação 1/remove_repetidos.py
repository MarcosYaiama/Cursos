def remove_repetidos(lista):
    listaComp = []
    elementoSubtrai = 0
    terminar = False
    tamanhoLista = len(lista)
    while terminar == False:
        for elemento in range(len(lista)):
            elemento -= elementoSubtrai
            if len(listaComp) == 0:
                listaComp.append(lista[elemento])
            else:
                repetiu = False
                for elementoComp in listaComp:
                    if elementoComp == lista[elemento]:
                        repetiu = True
                        break

                if repetiu:
                    del lista[elemento]
                    elementoSubtrai += 1
                else:
                    listaComp.append(lista[elemento])
                if elemento == (tamanhoLista - 1) - elementoSubtrai:
                    terminar = True
                    break
    lista = sorted(lista)
    return lista 
