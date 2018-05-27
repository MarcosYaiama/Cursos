import random
print('======DESAFIO 019 ======')
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

l = [a1, a2, a3, a4]
escolhido = choice(l)

print("O aluno escolhido é: {}".format(escolhido))

