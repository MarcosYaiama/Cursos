l = int(input("digite a largura: "))
a = int(input("digite a altura: "))
n = 1
n2 = 1
while(n <= l):
    print("#",end="")
    n += 1
    if(n == l):
        while(n2 < a):
            print("#",end="")
            print()
            n2 += 1
            n = 1
            break