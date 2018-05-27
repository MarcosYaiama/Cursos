print('====== DESAFIO 39 ======')
from datetime import date
from math import fabs
ano_atual = date.today().year
ano_nascimento = int(input('\033[30mAno de nascimento: '))
print('Qual o seu sexo?')
sexo = int(input('(0) HOMEM         (1)MULHER\nResposta: '))

idade = ano_atual - ano_nascimento
tempo = fabs(idade - 18)
validaResposta = False

if(sexo == 1):
    print('Você é mulher')
    print('O alistamento militar não é obrigatório!')
    print('Caso você queira se alistar..\n\n')
    validaResposta = True
elif(not sexo):
    print('Você é homem!')
    print('O alistamento militar é OBRIGATÓRIO!\n\n')
    validaResposta = True
else:
    print('OPÇÃO INVÁLIDA!')

if(validaResposta):

    print("Quem nasceu em {} tem {} anos em {}.".format(ano_nascimento, idade, ano_atual))

    if(idade > 18):
        alistamento = fabs(tempo - ano_atual)
        print('Você já deveria ter se alistado há {:.0f} ano(s)'.format(tempo))
        print('Seu alistamento foi em {:.0f}'.format(alistamento))
    elif(idade < 18):
        alistamento = tempo + ano_atual
        print('Ainda faltam {:.0f} ano(s) para o alistamento'.format(tempo))
        print('Seu alistamento será em {:.0f}'.format(alistamento))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!')

print('Programa finalizado!')

