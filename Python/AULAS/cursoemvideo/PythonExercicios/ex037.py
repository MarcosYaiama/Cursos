print('======DESAFIO 37 ======')
numero = int(input('Digite um número qualquer: '))

print('Vamos converter esse número para qual base de conversão?')
escolha = int(input('(1) BINARIO      (2)OCTAL        (3)HEXADECIMAL'))

if escolha == 1:
    print('Você escolheu BINÁRIO')
elif escolha == 2:
    print('Você escolheu OCTAL')
elif escolha == 3:
    print('Você escolheu HEXADECIMAL')
else:
    print('Escolha inválida, programa finalizado !')