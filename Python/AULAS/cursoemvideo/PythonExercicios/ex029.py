print('======DESAFIO 29 ======')
velocidade = float(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[1;31mMULTADO!\033[31m Você excedeu o limite permitido que é de \033[31m80Km/h\033[m\n\033[31mVocê deve pagar uma multa de \033[1;33mR$ {:.2f}!'.format(multa))
print('\033[33mTenha um bom dia e dirija com segurança!')

