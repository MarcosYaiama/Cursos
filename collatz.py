def collatz(number):
    col = number // 2
    print(col)
    if(number % 2 == 0):
        col = number // 2
        print(col)
    else:
        col = 3*number+1 
        print(col)
    return col
c = 0
n = int(input("Insira um numero: "))
resultado = 0
while(n !=1):
    c += 1
    n = collatz(n)
print("Foram {} chamadas".format(c))
