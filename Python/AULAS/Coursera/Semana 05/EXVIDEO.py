def fatorial(n):
    f = n - 1
    if n != 0:
        while f > 0:
            n = f * n
            f = f - 1
    else:
        n = 1
    return n

def coeficiente(n,k):
    return fatorial(n)/(fatorial(k)*fatorial(n - k))

print(coeficiente(3,4))