spam = ['apples', 'bananas' ,'tofu','cats']
spam2 = ['apples', 'bananas' ,'tofu','cats', 'dogs', 'apple pie']
def retorna_string(lista):
    texto = ''
    for t in range(len(lista)):
        if t == len(lista) - 1:
            texto += 'and ' + lista[t]
        else:
            texto += lista[t] + ' '
    return texto

res = retorna_string(spam)
print(res)
res = retorna_string(spam2)
print(res)