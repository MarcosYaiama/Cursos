from string import whitespace

print('{:=^40}'.format( 'DESAFIO 53' ))

repetir = True
while(repetir):
    palavra = input('Digite algo com espaços!!! \n ->>  ')
    palavra_junta = ''
    for i in range(0,len(palavra)):
        if(palavra[i] != ' '):
            palavra_junta += palavra[i]

    if(palavra_junta == palavra_junta[-1::-1]):
        print('Palindromo\n\n')
    else:
        print('Não é palindromo\n\n')
    print(palavra_junta, '\n')

    repetir = bool(input('Continuar? [0/1]'))
