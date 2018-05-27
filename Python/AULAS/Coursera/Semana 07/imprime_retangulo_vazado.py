l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i = 1
while(i <= a):
    
    if(i == 1 or i == a):
        print("#",end="")
        ia = 2
        
        while(ia <= l):
            print("#",end="")
            ia += 1
        print()
    else:
        print("#",end="")
        s = 3
        while(s <= l):
            print(" ",end='')
            s += 1
        print("#")
    i += 1
        