print('======DESAFIO 22 ======')
nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em maiúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))
#print("Seu primeiro nome tem {} letras".format(nome.find(' '))) #no .find(' ') ele pega oque tem no primeiro espaço

#Segunda forma de pegar o primeiro nome
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))