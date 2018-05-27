def maior_primo(k):
    p = 0
    primo = True
    if(k > 0):
        i = 1
        while(i <= k):
            if(i != 1):
                j = i
                primo = True
                while(j != 0):
                    d = i % j
                    if(d == 0 and j != 1 and j != i):
                        primo = False
                        break
                    else:
                        if(j == 1 and primo):
                            p = i
                    j -= 1
            i += 1
    return p
