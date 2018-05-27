print('======DESAFIO 015 ======')
dia = int(input('Durante quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago =(km * 0.15) + (dia * 60)

print('O total do aluguel foi de R${:.2f}'.format(pago))