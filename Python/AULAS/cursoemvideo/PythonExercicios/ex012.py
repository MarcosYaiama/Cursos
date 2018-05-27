print('======DESAFIO 012 ======')

preco = float(input('Qual o preço do produto? '))
novo = preco - (preco * 5/100)


print('O produto que custava R${},na promoção com desconto de 5% vai custar R${:.2f}'.format(preco,novo))
